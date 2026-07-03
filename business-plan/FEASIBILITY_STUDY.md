# CARER — Feasibility Study

*Can a private, always-free, carer-specific AI wellbeing companion be built, funded, governed, and sustained? An honest assessment.*

**Prepared by:** Wellnetix Ltd (United Kingdom) · **Product:** CARER · **Status:** v1, July 2026 (pre-launch)

This study assesses CARER across six feasibility dimensions, states the critical assumptions each rests on, and gives an overall Go / Conditional-Go / No-Go verdict with explicit conditions and kill criteria. It is deliberately sceptical: the goal is to find the weakest links before they find us.

---

## Summary verdict: **CONDITIONAL GO**

CARER is **feasible to build, govern, and launch**, and the demand it addresses is large and verified. The two things that are *not yet proven* — and on which the venture genuinely turns — are (1) **retention** (whether carers form a lasting relationship with the companion, against a category norm of heavy drop-off) and (2) **the funding-to-partnership bridge** (whether grants and mission capital can carry a free product until B2B2C partnership revenue scales). Everything else is a solved or solvable problem. The recommendation is to proceed, with the plan structured explicitly to test those two assumptions early and cheaply, and with pre-agreed kill/pivot criteria.

| Dimension | Rating | One-line basis |
|---|---|---|
| Market | **Strong** | ~69m UK+US carers; 63% report mental-health harm; support aimed at the wrong person |
| Technical | **Strong** | On-device SLMs now capable + near-zero marginal cost; core, privacy model, safety cage already built |
| Financial | **Moderate** | Free model viable *because* marginal cost ≈ £0, but depends on grant + partnership funding materialising |
| Operational | **Moderate** | Small team; needs Clinical Safety Officer + DPO; PPIE panel to stand up |
| Regulatory / legal | **Moderate** | Non-clinical so launchable now; NHS partnerships need DCB0129/DTAC; multi-jurisdiction needs counsel |
| Commercial / GTM | **Moderate** | B2B2C precedent strong (Homethrive/Wellthy/ianacare); statutory duties help; first contract unproven |

---

## 1. Market feasibility — **Strong**

**Finding:** demand is not in question. The addressable population is one of the largest under-served groups in health and social care, and its need is documented.

- ~5.8m unpaid carers in the UK (care valued at ~£184bn/yr); ~63m family caregivers in the US (+45% since 2015; ~$1.01tn/yr) — a combined TAM of ~69m people.
- ~63% of carers report caring harms their mental health; ~1 in 5 informal carers is at risk of burnout.
- Support overwhelmingly targets the care recipient; even statutory carer support (Care Act 2014) has low uptake and is practical, not emotional.
- The adjacent commercial pool is real and growing: mental-health apps ~$9bn (2025) → ~$23bn (2030); broader digital mental health ~$33bn → ~$180bn (2035).

**Critical assumption to test:** that carers will *adopt an app* for emotional support (not just that they need it). Early-access adoption + qualitative testimony are the Phase-0/1 evidence.

**Weakest link:** none material to feasibility — demand is the strongest dimension.

---

## 2. Technical feasibility — **Strong**

**Finding:** the technology thesis is credible today and much of it is already built.

- **On-device AI is now good enough.** Small language models under ~10B parameters (Phi-4-mini 3.8B, MIT licence, ~3GB at Q4, 128K context; Qwen3 from 0.6B, Apache) now match models many times larger on targeted tasks, running on a phone. On-device inference costs ~zero per query after download; the marginal cost of one more user is effectively nil — the economic foundation of the free model.
- **The privacy architecture is real.** Content-free signal sync, encrypted sync, and optional off-by-default cloud fallback keep sensitive content on the device. This is defensible and hard for cloud-first incumbents to retrofit.
- **Safety is engineered, not hoped-for.** A guardrail cage (generate → guardrail → retry → safe fallback) with a fixed schema keeps the companion inside a non-clinical, safe scope; the crisis layer works offline, pre-auth, and independently of the model.
- **Already built:** the core app (iOS in early access, Android in progress), the on-device model epic, the privacy/data model, the safety cage, region-aware crisis localisation (UK + US verified and tested; global fallback), and an API-based backend.

**Critical assumptions to test:** on-device model quality and latency across the real device fleet (older/cheaper phones); reliable model fallback; and that the safety cage holds under adversarial and real-world input (red-teaming is in place and must continue).

**Weakest link:** device fragmentation and the quality/safety of a small on-device model in genuinely sensitive emotional moments. Mitigation: tiered model strategy, cloud fallback (opt-in), continuous red-teaming, and conservative scope.

---

## 3. Financial feasibility — **Moderate**

**Finding:** the free-to-carer model is financially *feasible precisely because* the marginal cost of serving a user is near zero — but it depends on non-usage funding (grants, then partnerships) arriving on schedule.

- **Cost base is people + compliance, not compute.** On-device inference removes the per-user cost that sinks most free AI products. Burn is dominated by a small team and governance, not by scale.
- **Funding sources are real and available.** Non-dilutive UK innovation funding is active and relevant: SBRI Healthcare (up to £200k per innovation; recently £1.7m across nine digital-mental-health projects), NIHR Innovation Catalyst (up to £150k + a structured programme, for TRL-3+ digital health), NIHR i4i, and Innovate UK SBRI-style contracts (£0.2–1.5m). These fit CARER's stage and domain.
- **Precedent for the revenue model:** B2B2C caregiver platforms have raised heavily on this model (Homethrive ~$78M, Wellthy ~$78M, ianacare ~$16.7M with AARP), validating that employers and health plans pay to support carers.
- **Consumers do pay for wellbeing** (Calm/Headspace ~$70/yr), but the free mental-health-app segment alone was ~$6.1bn in 2025 — free is a legitimate, high-reach strategy, and the right one for this audience.

**Critical assumptions to test:** (a) that grants + mission seed cover ~24 months of runway; (b) that the first B2B2C contract closes within that window; (c) that partnership pricing at near-zero cost-to-serve yields healthy contribution.

**Weakest link:** the timing gap between spending on a free product and partnership revenue. Mitigation: grant-heavy capital stack, low burn, early pilot pipeline, and a supporter-tier trickle.

---

## 4. Operational feasibility — **Moderate**

**Finding:** operable by a small team, but two governance hires and a lived-experience structure gate the healthcare-partnership path.

- **Lean by design.** On-device architecture and an API-based backend keep ops light.
- **Governance gaps to close (near-term):** a named **Clinical Safety Officer** (required for DCB0129), a **Data Protection Officer**, ICO registration, and a **PPIE / lived-experience panel** of carers. These are the difference between a nice consumer app and a partnership-ready one.
- **Support and moderation** for a vulnerable audience must be resourced (escalation paths, safeguarding, crisis-content review) — modest at early-access scale, growing with the population.

**Critical assumption to test:** that the team can recruit credible safety/DPO capability affordably (fractional/advisory is feasible early).

**Weakest link:** key-person concentration in a small team. Mitigation: documented, API-based architecture; advisors; phased hiring tied to funding.

---

## 5. Regulatory and legal feasibility — **Moderate**

**Finding:** launchable now as a non-clinical product; partnership and multi-jurisdiction scale require deliberate compliance work already scoped.

- **Non-clinical positioning is defensible** and is enforced in-product — CARER is not a medical device, therapy, or emergency service. This is what makes direct-to-consumer launch legal today without CE/UKCA medical-device certification.
- **For NHS/social-care partnerships**, the recognised path is voluntary early adoption of **DCB0129** (clinical-risk management; needs a Clinical Safety Officer, Clinical Safety Case Report, Hazard Log), **DTAC** (five domains: clinical safety, data protection, technical security, interoperability, usability/accessibility), and alignment with **NICE's Evidence Standards Framework**. None is a blocker to launch; all are gates to commissioning revenue.
- **Data protection:** UK GDPR / DPA 2018 baseline; region-aware handling drafted for EU (GDPR), California (CCPA/CPRA), and beyond. Special-category (health/wellbeing) data plus a **research-consent** basis mean a solicitor/DPO sign-off before scale.
- **Legal foundation already drafted:** privacy notice, terms (18+, England & Wales governing law with local-law clauses), cookie and accessibility statements — pending professional review and ICO registration.

**Critical assumptions to test:** that a solicitor/DPO validates the research-consent basis and the multi-jurisdiction posture; that ICO registration completes before scale.

**Weakest link:** the research-consent/special-category-data basis in multiple jurisdictions. Mitigation: conservative opt-in consent (already the design), professional review before relying on it commercially.

---

## 6. Commercial / go-to-market feasibility — **Moderate**

**Finding:** the B2B2C route is precedented and the statutory tailwind is real, but the first contract is unproven and is the venture's key commercial milestone.

- **Precedent:** employers and health plans already pay for carer support (the Homethrive/Wellthy/ianacare model). CARER offers a lighter, cheaper, privacy-first emotional layer rather than a full concierge — a differentiated, lower-friction sell.
- **Statutory tailwind (UK):** the Care Act 2014 duty on local authorities to support carers, the Health and Care Act 2022 §25 duty on ICBs to involve carers, and Better Care Fund carers'-breaks funding create a real budget and mandate that a low-cost, always-on companion can serve.
- **Direct early-access GTM is cheap and informative:** app stores, website, carer communities, organic/search — enough to validate the product before spending on enterprise sales.

**Critical assumptions to test:** that at least one ICB/LA or employer signs within ~24 months; that per-seat pricing at ≈£0 cost-to-serve is attractive to both sides.

**Weakest link:** enterprise/public-sector sales cycles are slow. Mitigation: start pilots early, lead with the statutory duty + evidence + safety governance, and keep the direct free channel running regardless.

---

## Critical assumptions (the whole case rests on these)

1. **Carers retain.** CARER's design overcomes the category's D90 drop-off and produces a genuinely retained relationship. *(Test in Phase 0–1 with instrumented D7/D30/D90 + qualitative evidence.)*
2. **The funding bridge holds.** Grants + mission seed cover runway until the first B2B2C revenue. *(Test via grant applications in Phase 0–1 and a pilot pipeline in Phase 2.)*
3. **The safety cage holds** under real, emotionally-charged use. *(Test via continuous red-teaming; it currently passes an expanded crisis red-team.)*
4. **A partner signs.** At least one ICB/LA/employer/charity contracts within ~24 months. *(Test via early pilot outreach.)*

## Kill / pivot criteria (decide in advance, not in hope)

- If, after a fair Phase-1 effort, **D30 retention and qualitative evidence show no durable relationship** forms → pivot the product (or the audience) before scaling spend.
- If **no grant and no partnership pipeline** materialise within the runway window → re-scope to a smaller sustainable footprint or seek a strategic/charity home rather than raise growth equity against a free product.
- If the **safety cage cannot be kept reliably safe** for this audience at acceptable cost → narrow scope (e.g., companion-lite + signposting only) rather than over-reach.

## Conclusion

Build it. The demand is real, the technology is ready and largely built, the economics are feasible *because* of on-device AI, and the governance and legal paths are known and scoped. The venture's honest uncertainty is concentrated in two testable places — retention and the funding-to-partnership bridge — and the roadmap is structured to test both early and cheaply, with pre-agreed exits. That is a **conditional go**: proceed, instrument the two make-or-break assumptions from day one, and let the evidence — not optimism — govern the scale-up.

---

## References

Market and sector figures are third-party estimates; ranges reflect differing methodologies. Verified July 2026.

**Carers — population, value, health impact**
- Carers UK — *Key Facts & Figures* / *Facts about Carers* (2025): UK ~5.8m carers; ~£184bn/yr value of care. https://www.carersuk.org/
- Carers UK — *State of Caring* (2024): ~63% report caring harms their mental health. https://www.carersuk.org/
- AARP & National Alliance for Caregiving — *Caregiving in the US 2025*: ~63m US caregivers, +45% since 2015. https://www.aarp.org/
- AARP — *Valuing the Invaluable* (2026 update): ~$1.01tn/yr value of US unpaid care. https://www.aarp.org/
- Informal-caregiver mental-health / burnout meta-analysis (2025): ~1 in 5 at risk of burnout. https://www.sciencedirect.com/

**Market size**
- Market Research Future — *Digital Mental Health Market* (2025): ~$33bn (2025) → ~$180bn (2035), ~18.5% CAGR. https://www.marketresearchfuture.com/
- MarketsandMarkets — *Mental Health Apps Market* (2025): ~$9bn (2025) → ~$23bn (2030). https://www.marketsandmarkets.com/

**Retention / engagement / willingness to pay**
- Meta-analysis of mental-health-app RCTs: ~92% uptake, weak adherence; human support + reminders improve engagement. https://pmc.ncbi.nlm.nih.gov/
- App retention benchmarks (2025–26); mental-health apps with human touch D90 20–35% vs <10% for pure tracking. https://www.businessofapps.com/data/health-fitness-app-benchmarks/
- Free mental-health-app segment ~$6.1bn (2025); Calm/Headspace ~$70/yr; iOS higher WTP. https://www.marketsandmarkets.com/

**Comparable companies (B2B2C caregiver tech)**
- Homethrive — ~$78M raised ($20M round led by Telus Global Ventures / 7wire). https://www.mobihealthnews.com/news/homethrive-raises-20m-tech-enabled-caregiver-platform
- ianacare — ~$16.7M total (Series A $12.1M, incl. AARP); B2B2C, targeting 1M lives. https://news.mit.edu/2025/ianacare-builds-lifeline-for-family-caregivers-across-us-0811
- Wellthy — ~$78M raised; family-care concierge (B2B2C).

**UK carer policy & funding**
- Care Act 2014 — local-authority duty to assess/meet eligible carers' needs. https://www.legislation.gov.uk/ukpga/2014/23/contents
- Carers UK — ICBs/ICPs/ICSs and unpaid carers policy explainer (2025); Health & Care Act 2022 §25 duty. https://www.carersuk.org/
- Better Care Fund policy framework — carers'-breaks funding. https://www.gov.uk/

**Innovation funding**
- SBRI Healthcare — digital mental-health competition; up to £200k/innovation; £1.7m across 9 projects. https://sbrihealthcare.co.uk/
- NIHR Innovation Catalyst — up to £150k + programme (TRL 3+ digital health); NIHR i4i. https://www.nihr.ac.uk/
- Innovate UK — SBRI-style contracts £0.2–1.5m. https://www.ukri.org/councils/innovate-uk/

**Clinical safety & digital-health standards (partnership path)**
- NHS England — DCB0129 clinical-risk management (Clinical Safety Officer, Safety Case, Hazard Log). https://digital.nhs.uk/
- NHS — Digital Technology Assessment Criteria (DTAC). https://www.nhs.uk/
- NICE — Evidence Standards Framework for digital health technologies. https://www.nice.org.uk/

**On-device AI**
- Small-language-model capability/cost (Phi-4-mini, Qwen3); on-device ≈ zero marginal cost, 70–90% cost reduction. https://arxiv.org/ ; https://www.digitalapplied.com/
