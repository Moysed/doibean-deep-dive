# DoiBean — Prototype Design Prompt

> A single comprehensive brief for prototyping the DoiBean mobile + web product. Written to be pasted into AI design tools (v0, Lovable, Bolt, Cursor) **or** handed to a human designer. Keep tone, palette, and rules — adapt screen list as needed.

---

## TL;DR (paste this if you only want one paragraph)

Design a mobile-first AgriTech app called **DoiBean** that turns a Thai specialty coffee farmer into a global-grade producer. The visual direction is **"hand-stamped coffee bag meets Q-grader cupping form"** — modern, generous whitespace, sharp typography, but with vintage paper warmth and tactile coffee-shop heritage. Bone-and-brick palette with espresso ink and golden crema accents. Figtree (Latin) + system Helvetica fallback (Thai). The app must work for an Akha hill-tribe farmer wearing gloves at 1,200m altitude in mountain wind, AND for a Tokyo specialty roaster who reviews lots over morning espresso. Hero interaction = the camera scan that turns 50 green beans into an SCA score reveal. Avoid every AI-slop fingerprint: no glassmorphism, no purple-blue gradients, no rounded card grids, no neon accents on dark mode, no gradient text. Make every screen feel like a real artifact (a logbook page, a lot tag, a cupping form).

---

## 1. Product context

**DoiBean** = AI co-pilot for Thai specialty coffee farmers. Closes the 25× price gap between farm gate (฿100/kg) and consumer cup (฿2,500/kg) by owning the lifecycle: variety planting → growing → harvest → quality scan → direct-to-roaster marketplace.

- **Origin:** Doi Chang, Chiang Rai (1,200–1,420m, NE-facing slopes)
- **Hero moment:** scan 50 green beans on white A4 → on-device CV returns SCA score, defect breakdown, similar-lot profile lookup, and price floor in <2 seconds. *(CV measures defects/size/density; the "profile" is a database lookup over comparable Doi Chang lots — not visual flavor prediction. Real cupping notes come from the roaster cup after delivery.)*
- **Sector:** AgriTech in Chiang Mai Global Digital Economy initiative (NDEA-backed)
- **Stack the dev will use:** Flutter (mobile, Android Go targeting), TFLite on-device, Node + Postgres, Mapbox, on-device LLM (THaLLE preferred for Thai)

You're designing the **interface layer** for a system that already has a thesis. The thesis is in `docs/deep-dive.md` — read Chapter VII (six modules) and Chapter XV (60-day MVP) before designing.

---

## 2. Audience — three users, one wedge

Design for all three. Optimize the demo for **Somchai**.

### 1. Somchai · 47 · Doi Chang farmer · primary user
- Akha or Lisu hill-tribe descent. Speaks village dialect; reads ~3rd-grade Thai.
- Owns a Samsung A04 ($60 phone). Gloves on hands. Mountain wind. Sun glare.
- Visits the app: weekly during harvest (Oct–Feb), monthly otherwise.
- Cares about: a fair price for his beans, knowing what to plant, getting paid fast.
- Doesn't care about: notifications, settings menus, anything corporate-looking.
- **Design rule:** large tap targets (56px+), high contrast, voice-first where possible, Thai-only UI by default, photo-led not text-led.

### 2. Pim · 32 · Bangkok specialty roaster · secondary user
- Buys 200kg/month for a 6-bar café group. Speaks fluent Thai + English.
- Uses iPad Pro at the roastery, iPhone in transit.
- Cares about: traceability, consistent grade, story to tell customers.
- Pays a premium for verified provenance.
- **Design rule:** desktop/tablet web app; data-dense; Q-grader vocabulary; export to PDF.

### 3. Hiroshi · 38 · Tokyo importer · power user
- Buys quarterly 1-container lots. English/Japanese, basic Thai.
- Uses MacBook Pro at the desk, mostly during 10am–6pm Tokyo time.
- Needs documentation in English + cupping notes that match what he tastes when he cups.
- **Design rule:** English UI as a first-class language; PDF report-led; long memory of past lots.

---

## 3. Aesthetic direction — TWO MODES, deliberate split

### Single-sentence brief
DoiBean has a split personality: **friendly-warm everyday screens** (Home, Onboarding, Tutorial, Earnings) crossed with **editorial cupping-form data screens** (Score Reveal, Lot Detail, Variety Advisor). The mix is what makes it both approachable for a hill-tribe farmer and credible for a Tokyo Q-grader.

### Mode A — "Friendly Everyday" (warm, illustrated, photo-led)
Reference: `docs/references/style-reference-recipe-app.png` — coffee recipe app with warm illustrated barista hero, big rounded yellow/brick primary CTAs, pill chip selectors, photo cards with rank badges, friendly bottom-tab nav.

Stretch the reference's vibe onto OUR palette: bone background instead of peach, brick + crema instead of generic yellow/coral. Borrow the warmth, the rounded-full pills, the photo cards, the illustrated splash — keep our specific color identity.

For: Onboarding splash, Home/Today, Tutorial Videos, Earnings, Marketplace browse cards, profile/settings, empty states.

### Mode B — "Editorial Cupping Form" (precise, structured, honest)
Reference: real Q-grader cupping forms, Cereal Magazine layouts, hand-stamped coffee bag tags. Letterpress feel, registration ticks at corners, hand-numbered lots, mono labels, hairline rules, rotated stamps.

Each Mode B screen feels like a small physical document — a logbook page, a lot tag, a cupping form. This is where credibility lives.

For: Score Reveal, Lot Detail body (the cupping form + traceability section), Variety Advisor with SHAP explanations, Q-grader signoff, the cupping-form metaphor cover.

### Mode-switching rules
- **Same palette across both modes** — never break out of bone/brick/crema/espresso/moss/slate
- **Mode A signals**: rounded-full CTAs, photo cards, illustrated heroes, pill chips, larger corner radius (16–24px), softer shadows allowed on photo cards, more crema/yellow accents
- **Mode B signals**: corner radius max 4px, mono labels, hairline borders, registration ticks, brick on espresso, no shadows
- **Transitions feel intentional**: tapping a friendly Home card opens the editorial Score Reveal — feels like opening a serious document inside a friendly app
- **Never blend within a single screen** — pick the mode, commit. Bottom CTA can borrow Mode A buttons even on Mode B screens (acceptable boundary).

### Mood adjectives
**warm · structured · tactile · honest · slow-craft · paper-and-ink · numbered · stamped · ranked · scored · grounded**

NOT: minimal, neon, glassy, futuristic, AI-y, generic-SaaS, cyberpunk, "clean" without warmth.

### References (study these together — direction lives in their intersection)
- **Cereal Magazine** layouts — generous whitespace, editorial rhythm
- **Monocle** — small caps, structured indices, mono labels
- **Q-Grader cupping forms** — score grids, tick boxes, defect taxonomy
- **Field & Foundry** (real coffee bag designs) — letterpress, hand-stamped
- **Counter Culture Coffee** lot tags — number + altitude + producer + date
- **Real artifact references**: Q-grader evaluation sheets, agricultural lab reports, Thai government export documents, vintage burlap coffee bags, hand-numbered roaster bags
- **NOT** Linear, Notion, Vercel, Stripe (those are good but generic SaaS — wrong vibe)
- **NOT** Apple-flat or Material 3 — too generic; we want *specific*

### The "old scent" requirement (literal motifs to consider)
- **Corner registration ticks** — like printers proofs, in espresso ink
- **Stamped artifact look** — rotated "PRELIMINARY" or "GRADED" stamps in brick red
- **Hand-numbered lots** — every lot gets `LOT 047 · DOI CHANG · 2026-11-14`
- **Letterpress numerals** — large, slightly italic, in brick or crema
- **Paper texture** — barely-there grain, never a Photoshop noise layer; a single subtle paper grain SVG over bone background
- **Coffee-ring stains** — ONE of these on the splash screen, never elsewhere
- **Botanical line drawings** — thin-line coffee cherry/branch as section dividers, hand-drawn feel
- **Wax seal** for "verified by Q-grader" badge
- **Burlap pattern accent** as a footer texture (subtle, 3% opacity)

### The "modern" requirement
- **Fluid spacing** with `clamp()` — breathes between mobile and desktop
- **Sharp type hierarchy** — 5-step scale, real weight contrast (300 / 400 / 500 / 600)
- **Camera-as-canvas** — live overlay during scan with detected beans highlighted
- **Pull-to-reveal score** moment — the scan output animates in like a cupping form being filled
- **Bottom-sheet** patterns on mobile (not modals)
- **Scroll-snap** on lot browsing
- **Real-time price** ticker on roaster web
- **Dark mode for outdoor** — high contrast, espresso-on-bone *inverted to* bone-on-espresso, NOT generic dark gray
- **Haptics** on every score reveal, every payment confirm

---

## 4. Brand foundations (use these exact tokens)

### Palette (CSS custom properties)
```css
/* Paper & ink */
--bone:     #F4EFE6;   /* primary background */
--paper:    #FBF7EE;   /* cards, panels */
--espresso: #2A1810;   /* primary text, deep ink */
--ink:      #1A0F08;   /* darker, used for dark surfaces */

/* Coffee accents */
--crema:       #C8A268; /* primary accent — gold */
--crema-dim:   #A88C4F; /* numerals, secondary accent */
--crema-light: #E5C896; /* inverted accent on dark */

/* Editorial seasoning */
--brick: #B8543A;       /* hot accent — emphasis, score, action */
--moss:  #5C6B3F;       /* organic / certified / verified */
--stone: #C9C0B0;       /* hairline rules */
--stone-soft: #E4DDCB;  /* very soft dividers */
--slate: #5A4D3F;       /* secondary text */
```

**How to use them — Mode A (Friendly Everyday):**
- Bone background, warm crema as accent surface (cards, hero panels)
- Brick or crema as **primary CTA bg** (rounded-full, 56–64px tall, bone text)
- Pill chip selectors — bone bg + stone border default, brick bg + bone text when selected
- Photo cards with 16–20px corner radius, soft inner shadow OK
- Illustrations only in palette colors (no neon, no stock-illustration-ai-style)
- More crema/crema-light visible — warm and inviting

**How to use them — Mode B (Editorial Cupping Form):**
- Bone is the dominant surface (70%+)
- Espresso is the dominant ink. Never pure black.
- Crema (gold) for numerals, large display, verified marks
- Brick ONLY for emphasis — score numbers, primary CTAs, errors
- Moss ONLY for verified/certified/passed states
- Slate for secondary text, captions, mono labels
- Stone for hairline rules between sections

**Never (both modes):** purple, cyan, neon, gradient text, color combinations outside the palette.

### Typography
```css
--serif: "Figtree", "Helvetica Neue", Helvetica, sans-serif;       /* Latin */
--serif-th: "Figtree", "Helvetica Neue", Helvetica, sans-serif;    /* Thai falls back to system Thai */
--mono: "JetBrains Mono", ui-monospace, Menlo, monospace;          /* labels, eyebrows, numerals */
```

- **Display headlines** — Figtree 300 (Light), `letter-spacing: -0.02em`, line-height 0.9–1.05
- **Body** — Figtree 400, line-height 1.6 Latin / 1.7 Thai
- **Emphasis on Thai** — `font-weight: 500` + `color: var(--brick)` (NEVER italic — Tahoma/Helvetica skew Thai = ugly)
- **Emphasis on Latin** — italic 500 in brick (Figtree's italic is real and beautiful)
- **Mono labels** — JetBrains Mono 500, uppercase, `letter-spacing: 0.18em–0.32em`
- **Numerals** — Figtree 300 italic at large sizes for editorial flavor (Roman numerals: I, II, III)

### Spacing scale
Use `clamp()` for fluid sizing across mobile → desktop:
- gutters: `clamp(20px, 3.5vw, 56px)`
- section spacing: `clamp(48px, 8vh, 120px)`
- type scale: `clamp(15px, 1.05vw, 17px)` body / `clamp(48px, 8vw, 144px)` display

### Voice (writing for the UI)
- **Thai UI:** plain village-Thai, no English jargon. "เริ่มสแกน" not "Start Scan." "คะแนนเมล็ด" not "Bean Score."
- **English UI (roaster side):** specialty-coffee vocabulary. "Cupping notes" not "Tasting notes." "Lot ID" not "Product ID."
- Numbers ALWAYS lead — but as **ranges**, never single decimals. "82–86 SCA · ±2 confidence band" not "84.5 SCA". CV measures defects + size + color uniformity + density proxy (~20 SCA pts of signal); the remaining 80 pts come from a Q-grader cup. Show this contrast.
- Dates in stamped form: "2026-11-14 · DOI CHANG · 1,420m" not "November 14, 2026"
- Never say "Welcome" — say nothing or say what's happening.

---

## 5. Component vocabulary

### Pill Chip (Mode A — selectors and filters)
- Rounded-full, 36px tall, padding 12px 20px
- Default: bone bg, stone border, slate text
- Selected: brick bg (or crema for organic state), bone text, no border
- Inactive but enabled: stone-soft bg, slate text
- Used for: variety selection, score-range filter, process method, light/medium/strong, certification toggle
- Reference: the Light / Medium / Strong row in the recipe-app screenshot

### Primary CTA Button (Mode A)
- Rounded-full, 56–64px tall, full-width with 24px side margins on mobile
- Brick bg + bone text (default), or crema bg + ink text (alternate)
- Press state: scale 0.98 + slight darken
- Always has at least 16px vertical padding
- Reference: "Find My Recipe" yellow button + "Watch Videos" yellow button in the recipe-app screenshot

### Bottom Tab Nav (Mode A)
- Fixed bottom, 5 items max
- Filled-icon style (lucide-react filled or custom SVG), 24px icons
- Active: brick fill + tiny brick dot below
- Inactive: slate fill
- Center item can be elevated as a "create" capsule (brick bg with bone icon)
- Background: paper with hairline stone top border

### Photo Card with Rank Badge (Mode A)
- Photo at top (16:9 or 4:3), 16–20px rounded corners on photo
- Rank badge overlay top-left: small rounded-full crema bg + ink text "1", "2", "3"
- Below photo: title in Figtree 500, subtitle with avatar + name
- Used for: trending lots, tutorial videos, featured roasters

### Illustrated Hero (Mode A)
- Full-width or constrained image at top of splash/onboarding
- Hand-drawn style, palette colors only (bone + crema + brick + moss accents)
- Subject: Doi Chang farmer, coffee cherries, mountains, barista pouring, hands holding beans
- Aspect 4:5 or 5:6 vertical
- NEVER generic stock illustration. NEVER AI-generated illustration in the obvious style. Commission a real illustrator OR use a single matched style throughout.

### Lot Card (the core artifact — Mode B)
Every lot is rendered as a small physical-feeling card. Required:
- Number plate at top-left: `LOT 047`
- Origin line: `DOI CHANG · CHIANG RAI · 1,420m`
- Producer name in Figtree 500: `อุดร แซ่หม่า` or "Udorn Sae-Ma"
- Score range in giant brick numerals: `82–86` (range, never single decimal). Confidence band underneath in mono: `±2 SCA · sensory cup pending`
- Mini bar visualization for 6 cupping criteria (text-bar character `█████░░`)
- Stamp in corner: `VERIFIED Q · 2026-11-14` rotated -8°
- Hairline border in stone, no drop shadow

### Cupping Form (score reveal screen)
- Looks like a real Q-grader form
- 6 criteria rows: fragrance, flavor, aftertaste, acidity, body, balance
- Each row: criterion name (mono uppercase) + slider 0–10 + tick marks at integer points
- Defect declaration: `Cat-1: 0 · Cat-2: 3 (2 partial sour, 1 floater)`
- Final score: huge brick numeral with "Specialty Grade ≥80 SCA" stamp
- Bottom: Q-grader signature line (initials + date + farm)

### Camera Capture screen
- Full-bleed camera view
- Bottom sheet with capture instructions (Thai, large type, voice-readable)
- Detected-bean overlay: thin brick-red rectangles around each bean as CV finds them
- Bean count: `47 / 50` in large mono (target hit at 50)
- Capture button: 80px gold ring, espresso center, haptic on tap
- Top corner: kit indicator ("ใช้กระดาษ A4 ขาว" — small mono caption)

### Variety Advisor screen
- Map view with farmer's plot pinned (Mapbox)
- Below: 3 ranked variety recommendations with confidence bars
- Each variety: name + altitude band + climate-resilience score + SHAP-style reasons
- "อธิบาย" (explain) button → expands plain-Thai reasoning, not jargon
- Climate disclaimer in stone: "คำแนะนำเปลี่ยนได้ตามข้อมูล TMD ปีหน้า"

### Marketplace Lot Browse (roaster side)
- Desktop/tablet web
- Two-column: left is filter rail (origin, altitude, score range, process method, certification, producer), right is lot grid
- Lot grid uses the Lot Card component above
- Hover state: card lifts 2px, score number animates from grayscale to brick
- Infinite scroll with sticky filter rail
- **No** "Load More" buttons — scroll-driven

### Lot Detail (roaster side)
- Single full-width hero: photo of green beans (full-bleed)
- Below the fold: cupping form, defect declaration, traceability map, producer story
- Producer story is a single hand-written paragraph (translated via THaLLE), with original Thai shown via toggle
- Buy box: floating bottom-right on desktop, sticky bottom on mobile
- Price: `฿1,400 / kg` huge brick numeral + escrow-protected badge

### Pull Quote (used sparingly)
- Brick left rule, no quote marks
- Quote in Figtree 300, italic on Latin / weight-500 on Thai
- Attribution in mono uppercase below: `— SOMCHAI · DOI CHANG`

### Empty States
- Never say "No data" or "Nothing here"
- Show a hand-drawn coffee branch line illustration + a sentence in plain Thai
- Empty inbox: `ยังไม่มี roaster ทักเข้ามา · พักก่อน` ("No roaster has reached out yet — rest a while")

### Notifications
- Toast at top, espresso background, bone text, brick accent line on left
- Auto-dismiss in 4 sec
- Critical alerts: stay until dismissed, with "เข้าใจแล้ว" button

---

## 6. Screens to design (priority order)

Design these as separate frames. Show all relevant states (loading, success, error, empty, dark mode where applicable).

### Mobile (Somchai's app — Thai)
1. **Splash** — DoiBean wordmark + paper texture + coffee branch line + "v1.0 · ดอยช้าง"
2. **Onboarding** (3 steps) — language pick / phone OTP / GPS pin first plot
3. **Home / Today** — current harvest window, latest lot status, action card "ถ่ายเมล็ด"
4. **Camera Scan** — full-bleed camera + overlay + capture
5. **Score Reveal** — cupping form animates in, score counter ticks up to final, haptic
6. **Lot Detail (farmer view)** — what they scanned, market price, "ส่งไปขาย" CTA
7. **Marketplace Outbound** — list of submitted lots + status (waiting / offered / sold)
8. **Variety Advisor** — map + 3 recommendations + climate disclaimer
9. **Earnings** — chart of weekly income, last 12 lots, payout history
10. **Profile / Settings** — minimal: name + village + bank acct + language

### Desktop / Tablet (Pim's roaster web — bilingual)
11. **Roaster Home / Discover** — hero filter ("Find specialty Thai green") + featured 6 lots
12. **Marketplace Browse** — filter rail + lot grid
13. **Lot Detail** — hero photo + cupping + producer story + buy box
14. **My Cellar** — past purchases, cup notes, re-order flow
15. **Inbox** — direct messages with farmers, with auto-translate

### Optional / Phase 2
16. **Q-Grader review tool** (admin/QC) — accept/reject contested scans
17. **Variety XGBoost results page** (year 2 feature, plan now)
18. **Tokenized lot ownership** (Phase 2 — fractional via Bitkub Chain)

---

## 7. Interaction principles

### Tap targets
- Minimum 44px on iOS, 48px on Android
- Primary actions: 56px minimum, 80px on hero (camera capture)
- Outdoor-glove safe: increase by 1.2× when `prefers-coarse-pointer`

### Haptics
- Light tap on every interactive surface
- Medium impact on score reveal start
- Heavy impact on score reveal end (the "ka-thunk" of a cupping form filing)
- Success notification on payment confirmed (long buzz pattern)

### Motion (use sparingly, with purpose)
- **Score reveal**: criteria bars fill left-to-right with ease-out-quart, 600ms each, staggered 80ms
- **Number counter**: tick from 0 to final score over 800ms, ease-out-expo
- **Card hover** (web): translateY(-2px) + score color desaturate→brick over 200ms
- **Page transitions**: slide-fade, never zoom or fancy 3D
- **Reduced motion**: disable all of the above; show final state directly

### Loading states
- Never spinners. Always skeleton screens that mimic the actual content shape.
- Camera capture loading: bean overlay animates in one bean at a time as detected
- Score loading: criteria rows appear blank with mono dots `· · ·`, then fill

### Empty states
See component vocabulary above — never "No data found."

### Error states
- Errors have a personality. "เม็ดน้อยเกินไป — ลองใหม่อีกที พรุ่งนี้สดใหม่" (Too few beans — try again tomorrow when fresh)
- No red exclamation-mark icons. Use a small hand-drawn line illustration of a coffee cherry with a slight crack.
- Never modal. Always inline at the affected element.

### Forms
- One question per screen on mobile (progressive disclosure)
- Labels above fields, never floating
- Error inline below the field, brick text, no icon
- Submit buttons: full-width on mobile, 240px on desktop, espresso bg / bone text / brick underline-on-hover

---

## 8. Anti-patterns — do NOT do these

These are AI-slop fingerprints. Reject any output that includes them.

- ❌ Glassmorphism / frosted glass / backdrop-blur on cards
- ❌ Purple-to-blue gradients
- ❌ Cyan-on-dark color palette
- ❌ Neon accents on dark mode
- ❌ Gradient text on metrics or headings
- ❌ Identical card grids with icon + heading + text repeated
- ❌ Big rounded icons above every heading
- ❌ Generic drop shadows on rounded rectangles
- ❌ Centered hero with three-stat row "Big Number / Small Label"
- ❌ "Vol. 01 / Issue No. I" framing — already replaced with cupping form
- ❌ Italic Thai (Tahoma/Helvetica skew = synthetic and ugly)
- ❌ Drop caps on Thai content (Thai leading vowels ไ ใ เ แ โ break visually)
- ❌ Sparklines as decoration without data meaning
- ❌ Modal for anything that could be a bottom sheet or inline
- ❌ Linear/Notion/Vercel-clean — they're good but they're not *us*
- ❌ Material Design 3 components dropped in unchanged
- ❌ Stock photography of coffee — use real Doi Chang photos or commission illustrations
- ❌ Emoji icons in UI chrome
- ❌ "Welcome to DoiBean!" / "Get started in 3 easy steps!" — generic onboarding copy

---

## 9. Deliverables (pick what fits the tool)

### If you're using v0 / Lovable / Bolt (AI code generation)
Generate React/Next.js components for screens 1–10 above. Use the exact CSS variables in section 4. Mobile-first responsive. Tailwind allowed but only with arbitrary values matching the palette, no default Tailwind colors.

### If you're using Figma (designer brief)
- Single Figma file, organized by user (Somchai / Pim / Hiroshi as separate pages)
- Each page: 1 cover frame + N screen frames + 1 component library frame
- Auto-layout everywhere; design tokens as Figma variables
- Min 3 states per screen: loading / loaded / error

### If you're using Midjourney / Imagen for moodboard
Three image sets:
1. "Doi Chang green coffee beans on white A4 paper, soft natural light, hand-stamped corner, paper grain"
2. "Q-grader cupping form filled in by hand, espresso ink, brick red emphasis on score, vintage paper texture"
3. "Modern mobile app screen featuring a coffee lot card with hand-stamped numbering, bone background, brick accent, no glassmorphism, no gradients"

### Output format
- Light-mode primary
- Dark-mode for camera scan + outdoor screens (espresso bg, bone text, crema accents)
- Mobile (390×844 reference) + desktop (1440×900 reference)
- Include 3 sample lot cards with realistic Thai data (real Doi Chang producer names, real altitude numbers, similar-lot profile notes — labelled clearly as database lookup, not AI-from-photo)

---

## 10. Last note — the "old scent" test

Before submitting any screen, ask yourself:

> "Does this feel like a coffee artifact, or does it feel like a SaaS app?"

If it feels like SaaS, push it 30% more toward letterpress / cupping form / hand-stamped. The user should feel they're holding a small object made by someone who actually cares about coffee. That's the wedge.

A successful screen makes someone ask **"who made this app?"**, not **"which AI generated this?"**

---

**Brief author:** Almondo-local Boardroom · พฤษภาคม 2026
**Project repo:** https://github.com/Moysed/doibean-deep-dive
**Source content:** `docs/deep-dive.md` (Ch VII modules, Ch XV MVP scope), `docs/brand.md` (visual standards), `docs/9-box-ai-brief.th.md` (AI solution architecture)
