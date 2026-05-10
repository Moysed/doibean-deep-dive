# DoiBean — Deep Dive (English)

> Source: `index.html` (HTML edition)

---

**Volume 01** · Issue No. I
Deep Dive Report
May 2026 · Bangkok / Chiang Rai

Coffee · AI · Northern Thailand

# DoiBean

An AI co-pilot that takes a Doi Chang farmer from *฿100/kg* to global specialty markets — by owning the full lifecycle from variety planting to roaster cupping.

Audience
: Hackathon judges, co-founders, investor pre-read.

Read time
: ~18 minutes. 16 chapters. Drop in at any.

Edition
: v1.0 — sources cited at the back.

---
*Contents*

## Sixteen *chapters*

1. I. Executive Summary
2. II. The 25× Spread Problem
3. III. The 7-Stage Farmer Lifecycle
4. IV. Why Merging Wins
5. V. Market Sizing
6. VI. Competitive Landscape
7. VII. Product — Six Modules
8. VIII. Tech Stack — Justified
9. IX. Three Personas
10. X. Business Model
11. XI. Go-to-Market Phases
12. XII. Five Layers of Moat
13. XIII. Risks & Mitigations
14. XIV. Demo Day Strategy
15. XV. 60-Day MVP Plan
16. XVI. Why This Wins

*Chapter I — The Thesis*

## I. Executive Summary

Two coffee ideas — a quality scanner and a climate-aware variety advisor — collapse into one app because they serve the same farmer at different points in the same lifecycle. The merge unlocks a flywheel neither product could build alone.

25×

Price spread

Farmer ฿100/kg → consumer ฿2,500/kg roasted. The gap captured by middlemen and information asymmetry.

3,921

Specialty households

Chiang Rai alone, 2025 — up 25% since 2020. A growing user base hungry for tools.

98%

CV accuracy

Defect detection on green beans is now a solved technical problem (Springer, 2025).

−25%

Yield per +2°C

Climate is forcing variety changes within 5–10 years. Decisions made today.

★ Core Thesis

The Thai specialty coffee market sits on a **25× value gap** caused by three solvable failures: *no quality verification at the farm gate*, *no direct channel to roasters abroad*, and *no decision support for climate-resilient replanting*. Computer vision plus LLM translation plus a marketplace closes all three at once. Owning the lifecycle — not just one slice — is what makes this defensible against single-point competitors.

*Chapter II — Diagnosis*

## II. The 25× spread problem

Before designing a solution, understand exactly where the value evaporates. Three solvable failures, in order.

The distance from a green bean on a sorting cloth to a roasted cup on a café counter is not, in cost terms, very long. Yet almost every baht added to that bean between Doi Chang and a Bangkok espresso bar is captured by someone who never planted a tree.

### Where the money *goes*

฿100

Farmer · green · per kg

→

฿350

Co-op · exporter

→

฿2,500

Café cup · 200g retail

Total markup: **25× from soil to cup**. The farmer captures four percent.

### The three root *causes*

Root cause i — Information asymmetry

The farmer doesn't know their own beans' SCA score, defect profile, or cupping notes. The co-op buyer does (or claims to). Without verifiable quality data, the farmer is a price-taker. **This is what computer vision solves.**

Root cause ii — No direct channel

Even a high-scoring farmer cannot reach a Tokyo or Berlin roaster directly. Export bureaucracy, cross-border payment, language barriers, and trust deficits make direct trade impossible without infrastructure. **This is what the marketplace solves.**

Root cause iii — Wrong crop in five years

Climate is shifting growing zones uphill at roughly 150 metres per decade. A farmer planting Caturra today at 1,200 m will harvest a collapsed yield by 2035. Government extension services lack the data and tools. **This is what the variety advisor solves.**

Three things make 2026 the right year — smartphone penetration just crossed eighty percent in highland villages; Stripe Connect and PromptPay rails matured; and June 2025 hill-tribe ID reform removed the last friction in farmer banking.— Why Now, in one breath

▲   △   ▲

*Chapter III — The Lifecycle*

## III. Seven stages, every year

Every farmer passes through these seven stages annually. Two original ideas — quality scanner and variety advisor — hit different stages, which is exactly why they belong in one app.

Single-stage products churn because they are seen once a year. An app that lives at one moment in the calendar is a tool. An app that lives across the calendar is a companion — and companions get used, trusted, and recommended.

1

Plant

Wrong variety = 5 yrs lost

Idea #8

2

Grow

Pruning unknown

Idea #8

3

Scout

Pests invisible

4

Harvest

Pick too early/late

5

Process

Wrong method

6

Grade

Price-taker

Idea #7

7

Sell

Co-op only

Idea #7

Built separately, each idea is a *one-touch-per-year* app — high churn, low retention. Built together, plus modules three through five in between, you have a year-round companion the farmer opens a hundred times a year.— The Strategic Insight

*Chapter IV — The Argument*

## IV. Why merging wins

Three compounding reasons: lifecycle integration, data flywheel, and moat layering. None work alone; all three reinforce each other.

### 1 · Lifecycle *integration*

A farmer who used the variety advisor in March will have the app on their phone in November when harvest comes. Conversion to the scanner module is essentially free. The reverse is also true — a farmer impressed by their first scan score wants to know which variety would have scored higher. **One install, two products, zero re-acquisition cost.**

### 2 · Data *flywheel*

This is the one most teams miss. Each module's data improves the others:

- **Variety + GPS + harvest score** — over two seasons you build the world's first dataset linking Thai elevation and microclimate to actual cupping outcomes. No coffee research org has this.
- **Defect scans + processing method + final price** — trains a process recommender. Given your bean defects and the weather, should you do washed, honey, or natural to maximise price?
- **Roaster preferences + farmer profiles** — matches improve over time. After 1,000 transactions you can predict which roaster will love which lot before either knows.

Data Moat Math

Each scan equals one labelled training row. Hit 10,000 farmers averaging five scans per season and you have **50,000 Thai-specific labelled green-bean photos** per year. Public SCA datasets contain perhaps 5,000 photos total, mostly African and Latin American. After year one your model is *strictly better* at Thai beans than anything Cropster, Bext360, or BeanGrader can build remotely. The gap widens annually.

### 3 · Moat *layering*

Two products mean two competitors per slice. One integrated app means competitors must build all six modules to displace you. The cost of replacement grows faster than the cost of incremental features.

### The counter*factual*

If you ship the scanner and the advisor separately, here is what happens within eighteen months:

- The scanner alone gets cloned by an Indonesian or Vietnamese team within six months. Defect detection is published technique now.
- The advisor alone struggles with retention — farmers open it once a year, can't afford a subscription, churn is brutal.
- Together they reinforce each other and become a category-defining product. The combined version is ten times harder to clone.

*Chapter V — The Numbers*

## V. Market sizing

A grounded TAM, SAM, and SOM that doesn't lie to itself or to investors.

| Layer | Definition | Size | Reasoning |
| --- | --- | --- | --- |
| **TAM** | Global specialty coffee farmers + roasters | $50B GMV | SCA 2025. ~25M coffee farmers worldwide; specialty subset ~2M. |
| **SAM** | SE Asia coffee belt — TH + Laos + Vietnam Arabica + Myanmar | ~85,000 hh | TH 25k + Laos 30k + VN 25k + MM 5k. Same problems, overlapping languages. |
| **SOM Y1** | Doi Chang + Doi Tung + Doi Mae Salong | 500 farmers | Beachhead via Doi Tung Foundation. ~1% of TH specialty. |
| **SOM Y3** | All Thailand + early Laos PDR + 200 international roasters | 5,000 farmers | 20% of TH specialty households. Series A target. |

Revenue Math at SOM Y3

5,000 farmers × 30% Pro conversion × ฿99/mo = **฿1.5M/mo recurring** ($43k MRR). 200 roasters × ฿990/mo = **฿200k/mo** ($5.7k MRR). Marketplace GMV approximately $5M (5,000 farmers × $1,000 average lot × 1 lot/yr) × 8% take = **$400k/yr**. *Total Year 3 ARR ≈ $1M.* Decent for a vertical SaaS at series A.

*Chapter VI — The Field*

## VI. Competitive landscape

Map every adjacent player and find the gap nobody fills.

| Player | Geo | What they do | Gap they leave |
| --- | --- | --- | --- |
| **Cropster** | Austria → global | Roastery QC, cupping logs, inventory | Stops at the roaster door. Doesn't touch the farm. |
| **Bext360** | USA → Africa, LatAm | Blockchain provenance, big-corp focused | No on-device AI. Enterprise contracts. SE Asia not served. |
| **Sucafina · Caravela** | Switzerland · Colombia | Traditional green coffee importer-exporter | Human-relationship business. Doesn't scale. Margins to importers. |
| **BeanGrader** | USA | AI defect detection only, web upload | No marketplace, no farmer side. Pure tool. |
| **Ricult** | Thailand · Pakistan | Satellite + AI, generic field crops | No coffee depth. No vision. No specialty access. |
| **Doi Tung · Doi Chaang** | Thailand | Single-brand vertical: grow → roast → café | Their own farmers only. Doesn't tech-enable other communities. |
| **DoiBean** | Thailand → SEA belt | **Farm-to-roaster lifecycle app, vision + LLM + marketplace** | *This is the gap.* |

★ The Whitespace

Nobody owns the farmer-to-roaster journey end-to-end with on-device AI. Every adjacent player owns one slice. Western specialty infrastructure assumes farmers already have export channels — which Thai and SE Asian farmers don't. **An integrated app has to come from inside the region.**

*Chapter VII — The Product*

## VII. Six modules , deconstructed

Each module solves one stage of the lifecycle. Together they form an inseparable whole. Two are hero modules — the demo and the wedge — marked with the brick rule above.

I.

Pre-plant · Annual

### Site & Variety Advisor

Module 01

Farmer drops a GPS pin on their plot. The app pulls elevation, slope, aspect, soil type, twenty-year climate history, and IPCC RCP4.5 projections. Output: ranked variety recommendations with explanations the farmer understands.

Inputs

GPS lat/lng → DEM elevation → slope/aspect → LDD soil DB → TMD historical 20-yr climate → IPCC scenarios for 2030/2040.

Output

"Plot at 1,420m, NE-facing, 22°C avg. Recommend Catimor 70% + Typica 30%. By 2035, pure Caturra unviable — hedge by planting 200m lower."

Why this matters

A coffee tree takes 3–4 years to first harvest, 5+ to peak. A wrong variety choice today is a **seven-year economic mistake**. No farmer has access to this combined dataset; government extension officers don't either.

II.

Growing season · Weekly

### Disease & Pest Scout

Module 02

Farmer photographs a suspect leaf. On-device CV classifies common Thai threats — leaf rust (*roya*), coffee berry borer, coffee berry disease, anthracnose. A hyperlocal outbreak map shows what other farmers in the watershed are reporting.

Tech

TFLite vision, 4 MB, runs offline. Trained on PlantVillage + Thai-specific data we collect through field partnerships.

Treatment

Organic-cert friendly recommendations (matters for export premium). Links to nearest agri-shop with stock.

III.

Harvest window · Daily during season

### Harvest Timer

Module 03

Cherry photo → ripeness percentage via colour and firmness ML. Combined with a seven-day forecast: "Pick Tuesday, not today; rain Thursday will dilute Brix." Then the process recommender suggests washed, honey, or natural based on bean profile, weather window, and current market premiums.

IV.

★ Hero module · Post-harvest

### Bean Quality *Scanner*

Module 04 · Hero

Spread fifty to a hundred green beans on white A4 paper (free kit shipped to farmer). Phone camera captures. **MobileNetV3 fine-tuned on SCA defect taxonomy** classifies every visible bean.

```
SCA Score Estimate 84.5 ✓ Specialty Grade
Cat-1 Defects 0 ✓
Cat-2 Defects 3 (2 partial sour, 1 floater)
Bean Size Screen 17 (87%), Screen 16 (13%)
Similar-Lot Profile floral, jasmine, citrus  (n=47 lookup)*

*\* Honest framing: CV cannot infer flavor from a green bean photo. The "Similar-Lot Profile" line is a database lookup (variety + altitude + process + season → median Q-grader notes from comparable Doi Chang lots, 2023–2026). Real cupping notes come from the roaster cup after delivery and feed back into the system.*
Suggested Roast light to medium-light
Price Floor ฿1,400/kg green
```

Legal & Trust Boundary

Output is explicitly labelled **"pre-screening estimate"** — not a Q-grader certification. For commercial export, lots above 80 SCA route to a certified Q-grader (in-app, paid). This protects against legal liability and maintains trust with the specialty community. *Underclaiming credentials is a moat, not a weakness.*

V.

★ Hero module · Sell

### Direct-to-Roaster *Marketplace*

Module 05 · Hero

Each farmer's harvest becomes a **lot card** — photos, story video, similar-lot profile lookup, processing detail, organic and fair-trade certifications, available kilos. Roasters worldwide browse, request samples, negotiate, settle in escrow. Stripe Connect handles cross-border. Initial export logistics partnered with Beanspire or This Side Up.

Pricing Intelligence Layer

The lot is cross-referenced against recent global comparables: *"Similar 84.5-score Catimor honey from Aceh sold to Onyx for £14/kg green last month. Recommend asking £11–13."* This is the killer feature — a farmer who doesn't speak English now negotiates like an experienced exporter.

VI.

Marketing · Continuous

### Farmer Storyteller

Module 06

Farmer records a thirty-second voice note in Akha, Hmong, Karen, or Northern Thai. Claude translates and reframes it into English, Mandarin, Japanese, or Korean marketing copy that captures the cultural authenticity buyers crave. Auto-generates a vertical reel with farmer's face and farm B-roll for IG and TikTok.

Why this completes the moat

Direct trade isn't only about price discovery — it is about **relationship and story**. Specialty buyers pay a premium for narrative provenance ("this lot from a 4th-gen Akha family"). By owning storytelling, you build farmer brand *independent of the platform*. Counterintuitive but critical: farmers will trust a platform more if they see their personal brand outliving their account on it.

▲   △   ▲

*Chapter VIII — The Stack*

## VIII. Tech stack — each decision justified

Defensible technical choices, with reasoning a senior engineer can challenge.

| Layer | Choice | Why this, not the alternative |
| --- | --- | --- |
| Mobile framework | **Flutter** | Single codebase. Runs on Android Go (cheap phones farmers actually own). Better native performance than React Native for camera + ML inference. |
| On-device ML | **TFLite, MobileNetV3 quantized** | 4 MB model, runs offline. Critical because farms have intermittent 4G. Quantization to int8 keeps accuracy within 2% of float32 but cuts size 4×. |
| Defect detector | **Transfer-learn from ImageNet → fine-tune** | 500 hand-labelled Thai green-bean photos + 5,000 public SCA dataset is enough for >90% accuracy. Avoids expensive cold-start data collection. |
| Variety recommender | **XGBoost** (not deep learning) | Tabular, small feature set, need *explainability* for farmer trust. SHAP values let us show "this variety because elevation + soil pH + projected 2035 temperature." |
| Backend | **Node + Postgres + S3** | Boring, hireable, well-supported. Postgres + PostGIS handles geospatial queries (closest agri-shop, watershed neighbours). |
| LLM translation | **Claude Haiku 4.5** | Best Thai + minority-language translation among API-accessible models. Cheap enough to use per-message. |
| Payments | **Stripe Connect** | Cross-border escrow. Handles foreign currency, KYC, dispute resolution. Alternative (manual Wise transfers) doesn't scale past 50 transactions. |
| Maps + geo | **Mapbox + Thailand DOA soil layer** | Mapbox styles read better at the elevations farmers care about. DOA's soil GIS is free and authoritative. |

*Chapter IX — The People*

## IX. Three personas, designed around

Every product decision was tested against these three. If a feature serves none of them well, it does not ship.

Persona 01 · Entry: scanner

### Pong, 35 — *Akha*, Doi Chang

Speaks Akha at home, Northern Thai at market. Smartphone is shared with his wife. Five rai of mixed Catimor and Caturra at 1,300 m. Earns ฿80–120/kg green selling to a co-op buyer who arrives once a month. Has heard the word "specialty" but doesn't know what it means for him.

**Why he installs:** a youth ambassador shows him the scanner result on his own beans — 84.5, specialty grade. He can't unsee that number.

Persona 02 · Entry: variety advisor

### Nitaya, 50 — *Karen*, Mae Salong

Yields have dropped two seasons running. Read in a Bangkok Post article that climate is shifting growing zones. Has Android Go and uses LINE daily. Wants to know what to plant for her grandchildren to inherit.

**Why she installs:** a foundation extension officer demos the variety advisor on her plot. The output is an explanation, not a recommendation — and that's why she trusts it.

Persona 03 · Entry: marketplace

### Mark, 32 — *specialty roaster*, Bangkok

Roasts 200 kg/week. Burns six hours every Friday calling farms, chasing samples, vetting micro-lots. Saves fifteen hours and 30% on sourcing in his first month with DoiBean. The pricing intelligence layer is his unfair advantage.

**Why he subscribes:** the similar-lot profile lookup is good enough to skip the first sample shipment 70% of the time. That alone pays for the year.

*Chapter X — The Money*

## X. Three revenue streams

Subscription on both sides, plus a marketplace take and a foundation co-pay. No single stream carries the company.

Stream 01 · B2C

### Farmer freemium SaaS — ฿99/month Pro

Free tier: 5 scans/month, basic variety advice, 1 marketplace listing. Pro tier (฿99/mo): unlimited scans, full historical data, 3 active listings, priority storyteller queue. Conversion target 30% — one direct-trade sale pays two years of Pro.

Stream 02 · B2B

### Roaster source — ฿990/month + 8% take rate

Discoverable lot search, similar-lot profile lookups, sample escrow, settlement. Take rate of 8% on closed transactions — the comparable in coffee infrastructure is 12–15%, so we are deliberately under-priced for first three years.

Stream 03 · B2G · Foundation

### Government & partnership co-pay

Doi Tung Foundation, Thailand DOA, NGO partners co-fund onboarding at ฿200/farmer. Carbon-credit verification at $50–200/farm/year sits on top — a premium add-on for farmers exporting to ESG-conscious roasters in EU/JP.

Unit Economics

**Farmer LTV ≈ $350** (subscription path ~$22 + marketplace contribution ~$320 over 2-yr horizon). **Roaster LTV ≈ $990/year.** CAC blended around $100. *LTV/CAC ≈ 3.5×* — healthy for vertical SaaS.

*Chapter XI — The Wedge*

## XI. Beachhead, region , belt

Three phases over thirty-six months. The supply side cracks first — that is unusual for marketplaces, and it is the move.

Phase 01

### Doi Chang Beachhead

Months 0–6

- 500 farmers via Doi Tung Foundation
- 5 anchor Bangkok specialty roasters
- 10 farmers ship lots internationally
- Press: 1 Bangkok Post + 1 BBC piece
- Goal: prove direct-trade transaction works

Phase 02

### Northern Thailand

Months 6–18

- 2,500 farmers across Chiang Rai + Chiang Mai + Mae Hong Son
- 50 international roasters (Tokyo, Seoul, Berlin)
- $1M GMV through marketplace
- Series A raised on traction

Phase 03

### Regional Belt

Months 18–36

- Laos PDR + Vietnam Arabica + Myanmar
- 5,000 total farmers
- 200+ international roasters
- $1M ARR; profitable on contribution margin

*Chapter XII — Defensibility*

## XII. Five layers of moat

No single layer is sufficient. The combination is what makes a clone uneconomic.

i.

### Thai-specific data flywheel

Every scan fine-tunes the defect detector on Catimor, Typica, and Geisha grown in Doi Chang volcanic soil. Foreign datasets (Brazilian, Ethiopian) underperform. The year-one advantage compounds annually.

ii.

### Hill-tribe trust via foundation channel

The Doi Tung Foundation partnership represents thirty-plus years of community work and royal Thai legacy. Foreign competitors cannot replicate this. Trust takes decades; we own farmer mind-share from day one.

iii.

### Multi-language voice and storytelling

Akha, Hmong, Karen, Northern Thai (kham mueang), Lao. No global SaaS localizes this; no general LLM addresses it natively. A 3–5 year head start.

iv.

### Lifecycle integration lock-in

A farmer's variety choices, multi-season harvest data, and roaster relationships all live in DoiBean. Switching costs become punitive — a farmer would lose history. Roasters are invested in lot reviews and sample history.

v.

### Two-sided network effects

More farmers attract roasters; more roasters bid up prices, attracting farmers. Doi Tung cracks the supply-side chicken-and-egg first — unusual for marketplaces, and the right move.

*Chapter XIII — What Could Go Wrong*

## XIII. Risks & mitigations

| Risk | Severity | Mitigation |
| --- | --- | --- |
| **Older farmers don't use apps** | High | Voice-first UI in tribal languages; youth ambassadors paid ฿500 per onboarded farmer; in-person training at foundation centres. |
| **Photo variance kills accuracy** | Med | Free white A4 kit shipped with onboarding; in-camera framing guides; reject + retake flow for poor lighting. |
| **Roasters distrust similar-lot lookup** | High | Frame profile clearly as database lookup, not visual prediction; sample escrow always available; certified Q-grader backstop on premium lots; cupping notes from real roaster cup feed back into the database; never overclaim. |
| **Export bureaucracy** | Med | Partner with established Thai exporters (Beanspire) for first 18 months; build internal capability after volume justifies it. |
| **Climate model misforecast** | Med | Show ranges, not point estimates. Update annually with new TMD data. Variety advice always includes hedging. |
| **Foundation partnership falls through** | High | Parallel relationships with Mae Fah Luang + DOA + 2 NGOs; never single-source the channel. |

*Chapter XIV — The Stage*

## XIV. Demo day strategy — ninety seconds

A storyboard. Numbers are wallpaper; a live scan is a punch in the chest.

### Storyboard

0:00–0:10

**Open on smoke.** A photo of Doi Chang at dawn, burning season. "Every March, this is our farmer's office." Pause two beats.

0:10–0:25

**The 25× on screen.** Single number, no chart. "His beans sell here for ฿100. The same beans cost ฿2,500 in your Café Amazon. Where does the difference go?"

0:25–0:50

**Live scan on stage.** Real beans, real phone, real result. Hold the screen up. Read the SCA score aloud — *84.5, specialty grade*. Audience hears the number; that is the moment.

0:50–1:10

**Variety advisor.** Show the projected 2040 climate. "By the time his daughter takes over, this plot won't grow Caturra anymore. We tell him what to plant today."

1:10–1:25

**Marketplace.** Tap the scan into a lot card. A roaster in Berlin browsing. *"Three days from cherry to inquiry."*

1:25–1:30

**Closing line.** "The only thing between a Doi Chang farmer and a Berlin roaster is a four-megabyte app." Hold. End.

### Props *checklist*

- Real green beans (50–100), spread on white A4
- Phone with the app, fully charged, airplane-mode demo (proves offline)
- Backup phone, identical state
- One photo of Doi Chang dawn — your own, not stock
- Printed business cards with the app QR; hand to every judge after

*Chapter XV — The Build*

## XV. Sixty days, nine weeks

Cut three modules. Ship two. Prove one transaction. The shape of the MVP is what makes the demo possible.

Weeks 1–2

**Defect model.** Fine-tune MobileNetV3 on 500 hand-labelled Thai green beans + 5,000 public SCA. Target 85%+ Cat-1 accuracy. Quantize to int8. Package as TFLite.

Weeks 3–4

**Flutter shell.** Camera UI, on-device inference loop, scan output card. Variety advisor as rules-based MVP (lookup table, no XGBoost yet).

Weeks 5–6

**Marketplace.** Web frontend (Django + custom views). Lot listing on mobile. Claude Haiku story generation. Stripe Connect sandbox.

Weeks 7–8

**Pilot.** 3 Doi Chang farmers via Doi Tung. Anchor 1 Bangkok roaster for 1 lot. Complete end-to-end transaction. Document for demo video.

Week 9

**Polish.** 90-second demo video. 10-slide deck. Rehearse twenty times. Pre-test failure modes (no signal, dim lighting, wrong bean count).

Cut from MVP — pest scout, harvest timer, auto-video storyteller. The riskiest assumption is whether a vision-graded lot closes a real transaction with a real roaster. *Everything else is decoration until that works.*— Scope discipline

*Chapter XVI — The Close*

## XVI. Why this wins

Six reasons, one breath each.

01

### A real, urgent problem

25× spread, climate collapse, hill-tribe poverty. Everyone in the audience drinks coffee.

02

### Technical depth in five layers

On-device CV, geospatial ML, LLM translation, marketplace, payments. Not a wrapper.

03

### Demo-able on stage

The scanner is the demo. Real beans, real phone, real result. No slides for the killshot.

04

### Realistic numbers

$50B TAM, 5,000-farmer SOM, $1M ARR Y3. Investor math, not hackathon math.

05

### Defensible social impact

Real income lift, real climate adaptation, real preservation of language and craft.

06

### Story the press loves

"Hill-tribe kid attends university because dad sold beans directly to Berlin." Headline writes itself.

*The only thing between a Doi Chang farmer and a Berlin roaster is a four-megabyte app.*— Closing line

---
*Bibliographic Note*

## Sources & *citations*

SCA Standards 2018 — Specialty grade defect taxonomy. [sca.coffee](https://sca.coffee)

Heinrich Böll Foundation — Chiang Rai specialty households 2025.

World Coffee Research — Climate impact on Arabica yield, +2°C scenario.

Springer 2025 — MobileNetV3 defect detection 98% accuracy.

Drip Roast — Thailand specialty retail price benchmarks.

IPCC AR6 RCP4.5 — Regional climate projections SE Asia.

TMD Thailand Meteorological Department — 20-yr historical climate.

LDD Thailand Land Development Department — Soil GIS layer.

Stripe Connect — Cross-border escrow, KYC flows.

Bangkok Post 2025 — Hill-tribe ID reform; specialty coffee coverage.

DoiBean Deep Dive — *fascicle i*
Set in Figtree and Helvetica. Printed in pixels, May 2026.

[ภาษาไทย](index-th.html) · [Pitch deck](pitch-th.html) · [Standards](brand.html)

DoiBean Vol. 01 ·  ∎
