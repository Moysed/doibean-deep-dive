# DoiBean — Deep Dive Report

An AI co-pilot concept that takes a Doi Chang coffee farmer from **100 baht/kg** to global specialty markets — by owning the full lifecycle from variety planting to roaster cupping.

## What's in this repo

Two self-contained HTML deep-dive reports:

| File | Language | Description |
|------|----------|-------------|
| [`index.html`](./index.html) | English | Full deep dive — 16 sections, ~18 min read |
| [`index-th.html`](./index-th.html) | ภาษาไทย | เวอร์ชันไทย — 16 sections, ~18 นาที |
| [`pitch-th.html`](./pitch-th.html) | ภาษาไทย | Pitch deck 10 สไลด์ · navigate ด้วย arrow keys · ~10 นาที |
| [`brand.html`](./brand.html) | ภาษาไทย | Brand guidelines · logo variants · color palette · typography |
| [`chiangmai-research.html`](./chiangmai-research.html) | ภาษาไทย | CM pain points × 9 hackathon categories · real user voice · stats grounded in research |

Brand assets:
- [`logo.svg`](./logo.svg) — primary horizontal logo
- [`logo-stacked.svg`](./logo-stacked.svg) — stacked version (square avatar)
- [`logo-icon.svg`](./logo-icon.svg) — icon only
- [`logo-mono.svg`](./logo-mono.svg) — single-color version

Open any file in a modern browser. No build step, no dependencies.

## The pitch in one paragraph

The Thai specialty coffee market sits on a **25× value gap**: farmers earn ฿100/kg green, while the same beans retail at ฿2,500/kg roasted. Three solvable failures cause this — no quality verification at the farm gate, no direct channel to roasters abroad, and no decision support for climate-resilient replanting. **DoiBean** combines on-device computer vision (SCA defect grading), an LLM-powered farmer storyteller (Akha/Hmong/Karen/Thai → English/Chinese/Japanese), a climate-aware variety advisor, and a direct-to-roaster marketplace. Owning the full lifecycle (not just one slice) is what makes it defensible against single-point competitors like Cropster, Bext360, or BeanGrader.

## Report structure

1. Executive summary
2. The 25× spread problem
3. 7-stage farmer lifecycle
4. Why merging two ideas wins
5. Market sizing (TAM/SAM/SOM)
6. Competitive landscape
7. Product — six modules, deconstructed
8. Tech stack decisions justified
9. Three personas
10. Business model with unit economics
11. Go-to-market phases
12. Five moat layers
13. Risks &amp; mitigations
14. Demo day strategy
15. 60-day MVP plan
16. Why this wins the hackathon

## Key numbers

| Metric | Value | Source |
|--------|-------|--------|
| Specialty households (Chiang Rai 2025) | 3,921 (+25% since 2020) | Heinrich Böll Foundation |
| Climate impact on Arabica yield | -25% per +2°C | World Coffee Research |
| CV defect detection accuracy | 98% (MobileNetV3) | Springer 2025 |
| SCA specialty grade requirement | 0 Cat-1, ≤5 Cat-2 defects | SCA Standards 2018 |
| Doi Chang farmer green price | ฿80-120/kg | Field reports |
| Specialty retail (Thailand) | ฿1,800-3,000/kg roasted | Drip Roast |

## Tech stack (proposed MVP)

- **Mobile:** Flutter, offline-first
- **On-device ML:** TFLite, MobileNetV3 quantized to int8 (~4MB)
- **Backend:** Node + Postgres + S3
- **Variety recommender:** XGBoost (chosen for explainability)
- **LLM:** Claude Haiku 4.5 (Thai + minority languages)
- **Payments:** Stripe Connect (cross-border escrow)
- **Maps:** Mapbox + Thailand DOA soil layer

## Status

Hackathon co-pilot deep-dive — pre-build research, market analysis, and product strategy. Numbers grounded in cited research. Product strategy and unit economics modeled from documented analogues. Not financial advice.
