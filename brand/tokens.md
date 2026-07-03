# CARER Brand Tokens

Machine-readable version: `tokens.json`. This file is the human-readable companion.

## Colours

```
clay        #A46349   Primary — logo, CTAs, display headings on cream
clay-ref    #A8663C   Brand reference (design tool swatch match)
cream       #FAF2E8   Page / screen background
espresso    #4A3528   Primary text, display headings
stone       #A08C82   Secondary / support text, captions
aurora-bg   #F7EFE7   Aurora tile base colour
peach       #F4CDA6   Aurora warm accent (top-left zone)
rose        #E4A79E   Aurora warm mid
lavender    #D5A3B2   Aurora cool accent (bottom-right zone)
```

## Typography

| Role | Family | Weight range | File |
|---|---|---|---|
| Display / headings | Lora (variable) | 400–750 | `carer_frontend/brand/logo/fonts/Lora-VariableFont_wght.ttf` |
| Body / UI labels | Inter (or system) | 400–600 | system / CDN |

CSS variables (add to `:root`):
```css
--color-clay:      #A46349;
--color-cream:     #FAF2E8;
--color-espresso:  #4A3528;
--color-stone:     #A08C82;
--color-aurora-bg: #F7EFE7;

--font-display: 'Lora', Georgia, serif;
--font-body:    'Inter', -apple-system, 'Helvetica Neue', Arial, sans-serif;
```

## Logo

SVG files in `carer_frontend/brand/logo/svg/` (copies in this repo: `brand/svg/`):

| File | Use |
|---|---|
| `mark-primary.svg` | Standalone mark, clay on transparent |
| `mark-cream.svg` | Mark, cream (for dark backgrounds) |
| `mark-mono.svg` | Single-colour mark |
| `wordmark.svg` | "carer" wordmark only |
| `lockup-horizontal.svg` | Mark + wordmark side by side |
| `lockup-stacked.svg` | Mark + wordmark stacked |
| `appicon-aurora.svg` | App icon with aurora background |
| `appicon-clay.svg` | App icon, clay background |

## Aurora Gradient

The aurora is a layered radial-gradient composition. Two variants:

**Phone / portrait** — used on iPhone + Play phone + Play 7" store screenshots and social portrait cards.

**Tablet / landscape** — used on iPad + Play 10" screenshots and landscape social cards.

Full CSS strings are in `tokens.json` → `aurora.phone` and `aurora.tablet`.

Quick inline (phone):
```css
background-color: #F7EFE7;
background-image:
  radial-gradient(58% 52% at 18% 20%, rgba(248,201,160,.76) 0%, transparent 70%),
  radial-gradient(54% 50% at 84% 14%, rgba(244,197,180,.66) 0%, transparent 70%),
  radial-gradient(64% 58% at 72% 84%, rgba(206,188,222,.68) 0%, transparent 72%),
  radial-gradient(60% 54% at 10% 82%, rgba(237,190,198,.65) 0%, transparent 72%),
  radial-gradient(52% 40% at 50%  0%, rgba(255,243,218,.94) 0%, transparent 52%),
  radial-gradient(38% 30% at 50% 46%, rgba(248,222,196,.36) 0%, transparent 58%);
```
