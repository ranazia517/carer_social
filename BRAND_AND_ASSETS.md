# CARER — Brand & Assets Master Reference

> Single source of truth for all CARER brand decisions, asset locations, and quick-change runbooks.
> Update this file whenever a decision changes.

---

## 1. CARER in a Nutshell

| | |
|---|---|
| **Primary one-liner** | "You look after them. CARER is here to look after a little of you." |
| **Home hero** | "You hold everyone else. Let CARER hold a little of you." |
| **Tagline** | "A little light, kept." |
| **Category** | Mental wellness / companion app — NOT a clinical tool |
| **Age gate** | 18+ |
| **Price** | Free (no freemium, no in-app purchases) |
| **Made by** | Wellnetix Ltd (UK) |
| **Coverage** | Global — UK + US crisis resources built-in; Find A Helpline fallback for all other countries |
| **Status** | Pre-launch / early access — NOT yet live on App Store or Play Store |

### Voice in one sentence
Warm, calm, human. Anti-guilt. Never salesy. Never clinical. Speak like a trusted friend who has done their own therapy — not like an app.

---

## 2. Brand System

### Colours

| Token | Hex | Usage |
|---|---|---|
| `clay` | `#A46349` | Primary brand, logo, CTAs, headings |
| `clay-ref` | `#A8663C` | Brand reference / design tool match |
| `cream` | `#FAF2E8` | Page background |
| `espresso` | `#4A3528` | Primary text, display headings |
| `stone` | `#A08C82` | Secondary / support text |
| `peach` | `#F4CDA6` | Aurora gradient start |
| `rose` | `#E4A79E` | Aurora gradient mid |
| `lavender` | `#D5A3B2` | Aurora gradient end |
| `aurora-bg` | `#F7EFE7` | Aurora tile base |

### Aurora radial gradient (phone / portrait)
```css
background-color: #F7EFE7;
background-image:
  radial-gradient(58% 52% at 18% 20%, rgba(248,201,160,0.76) 0%, transparent 70%),
  radial-gradient(54% 50% at 84% 14%, rgba(244,197,180,0.66) 0%, transparent 70%),
  radial-gradient(64% 58% at 72% 84%, rgba(206,188,222,0.68) 0%, transparent 72%),
  radial-gradient(60% 54% at 10% 82%, rgba(237,190,198,0.65) 0%, transparent 72%),
  radial-gradient(52% 40% at 50%  0%, rgba(255,243,218,0.94) 0%, transparent 52%),
  radial-gradient(38% 30% at 50% 46%, rgba(248,222,196,0.36) 0%, transparent 58%);
```

### Aurora radial gradient (tablet / landscape)
```css
background-color: #F7EFE7;
background-image:
  radial-gradient(65% 56% at 14% 22%, rgba(248,210,162,0.78) 0%, transparent 68%),
  radial-gradient(60% 52% at 86% 18%, rgba(244,197,180,0.68) 0%, transparent 68%),
  radial-gradient(70% 60% at 70% 86%, rgba(206,188,222,0.70) 0%, transparent 72%),
  radial-gradient(65% 56% at 12% 82%, rgba(237,190,198,0.66) 0%, transparent 72%),
  radial-gradient(54% 42% at 50% -2%, rgba(255,243,218,0.96) 0%, transparent 50%),
  radial-gradient(44% 35% at 50% 50%, rgba(248,220,195,0.30) 0%, transparent 58%);
```

### Fonts

| Role | Family | File |
|---|---|---|
| Display / headings | **Lora** (variable, wght 100–900) | `carer_frontend/brand/logo/fonts/Lora-VariableFont_wght.ttf` |
| Body / UI | **Inter** (system stack fallback) | `inter` via system or CDN |

CSS shorthand:
```css
--font-display: 'Lora', Georgia, serif;
--font-body:    'Inter', -apple-system, 'Helvetica Neue', Arial, sans-serif;
```

### Logo — "Kept Light" mark

SVG inline (clay C-mark + dot — used in all rendered assets):
```svg
<svg viewBox="0 0 100 100" width="100%" height="100%" fill="none"
     xmlns="http://www.w3.org/2000/svg">
  <path d="M71.85 76.04 A34 34 0 1 1 71.85 23.96"
        stroke="#A46349" stroke-width="14.5" stroke-linecap="round"/>
  <circle cx="54.5" cy="56" r="7" fill="#A46349"/>
</svg>
```

Logo file locations (`carer_frontend/brand/logo/`):

| Variant | SVG | PNG sizes |
|---|---|---|
| Mark (primary clay) | `svg/mark-primary.svg` | `png/mark-primary-{16,32,64,128,256,512,1024}.png` |
| Mark (cream on dark) | `svg/mark-cream.svg` | `png/mark-cream-*.png` |
| Mark (mono) | `svg/mark-mono.svg` | `png/mark-mono-*.png` |
| Wordmark | `svg/wordmark.svg` | `png/wordmark-*.png` |
| Lockup horizontal | `svg/lockup-horizontal.svg` | `png/lockup-horizontal-*.png` |
| Lockup stacked | `svg/lockup-stacked.svg` | `png/lockup-stacked-*.png` |
| App icon (aurora bg) | `svg/appicon-aurora.svg` | `png/appicon-aurora-*.png` |
| App icon (clay bg) | `svg/appicon-clay.svg` | `png/appicon-clay-*.png` |
| Favicon | `svg/favicon.svg` | `png/favicon-*.png`, `ico/favicon.ico` |

Also in `brand-kit` branch of `carer_social`: `brand/svg/` contains copies of the key SVGs.

### Voice & Tone

- **Warm** — write to one person, not a crowd
- **Calm** — no urgency, no push notifications badgering
- **Anti-guilt** — "you're already doing so much" not "you should take care of yourself"
- **Non-clinical** — companion, not a diagnostic tool; never use disorder names or clinical language
- **Human** — contractions, short sentences, real feelings
- **Never salesy** — no "unlock", "premium", "supercharge"
- **Crisis-aware** — always note CARER is not an emergency service; crisis resources are always visible

---

## 3. Asset Inventory

### 3a. Website

| | |
|---|---|
| **Local path** | `~/Developer/carer/website/` |
| **Branch** | `carer_social@website` |
| **Deploy zip** | `~/Documents/carer-website-deploy.zip` |
| **Pages** | index, about, features, how-it-works, product, principles, who-its-for, safety, faq, contact, privacy, privacy-notice, cookies, accessibility, terms, onepager |
| **Assets** | `website/assets/` — `styles.css` (CSS custom properties / tokens), images |

**Quick-change runbook:**

| Change | What to edit |
|---|---|
| Page copy | Edit the relevant `.html` file directly |
| Brand colour | Edit `assets/styles.css` — change the `--color-*` custom properties at the top |
| Domain | Search-replace `[YOUR-DOMAIN]` across all `.html` files |
| Deploy | Zip `website/` → hPanel File Manager → upload to `public_html/`, or push to `website` branch and sync via Git |

**Pending:** Replace all `[YOUR-DOMAIN]` placeholders before going live.

---

### 3b. Store Assets

| | |
|---|---|
| **Local path** | `~/Developer/carer/store-assets/` |
| **Branch** | `carer_social@store-assets` (SHA `cc8656e`) |
| **Script** | `store-assets/scripts/produce_v5.py` (also `brand-kit@scripts/produce_v5.py`) |

**Slot sizes:**

| Slot | Canvas | Branch subdir |
|---|---|---|
| iPhone 6.9" | 1320 × 2868 | `app-store/iphone-6.9/` |
| iPad 13" | 2064 × 2752 | `app-store/ipad-13/` |
| Play phone | 1080 × 1920 | `google-play/phone/` |
| Play 7" tablet | 1080 × 1920 | `google-play/tablet-7/` |
| Play 10" tablet | 1200 × 1920 | `google-play/tablet-10/` |
| Feature graphic | 1024 × 500 | `google-play/feature-graphic/` |
| App Store icon | 1024 × 1024 | `store-assets/icons/appstore-icon-1024.png` |
| Play icon | 512 × 512 | `store-assets/icons/play-icon-512.png` |

**Regenerate all 41 frames + feature graphic:**
```bash
cd ~/Developer/carer/store-assets
python3 scripts/produce_v5.py
# Then rsync back to carer_social and push:
rsync -a ~/Developer/carer/store-assets/app-store/ \
         ~/Developer/carer/carer_social/store-assets/app-store/
rsync -a ~/Developer/carer/store-assets/google-play/ \
         ~/Developer/carer/carer_social/store-assets/google-play/
cd ~/Developer/carer/carer_social
git checkout store-assets
git add store-assets && git commit -m "Regenerate store screenshots"
git -c http.postBuffer=524288000 push origin store-assets
```

**Where to edit in `produce_v5.py`:**

| Change | Location in script |
|---|---|
| Frame headlines + support lines | `FRAMES` list (slug, headline_html, support, primary_screen, secondary_screen) |
| Headline → app screen mapping | `SCR_MAP` dict + `FRAMES` tuples (4th + 5th element) |
| App screen source PNGs | `SRC` path + `SCR_MAP` filenames |
| Brand aurora colours | `AP` (phone) / `AT` (tablet) / `AF` (feature) constants |
| Slot canvas sizes | `SINGLE_SLOTS` / `DUAL_SLOTS` tuples |
| Font | `LORA` path constant |
| Feature graphic headline | `feat_html()` function body (hardcoded "A little light, kept.") |

**Listing copy:** `store-assets/listing/appstore-listing.md` and `play-listing.md`

---

### 3c. Icons & Logo Files

| | |
|---|---|
| **Source** | `~/Developer/carer/carer_frontend/brand/logo/` |
| **Branch** | `carer_social@brand-logo` |
| **Formats** | SVG, PNG (multiple sizes), JPEG, TIFF, ICO, PDF |
| **Key files for apps** | `png/appicon-aurora-1024.png` (App Store), `png/appicon-clay-512.png` (Play) |

---

### 3d. Social Kit

| | |
|---|---|
| **Local path** | `~/Developer/carer/social-kit/` |
| **Branch** | `carer_social@brand-kit` (under `social-kit/`) |
| **Card script** | `social-kit/scripts/make_social_card.py` |
| **Examples** | `social-kit/examples/` |

**Render a new social card:**
```bash
python3 ~/Developer/carer/social-kit/scripts/make_social_card.py \
  --headline "Your headline here." \
  --support "Optional support line." \
  --format square \
  --out ~/Desktop/my-card.png
```
Formats: `square` (1080×1080), `portrait` (1080×1350), `story` (1080×1920), `landscape` (1200×630), `x` (1600×900)

Add `--screen path/to/screen.png` to include an app screenshot in the composition.

---

## 4. Open Placeholders

These must be filled before any public launch:

| Placeholder | Where it appears | Notes |
|---|---|---|
| `[YOUR-DOMAIN]` | All website `.html` files | Replace globally with real domain |
| ICO registration number | Privacy Notice, Cookie Policy, Terms | Register with ICO first |
| App Store links | Website, social posts | Not live yet |
| Google Play links | Website, social posts | Not live yet |
| Company registration number | Terms, About, Privacy | Wellnetix Ltd reg |
| DPO contact details | Privacy Notice | If required under UK GDPR |
| PPIE sign-off | Safety page, App Store description | Clinical safety / patient involvement |
| On-device model host URL | App settings / onboarding | LLM inference endpoint |

---

## 5. Key Decisions Log

| Decision | Status | Notes |
|---|---|---|
| Pricing | Free, no IAP | Confirmed |
| Age gate | 18+ | Confirmed |
| Crisis coverage | UK + US built-in, Find A Helpline global fallback | Backend `aff0909` / Frontend `cecd8eb` |
| Store category | Health & Fitness | iOS 17+ rating |
| Clinical classification | Non-clinical companion | Not a medical device |
| Solicitor review | Pending | Terms + Privacy |
| App Store / Play submission | Not yet submitted | Pre-launch |
| Company | Wellnetix Ltd (UK) | |
