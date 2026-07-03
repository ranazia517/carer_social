#!/usr/bin/env python3
"""
CARER social card renderer.

Usage:
  python3 make_social_card.py --headline "A little light, kept." \
      --support "For the person holding everything together." \
      --format square --out ~/Desktop/card.png

  # With an app screen:
  python3 make_social_card.py --headline "A companion who listens." \
      --support "Present for you, whenever you need." \
      --format portrait --screen path/to/screen.png --out ~/Desktop/card.png

Formats:
  square    1080 × 1080   Instagram feed square
  portrait  1080 × 1350   Instagram feed portrait
  story     1080 × 1920   Instagram / Facebook Story
  landscape 1200 × 630    Facebook / LinkedIn
  x         1600 × 900    X (Twitter) / LinkedIn banner
"""
import argparse, asyncio, io, base64, sys
from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image

LORA = Path.home() / "Developer/carer/carer_frontend/brand/logo/fonts/Lora-VariableFont_wght.ttf"

LOGO_SVG = ('<svg viewBox="0 0 100 100" width="100%" height="100%" fill="none" '
            'xmlns="http://www.w3.org/2000/svg">'
            '<path d="M71.85 76.04 A34 34 0 1 1 71.85 23.96" stroke="#A46349" '
            'stroke-width="14.5" stroke-linecap="round"/>'
            '<circle cx="54.5" cy="56" r="7" fill="#A46349"/></svg>')

AP = ("background-color:#F7EFE7;background-image:"
      "radial-gradient(58% 52% at 18% 20%,rgba(248,201,160,.76) 0%,transparent 70%),"
      "radial-gradient(54% 50% at 84% 14%,rgba(244,197,180,.66) 0%,transparent 70%),"
      "radial-gradient(64% 58% at 72% 84%,rgba(206,188,222,.68) 0%,transparent 72%),"
      "radial-gradient(60% 54% at 10% 82%,rgba(237,190,198,.65) 0%,transparent 72%),"
      "radial-gradient(52% 40% at 50%  0%,rgba(255,243,218,.94) 0%,transparent 52%),"
      "radial-gradient(38% 30% at 50% 46%,rgba(248,222,196,.36) 0%,transparent 58%)")

AL = ("background-color:#F7EFE7;background-image:"
      "radial-gradient(65% 56% at 14% 22%,rgba(248,210,162,.78) 0%,transparent 68%),"
      "radial-gradient(60% 52% at 86% 18%,rgba(244,197,180,.68) 0%,transparent 68%),"
      "radial-gradient(70% 60% at 70% 86%,rgba(206,188,222,.70) 0%,transparent 72%),"
      "radial-gradient(65% 56% at 12% 82%,rgba(237,190,198,.66) 0%,transparent 72%),"
      "radial-gradient(54% 42% at 50% -2%,rgba(255,243,218,.96) 0%,transparent 50%),"
      "radial-gradient(44% 35% at 50% 50%,rgba(248,220,195,.30) 0%,transparent 58%)")

# (width, height, aurora, layout)
# layout: 'centre' (text centred, screen below if given)
#          'left'  (text left, screen right — landscape cards)
FORMATS = {
    'square':    (1080, 1080, AP, 'centre'),
    'portrait':  (1080, 1350, AP, 'centre'),
    'story':     (1080, 1920, AP, 'centre'),
    'landscape': (1200,  630, AL, 'left'),
    'x':         (1600,  900, AL, 'left'),
}


def b64(p: Path) -> str:
    buf = io.BytesIO(); Image.open(p).save(buf, 'PNG')
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


def _logo_css(cw: int) -> dict:
    scale = cw / 1080
    return dict(
        lm=round(52 * scale),
        lw=round(38 * scale),
        lg=round(10 * scale),
    )


def build_html_centre(cw: int, ch: int, aurora: str, headline: str,
                      support: str, screen_b64: str | None) -> str:
    L = LORA.as_posix()
    sc = cw / 1080
    lm, lw, lg = round(52*sc), round(38*sc), round(10*sc)
    pt = round(72 * sc)          # logo padding-top
    h1g = round(60 * sc)         # gap: logo → headline
    h1s = round(72 * sc)         # headline font-size
    h1mw = round(900 * sc)
    pg = round(24 * sc)          # gap: headline → support
    ps = round(34 * sc)
    pmw = round(820 * sc)

    screen_block = ""
    if screen_b64:
        sw = round(cw * 0.55)    # phone width = 55% of canvas
        sw = min(sw, 540)
        # derive height from screen aspect 1170:2532
        sh = round(sw * 2532 / 1170)
        bz = round(16 * sc)
        fbr = round(48 * sc)
        sbr = round(34 * sc)
        iw = round(80 * sc); ih = round(18 * sc)
        # top of phone: leave ~40% of canvas for header
        pt_ph = round(ch * 0.42)
        screen_block = f"""
.pw{{position:absolute;top:{pt_ph}px;left:50%;transform:translateX(-50%);
  width:{sw}px;height:{sh}px}}
.pf{{position:relative;width:100%;height:100%;background:#1A1A1C;
  border-radius:{fbr}px;
  box-shadow:0 50px 120px rgba(0,0,0,.28),0 0 80px rgba(190,148,188,.16)}}
.di{{position:absolute;top:{bz}px;left:50%;transform:translateX(-50%);
  width:{iw}px;height:{ih}px;background:#1A1A1C;border-radius:{ih//2}px;z-index:2}}
.sc{{position:absolute;top:{bz}px;bottom:{bz}px;left:{bz}px;right:{bz}px;
  border-radius:{sbr}px;overflow:hidden}}
.sc img{{width:100%;height:100%;object-fit:cover;display:block}}"""

    phone_html = ""
    if screen_b64:
        phone_html = f"""
<div class="pw"><div class="pf"><div class="di"></div>
  <div class="sc"><img src="{screen_b64}"></div></div></div>"""

    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Lora;src:url('file://{L}') format('truetype');font-weight:100 900}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{cw}px;height:{ch}px;overflow:hidden;position:relative;{aurora}}}
.hdr{{position:absolute;top:0;left:0;right:0;display:flex;flex-direction:column;
  align-items:center;padding-top:{pt}px;text-align:center}}
.logo{{display:flex;align-items:center;gap:{lg}px;white-space:nowrap}}
.lm{{width:{lm}px;height:{lm}px;flex-shrink:0}}
.lw{{font-family:Lora,serif;font-size:{lw}px;font-weight:500;color:#A46349;letter-spacing:-.02em}}
h1{{margin-top:{h1g}px;font-family:Lora,serif;font-size:{h1s}px;font-weight:750;color:#4A3528;
  line-height:1.18;letter-spacing:-.03em;max-width:{h1mw}px}}
p{{margin-top:{pg}px;font-family:-apple-system,Arial,sans-serif;font-size:{ps}px;
  color:#A08C82;letter-spacing:-.005em;max-width:{pmw}px}}
{screen_block}
</style></head><body>
<div class="hdr">
  <div class="logo"><div class="lm">{LOGO_SVG}</div><span class="lw">carer</span></div>
  <h1>{headline}</h1><p>{support}</p>
</div>
{phone_html}
</body></html>"""


def build_html_left(cw: int, ch: int, aurora: str, headline: str,
                    support: str, screen_b64: str | None) -> str:
    L = LORA.as_posix()
    sc = cw / 1200
    lm, lw, lg = round(48*sc), round(36*sc), round(9*sc)
    lt = round(56 * sc)
    lx = round(64 * sc)          # left margin
    h1t = round(lt + lm + round(44*sc))
    h1s = round(56 * sc)
    h1mw = round(520 * sc)
    pt_txt = round(h1t + h1s*2.4 + round(18*sc))
    ps = round(26 * sc)
    pmw = round(480 * sc)

    screen_block = phone_html = ""
    if screen_b64:
        sw = round(ch * 0.58 * 1170 / 2532)
        sh = round(sw * 2532 / 1170)
        bz = round(14 * sc)
        fbr = round(40 * sc); sbr = round(28 * sc)
        iw = round(70 * sc); ih = round(16 * sc)
        px = round(cw * 0.56)
        py = round((ch - sh) // 2)
        screen_block = f"""
.pw{{position:absolute;top:{py}px;left:{px}px;width:{sw}px;height:{sh}px}}
.pf{{position:relative;width:100%;height:100%;background:#1A1A1C;
  border-radius:{fbr}px;
  box-shadow:0 40px 100px rgba(0,0,0,.26),0 0 70px rgba(190,148,188,.14)}}
.di{{position:absolute;top:{bz}px;left:50%;transform:translateX(-50%);
  width:{iw}px;height:{ih}px;background:#1A1A1C;border-radius:{ih//2}px;z-index:2}}
.sc{{position:absolute;top:{bz}px;bottom:{bz}px;left:{bz}px;right:{bz}px;
  border-radius:{sbr}px;overflow:hidden}}
.sc img{{width:100%;height:100%;object-fit:cover;display:block}}"""
        phone_html = f"""
<div class="pw"><div class="pf"><div class="di"></div>
  <div class="sc"><img src="{screen_b64}"></div></div></div>"""

    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Lora;src:url('file://{L}') format('truetype');font-weight:100 900}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{cw}px;height:{ch}px;overflow:hidden;position:relative;{aurora}}}
.logo{{position:absolute;top:{lt}px;left:{lx}px;display:flex;align-items:center;gap:{lg}px}}
.lm{{width:{lm}px;height:{lm}px;flex-shrink:0}}
.lw{{font-family:Lora,serif;font-size:{lw}px;font-weight:500;color:#A46349;letter-spacing:-.02em}}
h1{{position:absolute;top:{h1t}px;left:{lx}px;
  font-family:Lora,serif;font-size:{h1s}px;font-weight:750;color:#4A3528;
  line-height:1.2;letter-spacing:-.03em;max-width:{h1mw}px}}
p{{position:absolute;top:{pt_txt}px;left:{lx}px;
  font-family:-apple-system,Arial,sans-serif;font-size:{ps}px;
  color:#A08C82;letter-spacing:-.005em;max-width:{pmw}px}}
{screen_block}
</style></head><body>
<div class="logo"><div class="lm">{LOGO_SVG}</div><span class="lw">carer</span></div>
<h1>{headline}</h1><p>{support}</p>
{phone_html}
</body></html>"""


async def render_card(fmt: str, headline: str, support: str,
                      screen: Path | None, out: Path) -> None:
    if fmt not in FORMATS:
        sys.exit(f"Unknown format '{fmt}'. Choose: {', '.join(FORMATS)}")
    cw, ch, aurora, layout = FORMATS[fmt]
    screen_b64 = b64(screen) if screen else None
    if layout == 'centre':
        html = build_html_centre(cw, ch, aurora, headline, support, screen_b64)
    else:
        html = build_html_left(cw, ch, aurora, headline, support, screen_b64)

    tmp = out.with_suffix('.html')
    tmp.write_text(html, encoding='utf-8')

    async with async_playwright() as pw:
        br = await pw.chromium.launch()
        ctx = await br.new_context(viewport={'width': cw, 'height': ch},
                                   device_scale_factor=1)
        pg = await ctx.new_page()
        await pg.goto(f"file://{tmp}", wait_until='domcontentloaded')
        await pg.wait_for_timeout(1200)
        buf = await pg.screenshot(type='png',
                                  clip={'x': 0, 'y': 0, 'width': cw, 'height': ch})
        img = Image.open(io.BytesIO(buf)).convert('RGB')
        out.parent.mkdir(parents=True, exist_ok=True)
        img.save(out, 'PNG')
        await br.close()
    tmp.unlink(missing_ok=True)
    print(f"  {out}  {img.size}")


def main():
    p = argparse.ArgumentParser(description='Render a CARER social card.')
    p.add_argument('--headline', required=True, help='Main headline (HTML allowed for <br>)')
    p.add_argument('--support',  default='',   help='Support / subheadline text')
    p.add_argument('--format',   required=True,
                   choices=list(FORMATS), help='Card format')
    p.add_argument('--screen',   default=None, type=Path,
                   help='Optional app screen PNG (1170×2532)')
    p.add_argument('--out',      required=True, type=Path, help='Output PNG path')
    args = p.parse_args()
    asyncio.run(render_card(args.format, args.headline, args.support,
                            args.screen, args.out))


if __name__ == '__main__':
    main()
