# CARER Pitch Deck

20-slide investor / academic / public deck. Aurora brand, built in claude.ai/design ("CARER Pitch Deck" project file).

## Files

| File | Format | Size | Notes |
|---|---|---|---|
| `carer-pitch-deck.html` | Standalone HTML | ~862KB | Self-contained; opens in any browser. Navigate with ← → arrow keys. |
| `carer-pitch-deck.pptx` | PowerPoint | ~541KB | Exported from claude.ai/design as `CARER_Mobile_Wellbeing_App.pptx`; rename as needed. |
| `carer-pitch-deck.pdf` | PDF | ~1.2MB | Generated from the HTML via headless Chromium (print-to-PDF, landscape A4, `printBackground:true`). |
| `preview/deck-01.png` … `deck-20.png` | PNG previews | 1920×1080 | Playwright screenshots, one per slide. |

## Slide Map

| # | Title | Key content |
|---|---|---|
| 01 | Cover | "A little light, kept." — tagline + product descriptor |
| 02 | The Problem | Carers hold everyone together and quietly fall apart |
| 03 | The Scale | TAM: 13.6M UK unpaid carers; global scope |
| 04 | Who Carers Are | All kinds of caring relationships |
| 05 | Why Today's Support Fails | Gap in existing apps/services |
| 06 | The Solution | CARER overview |
| 07 | The Experience | App walkthrough / key screens |
| 08 | Product | Feature set — companion chat, memory, journey, crisis |
| 09 | Our Constitution | 7 rules (no scoring, no tracking, not a therapist…) |
| 10 | Safety & Ethics | Safety spine, crisis resources, content policy |
| 11 | Technology & Moat | On-device AI, private-by-architecture |
| 12 | The Science | Evidence base |
| 13 | Market Size | TAM / SAM / SOM |
| 14 | Go-to-Market | UK-first rollout |
| 15 | Business Model | Free for carers; sustainability model |
| 16 | Competitive Landscape | Positioning matrix |
| 17 | Status | Feature-complete, safety-reviewed |
| 18 | Roadmap | Now / 6mo / 12mo |
| 19 | Team & Governance | Wellnetix Ltd |
| 20 | Ask | CTA / funding ask |

## Open Items

- **Funding ask (slide 20):** Amount and use-of-funds not yet specified. Fill in before investor meetings.
- **App screen photos (slide 7):** Phone mockup placeholders — replace with real screenshots from `store-assets/scripts/` or the exported v2 PNGs in `scratchpad/scr_v2_pngs/`.
- **Team names (slide 19):** Team section to be completed with real names/bios before public use.
- **App Store / Play links:** App is pre-launch; update slide 17 or 20 when live.
- **Company registration number:** Wellnetix Ltd reg to be added to slide 19 / back matter.

## How to Update

**Edit in claude.ai/design:**
1. Open the "CARER Pitch Deck" project in claude.ai/design
2. Make edits on any slide
3. Re-export: Download → HTML (standalone) + PPTX
4. Copy exports to this folder (rename to `carer-pitch-deck.html` / `.pptx`)
5. Re-generate previews:
   ```bash
   python3 ~/Developer/carer/slides/render_previews.py
   ```

**Edit the PPTX directly:**
Open `carer-pitch-deck.pptx` in PowerPoint or Keynote. Re-export to PDF from there if needed.

**Re-generate PDF from HTML:**
```python
# Playwright print-to-PDF
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    br = pw.chromium.launch()
    pg = br.new_page()
    pg.goto("file:///path/to/carer-pitch-deck.html#1")
    pg.wait_for_timeout(3000)
    pg.pdf(path="carer-pitch-deck.pdf", format="A4", landscape=True,
           print_background=True, margin={"top":"0","right":"0","bottom":"0","left":"0"})
    br.close()
```

**Re-generate slide previews (all 20):**
```bash
python3 - << 'EOF'
import asyncio, io
from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image

HTML = Path("~/Developer/carer/slides/carer-pitch-deck.html").expanduser()
PREV = Path("~/Developer/carer/slides/preview").expanduser()
PREV.mkdir(exist_ok=True)

async def main():
    async with async_playwright() as pw:
        br = await pw.chromium.launch()
        ctx = await br.new_context(viewport={'width':1920,'height':1080})
        pg = await ctx.new_page()
        await pg.goto(f"file://{HTML}#1", wait_until='networkidle')
        await pg.wait_for_timeout(3000)
        await pg.click('body')
        for i in range(1, 21):
            buf = await pg.screenshot(type='png', clip={'x':0,'y':0,'width':1920,'height':1080})
            Image.open(io.BytesIO(buf)).convert('RGB').save(PREV / f"deck-{i:02d}.png", 'PNG')
            if i < 20:
                await pg.keyboard.press('ArrowRight')
                await pg.wait_for_timeout(800)
        await br.close()
asyncio.run(main())
EOF
```

Note: The HTML deck navigates with ← → arrow keys (single-page React app, 20 `<section>` elements; hash updates as `#1`–`#20` but the app must already be loaded — `goto(url#N)` resets to slide 1, so always use keyboard navigation for sequential capture).
