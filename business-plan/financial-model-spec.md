# CARER — Financial Model Spec (build `financial-model.xlsx` from this)

All figures **illustrative / [owner-set]**, GBP, fully-loaded. Model is lean + scenario-based; the point is the *shape* (near-zero marginal cost, grant-then-partnership funding), not false precision. Build with the `xlsx` skill; aurora accents (headers clay `#A8663C` on cream `#FAF2E8`, espresso `#4A3528` text); number format £#,##0; a clearly-labelled "ILLUSTRATIVE — owner to finalise" banner on each sheet.

## Sheet 1 — "Assumptions" (drivers, editable)
| Driver | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| Team FTE | 4 | 6 | 9 |
| Blended cost / FTE | £70,000 | £72,000 | £74,000 |
| Infrastructure (on-device → low) | £12,000 | £24,000 | £48,000 |
| Compliance / legal / audit (DCB0129, DPO, ICO, security) | £40,000 | £45,000 | £50,000 |
| Evidence / PPIE / research study | £15,000 | £60,000 | £40,000 |
| GTM / partnerships / marketing | £20,000 | £50,000 | £90,000 |
| Product / design / tooling / misc | £15,000 | £20,000 | £25,000 |
| Partnership seats (carers covered) | 0 | ~1,500 | ~9,000 |
| Partnership price / carer / month | £3.00 | £3.00 | £3.00 |
| Supporter donations | £2,000 | £10,000 | £25,000 |

## Sheet 2 — "Costs" (from drivers; add a Total row + 3-yr total)
People = FTE × cost/FTE → Y1 £280,000 · Y2 £432,000 · Y3 £666,000.
Plus the five cost lines above. Total cost: **Y1 ≈ £382,000 · Y2 ≈ £631,000 · Y3 ≈ £919,000 · 3-yr ≈ £1.93m.**

## Sheet 3 — "Funding & revenue"
| Source | Year 1 | Year 2 | Year 3 | Note |
|---|---|---|---|---|
| Grants (non-dilutive) | £200,000 | £350,000 | £100,000 | SBRI ≤£200k; NIHR Catalyst £150k; Innovate UK £200k |
| Mission seed capital | £400,000 | £400,000 | £0 | Patient/mission investor(s) |
| B2B2C partnership revenue | £0 | £54,000 | £324,000 | seats × price × 12 (Y2 1,500·£3·12; Y3 9,000·£3·12) |
| Supporter donations | £2,000 | £10,000 | £25,000 | optional "keep the light on" |
| **Total inflow** | **£602,000** | **£814,000** | **£449,000** | |

## Sheet 4 — "Cash summary"
Net (inflow − cost): Y1 +£220,000 · Y2 +£183,000 · Y3 −£470,000 (Y3 dip = team scale-up ahead of partnership ramp → the point where either partnership revenue accelerates or a Series-seed/major-grant tops up). Cumulative cash + a **runway** line. Show the **24-month funding need ≈ £1.01m gross cost, ~£0.55m grant-covered → ~£0.5–0.7m mission-seed bridge**, reconciling to the plan's **~£0.75m–£1.2m blended ask**.

## Sheet 5 — "Scenarios" (toggle: Base / Conservative / Stretch)
- **Base:** as above; first partnership Y2.
- **Conservative:** partnership slips to Y3 (Y2 partnership £0), retention lower → supporter −50%; larger seed / slower hiring needed. Show the wider funding gap.
- **Stretch:** 2 ICB/employer pilots in Y2 (seats ×2), faster Y3 ramp (seats ~15,000), supporter ×2 → path to near-break-even in Y3.

Include a short **Unit-economics** box: marginal cost to serve one more carer ≈ **£0** (on-device inference); cost-to-serve is fixed (team + compliance), so every partnership seat is near-pure contribution to sustainability. This is the model's whole thesis.
