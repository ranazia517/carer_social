# CARER — Store Asset Kit

_Prepared 3 July 2026. Screenshot frames (device + headline + gradient) are produced in the next step from an approved design._

---

## Folder layout

```
store-assets/
├── icons/
│   ├── appstore-icon-1024.png   1024×1024 RGB, NO alpha — Apple-ready
│   └── play-icon-512.png        512×512 RGB — Play-ready
│
├── app-store/
│   ├── iphone-6.9/              iPhone 6.9" screenshots (1320×2868, PNG/JPEG, RGB)
│   ├── iphone-6.5/              iPhone 6.5" screenshots (1284×2778, PNG/JPEG, RGB)
│   └── ipad-13/                 iPad 13" screenshots go here (2064×2752, PNG/JPEG, RGB)
│
├── google-play/
│   ├── phone/                   Phone screenshots (1080×1920, PNG/JPEG)
│   ├── tablet-7/                7" tablet screenshots (1080×1920, PNG/JPEG)
│   ├── tablet-10/               10" tablet screenshots (1200×1920, PNG/JPEG)
│   └── feature-graphic/         Feature graphic (1024×500, PNG/JPEG)
│
├── listing/
│   ├── appstore-listing.md      App Store Connect copy — name, subtitle, promo, keywords, description
│   └── play-listing.md          Google Play Console copy — name, short desc, full desc, ratings guidance
│
├── source-screens/              14 app-screen PNGs copied from website/assets/img/screens/
│                                These are the reference content for screenshot production.
│
└── README.md                    This file
```

---

## Slot sizes (verified for 2026 submission requirements)

### Apple App Store

| Slot | Dimensions | Notes |
|------|-----------|-------|
| App icon | 1024 × 1024 px | RGB, **NO alpha**. Apple rejects alpha channels. |
| iPhone 6.9" screenshots | 1320 × 2868 px | PNG or JPEG, RGB, no alpha. Up to 10. |
| iPhone 6.5" screenshots | 1284 × 2778 px | Slot accepts ONLY 1242×2688 / 2688×1242 / 1284×2778 / 2778×1284. |
| iPad 13" screenshots | 2064 × 2752 px | PNG or JPEG, RGB, no alpha. Up to 10. |

- Portrait orientation required for all; landscape optional (separate slot).
- **The 6.9" and 6.5" slots are separate uploads and do not accept each other's
  files.** Uploading a 1320×2868 file into the 6.5" box fails validation. Use
  `app-store/iphone-6.9/` for the 6.9" box and `app-store/iphone-6.5/` for the
  6.5" box.
- First screenshot is the hero — shown in search results without tapping.
- Apple accepts both PNG and JPEG; PNG preferred for crisp UI text.

### Google Play

| Slot | Dimensions | Notes |
|------|-----------|-------|
| App icon | 512 × 512 px | PNG. Alpha allowed; use full-bleed square. |
| Phone screenshots | 1080 × 1920 px | PNG or JPEG. Up to 8. |
| 7" tablet screenshots | 1080 × 1920 px | PNG or JPEG. Up to 8. |
| 10" tablet screenshots | 1200 × 1920 px | PNG or JPEG. Up to 8. |
| Feature graphic | 1024 × 500 px | PNG or JPEG. Required for store listing. |

- Play requires at minimum 2 screenshots before publishing.
- Feature graphic is shown as the header image on the Play store listing page.

---

## Icon source

**Source file used:** `carer_frontend/brand/logo/png/appicon-aurora-square-1024.png`
- 1024×1024, RGB, no alpha — full-bleed aurora gradient background, mark centred.
- Chosen over `appicon-aurora-1024.png` (RGBA — has transparent corners, Apple-unsafe)
  and `appicon-aurora-bg-1024.png` (RGB — also suitable, but square variant is canonical icon form).

Icons generated with PIL/Pillow (LANCZOS downsample for 512):
- `icons/appstore-icon-1024.png` — 1024×1024 RGB ✓
- `icons/play-icon-512.png` — 512×512 RGB ✓

---

## Source screens — status and recommendation

### What's in `source-screens/`

14 PNG exports copied from `website/assets/img/screens/`:

| File | Width × Height | Notes |
|------|---------------|-------|
| screen-01-welcome.png | 780 × 1690 | Standard height |
| screen-02-scope.png | 780 × 1690 | Standard height |
| screen-03-first-exchange.png | 780 × 1690 | Standard height |
| screen-04-companion.png | 780 × 1916 | Slightly taller |
| screen-05-private-space.png | 780 × 1690 | Standard height |
| screen-06-journey.png | 780 × 1736 | Standard height |
| screen-07-grief.png | 780 × 1812 | Standard height |
| screen-08-crisis.png | 780 × 3998 | **Tall scroll** — crop to single screen |
| screen-09-settings.png | 780 × 2448 | **Scrolled** — crop to single screen |
| screen-10-reflection.png | 780 × 1690 | Standard height |
| screen-11-notifications.png | 780 × 856 | **Short** — partial screen only |
| screen-12-memory.png | 780 × 1690 | Standard height |
| screen-13-signpost.png | 780 × 2682 | **Scrolled** — crop |
| screen-14-ondevice.png | 780 × 1690 | Standard height |

### Which source to use for production screenshots

**Use the HTML source files, not these PNGs.**

The original self-contained HTML screens are at:
`carer_frontend/design-reference/screens/` (14 × .html, one per screen)

These are the authoritative pixel-perfect source and can be rendered at any resolution in a headless browser (Playwright, puppeteer) or Chrome DevTools Device Mode.

**Why the HTML source is better:**
- 780px wide is ~1× density. iPhone 6.9" store slot (1320×2868) needs the screens at ~1.7× width minimum, and Apple recommends 3× (pixel-perfect Retina). At 780px, upscaling to 1320px introduces blur.
- The HTML files can be rendered directly at e.g. 1242px wide (standard iPhone logical width × 3 = 3× Retina), then trimmed to the 1320×2868 canvas.
- Several of the website PNGs are scrolled composites (screen-08 at 3998px tall) — the HTML lets you render the exact viewport you need.

**Recommended screenshot production workflow (next step):**
1. Render each of the 14 HTML files headless at 1242 × 2688px (iPhone viewport at 3×).
2. Crop/pad to the target canvas (1320×2868 for iPhone 6.9").
3. Composite onto a branded frame (device mockup + gradient + headline) from the approved design.
4. Output to `app-store/iphone-6.9/` (PNG, RGB, no alpha).
5. Repeat at 820 × 1180px → 2064×2752 canvas for iPad 13".
6. For Play: render at 1080×1920 (phone) and 1200×1920 (10" tablet).

**These existing PNGs are useful as:**
- Content reference / art direction review — you can see exactly what's on each screen.
- Lower-res preview during design (for the approved mockup design step).

---

## Listing copy

See `listing/appstore-listing.md` and `listing/play-listing.md` for:
- All character-counted fields
- Category rationale (Health & Fitness, not Medical)
- Age/content rating guidance
- Support URL and privacy URL placeholders (update with confirmed domain)
- Console submission checklists

---

## Screenshot production — what's in this kit

All 8 composition frames have been rendered at each slot size (41 PNGs total).
See `MANIFEST.md` for the full file → slot → screen → headline mapping.

### Template design
Each portrait frame uses the aurora-dusk gradient background (cream #F7EFE7 → peach →
rose → lavender), the CARER logo mark + "carer" wordmark in Lora, a bold Lora headline,
a muted Inter support line, and a dark phone mockup (dynamic island, 60px border-radius,
aurora glow shadow) holding the rendered app screen. The phone bleeds slightly off the
bottom edge of each frame.

App screens were rendered headless from
`carer_frontend/design-reference/screens/*.html` at 390×844 viewport (2× scale → 780×1688)
with animations frozen at the first frame. The 780×1688 source is embedded in each
composition and displayed at the phone's screen content width; aspect-ratio 390/844 is
preserved exactly.

### Tablet-slot note
Tablet screenshots (ipad-13, play-tab7, play-tab10) compose the phone mockup on a wider
aurora canvas — a valid and common store composition style. The phone is centred with more
gradient field visible around it, visually distinguishing it from the phone-slot frames.
True tablet-optimised layouts (showing a tablet-proportion UI) would require tablet app
designs, which are not yet built.

---

## Owner actions before submission

1. **Confirm domain** — update all `[YOUR-DOMAIN]` placeholders in both listing files.
2. **Legal review** — solicitor sign-off on multi-jurisdiction privacy notice before the privacy URL goes live in store listings.
3. **Crisis config maintainer** — named human must be on record (launch blocker per the safety design).
4. **App Review notes** — copy the "Notes for Reviewers" text from `play-listing.md` into Play Console, and prepare equivalent notes for App Store Review (the crisis layer + age gate).
5. **Data safety / privacy nutrition labels** — complete both stores' data disclosure forms (on-device processing, optional encrypted backup, de-identified analytics).
