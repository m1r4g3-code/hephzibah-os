"""
Renders a branded LinkedIn post card per wiki/concepts/linkedin-brand-system.md.
Mechanical arm only — HTML/CSS layout is fixed by the brand spec; this script
just fills in the content and rasterizes it with Playwright.

Usage:
  python scripts/render_card.py \
    --image PATH_TO_HERO_IMAGE \
    --eyebrow "CLIENT x HEPHZIBAH -- PROJECT TYPE" \
    --quote "Exact client brief or key line" \
    --stats "N deliverables . N days . Result" \
    --role1 "Creative direction" --name1 "Collaborator Name" \
    --role2 "Automation design" --name2 "Emmanuel Adekoya" \
    --theme both \
    --out Desktop
"""
import argparse
import base64
import mimetypes
import os
import sys
from pathlib import Path
from string import Template

from playwright.sync_api import sync_playwright

CARD_TEMPLATE = Template("""<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@1,700&family=Inter:wght@400&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body {
    width: 540px; height: 675px;
    background: $page_bg;
  }
  .page {
    width: 540px; height: 675px;
    display: flex; align-items: center; justify-content: center;
  }
  .card {
    width: 492px; height: 627px;
    background: $card_bg;
    border-radius: 24px;
    padding: 24px;
    box-shadow: $shadow;
    display: flex;
    flex-direction: column;
  }
  .eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 500;
    font-size: 8px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: $muted;
    margin-bottom: 12px;
  }
  .hero-wrap {
    width: 100%;
    height: 296px;
    border-radius: 14px;
    overflow: hidden;
    flex-shrink: 0;
    background: $card_bg;
  }
  .hero-wrap img {
    width: 100%; height: 100%; object-fit: contain;
    filter: contrast(0.88) brightness(1.05) saturate(0.82);
  }
  .quote {
    font-family: 'Poppins', sans-serif;
    font-style: italic;
    font-weight: 700;
    font-size: 15px;
    line-height: 1.45;
    color: $ink_text;
    margin-top: 18px;
  }
  .stats-chip {
    display: inline-block;
    margin-top: 14px;
    background: #18140E;
    color: #E8FF3A;
    border-radius: 8px;
    padding: 8px 14px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    letter-spacing: 0.18em;
    line-height: 1;
    text-transform: uppercase;
  }
  .rule {
    border: none;
    border-top: 1px solid $rule_color;
    margin: 16px 0;
  }
  .attribution { flex: 1; }
  .attr-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    align-items: center;
    padding: 6px 0;
  }
  .attr-role {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: $muted;
  }
  .attr-name {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-size: 12px;
    color: $ink_text;
    text-align: right;
  }
  .brandmark {
    display: inline-block;
    align-self: flex-start;
    background: #18140E;
    color: #E8FF3A;
    border-radius: 6px;
    padding: 5px 11px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 8px;
    letter-spacing: 0.28em;
    text-transform: uppercase;
  }
</style>
</head>
<body>
  <div class="page">
    <div class="card">
      <div class="eyebrow">$eyebrow</div>
      <div class="hero-wrap"><img src="$image_src" /></div>
      <div class="quote">&ldquo;$quote&rdquo;</div>
      <div class="stats-chip">$stats</div>
      <hr class="rule" />
      <div class="attribution">
        $attr_rows
      </div>
      <hr class="rule" />
      <div class="brandmark">HEPHZIBAH &copy; 2026</div>
    </div>
  </div>
</body>
</html>
""")

ATTR_ROW = Template(
    '<div class="attr-row"><div class="attr-role">$role</div>'
    '<div class="attr-name">$name</div></div>'
)

THEMES = {
    "light": dict(
        page_bg="#E2DDD0",
        card_bg="#EDE8DC",
        muted="#6B675C",
        ink_text="#18140E",
        rule_color="rgba(24,20,14,0.12)",
        shadow="0 2px 6px rgba(0,0,0,0.05), 0 10px 28px rgba(0,0,0,0.09), 0 28px 56px rgba(0,0,0,0.07)",
    ),
    "dark": dict(
        page_bg="#060608",
        card_bg="#0C0C12",
        muted="#9A9A9A",
        ink_text="#FAFAFA",
        rule_color="rgba(250,250,250,0.12)",
        shadow="0 2px 8px rgba(0,0,0,0.30), 0 12px 32px rgba(0,0,0,0.40), 0 32px 64px rgba(0,0,0,0.30)",
    ),
}


def image_to_data_uri(path: str) -> str:
    mime, _ = mimetypes.guess_type(path)
    mime = mime or "image/png"
    data = Path(path).read_bytes()
    b64 = base64.b64encode(data).decode("ascii")
    return f"data:{mime};base64,{b64}"


def resolve_out_dir(out: str) -> Path:
    if out.strip().lower() == "desktop":
        p = Path.home() / "Desktop"
    else:
        p = Path(out)
    p.mkdir(parents=True, exist_ok=True)
    return p


def render(theme: str, args, out_dir: Path):
    tokens = THEMES[theme]
    attr_rows = []
    if args.role1 and args.name1:
        attr_rows.append(ATTR_ROW.substitute(role=args.role1, name=args.name1))
    if args.role2 and args.name2:
        attr_rows.append(ATTR_ROW.substitute(role=args.role2, name=args.name2))

    html = CARD_TEMPLATE.substitute(
        **tokens,
        eyebrow=args.eyebrow,
        quote=args.quote,
        stats=args.stats,
        image_src=image_to_data_uri(args.image),
        attr_rows="\n".join(attr_rows),
    )

    out_path = out_dir / f"card_{theme}.png"
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 540, "height": 675}, device_scale_factor=2)
        page.set_content(html, wait_until="networkidle")
        page.screenshot(path=str(out_path))
        browser.close()
    return out_path


def main():
    ap = argparse.ArgumentParser(description="Render a Hephzibah LinkedIn brand card")
    ap.add_argument("--image", required=True, help="Path to hero image")
    ap.add_argument("--eyebrow", required=True)
    ap.add_argument("--quote", required=True)
    ap.add_argument("--stats", required=True)
    ap.add_argument("--role1", default="")
    ap.add_argument("--name1", default="")
    ap.add_argument("--role2", default="")
    ap.add_argument("--name2", default="")
    ap.add_argument("--theme", choices=["light", "dark", "both"], default="both")
    ap.add_argument("--out", default="Desktop")
    args = ap.parse_args()

    if not os.path.isfile(args.image):
        print(f"Image not found: {args.image}", file=sys.stderr)
        sys.exit(1)

    out_dir = resolve_out_dir(args.out)
    themes = ["light", "dark"] if args.theme == "both" else [args.theme]
    for theme in themes:
        out_path = render(theme, args, out_dir)
        print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
