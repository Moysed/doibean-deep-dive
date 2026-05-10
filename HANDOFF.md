# DoiBean — Prototype Handoff

> An AI co-pilot for Thai specialty coffee farmers. Closes the 25× price gap between farm gate (฿100/kg) and consumer cup (฿2,500/kg) by owning the full lifecycle: variety planting → quality scanning → direct-to-roaster marketplace.

**You're being handed**: a fully-specced concept (5 HTML docs in this repo), a brand system, and a 60-day MVP plan from Chapter XV of `index.html`. Your job: build the prototype.

---

## Read first (in this order)

All source docs live in `docs/` as markdown. Original HTML editions (with editorial design) are at the repo root if you want the visual version.

1. **`docs/pitch.th.md`** — fastest way to understand what we're building and why. ~5 min read. *Visual version: `pitch-th.html` (arrow keys to navigate, press `G` to jump to a slide).*
2. **`docs/deep-dive.md`** Chapter VII — the six product modules.
3. **`docs/deep-dive.md`** Chapter VIII — tech stack with justifications. Don't change these unless you have a strong reason; they're defended choices.
4. **`docs/deep-dive.md`** Chapter XV — 60-day MVP plan. **This is your scope.**
5. **`docs/brand.md`** — visual standards. Logo, palette, type, do/don'ts.
6. **`docs/field-notes.md`** — Chiang Mai field notes. Skim before designing flows; the pain points are real and named.

Thai-language editions: `docs/deep-dive.th.md`, `docs/pitch.th.md`.

---

## MVP scope (from Chapter XV)

**Ship three modules. Cut three.**

| Build | Cut |
|-------|-----|
| Module 04 — Bean Quality Scanner (hero) | Module 02 — Pest Scout |
| Module 01 — Variety Advisor (rules-based MVP) | Module 03 — Harvest Timer |
| Module 06 — Marketplace + roaster matching | Module 05 — Auto-video Storyteller |

**The riskiest assumption**: that a vision-graded lot closes a real transaction with a real roaster. Everything else is decoration until that works. Optimize for proving this end-to-end.

---

## Tech stack (locked — see Chapter VIII)

- **Mobile**: Flutter (Android Go target — cheap phones farmers actually own)
- **On-device ML**: TFLite, MobileNetV3 quantized to int8 (~4 MB)
- **Defect model**: Transfer learn from ImageNet → fine-tune on 500 hand-labelled Thai green beans + 5,000 public SCA dataset. Target ≥85% Cat-1 accuracy.
- **Variety recommender (MVP)**: lookup table. XGBoost is post-MVP.
- **Backend**: Node + Postgres (with PostGIS) + S3
- **LLM**: Claude Haiku 4.5 for Thai + roaster-language translation
- **Payments**: Stripe Connect (sandbox for prototype)
- **Maps**: Mapbox + Thailand DOA soil layer (free, authoritative)

If you want to deviate, write up the why and ping the product owner — these aren't arbitrary.

---

## Build order (60 days, 9 weeks)

| Weeks | Deliverable |
|-------|-------------|
| 1–2 | Defect model: fine-tuned MobileNetV3, quantized, packaged as TFLite |
| 3–4 | Flutter shell: camera UI, on-device inference loop, scan output card. Variety advisor as rules-based lookup. |
| 5–6 | Marketplace: web frontend (Django + custom views). Lot listing from mobile. Claude Haiku story generation. Stripe Connect sandbox. |
| 7–8 | Pilot: 3 Doi Chang farmers via Doi Tung. 1 Bangkok roaster for 1 lot. Complete end-to-end transaction. Document for demo video. |
| 9 | Polish: 90-second demo video, 10-slide deck, rehearse. Pre-test failure modes (no signal, dim lighting, wrong bean count). |

Pilot is week 7. Don't postpone it. The transaction is the demo.

---

## Brand & UX rules (from `brand.html`)

**Palette** (CSS vars, copy-paste from any page in this repo):

```css
--bone:#F4EFE6;     /* page background */
--paper:#FBF7EE;    /* card / panel */
--espresso:#2A1810; /* primary text */
--ink:#1A0F08;      /* deep dark surfaces */
--crema:#C8A268;    /* primary accent (warm gold) */
--brick:#B8543A;    /* emphasis / hot accent */
--moss:#5C6B3F;     /* organic / certified accent */
--stone:#C9C0B0;    /* hairline rules, dividers */
--slate:#5A4D3F;    /* secondary text */
```

**Type**:

- `--serif: "Figtree","Helvetica Neue",Helvetica,sans-serif` — both Latin and Thai
- `--mono: "JetBrains Mono",ui-monospace,Menlo,monospace` — labels, numerals, eyebrows
- Thai script falls back to system Thai face. Don't add other Thai webfonts without asking.

**Do**:

- Editorial pacing: hairline rules, generous whitespace, sparing accent color.
- Mono labels in uppercase with letter-spacing 0.18em–0.32em for eyebrows.
- Color emphasis (brick) over italic on Thai content. Italic on Latin Roman numerals only.

**Don't**:

- Don't use drop caps on Thai content. Thai leading vowels (ไ ใ เ แ โ) attach to the next consonant; pulling them out breaks words.
- Don't apply `font-style: italic` to Thai. There's no designed Thai italic in the stack — the browser will fake it as a skew and it looks bad.
- No emoji icons, no glassmorphism, no gradient text, no rounded card grids. The whole design system rejects "AI slop" — keep it editorial.

---

## Personas (Chapter IX)

Three users; design for all three but optimize the demo for #1.

1. **Somchai, 47, Doi Chang farmer.** Smartphone-literate but not app-fluent. Thai hill-tribe dialect. Reads ~3rd-grade Thai. Cares about: getting a fair price, knowing what to plant. Visits the app weekly during harvest, monthly otherwise.
2. **Pim, 32, Bangkok specialty roaster.** Buys 200kg/month. Wants traceability, consistent grade, direct relationships. Pays a premium for verified provenance.
3. **Hiroshi, 38, Tokyo importer.** English/Japanese. Buys quarterly containers. Needs documentation in English + cupping notes that match what he tastes.

Somchai is the wedge. The pilot is 3 Somchais.

---

## Open questions for the product owner

Answer these before week 1:

- [ ] Do we have access to the 500 hand-labelled green-bean photos, or does the dev capture them?
- [ ] Doi Tung partnership — confirmed for the 3-farmer pilot?
- [ ] Bangkok roaster — named and committed, or to-be-found?
- [ ] Anthropic API key for Claude Haiku — provided, or dev procures?
- [ ] Stripe Connect account — Thai entity ready, or sandbox-only for prototype?
- [ ] Repo target — does this prototype live in a separate repo, or as `app/` in this one?
- [ ] Design system: is it OK to fork a small Flutter widget kit that mirrors the editorial palette, or do you want native Material with our colors?

---

## Non-goals for the prototype

- Not building modules 02, 03, 05. They're in the deep-dive but cut from MVP.
- Not building the XGBoost variety model — rules-based lookup is enough for the demo.
- Not building admin/back-office tools. Hand-curate from the database for the pilot.
- Not building marketing site. The HTML deep-dive in this repo IS the pre-read.
- Not optimizing for scale. 50 farmers and 5 roasters is the upper bound for the prototype phase.

---

## How to think about decisions

When in doubt, the deep-dive has the answer. If it doesn't, ask. Don't invent.

The pitch (`pitch-th.html`) is the spine — every decision should make demo day stronger. If a feature doesn't help close a transaction in 90 seconds, defer it.

---

**Repo**: https://github.com/Moysed/doibean-deep-dive
**Brand owner / product**: Mond (@Moysed)
**Edition**: v1.0 (May 2026)
