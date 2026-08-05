#!/usr/bin/env python3
"""CARER store-asset production — iPhone App Store 6.5" slot (1284×2778).

Why this script exists
----------------------
`produce_v5.py` renders the iPhone frames at 1320×2868 (the iPhone 6.9" slot).
App Store Connect's 6.5" upload slot accepts ONLY 1242×2688 / 2688×1242 /
1284×2778 / 2778×1284, so a 1320×2868 file is rejected there. This script
re-renders the same 8 frames NATIVELY onto a 1284×2778 canvas.

Native re-render, not a rescale: every element (type, logo, phone mockup,
gradient) is laid out by the browser at the target size, so text stays crisp
and there are no letterbox/pillarbox bars. The composition is preserved by
scaling every layout constant from the 6.9" slot by a single uniform factor
k = 2778/2868, so nothing is stretched or distorted.

Only the iPhone App Store slot is touched. iPad, Google Play, icons, listings
and source-screens are untouched by this script.
"""
import asyncio, io, base64, pathlib, os
from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image

STORE_ROOT = Path.home() / "Developer/carer/store-assets"
# SRC defaults to the working-copy screens, but the store-assets BRANCH has an
# older, canonical set. A dimensions fix must not silently swap app-screen
# content, so the driver pins SRC to the screens extracted from the branch.
SRC   = Path(os.environ.get("CARER_SRC_SCREENS", STORE_ROOT / "source-screens"))
LORA  = Path.home() / "Developer/carer/carer_frontend/brand/logo/fonts/Lora-VariableFont_wght.ttf"
STORE = Path(os.environ.get("CARER_OUT_ROOT", STORE_ROOT))
HTML_DIR = pathlib.Path(
    "/private/tmp/claude-501/-Users-ayeshazia-Developer-carer/"
    "e19def3f-e040-40d9-b7e5-807f76909388/scratchpad/html_i65"
)
HTML_DIR.mkdir(parents=True, exist_ok=True)

OUT_SUBDIR = os.environ.get("CARER_OUT_SUBDIR", 'app-store/iphone-6.5')
# App Store Connect 6.5" portrait — permitted exactly. Overridable so the same
# layout maths can render a 1320×2868 control frame for fidelity checking.
CW = int(os.environ.get("CARER_CW", 1284))
CH = int(os.environ.get("CARER_CH", 2778))

# ── Assets (identical to produce_v5.py) ──────────────────────────────────────

LOGO = ('<svg viewBox="0 0 100 100" width="100%" height="100%" fill="none" '
        'xmlns="http://www.w3.org/2000/svg">'
        '<path d="M71.85 76.04 A34 34 0 1 1 71.85 23.96" stroke="#A46349" '
        'stroke-width="14.5" stroke-linecap="round"/>'
        '<circle cx="54.5" cy="56" r="7" fill="#A46349"/></svg>')

AP = ("background-color:#F7EFE7;background-image:"
      "radial-gradient(58% 52% at 18% 20%,rgba(248,201,160,.76) 0%,transparent 70%),"
      "radial-gradient(54% 50% at 84% 14%,rgba(244,197,180,.66) 0%,transparent 70%),"
      "radial-gradient(64% 58% at 72% 84%,rgba(206,188,222,.68) 0%,transparent 72%),"
      "radial-gradient(60% 54% at 10% 82%,rgba(237,190,198,.65) 0%,transparent 72%),"
      "radial-gradient(52% 40% at 50% 0%,rgba(255,243,218,.94) 0%,transparent 52%),"
      "radial-gradient(38% 30% at 50% 46%,rgba(248,222,196,.36) 0%,transparent 58%)")

SCR_MAP = {
    'welcome':  'screen-01-welcome.png',
    'exchange': 'screen-03-first-exchange.png',
    'memory':   'screen-12-memory.png',
    'journey':  'screen-06-journey.png',
    'private':  'screen-05-private-space.png',
    'reflect':  'screen-10-reflection.png',
    'ondevice': 'screen-14-ondevice.png',
    'crisis':   'screen-08-crisis.png',
}

# Same 8 frames / same copy as produce_v5.py — design unchanged.
FRAMES = [
    ('01_you-look-after-them', 'You look after them.',
     'CARER looks after a little of you.',   'welcome'),
    ('02_companion-listens',   'A companion who listens.',
     'Present for you, whenever you need.',  'exchange'),
    ('03_words-remembered',    'Words, remembered.',
     'Every conversation, privately kept.',  'memory'),
    ('04_journey',             'Your journey, mapped.',
     "See how far you've come.",             'journey'),
    ('05_private-space',       'Your space. Private.',
     'Safe to think, feel, and be honest.',  'private'),
    ('06_no-scores',           'Not a score.<br>Not a tracker.',
     'A companion, not a tool.',             'reflect'),
    ('07_private-by-design',   'Private by design.',
     'Your data stays on your device.',      'ondevice'),
    ('08_help-one-tap',        'Help, one tap away.',
     'Support whenever you need it.',        'crisis'),
]

# ── Layout: uniform downscale of the 6.9" constants ──────────────────────────
# Source slot 1320×2868 → target 1284×2778.
#   height ratio = 2778/2868 = 0.96862   width ratio = 1284/1320 = 0.97273
# We scale everything by the SMALLER (height) factor so the composition can
# never overflow vertically; the ~5px of slack in width simply becomes a
# fractionally wider gradient margin. Uniform factor ⇒ zero distortion.

K = CH / 2868          # 0.9686192...
s = lambda v: round(v * K)

LT, LM, LW, LG      = s(87), s(56), s(42), s(12)        # logo block
H1G, H1S, H1MW      = s(115), s(108), s(1200)           # headline
PG,  PS,  PMW       = s(50), s(38), s(1060)             # support line
PHT                 = s(746)                            # phone top
BZ                  = s(18)                             # bezel
FBR, SBR            = s(64), s(46)                      # frame / screen radius
IW,  IH             = s(134), s(30)                     # dynamic island

# Phone body: derive height from width so the inner screen keeps the exact
# aspect used at 6.9" (1024×2218), rather than rounding each axis separately.
PHW        = s(1060)
_screen_w  = PHW - 2 * BZ
_screen_h  = round(_screen_w * 2218 / 1024)
PHH        = _screen_h + 2 * BZ

# ── HTML (verbatim structure from produce_v5.single_html) ────────────────────

def single_html(L, cw, ch, aurora,
                lt, lm, lw, lg,
                h1g, h1s, h1mw, pg, ps, pmw,
                pht, phw, phh, bz, fbr, sbr, iw, ih,
                scr, h1, p):
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Lora;src:url('file://{L}') format('truetype');font-weight:100 900}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{cw}px;height:{ch}px;overflow:hidden;position:relative;{aurora}}}
.hdr{{position:absolute;top:0;left:0;right:0;
  display:flex;flex-direction:column;align-items:center;
  padding-top:{lt}px;text-align:center}}
.logo{{display:flex;align-items:center;gap:{lg}px;white-space:nowrap}}
.lm{{width:{lm}px;height:{lm}px;flex-shrink:0}}
.lw{{font-family:Lora,serif;font-size:{lw}px;font-weight:500;color:#A46349;letter-spacing:-.02em}}
h1{{margin-top:{h1g}px;font-family:Lora,serif;font-size:{h1s}px;font-weight:750;color:#4A3528;
  line-height:1.18;letter-spacing:-.03em;max-width:{h1mw}px}}
p{{margin-top:{pg}px;font-family:-apple-system,Arial,sans-serif;font-size:{ps}px;font-weight:400;
  color:#A08C82;letter-spacing:-.005em;max-width:{pmw}px}}
.pw{{position:absolute;top:{pht}px;left:50%;transform:translateX(-50%);
  width:{phw}px;height:{phh}px}}
.pf{{position:relative;width:100%;height:100%;background:#1A1A1C;
  border-radius:{fbr}px;
  box-shadow:0 60px 140px rgba(0,0,0,.28),0 0 90px rgba(190,148,188,.16)}}
.di{{position:absolute;top:{bz}px;left:50%;transform:translateX(-50%);
  width:{iw}px;height:{ih}px;background:#1A1A1C;border-radius:{ih//2}px;z-index:2}}
.sc{{position:absolute;top:{bz}px;bottom:{bz}px;left:{bz}px;right:{bz}px;
  border-radius:{sbr}px;overflow:hidden}}
.sc img{{width:100%;height:100%;object-fit:cover;display:block}}
</style></head><body>
<div class="hdr">
  <div class="logo"><div class="lm">{LOGO}</div><span class="lw">carer</span></div>
  <h1>{h1}</h1><p>{p}</p>
</div>
<div class="pw"><div class="pf"><div class="di"></div>
  <div class="sc"><img src="{scr}"></div></div></div>
</body></html>"""


def b64(p):
    buf = io.BytesIO(); Image.open(p).save(buf, 'PNG')
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


async def snap(page, html, W, H, out, tag):
    f = HTML_DIR / f"{tag}.html"
    f.write_text(html, encoding='utf-8')
    await page.goto(f"file://{f}", wait_until='domcontentloaded')
    await page.wait_for_timeout(1200)
    buf = await page.screenshot(type='png', clip={'x':0,'y':0,'width':W,'height':H})
    img = Image.open(io.BytesIO(buf)).convert('RGB')   # RGB ⇒ no alpha (Apple rejects alpha)
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, 'PNG')
    print(f"  {out.relative_to(STORE)}  {img.size}  {img.mode}")


async def main():
    L = LORA.as_posix()
    print(f"=== iPhone App Store 6.5\" — {CW}×{CH} ===")
    print(f"  uniform scale from 6.9\" layout: k={K:.6f}")
    print(f"  phone {PHW}×{PHH}  bezel {BZ}  screen {_screen_w}×{_screen_h}"
          f"  bottom={PHT+PHH} (canvas {CH}, overhang {PHT+PHH-CH})")
    print(f"  headline {H1S}px  support {PS}px  logo {LM}px")

    SCRS = {k: b64(SRC / v) for k, v in SCR_MAP.items()}
    print(f"  {len(SCRS)} source screens loaded\n")

    async with async_playwright() as pw:
        br  = await pw.chromium.launch()
        ctx = await br.new_context(viewport={'width':CW,'height':CH}, device_scale_factor=1)
        pg  = await ctx.new_page()
        for slug, h1, p, pri_k in FRAMES:
            html = single_html(L, CW, CH, AP,
                               LT, LM, LW, LG,
                               H1G, H1S, H1MW, PG, PS, PMW,
                               PHT, PHW, PHH, BZ, FBR, SBR, IW, IH,
                               SCRS[pri_k], h1, p)
            await snap(pg, html, CW, CH, STORE / OUT_SUBDIR / f"{slug}.png",
                       f"i65-{slug}")
        await ctx.close()
        await br.close()

    print("\n=== Verify (App Store Connect 6.5\" contract) ===")
    PERMITTED = {(1242, 2688), (2688, 1242), (1284, 2778), (2778, 1284)}
    control = (CW, CH) not in PERMITTED   # e.g. the 1320×2868 fidelity control
    ok = fail = 0
    for png in sorted((STORE / OUT_SUBDIR).glob('*.png')):
        img  = Image.open(png)
        good = img.size == (CW, CH) and img.mode == 'RGB' and (control or img.size in PERMITTED)
        note = '  (control frame — not an ASC 6.5" size)' if control else ''
        print(f"  {'OK  ' if good else 'FAIL'} {png.name}  {img.size}  {img.mode}{note}")
        ok, fail = (ok + 1, fail) if good else (ok, fail + 1)
    print(f"\n  {ok}/8 OK  fail={fail}")
    if fail:
        raise SystemExit(1)

asyncio.run(main())
