# CARER Social Kit

On-brand social card generator + caption library. One command per new post.

## Render a card

```bash
python3 scripts/make_social_card.py \
  --headline "A little light, kept." \
  --support "For the person holding everything together." \
  --format square \
  --out ~/Desktop/tagline-square.png
```

Add `--screen path/to/screen.png` (a 1170×2532 PNG from the app) to drop an app screenshot into the composition.

## Formats

| Key | Size | Platform |
|---|---|---|
| `square` | 1080 × 1080 | Instagram feed |
| `portrait` | 1080 × 1350 | Instagram portrait |
| `story` | 1080 × 1920 | Instagram / Facebook Story |
| `landscape` | 1200 × 630 | Facebook, LinkedIn |
| `x` | 1600 × 900 | X (Twitter), LinkedIn banner |

## App screens

Source app screenshots (1170×2532 RGB PNG) live at:
```
/private/tmp/claude-501/.../scratchpad/scr_v2_pngs/
```
Or re-capture from the running app via Playwright at @3× scale.

## Caption library

See `social-voice-and-captions.md` — 8 ready-to-use captions (launch, value-prop, tagline, is-this-you, privacy, free-forever, journey, crisis). Includes tone guidance and hashtag approach.

## Examples

Three rendered examples in `examples/`:
- `tagline-square.png` — 1080×1080, aurora, tagline only
- `value-prop-portrait.png` — 1080×1350, with app screen
- `is-this-you-story.png` — 1080×1920, copy-led, no screen

## Brand reference

Full brand tokens (colours, fonts, aurora CSS): `../brand/tokens.md` and `../brand/tokens.json`.
