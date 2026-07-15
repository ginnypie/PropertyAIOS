#!/usr/bin/env python3
"""
Render a themed appraisal-report PDF from a data JSON file.

Usage:
    python3 render.py data.json --theme 66days --out /path/report.pdf

- data.json  : property fields + comparables (see example-11-apollo.json)
- --theme    : a filename in themes/ (66days | harbour | noir | <yours>)
- --out      : output PDF path (a sibling .html is written too)

Layout CSS comes from master.template.html (its <head>); the body comes from
report.body.template.html. Images may be local paths or http(s) URLs — both are
downloaded/read and inlined as base64 so the PDF is fully self-contained.
"""
import argparse, base64, json, pathlib, re, subprocess, sys, tempfile, time, urllib.request

import shutil
HERE = pathlib.Path(__file__).resolve().parent

def find_chrome():
    """Locate Chrome/Chromium/Edge across macOS, Windows and Linux. Falls back to none."""
    cands = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    ]
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser",
                 "chrome", "microsoft-edge"):
        p = shutil.which(name)
        if p: cands.insert(0, p)
    for c in cands:
        if c and pathlib.Path(c).exists():
            return c
    return None

CHROME = find_chrome()

def img_uri(src):
    """Return a data: URI for a local path or http(s) URL. Empty on failure."""
    try:
        if str(src).startswith(("http://", "https://")):
            req = urllib.request.Request(src, headers={"User-Agent": "Mozilla/5.0"})
            data = urllib.request.urlopen(req, timeout=30).read()
        else:
            p = (src if pathlib.Path(src).is_absolute() else HERE / src)
            data = pathlib.Path(p).read_bytes()
        mime = "jpeg"
        if data[:4] == b"\x89PNG": mime = "png"
        elif data[:4] == b"RIFF" and data[8:12] == b"WEBP": mime = "webp"
        elif data[:3] == b"GIF": mime = "gif"
        return f"data:image/{mime};base64," + base64.b64encode(data).decode()
    except Exception as e:
        print(f"  ! image failed ({src}): {e}", file=sys.stderr)
        return ""

def money(n):
    """1620000 -> '$1.62m'; passes through strings unchanged."""
    if isinstance(n, str):
        return n
    return f"${n/1_000_000:.2f}m"

# Brand identity is a property of the THEME, not the per-report data. This keeps the
# header, footer and signature in sync so one report can never show three different brand
# names (e.g. a "66 Days to Property" header with a stray "Cowork Property Appraisal"
# signature). A data JSON may still override any field, but by default the whole report
# speaks with one voice chosen by --theme. Add an entry here when you add a theme.
THEME_BRANDS = {
    "66days":  {"brand_name": "66 Days to Property", "brand_sub": "PROPERTYAIOS",
                "footer_brand": "66 DAYS TO PROPERTY", "signature": "66 Days to Property"},
    "harbour": {"brand_name": "Harbour Property",    "brand_sub": "PROPERTYAIOS",
                "footer_brand": "HARBOUR PROPERTY",   "signature": "Harbour Property"},
    "noir":    {"brand_name": "PropertyAIOS",         "brand_sub": "APPRAISAL",
                "footer_brand": "PROPERTYAIOS",        "signature": "PropertyAIOS"},
}
DEFAULT_BRAND = THEME_BRANDS["66days"]

def build(data, theme):
    head = (HERE / "master.template.html").read_text()
    head = head[:head.index("</head>") + len("</head>")]
    theme_css = (HERE / "themes" / f"{theme}.css").read_text()
    head = head.replace("/*__THEME__*/", theme_css)

    body = (HERE / "report.body.template.html").read_text()

    comps = data["comparables"]
    imgs = {c["ref"]: img_uri(c["image"]) for c in comps}
    subject_uri = img_uri(data["image"])

    # ---- photo thumbs (first 4 comps) ----
    thumbs = "".join(f'<img src="{imgs[c["ref"]]}" alt="">' for c in comps[:4])
    body = body.replace("<!--PHOTO_THUMBS-->", thumbs)

    # ---- number line ----
    prices = [c["price"] for c in comps if isinstance(c["price"], (int, float))]
    lo = min(prices + [data["range_low"]]) * 0.98
    hi = max(prices + [data["range_high"]]) * 1.02
    span = hi - lo or 1
    pos = lambda v: max(0, min(100, (v - lo) / span * 100))
    ticks = "".join(f"<span>{(lo + span*i/3)/1e6:.2f}M</span>" for i in range(4))
    body = body.replace("<!--SCALE_TICKS-->", ticks)
    dots = "".join(f'<div class="dotc" style="left:{pos(p):.0f}%"></div>' for p in prices)
    dots += f'<div class="dotc rng" style="left:{pos((data["range_low"]+data["range_high"])/2):.0f}%"></div>'
    dots += f'<div class="dotc sub" style="left:{pos(data["value_mid"]):.0f}%"></div>'
    body = body.replace("<!--SCALE_DOTS-->", dots)

    # ---- comparable cards ----
    tagcls = {"Comparable": "t-comp", "Superior": "t-sup", "Inferior": "t-inf"}
    cards = []
    for c in comps:
        anchor = " anchor" if c.get("anchor") else ""
        rel = c["relation"]
        cards.append(f'''<div class="ccard{anchor}">
      <div class="ctop"><div class="cimg"><span class="badge">{c["ref"]}</span><img src="{imgs[c["ref"]]}"></div>
        <div class="cright"><div class="caddr">{c["address"]}</div>
          <div class="cicons"><span>{c["beds"]} bd</span><span>{c["baths"]} ba</span><span>{c["cars"]} car</span></div></div></div>
      <div class="cbody">
        <div class="crow cprice"><span>Last sale</span><b>{money(c["price"])} · {c["date"]}</b></div>
        <div class="crow"><span>{c["line2_label"]}</span><b>{c["line2"]}</b></div>
      </div>
      <div class="tags"><span class="tag t-set">Settled</span><span class="tag {tagcls.get(rel,"t-comp")}">{rel}</span></div>
    </div>''')
    body = body.replace("<!--COMP_CARDS-->", "\n".join(cards))

    # ---- reasoning paragraphs ----
    reason = "".join(f"<p>{p}</p>" for p in data["reasoning"])
    body = body.replace("<!--REASON-->", reason)

    # ---- scalar tokens ----
    # Brand fields default from the theme (see THEME_BRANDS) so header, footer and
    # signature always match; a data JSON only overrides them if deliberately set.
    brand = THEME_BRANDS.get(theme, DEFAULT_BRAND)
    tok = {
        "BRAND_NAME": data.get("brand_name", brand["brand_name"]),
        "BRAND_SUB": data.get("brand_sub", brand["brand_sub"]),
        "FOOTER_BRAND": data.get("footer_brand", brand["footer_brand"]),
        "KICKER": data.get("kicker", "Indicative Market Appraisal"),
        "TITLE": data.get("title", "Market Appraisal<br>Report"),
        "ADDRESS": data["address"], "DATE": data["date"],
        "IMG_SUBJECT": subject_uri,
        "PREPARED_FOR": data.get("prepared_for", "—"),
        "PREPARED_BY": data.get("prepared_by", "PropertyAIOS"),
        "PURPOSE": data.get("purpose", "Research / underwrite"),
        "VALUE_MID": money(data["value_mid"]),
        "VALUE_RANGE": f'{money(data["range_low"])} – {money(data["range_high"])}',
        "LAST_SALE": data.get("last_sale", "—"), "AVM": data.get("avm", "—"),
        "TYPE": data.get("type", "House"), "BEDS": data["beds"], "BATHS": data["baths"],
        "CARS": data["cars"], "HIGHLIGHT": data.get("highlight", "Feature"),
        "LIVING": data.get("living", "—"), "LAND": data.get("land", "—"),
        "TITLE_REF": data.get("title_ref", "—"), "LGA": data.get("lga", "—"),
        "ZONING": data.get("zoning", "—"), "IMPROVEMENTS": data.get("improvements", "—"),
        "CAR_ACCOM": data.get("car_accom", "—"),
        "CONFIDENCE": data.get("confidence", "Medium"),
        "CONFIDENCE_NOTE": data.get("confidence_note", ""),
        "SIGNATURE": data.get("signature", brand["signature"]),
        "COMPS_SUMMARY": data.get("comps_summary", f"{len(comps)} sales"),
        "COMPS_NOTE": data.get("comps_note", ""),
    }
    for k, v in tok.items():
        body = body.replace("{{" + k + "}}", str(v))
        head = head.replace("{{" + k + "}}", str(v))   # title etc. live in <head>

    return head + "\n" + body

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("data")
    ap.add_argument("--theme", default="66days")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    data = json.loads(pathlib.Path(a.data).read_text())
    html = build(data, a.theme)
    out = pathlib.Path(a.out)
    html_path = out.with_suffix(".html")
    html_path.write_text(html)
    print(f"HTML  -> {html_path}")

    if not CHROME:
        print("No Chrome/Chromium/Edge found — open the .html above in any browser and "
              "use Print → Save as PDF (the fonts and images are already embedded).",
              file=sys.stderr)
        return
    if out.exists():
        out.unlink()
    profile = tempfile.mkdtemp(prefix="chr-")
    proc = subprocess.Popen(
        [CHROME, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
         "--no-pdf-header-footer", "--virtual-time-budget=10000",
         f"--user-data-dir={profile}", f"--print-to-pdf={out}", f"file://{html_path}"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # Poll for the PDF rather than waiting for Chrome to self-exit (it sometimes hangs on web fonts).
    deadline, size = time.time() + 45, -1
    while time.time() < deadline:
        if proc.poll() is not None:
            break
        if out.exists():
            s = out.stat().st_size
            if s > 1000 and s == size:      # file has stopped growing
                break
            size = s
        time.sleep(1)
    if proc.poll() is None:
        proc.terminate()
        try: proc.wait(timeout=5)
        except subprocess.TimeoutExpired: proc.kill()
    if out.exists() and out.stat().st_size > 1000:
        print(f"PDF   -> {out}  ({out.stat().st_size//1024} KB)")
    else:
        print("PDF render failed — open the .html in a browser and print to PDF.", file=sys.stderr)

if __name__ == "__main__":
    main()
