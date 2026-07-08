# Report assets — "66 Days" valuation-report style

The reusable, brand-matched appraisal report.

## Files
- `appraisal-report.template.html` — 3-page A4 template (Cover · Summary · Comparables).
  Uses the [66 Days brand tokens](../66-days-brand.css) and follows [report-style.md](../report-style.md).
  Layout modelled on a bank Remote Market Valuation Report — **structure only**, no lender logo or valuer identity.
- Image placeholders: `{{SUBJECT}}`, `{{C12APOLLO}}`, `{{C9MARINA}}`, `{{C46MARINA}}`,
  `{{C42MARINA}}`, `{{C54HARBOUR}}`, `{{C121HARBOUR}}` — replace with base64 `data:` URIs
  (keeps the PDF fully self-contained).

## To render a new report
1. Copy the template, swap the property text + image placeholders.
2. Inline images as base64 data URIs (so the PDF is portable):
   ```python
   import base64, pathlib
   uri = "data:image/jpeg;base64," + base64.b64encode(pathlib.Path("photo.jpg").read_bytes()).decode()
   ```
3. Render to PDF with headless Chrome:
   ```bash
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
     --headless --disable-gpu --no-pdf-header-footer --virtual-time-budget=12000 \
     --print-to-pdf=out.pdf "file:///abs/path/report.html"
   ```

First built for: 11 Apollo Quay, Trinity Park QLD 4879 (9 Jul 2026).
