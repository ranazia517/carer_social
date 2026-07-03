#!/usr/bin/env python3
"""CARER store-asset production v5 — 41 frames + feature graphic.
All slots use corrected composition: phone width set so screen extends past
canvas bottom (no black), full-width screen fit, no horizontal clipping.
"""
import asyncio, io, base64
from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image

SCRATCH  = Path("/private/tmp/claude-501/-Users-ayeshazia-Developer-carer/"
               "e872dd82-b574-48aa-9058-c57ab058a11c/scratchpad")
SRC      = SCRATCH / "scr_v2_pngs"
LORA     = Path.home() / "Developer/carer/carer_frontend/brand/logo/fonts/Lora-VariableFont_wght.ttf"
STORE    = Path.home() / "Developer/carer/store-assets"
HTML_DIR = SCRATCH / "html_v5"; HTML_DIR.mkdir(exist_ok=True)

# ── Assets ──────────────────────────────────────────────────────────────────

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

AT = ("background-color:#F7EFE7;background-image:"
      "radial-gradient(65% 56% at 14% 22%,rgba(248,210,162,.78) 0%,transparent 68%),"
      "radial-gradient(60% 52% at 86% 18%,rgba(244,197,180,.68) 0%,transparent 68%),"
      "radial-gradient(70% 60% at 70% 86%,rgba(206,188,222,.70) 0%,transparent 72%),"
      "radial-gradient(65% 56% at 12% 82%,rgba(237,190,198,.66) 0%,transparent 72%),"
      "radial-gradient(54% 42% at 50% -2%,rgba(255,243,218,.96) 0%,transparent 50%),"
      "radial-gradient(44% 35% at 50% 50%,rgba(248,220,195,.30) 0%,transparent 58%)")

AF = ("background-color:#F7EFE7;background-image:"
      "radial-gradient(60% 80% at 0% 50%,rgba(248,201,160,.72) 0%,transparent 68%),"
      "radial-gradient(50% 80% at 100% 30%,rgba(244,197,180,.60) 0%,transparent 68%),"
      "radial-gradient(70% 100% at 60% 100%,rgba(206,188,222,.65) 0%,transparent 72%),"
      "radial-gradient(45% 60% at 45% 0%,rgba(255,243,218,.90) 0%,transparent 50%),"
      "radial-gradient(35% 50% at 25% 50%,rgba(248,222,196,.30) 0%,transparent 56%)")

# ── Frames & screens ─────────────────────────────────────────────────────────

SCR_MAP = {
    'welcome':  '01_onboarding_welcome.png',
    'exchange': '03_onboarding_first_exchange.png',
    'memory':   '12_inline_memory_card.png',
    'journey':  '06_journey.png',
    'private':  '05_private_space.png',
    'reflect':  '10_reflection_no_score.png',
    'ondevice': '14_on_device_setup.png',
    'crisis':   '08_crisis_sheet.png',
}

# (slug, headline_html, support, primary_screen_key, secondary_screen_key)
FRAMES = [
    ('01_you-look-after-them', 'You look after them.',
     'CARER looks after a little of you.',         'welcome',  'exchange'),
    ('02_companion-listens',   'A companion who listens.',
     'Present for you, whenever you need.',         'exchange', 'memory'),
    ('03_words-remembered',    'Words, remembered.',
     'Every conversation, privately kept.',         'memory',   'journey'),
    ('04_journey',             'Your journey, mapped.',
     "See how far you've come.",                   'journey',  'private'),
    ('05_private-space',       'Your space. Private.',
     'Safe to think, feel, and be honest.',         'private',  'reflect'),
    ('06_no-scores',           'Not a score.<br>Not a tracker.',
     'A companion, not a tool.',                    'reflect',  'ondevice'),
    ('07_private-by-design',   'Private by design.',
     'Your data stays on your device.',             'ondevice', 'crisis'),
    ('08_help-one-tap',        'Help, one tap away.',
     'Support whenever you need it.',               'crisis',   'welcome'),
]

# ── Slot configs ─────────────────────────────────────────────────────────────
# phone_h is computed so screen slot (phone_w-2*bz) × (phone_h-2*bz) matches
# source aspect 1170:2532, and the phone extends past the canvas bottom.

SINGLE_SLOTS = [
    # (name, cw, ch, aurora,
    #  logo_top(=hdr padding-top), mark, word, gap,
    #  h1_gap(margin-top below logo), h1_sz, h1_maxw,
    #  p_gap(margin-top below h1),   p_sz,  p_maxw,
    #  ph_top, ph_w, ph_h, bz, fbr, sbr, iw, ih,
    #  out_subdir)
    #
    # Header is block flow (.hdr flex-col) so p always sits BELOW headline,
    # even when headline wraps to 2 lines. No absolute top collision possible.
    #
    # iPhone 6.9":  ph_w=1060 → screen 1024×2218 (aspect 0.4617≈0.4622)
    #   header 2-line max bottom ≈ 87+56+115+254+50+57 = 619px < phone_top 746
    ('iphone-6.9', 1320, 2868, AP,
     87, 56, 42, 12,
     115, 108, 1200, 50, 38, 1060,
     746, 1060, 2254, 18, 64, 46, 134, 30,
     'app-store/iphone-6.9'),

    # Play phone 9:16:  ph_w=780 → screen 744×1611 (aspect 0.4618)
    #   header 2-line max bottom ≈ 54+46+50+208+38+47 = 443px < phone_top 499
    ('play-phone', 1080, 1920, AP,
     54, 46, 34, 10,
     50, 88, 980, 38, 31, 870,
     499, 780, 1647, 18, 48, 30, 99, 22,
     'google-play/phone'),

    # Play 7" — same canvas/layout as Play phone
    ('play-tab7', 1080, 1920, AP,
     54, 46, 34, 10,
     50, 88, 980, 38, 31, 870,
     499, 780, 1647, 18, 48, 30, 99, 22,
     'google-play/tablet-7'),
]

DUAL_SLOTS = [
    # (name, cw, ch, aurora,
    #  logo_top, mark, word, gap,
    #  h1_gap, h1_sz, h1_maxw, p_gap, p_sz, p_maxw,
    #  pri_top, pri_left, pri_w, pri_h, pri_bz, pri_fbr, pri_sbr, pri_iw, pri_ih,
    #  sec_top, sec_left, sec_w, sec_h, sec_bz, sec_fbr, sec_sbr, sec_iw, sec_ih,
    #  out_subdir)
    #
    # iPad 13":  header 2-line max bottom ≈ 70+80+43+298+40+59 = 590px < pri_top 715
    ('ipad-13', 2064, 2752, AT,
     70, 80, 60, 18,
     43, 126, 1900, 40, 50, 1700,
     715, 619, 1032, 2193, 18, 64, 46, 134, 30,
     846, 309,  908, 1924, 16, 60, 44, 118, 26,
     'app-store/ipad-13'),

    # Play 10" 5:8:  header 2-line max bottom ≈ 53+48+33+172+35+43 = 384px < pri_top 499
    ('play-tab10', 1200, 1920, AT,
     53, 48, 36, 11,
     33, 73, 1100, 35, 29, 1060,
     499, 312, 696, 1465, 18, 42, 24, 88, 20,
     590, 122, 644, 1358, 16, 38, 22, 80, 18,
     'google-play/tablet-10'),
]

# ── HTML generators ───────────────────────────────────────────────────────────

def single_html(L, cw, ch, aurora,
                lt, lm, lw, lg,
                h1g, h1s, h1mw, pg, ps, pmw,
                pht, phw, phh, bz, fbr, sbr, iw, ih,
                scr, h1, p):
    # .hdr is a top-anchored flex column: logo → h1 → p always stack in order
    # so p can never collide with h1 regardless of how many lines h1 takes.
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


def dual_html(L, cw, ch, aurora,
              lt, lm, lw, lg,
              h1g, h1s, h1mw, pg, ps, pmw,
              pri_top, pri_left, pri_w, pri_h, pri_bz, pri_fbr, pri_sbr, pri_iw, pri_ih,
              sec_top, sec_left, sec_w, sec_h, sec_bz, sec_fbr, sec_sbr, sec_iw, sec_ih,
              pri_scr, sec_scr, h1, p):
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
.pf{{position:relative;width:100%;height:100%;background:#1A1A1C}}
.di{{position:absolute;left:50%;transform:translateX(-50%);background:#1A1A1C;z-index:2}}
.sc{{position:absolute;overflow:hidden}}
.sc img{{width:100%;height:100%;object-fit:cover;display:block}}
.psec{{position:absolute;top:{sec_top}px;left:{sec_left}px;
  width:{sec_w}px;height:{sec_h}px;z-index:1;opacity:.92}}
.psec .pf{{border-radius:{sec_fbr}px;
  box-shadow:0 50px 100px rgba(0,0,0,.18),0 0 70px rgba(190,148,188,.10)}}
.psec .di{{top:{sec_bz}px;width:{sec_iw}px;height:{sec_ih}px;border-radius:{sec_ih//2}px}}
.psec .sc{{top:{sec_bz}px;bottom:{sec_bz}px;left:{sec_bz}px;right:{sec_bz}px;
  border-radius:{sec_sbr}px}}
.ppri{{position:absolute;top:{pri_top}px;left:{pri_left}px;
  width:{pri_w}px;height:{pri_h}px;z-index:2}}
.ppri .pf{{border-radius:{pri_fbr}px;
  box-shadow:0 75px 150px rgba(0,0,0,.30),0 0 110px rgba(190,148,188,.20)}}
.ppri .di{{top:{pri_bz}px;width:{pri_iw}px;height:{pri_ih}px;border-radius:{pri_ih//2}px}}
.ppri .sc{{top:{pri_bz}px;bottom:{pri_bz}px;left:{pri_bz}px;right:{pri_bz}px;
  border-radius:{pri_sbr}px}}
</style></head><body>
<div class="hdr">
  <div class="logo"><div class="lm">{LOGO}</div><span class="lw">carer</span></div>
  <h1>{h1}</h1><p>{p}</p>
</div>
<div class="psec"><div class="pf"><div class="di"></div>
  <div class="sc"><img src="{sec_scr}"></div></div></div>
<div class="ppri"><div class="pf"><div class="di"></div>
  <div class="sc"><img src="{pri_scr}"></div></div></div>
</body></html>"""


def feat_html(L, scr_a, scr_b):
    # Phone A (front): w=230, bz=12, screen 206×446, ph_h=470, top=-25 → bottom=445
    # Phone B (back):  w=200, bz=12, screen 176×381, ph_h=405, top=15  → bottom=420
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Lora;src:url('file://{L}') format('truetype');font-weight:100 900}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1024px;height:500px;overflow:hidden;position:relative;{AF}}}
.logo{{position:absolute;top:60px;left:70px;display:flex;align-items:center;gap:10px}}
.lm{{width:52px;height:52px;flex-shrink:0}}
.lw{{font-family:Lora,serif;font-size:38px;font-weight:500;color:#A46349;letter-spacing:-.02em}}
h1{{position:absolute;top:148px;left:70px;
  font-family:Lora,serif;font-size:58px;font-weight:750;color:#4A3528;
  line-height:1.18;letter-spacing:-.03em;max-width:460px}}
p{{position:absolute;top:318px;left:70px;
  font-family:-apple-system,Arial,sans-serif;font-size:24px;font-weight:400;
  color:#A08C82;letter-spacing:-.005em;max-width:440px}}
.pf{{position:relative;width:100%;height:100%;background:#1A1A1C}}
.di{{position:absolute;left:50%;transform:translateX(-50%);background:#1A1A1C;z-index:2}}
.sc{{position:absolute;overflow:hidden}}
.sc img{{width:100%;height:100%;object-fit:cover;display:block}}
.pa{{position:absolute;top:-25px;left:580px;width:230px;height:470px;z-index:2}}
.pa .pf{{border-radius:36px;
  box-shadow:0 50px 100px rgba(0,0,0,.28),0 0 70px rgba(190,148,188,.16)}}
.pa .di{{top:12px;width:80px;height:18px;border-radius:9px}}
.pa .sc{{top:12px;bottom:12px;left:12px;right:12px;border-radius:24px}}
.pb{{position:absolute;top:15px;left:710px;width:200px;height:405px;z-index:1;opacity:.88}}
.pb .pf{{border-radius:32px;
  box-shadow:0 35px 75px rgba(0,0,0,.18),0 0 50px rgba(190,148,188,.10)}}
.pb .di{{top:12px;width:68px;height:16px;border-radius:8px}}
.pb .sc{{top:12px;bottom:12px;left:12px;right:12px;border-radius:20px}}
</style></head><body>
<div class="logo"><div class="lm">{LOGO}</div><span class="lw">carer</span></div>
<h1>A little light,<br>kept.</h1>
<p>A companion for the caregiving journey.</p>
<div class="pb"><div class="pf"><div class="di"></div>
  <div class="sc"><img src="{scr_b}"></div></div></div>
<div class="pa"><div class="pf"><div class="di"></div>
  <div class="sc"><img src="{scr_a}"></div></div></div>
</body></html>"""


# ── Render helpers ────────────────────────────────────────────────────────────

def b64(p):
    buf = io.BytesIO(); Image.open(p).save(buf, 'PNG')
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()

async def snap(page, html, W, H, out, tag):
    f = HTML_DIR / f"{tag}.html"
    f.write_text(html, encoding='utf-8')
    await page.goto(f"file://{f}", wait_until='domcontentloaded')
    await page.wait_for_timeout(1200)
    buf = await page.screenshot(type='png', clip={'x':0,'y':0,'width':W,'height':H})
    img = Image.open(io.BytesIO(buf)).convert('RGB')
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, 'PNG')
    print(f"  {out.relative_to(STORE)}  {img.size}")


# ── Main ──────────────────────────────────────────────────────────────────────

async def main():
    L = LORA.as_posix()

    print("=== Loading screens ===")
    SCRS = {k: b64(SRC / v) for k, v in SCR_MAP.items()}
    print(f"  {len(SCRS)} screens loaded")

    async with async_playwright() as pw:
        br = await pw.chromium.launch()

        # ── Single-phone slots ─────────────────────────────────────────────
        for (slot_name, cw, ch, aurora,
             lt, lm, lw, lg,
             h1t, h1s, h1mw, pt, ps, pmw,
             pht, phw, phh, bz, fbr, sbr, iw, ih,
             out_sub) in SINGLE_SLOTS:
            print(f"\n=== {slot_name} {cw}×{ch} ===")
            ctx = await br.new_context(viewport={'width':cw,'height':ch}, device_scale_factor=1)
            pg  = await ctx.new_page()
            for slug, h1, p, pri_k, _ in FRAMES:
                html = single_html(L, cw, ch, aurora,
                                   lt, lm, lw, lg,
                                   h1t, h1s, h1mw, pt, ps, pmw,
                                   pht, phw, phh, bz, fbr, sbr, iw, ih,
                                   SCRS[pri_k], h1, p)
                await snap(pg, html, cw, ch,
                           STORE / out_sub / f"{slug}.png",
                           f"{slot_name}-{slug}")
            await ctx.close()

        # ── Dual-phone slots ───────────────────────────────────────────────
        for (slot_name, cw, ch, aurora,
             lt, lm, lw, lg,
             h1t, h1s, h1mw, pt, ps, pmw,
             pri_top, pri_left, pri_w, pri_h, pri_bz, pri_fbr, pri_sbr, pri_iw, pri_ih,
             sec_top, sec_left, sec_w, sec_h, sec_bz, sec_fbr, sec_sbr, sec_iw, sec_ih,
             out_sub) in DUAL_SLOTS:
            print(f"\n=== {slot_name} {cw}×{ch} ===")
            ctx = await br.new_context(viewport={'width':cw,'height':ch}, device_scale_factor=1)
            pg  = await ctx.new_page()
            for slug, h1, p, pri_k, sec_k in FRAMES:
                html = dual_html(L, cw, ch, aurora,
                                 lt, lm, lw, lg,
                                 h1t, h1s, h1mw, pt, ps, pmw,
                                 pri_top, pri_left, pri_w, pri_h, pri_bz, pri_fbr, pri_sbr, pri_iw, pri_ih,
                                 sec_top, sec_left, sec_w, sec_h, sec_bz, sec_fbr, sec_sbr, sec_iw, sec_ih,
                                 SCRS[pri_k], SCRS[sec_k], h1, p)
                await snap(pg, html, cw, ch,
                           STORE / out_sub / f"{slug}.png",
                           f"{slot_name}-{slug}")
            await ctx.close()

        # ── Feature graphic ────────────────────────────────────────────────
        print("\n=== feature-graphic 1024×500 ===")
        ctx = await br.new_context(viewport={'width':1024,'height':500}, device_scale_factor=1)
        pg  = await ctx.new_page()
        out = STORE / 'google-play' / 'feature-graphic' / 'feature-graphic-1024x500.png'
        html = feat_html(L, SCRS['welcome'], SCRS['exchange'])
        await snap(pg, html, 1024, 500, out, 'feature')
        await ctx.close()

        await br.close()

    # ── PIL verify ────────────────────────────────────────────────────────────
    print("\n=== Verify ===")
    EXPECT = {
        'app-store/iphone-6.9':            (1320, 2868),
        'app-store/ipad-13':               (2064, 2752),
        'google-play/phone':               (1080, 1920),
        'google-play/tablet-7':            (1080, 1920),
        'google-play/tablet-10':           (1200, 1920),
        'google-play/feature-graphic':     (1024,  500),
    }
    ok = fail = 0
    for png in sorted(STORE.rglob('*.png')):
        rel  = png.relative_to(STORE)
        key  = '/'.join(rel.parts[:2])
        img  = Image.open(png)
        exp  = EXPECT.get(key)
        good = exp and img.size == exp and img.mode == 'RGB'
        tag  = 'OK  ' if good else 'FAIL'
        print(f"  {tag} {rel}  {img.size}  {img.mode}")
        if good: ok += 1
        else:    fail += 1
    print(f"\n  {ok}/41 OK  fail={fail}")

asyncio.run(main())
