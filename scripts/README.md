# Store Screenshot Scripts

## Regenerate all 41 frames + feature graphic

```bash
cd ~/Developer/carer/store-assets
python3 scripts/produce_v5.py
```

The script renders all frames, does PIL size+mode verification, and prints a summary table. Then sync to git:

```bash
rsync -a ~/Developer/carer/store-assets/app-store/ \
         ~/Developer/carer/carer_social/store-assets/app-store/
rsync -a ~/Developer/carer/store-assets/google-play/ \
         ~/Developer/carer/carer_social/store-assets/google-play/
cd ~/Developer/carer/carer_social
git checkout store-assets
git add store-assets
git commit -m "Regenerate store screenshots: <reason>"
git -c http.postBuffer=524288000 push origin store-assets
```

## Where to edit

| Change | Location in `produce_v5.py` |
|---|---|
| **Frame headlines** | `FRAMES` list — 2nd element per tuple (HTML allowed, use `<br>` for line breaks) |
| **Support lines** | `FRAMES` list — 3rd element per tuple |
| **Headline → app screen** | `FRAMES` tuples 4th (primary) + 5th (secondary) — keys into `SCR_MAP` |
| **App screen source files** | `SCR_MAP` dict + `SRC` path constant at top of script |
| **Aurora colours** | `AP` (phone aurora), `AT` (tablet aurora), `AF` (feature graphic aurora) constants |
| **Font** | `LORA` path constant |
| **Slot canvas sizes / positions** | `SINGLE_SLOTS` list (iPhone, Play phone, Play 7") + `DUAL_SLOTS` list (iPad, Play 10") |
| **Feature graphic headline** | `feat_html()` function — headline hardcoded as `"A little light,<br>kept."` |

## Slot reference

| Slot | Canvas | Tuple list | Subdir |
|---|---|---|---|
| iPhone 6.9" | 1320 × 2868 | `SINGLE_SLOTS[0]` | `app-store/iphone-6.9/` |
| Play phone | 1080 × 1920 | `SINGLE_SLOTS[1]` | `google-play/phone/` |
| Play 7" | 1080 × 1920 | `SINGLE_SLOTS[2]` | `google-play/tablet-7/` |
| iPad 13" | 2064 × 2752 | `DUAL_SLOTS[0]` | `app-store/ipad-13/` |
| Play 10" | 1200 × 1920 | `DUAL_SLOTS[1]` | `google-play/tablet-10/` |
| Feature graphic | 1024 × 500 | (hardcoded in `main()`) | `google-play/feature-graphic/` |

## Header layout

All frames use a flex-column `.hdr` block: logo → h1 (margin-top gap) → p (margin-top gap).
This ensures the support line always sits below the full headline even when it wraps to 2 lines.
Gaps are the 9th param (`h1g`) and 12th param (`pg`) in each slot tuple.

## Dependencies

```
pip install playwright pillow
playwright install chromium
```
