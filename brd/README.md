# CARER — Business Requirements Document

Requirements pack for **CARER** (Wellnetix Ltd) — the private, non-clinical AI wellbeing
companion for unpaid family carers. Compiled August 2026, **pre-launch**.

## Contents

- **`BRD.md`** — the full Business Requirements Document v1.0: purpose & scope, business
  objectives, problem statement, target users (six personas), product overview, functional
  requirements by module, non-functional requirements, data & privacy, safety & crisis
  handling, compliance, the anti-feature list, KPIs, assumptions, dependencies, and the open
  release gates and risks.

## What this document is

A **requirements** document — what MUST be true for CARER to be a legitimate, safe, and
releasable product. It is not a status report and not a marketing document.

It was compiled from the actual built product and its governing records (the carer
constitution, the locked `CONTRACT.md` API surface, the governance record, the developer
handoff, the crisis-localisation slice, and the business plan). Every requirement is traceable
to one of those sources; none was invented.

**No BRD existed before this one.**

## Authority

This BRD is **subordinate to `docs/CONSTITUTION.md`** in the product repos. Where the two
disagree, **the constitution wins.**

## Status — read this before quoting anything

- **The product is pre-launch. No real carer has used the live product.**
- The system is built end-to-end on the **dev/mock** path. Every external dependency —
  identity provider, LLM, managed database, KMS, object storage, push, crisis-config service —
  currently points at a mock or local implementation. Going live is a configuration change,
  not a rewrite.
- **All release gates are OPEN.** No sign-off, ratification, assessment, or registration has
  been obtained: the Clinical Safety Officer, Data Protection Officer, and crisis-config
  maintainer are **unappointed**; the PPIE lived-experience panel is **not convened**; the
  DPIA is a live unsigned document; ICO registration is outstanding. See §15.1 of `BRD.md`.
- **No regulatory clearance has been sought or obtained, and no clinical-efficacy claim is
  made anywhere in the document.**

## Positioning (non-negotiable)

CARER is an **independently-branded, UK, non-clinical** wellbeing companion for the unpaid
carer's **own inner life**. It is **not a medical device**, not therapy, not a diagnostic tool,
and not an emergency service. It gives **no advice about the carer or the person they care
for** — it signposts, and never advises or assesses either party.

The cared-for person is **never a user, never a data subject, and never profiled or
surveilled**.

## Open items for the founding team

Appoint the Clinical Safety Officer, DPO, and crisis-config maintainer · convene the PPIE
panel and ratify the crisis and safeguarding copy (currently PPIE-flagged placeholders) ·
finalise and sign the DPIA/ROPA · complete ICO registration · solicitor review of the legal and
consent basis · production wiring · owner review and merge of the region-aware crisis routing ·
close the remaining persona lanes.
