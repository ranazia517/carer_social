# CARER — "The Kept Light" logo assets

Clean, multi-format masters of the approved CARER app logo. The mark is a bold,
near-circular **C** (thick ring, right-side opening, round terminals) holding a
small **kept-light dot** — a warm dawn gradient — in its mouth at vertical centre.

---

## Colour (locked, sampled from the approved artwork)

| Token            | Hex        | Use |
|------------------|------------|-----|
| **Clay / terracotta** | `#A46349` | Primary mark + wordmark ink. The brand's signature colour. |
| **Cream**        | `#FAF2E8`  | Reversed ink on dark/clay surfaces; light tile fill. |
| **Espresso**     | `#4A3528`  | Supporting dark ink (body text on cream). |
| **Dawn dot** (radial) | `#F4CDA6` → `#E4A79E` → `#D5A3B2` | Kept-light dot: peach centre → rose → lavender edge. |
| **Aurora tile** (diagonal) | `#EFC9A6` → `#E4A89E` → `#D3A0B4` | Primary app-icon tile: peach → rose → lavender. |
| **Warm-dark C** (vertical) | `#E7B89A` → `#A46349` | `mark-warmdark` C gradient (peach → clay). |

> Note: the shared brand system also references a warmer clay token `#A8663C`
> (and the aurora tile base reads ~`#A8664C`). The mark itself is locked to the
> sampled **`#A46349`** to match the approved master exactly.

## Type

- Wordmark **"carer"** — all-lowercase, **Lora** (soft serif, SIL Open Font License), weight ~500.
- Bundled at `fonts/Lora-VariableFont_wght.ttf`.
- Text-based SVGs declare a fallback stack: `Lora, Georgia, 'Times New Roman', serif`.
- Every wordmark/lockup master also ships an **`-outlined.svg`** with the text
  converted to vector paths (font-independent — use these for rasterising/handoff).

---

## What's here

```
svg/    14  vector masters (+ -outlined lockup/wordmark)
png/    68  transparent rasters
jpeg/    6  flattened on cream #FAF2E8 (no alpha)
tiff/    3  lossless (LZW)
pdf/     2  vector
ico/     1  favicon.ico (16/32/48)
fonts/   1  Lora variable TTF
```

### SVG masters (`svg/`)
| File | Description |
|------|-------------|
| `mark-primary.svg`   | Clay C + dawn-gradient dot (transparent). **Default mark.** |
| `mark-mono.svg`      | Flat clay C + clay dot (single ink). |
| `mark-cream.svg`     | Cream C + dot — reverse onto dark/clay. |
| `mark-warmdark.svg`  | Peach→clay gradient C + dawn dot — for warm-dark surfaces. |
| `wordmark.svg` / `-outlined.svg` | "carer" in Lora, clay. |
| `lockup-horizontal.svg` / `-outlined.svg` | Mark + "carer" side by side, baseline-aligned. |
| `lockup-stacked.svg` / `-outlined.svg`    | Mark centred above "carer". |
| `appicon-aurora.svg` | **Primary app icon** — dawn aurora squircle + cream mark. |
| `appicon-clay.svg`   | Clay squircle + cream mark. |
| `appicon-cream.svg`  | Cream squircle + clay mark. |
| `favicon.svg`        | Simplified mark tuned to read at 16 px. |

### Raster sizes
- **Marks** (`mark-*`, `favicon`): 1024, 512, 256, 128, 64, 32, 16
- **Wordmark / lockups**: 1024, 512, 256, 128, 64 (smaller sizes omitted — text unreadable)
- **App icons**: 1024, 512, 256, 180, 120, 64
- **JPEG** (flattened cream): `mark-primary`, `lockup-horizontal`, `appicon-aurora` @ 1024, 512
- **TIFF** (lossless): same three @ 1024
- **PDF** (vector): `mark-primary`, `lockup-horizontal`
- **ICO**: `favicon.ico` bundling 16/32/48

---

## Usage guidance

**Which file where**
- App UI / web mark → `svg/mark-primary.svg` (or `png/mark-primary-*.png`).
- On clay or photographic/dark backgrounds → `mark-cream` or `mark-warmdark`.
- Single-colour print, embroidery, stamps → `mark-mono`.
- Website favicon → `ico/favicon.ico` + `png/favicon-32.png`.
- Marketing lockups → `lockup-horizontal` (wide) / `lockup-stacked` (square-ish).
- Print / vector handoff → `pdf/` and the `-outlined.svg` masters.

**Clearspace** — keep free space around the mark equal to the stroke width of the
C (≈ ¼ of the mark's height) on all sides. For lockups, use the C's stroke width
as the minimum margin.

**Minimum size** — mark: 20 px digital / 6 mm print. Favicon variant handles
16 px. Wordmark: keep "carer" ≥ 64 px wide.

**Do** reverse the mark to cream on clay/dark. **Don't** recolour the C outside the
tokens above, rotate it, stretch it, or fill the C's opening.

## App icons (Flutter / iOS)

The app-icon PNGs are export-ready for `flutter_launcher_icons` and
`Assets.xcassets`:
- `appicon-aurora-1024.png` → iOS `AppIcon` / Android adaptive foreground source.
- 180/120 → iOS `@3x`/`@2x`; 512/256/64 → Android densities.

⚠️ These are **not** wired in — this drop does **not** overwrite the app's current
launcher icons. Wire them deliberately in a separate change.
