# CARER — Business Plan

*A private, always-free wellbeing companion for the people who do the caring.*

**Prepared by:** Wellnetix Ltd (United Kingdom)
**Product:** CARER
**Document status:** Working plan, v1 — July 2026. Pre-launch (early access).
**Confidential.** Figures marked *[owner-set]* are placeholders for the founding team to finalise.

---

## 1. Executive summary

CARER is a private, non-clinical AI wellbeing companion for unpaid family carers — the 5.8 million people in the UK and 63 million in the US who look after an ageing parent, an ill partner, a disabled child, or a relative living with a serious mental illness. It is not a care-management or logistics tool. It is a warm, always-available companion that listens without judgement, remembers what the carer has told it so they never have to explain twice, offers gentle nudges rather than scores or streaks, and puts calm, verified crisis support one tap away.

The problem is large, verified, and under-served. Around 63% of carers report that caring harms their own mental health, yet almost every product and public programme is aimed at the person receiving care, not the carer. The people holding families together are the ones with the least support.

CARER's wedge is a combination that no incumbent occupies at once: **emotional-first** (a companion, not a task manager), **privacy-first** (on-device AI, content-free signal sync, never sells data), and **free-first** (core and crisis support free forever, funded by mission-aligned partners rather than by charging exhausted carers). The well-funded caregiver-tech companies — Homethrive (~$78M raised), Wellthy (~$78M), ianacare (~$16.7M) — are US, human-concierge, care-navigation platforms sold through employers and health plans. They solve logistics. CARER solves the loneliness and load of the caring role itself, and does it privately and for free.

The technology thesis is now credible in a way it was not two years ago. On-device small language models (Phi-4-mini, Qwen3) have reached a capability level that matches much larger models on targeted tasks while running on a phone, at effectively **zero marginal cost per user** and with data that never leaves the device. This makes a free, private, planet-scale companion economically feasible for the first time.

CARER is built by Wellnetix Ltd, a UK company. The iOS app is in early access; Android follows. Crisis support is live and verified for the UK and US with a global fallback (Find A Helpline, 175+ countries). The core app, on-device model layer, privacy architecture, and legal foundation are already built.

**What we are raising / seeking:** a blended **[owner-set: ~£0.75m–£1.2m]** package of non-dilutive grants (SBRI Healthcare, NIHR Innovation Catalyst / i4i, Innovate UK) and mission-aligned seed capital to fund ~24 months of runway — enough to reach engagement validation, a clinical-safety and evidence base, and the first B2B2C partnership revenue that sustains the free model.

**The 3–5 year vision:** CARER becomes the default private, always-free wellbeing companion for unpaid carers worldwide, embedded in health and social-care carer pathways, and the source of a consented, de-identified evidence base that advances the science of carer wellbeing.

---

## 2. Company and mission

**Wellnetix Ltd** is the UK legal entity behind CARER. CARER is an independently-branded product with its own identity ("A little light, kept.") — deliberately separate from any clinical or diagnostic positioning.

**Mission:** to look after a little of the people who look after everyone else — privately, warmly, and without asking them to pay or to hand over their story.

**Operating principles** (these are product constraints, not slogans):

- **Non-clinical by design.** CARER is not therapy, not a medical device, not an emergency service, and says so plainly. It complements human and clinical support; it never replaces it.
- **Private by architecture, not by policy.** Privacy is enforced in code — on-device inference, content-free signal sync, optional and off-by-default cloud features — not merely promised in a notice.
- **Free where it matters, forever.** Core companionship and crisis support are free and always will be. Carers are never the revenue source for those.
- **Consent-based science.** De-identified, aggregated learnings can improve the product and advance carer research, but only with explicit opt-in consent, never sold, and never profiling the cared-for person.
- **18+, and honest about scope.** A hard age gate, with a warm signpost out for under-18 carers to appropriate youth services.

**Team.** A small founding team under Wellnetix Ltd. Named team and advisors are *[owner-set placeholder]*. The plan below identifies the two governance hires that gate credible healthcare partnerships — a **Clinical Safety Officer** and a **Data Protection Officer** — as near-term priorities.

---

## 3. The problem

Unpaid carers are the invisible infrastructure of every health and social-care system, and they are quietly breaking under the load.

- **The population is enormous and growing.** The UK has ~5.8 million unpaid carers providing care worth an estimated £184 billion a year (Carers UK). The US has ~63 million family caregivers, up ~45% since 2015, providing unpaid care valued at ~$1.01 trillion a year (AARP, *Valuing the Invaluable*, 2026).
- **Caring harms the carer's own health.** Around 63% of carers say caring has negatively affected their mental health (Carers UK, *State of Caring*). Roughly one in five informal carers is at risk of burnout. Loneliness, guilt, anticipatory grief, and the erosion of the carer's own identity are near-universal and rarely addressed.
- **Support is aimed at the wrong person.** Public programmes, apps, and services overwhelmingly target the care recipient. The carer is treated as a resource to be sustained, not a person to be supported. Even where statutory support exists (in England, the Care Act 2014 places a duty on local authorities to assess and meet eligible carers' needs), uptake is low, waits are long, and the support is practical rather than emotional.
- **The moments that matter happen at 2am, not in office hours.** The hardest parts of caring — the sleepless nights, the sudden crisis, the small daily griefs — do not fit a 9-to-5 appointment model. Carers need something that is there in the moment, private, and non-judgemental.

The result is a structural gap: the largest, most economically valuable, most at-risk group in the care system has the least support designed for *them*.

---

## 4. The product

CARER is a mobile companion (iOS live in early access; Android next) built around one idea: **be genuinely present for the carer, privately, whenever they need it.**

**Core experience.**

- **A companion that listens.** A warm, always-available conversational companion that meets the carer where they are, with no forms to fill and nothing to explain from scratch.
- **Your words, remembered.** CARER remembers what the carer has shared, so they never have to re-tell their story — a memory layer that makes the relationship feel continuous and known.
- **No scores. No streaks.** Deliberately no gamification, no guilt mechanics, no "you missed a day." Gentle, optional nudges instead of pressure.
- **Help, one tap away.** A calm, always-reachable crisis layer ("you're not alone") with verified, region-aware resources — UK and US fully supported and tested, with a global fallback (Find A Helpline, 175+ countries). Crisis support works offline, before sign-in, and independently of the AI model.
- **Space for the whole of it.** Reflection ("a moment for you"), a private space, a grief space for the after, and honest, disease-aware signposting to appropriate human and clinical help.

**How it is built (and why that matters commercially).**

- **On-device-first AI.** The companion runs on-device where possible (Apple Foundation Models / Android AICore, with a portable Phi-4-mini / Qwen3 tier via a single llama.cpp runtime). This gives near-zero marginal cost per user and privacy by architecture.
- **Privacy-first data model.** Content-free signal sync, encrypted sync, and a cloud fallback that is optional and off by default. The cared-for person is never profiled. Sensitive content stays on the device.
- **A safety "cage."** Model output passes through a guardrail system (generate → guardrail check → retry → safe fallback) with a fixed schema, so the companion stays inside its non-clinical, safe scope.
- **API-based backend.** Everything is exposed as versioned REST endpoints (Pydantic, Firebase auth); clients never couple directly to the database. This keeps the platform portable, auditable, and partnership-ready.

**What CARER is not:** a diagnosis tool, a therapy replacement, a care-scheduling/logistics platform, or an emergency service. Those boundaries are stated in-product and enforced in the safety layer.

---

## 5. Market

**Top-down sizing** (verified third-party estimates; ranges reflect differing methodologies):

| Layer | Definition | Figure | Source |
|---|---|---|---|
| **TAM** | Unpaid carers, UK + US | ~69 million people | Carers UK; AARP/NAC *Caregiving in the US 2025* |
| **Adjacent value pool** | Global mental-health apps market | ~$9bn (2025) → ~$23bn (2030); broader digital-mental-health ~$33bn (2025) → ~$180bn (2035) | MarketsandMarkets; Market Research Future |
| **SAM** | Smartphone-owning carers in supported English-speaking markets who would engage with a wellbeing companion | tens of millions | Derived |
| **SOM (3-yr)** | Realistically reachable engaged early-access + partnership-referred carers | *[owner-set target]* | Plan assumption |

**Demand is proven; the category's hard problem is retention.** Mental-health apps see very high uptake (~92% in a meta-analysis of RCTs) but historically weak adherence: pure self-tracking apps often retain under 10% at 90 days, while apps with a genuine relationship or human touch reach 20–35%. This is the single most important fact in the plan: **CARER's entire design — memory, a real sense of being known, gentle nudges, no guilt mechanics — is aimed precisely at the retention problem that kills wellbeing apps.** It is also the metric on which the business must be judged, and the plan instruments it from day one.

**Willingness to pay and the free model.** Consumers do pay for wellbeing (Calm and Headspace both ~$70/year), and iOS users in particular spend more. But the free segment of the mental-health-app market alone generated ~$6.1bn in 2025 — free is a proven route to reach and impact. CARER deliberately keeps the carer-facing core free and monetises through mission-aligned third parties (below), because charging exhausted, often financially-stretched carers for emotional support is both wrong for the mission and a weak acquisition model for this audience.

---

## 6. Competition and moat

**The landscape splits into three groups, and CARER sits in the white space between them.**

1. **Care-logistics / navigation platforms (well-funded, US, B2B2C):** Homethrive (~$78M raised; sold via employers and health plans), Wellthy (~$78M; family-care concierge), ianacare (~$16.7M; Series A included AARP; targeting 1M lives via B2B2C). These are excellent at *logistics* — coordinating tasks, navigating benefits, human care coaches. They are not emotional-companion products, they are not privacy-first, and they reach people through an employer or insurer, not directly.
2. **General wellbeing / mental-health apps (Calm, Headspace, AI companions):** broad self-care and meditation, or general AI chat companions. None is built *for the specific experience of caring* — the guilt, the anticipatory grief, the identity loss, the 2am crisis — and the AI-companion category carries real safety and trust concerns for a vulnerable audience.
3. **Charities and statutory support (Carers UK, local authorities):** trusted and essential, but under-resourced, practical rather than emotional, and not always available in the moment.

**CARER's defensible position:**

- **Positioning moat:** the only product that is *carer-specific, emotional-first, private, and free*. Each incumbent would have to give up something core to their model to copy all four at once (the logistics players sell to employers and monetise seats; the wellbeing apps aren't carer-specific; the AI companions aren't privacy-first or safety-caged).
- **Architecture moat:** on-device, privacy-by-design AI is genuinely hard to retrofit onto a cloud-first product, and it is the credible answer to the trust problem that dogs AI mental-health tools.
- **Trust and safety moat:** a purpose-built safety cage, verified crisis localisation, and a governance path (DCB0129, DPO, PPIE) that most consumer apps will not invest in — and which becomes the passport to NHS / social-care partnerships.
- **Data-as-mission moat (consented):** a growing, de-identified, consented evidence base on carer wellbeing that no one else is positioned to build, feeding both product and published science.

**Honest risk:** the logistics incumbents are far better capitalised and could add an "AI companion" feature. CARER's counter is focus, privacy architecture, and the free/mission model they are structurally unlikely to adopt — plus speed to an evidence and partnership base.

---

## 7. Business model

**Principle: the carer never pays for the core. Mission-aligned third parties who benefit from healthier, more sustainable carers do.**

**Free forever (never monetised):** the companion, memory, nudges, and crisis support. No ads. Data never sold.

**Revenue lines (all downstream of, and subordinate to, the free core):**

1. **B2B2C partnerships (primary long-term engine).** Organisations with a duty or incentive to support carers license CARER to offer free to *their* carers, paid per-seat or per-population:
   - **Health & social care** — NHS Integrated Care Boards and local authorities carry statutory duties toward unpaid carers (Care Act 2014; Health and Care Act 2022 §25; Better Care Fund carers'-breaks funding). CARER can be a low-cost, always-on element of a carer-support offer.
   - **Employers** — ~1 in 7 workers is a carer; carer benefits reduce absenteeism and attrition. This is exactly the channel Homethrive, Wellthy, and ianacare have proven — but CARER offers a lighter, cheaper, privacy-first emotional-support layer rather than a full concierge.
   - **Carer charities and disease-specific organisations** — white-labelled or co-branded companion support.
2. **Optional individual supporter tier / donations.** For carers or supporters who *want* to contribute, a "keep the light on" supporter option — never a paywall on anything that matters.
3. **Grants and mission capital (bridge, not a business line).** Non-dilutive innovation funding (SBRI Healthcare up to £200k; NIHR Innovation Catalyst £150k + programme; NIHR i4i; Innovate UK £0.2–1.5m contracts) funds the validation and evidence phase before partnership revenue scales.

**Why the unit economics work:** because inference is on-device, the **marginal cost of serving one more carer is close to zero**. Cost is dominated by people (product, safety, partnerships) and compliance, not by usage. This is what lets the core be free at scale and lets partnership revenue flow largely to sustainability rather than to covering per-user cost.

---

## 8. Go-to-market

**Phase A — Direct early access (now).** Reach engaged early-access carers directly through the app stores, the website, carer communities, and organic/search. Goal: not scale, but *learning* — validate that carers form a real, retained relationship with CARER, and gather the wellbeing signal and testimony that everything else depends on.

**Phase B — Evidence + first partnerships (~12–24 mo).** Convert early-access learning and a real-world-evidence study into the credibility needed to sign the first one or two ICB/local-authority pilots and one or two employer deployments. The statutory duty on carers and the low cost-to-serve are the pitch; the safety governance and evidence are the proof.

**Phase C — Partnership-led scale (~24–36 mo).** Repeatable B2B2C motion across health/social-care commissioners, employers, and charities, in multiple countries, sustaining the free core.

**Positioning wedge throughout:** *carer-specific, private, always free.* That single line differentiates CARER from logistics platforms, general wellbeing apps, and AI companions simultaneously.

---

## 9. Operations, technology, and governance

**Technology.** On-device-first AI (Apple FM / AICore + portable Phi-4-mini/Qwen3 via llama.cpp); privacy-first data model (content-free signal sync, encrypted sync, optional off-by-default cloud fallback); a guardrail safety cage; an API-based backend (versioned REST, Pydantic, Firebase auth). The architecture is deliberately portable and auditable — a prerequisite for healthcare partnerships.

**Safety and clinical governance (the partnership passport).** CARER is non-clinical and does not *require* NHS clinical-safety certification to operate direct-to-consumer. But to partner with the NHS and social care, the credible path is to adopt the recognised standards voluntarily and early: **DCB0129** clinical-risk management (which requires a named **Clinical Safety Officer**, a Clinical Safety Case Report, and a Hazard Log), **DTAC** (the NHS Digital Technology Assessment Criteria — clinical safety, data protection, technical security, interoperability, usability/accessibility), and alignment with **NICE's Evidence Standards Framework** for digital health. Appointing a Clinical Safety Officer and a DPO, and registering with the ICO, are near-term governance milestones.

**Lived-experience governance (PPIE).** A patient-and-public-involvement / lived-experience panel of carers governs product and safety decisions — both the right thing to do and a credibility marker for funders and partners.

**Data protection.** UK GDPR / DPA 2018 as the baseline, with region-aware handling for the EU (GDPR), California (CCPA/CPRA), and other jurisdictions as the footprint grows; special-category (health/wellbeing) data and a research-consent basis mean a solicitor/DPO review before scale.

---

## 10. Financial plan (summary)

A lean, honest, scenario-based model accompanies this plan (`financial-model.xlsx`). Headlines:

- **Cost base is people + compliance, not compute.** Because inference is on-device, infrastructure is a minor line. The team scales from a small founding group to roughly **[owner-set] ~8–10 FTE** over three years, weighted toward product, safety/compliance, and partnerships.
- **Year 1 (validation):** funded primarily by non-dilutive grants + founder capital. Focus: retention validation, safety governance stand-up, Android launch. Revenue ~£0 by design.
- **Year 2 (evidence + first revenue):** grants + mission seed; first B2B2C pilots begin to produce modest recurring revenue; real-world-evidence study runs.
- **Year 3 (partnership ramp):** recurring B2B2C revenue from ICB/LA, employer, and charity contracts scales toward covering the (low, on-device) cost-to-serve and a growing share of the team — the path to mission-sustainability.
- **Funding ask:** a blended **[owner-set: ~£0.75m–£1.2m]** across grants and mission seed for ~24 months of runway to reach evidence + first partnership revenue. Because the model is free-to-carer and mission-driven, the ideal capital stack is *grant-heavy and patient*, not growth-equity-heavy.

**Key sensitivities:** retention (the single biggest driver of both impact and partnership value), speed to the first partnership contract, and grant timing. The model shows each as an explicit scenario.

---

## 11. Risks and mitigations

| # | Risk | Severity | Mitigation |
|---|---|---|---|
| 1 | **Retention** — wellbeing apps historically shed most users by D90 | High | Design is built around exactly this (memory, being known, gentle nudges, no guilt); instrument D7/D30/D90 from day one; human-warmth and reasons-to-return as first-class product work |
| 2 | **Free model needs sustained funding** before partnership revenue scales | High | Grant-heavy capital stack (SBRI/NIHR/Innovate UK); early partnership pilots; near-zero marginal cost means low burn per user |
| 3 | **Well-funded incumbents** add an AI companion | Medium-High | Focus, privacy-by-architecture, carer-specificity, and the free/mission model they are structurally unlikely to copy; speed to evidence + partnerships |
| 4 | **AI safety / trust** for a vulnerable audience | High | Safety cage, non-clinical scope enforced in code, verified crisis layer, human/clinical signposting, DCB0129 governance |
| 5 | **Regulatory / multi-jurisdiction** (health data, research consent, DTAC, EU/US law) | Medium-High | DPO + solicitor review before scale; ICO registration; region-aware legal already drafted; adopt DCB0129/DTAC voluntarily |
| 6 | **Clinical-safety credibility gap** blocks NHS partnerships | Medium | Appoint Clinical Safety Officer early; build the safety case and evidence base as a Phase-1 priority |
| 7 | **Key-person / small-team** concentration | Medium | Governance hires, PPIE panel, advisors, documented and API-based architecture |

---

## 12. The ask and use of funds

CARER is seeking a blended **[owner-set: ~£0.75m–£1.2m]** of non-dilutive grants and mission-aligned seed capital for ~24 months of runway. Indicative use of funds: product and on-device model engineering (~40%), safety & clinical governance and evidence/PPIE (~25%), partnerships & go-to-market (~20%), and compliance, legal, and operating costs (~15%).

**What that buys:** Android launch; a validated retention and wellbeing signal; a clinical-safety case and real-world evidence base; the first B2B2C partnership contracts; and expansion of verified crisis/localisation coverage beyond the UK and US — i.e., everything needed to prove that a private, free, carer-specific companion both works and can sustain itself on mission terms.

The roadmap that sequences all of this is presented separately (`roadmap/`), designed to be read alongside this plan and the feasibility study.

---

*Sources for market and sector figures are listed in the feasibility study's reference section and mirror the verified sources on the CARER pitch deck. Figures marked [owner-set] are for the founding team to finalise.*
