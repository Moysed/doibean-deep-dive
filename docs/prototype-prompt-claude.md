# DoiBean — Claude Artifact Prompt

> Paste this entire prompt into a fresh Claude.ai conversation. It will produce a working interactive prototype as a single artifact.

---

## ⤵️ COPY FROM HERE ⤵️

Build a working interactive prototype of **DoiBean** — a mobile-first AI app for Thai specialty coffee farmers. Single React + Tailwind artifact with screen-switching navigation. Use the exact design tokens below; do not invent new colors or fonts.

### What it is

DoiBean lets a Thai hill-tribe farmer scan their green coffee beans with a phone camera, get an instant SCA quality score, then sell directly to international roasters at 14× the co-op price. The hero interaction is the camera scan that turns 50 beans on a white A4 paper into a live cupping form filling in.

### Aesthetic direction (read carefully — TWO MODES)

**Two-mode design: friendly-everyday × editorial-data.**

The app has a split personality, intentional and load-bearing:

#### Mode A — "Friendly Everyday" (warm, illustrated, approachable)
For screens the farmer touches every day: **Splash, Onboarding, Home, Tutorial Videos, Earnings, Empty states.**

Reference: see `docs/references/style-reference-recipe-app.png` — soft beige background, illustrated barista hero, big rounded yellow/brick primary buttons, pill-shaped chip selectors, photo thumbnails in cards with rank badges, friendly bottom-tab nav with filled icons. Warm coral + yellow + cream palette, but stretched onto OUR palette (bone + crema + brick instead of generic peach/coral).

The vibe: a coffee-recipe app made by people who actually love coffee. Welcoming. Not intimidating to a hill-tribe farmer.

#### Mode B — "Editorial Cupping Form" (precise, structured, honest)
For data-credibility screens: **Score Reveal, Lot Detail (roaster view), Q-grader signoff, Variety Advisor with SHAP explanations.**

Reference: a Q-grader cupping form. Letterpress feel, hand-stamped corner marks, hand-numbered lots, coffee artifact references. Cereal Magazine layouts crossed with a real Q-grader cupping evaluation form, not Linear or Notion. Each data screen feels like a small physical object — a logbook page, a lot tag, a cupping form.

This mode is where the credibility lives. When the farmer scans beans or the roaster reads a lot detail, they see a real evaluation document, not a friendly app.

#### How to switch between modes
- Use **the same palette** — never break out of bone/brick/crema/espresso/moss/slate
- Mode A = more crema (warm gold), more yellow accents on CTAs, illustrations as hero, photos in cards, pill chips, larger button radius (rounded-full)
- Mode B = more espresso/ink, mono labels, hairline rules, registration ticks, score grids, smaller corner radius (4px)
- Transitions between modes feel intentional — going from Home (friendly) into a Score Reveal (editorial) should feel like opening a serious document inside a friendly app

Never blend the modes within a single screen. Pick one and commit.

### Design tokens (use exactly these)

```css
/* Palette */
--bone:        #F4EFE6;  /* primary bg, 70% of screen */
--paper:       #FBF7EE;  /* card / panel surface */
--espresso:    #2A1810;  /* primary text — never pure black */
--ink:         #1A0F08;  /* deep dark surfaces */
--crema:       #C8A268;  /* primary gold accent */
--crema-dim:   #A88C4F;  /* numerals secondary */
--crema-light: #E5C896;  /* inverted accent on dark */
--brick:       #B8543A;  /* hot accent — score, CTA, emphasis */
--moss:        #5C6B3F;  /* verified / certified state */
--stone:       #C9C0B0;  /* hairline rules */
--stone-soft:  #E4DDCB;  /* very soft dividers */
--slate:       #5A4D3F;  /* secondary text */

/* Type */
--serif: 'Figtree', 'Helvetica Neue', Helvetica, sans-serif;
--mono:  'JetBrains Mono', ui-monospace, Menlo, monospace;
```

Load Figtree from Google Fonts. JetBrains Mono too. No other fonts.

### Color use rules

**Mode A — Friendly Everyday:**
- Bone background, crema as warm accent, larger areas of warm gold (`#C8A268`) or `crema-light` (`#E5C896`)
- Primary CTAs: rounded-full, brick (`#B8543A`) or crema bg, bone text — large (56–64px tall)
- Pill chip selectors: bone bg + stone border, selected state = brick bg + bone text
- Photo cards: full-bleed photos with rounded 16–20px corners, soft inner shadow OK here
- Illustrations: warm-tone hand-drawn (coffee cherry, barista, farmer with beans), in palette colors only — no AI-generated stock illustration

**Mode B — Editorial Cupping Form:**
- Bone is the dominant surface (70%+).
- Espresso is the dominant ink. Never pure black.
- Brick ONLY for emphasis: score numbers, primary CTAs, errors.
- Moss ONLY for verified/certified/passed states.
- Crema for numerals, large display numbers, verified marks.
- Slate for secondary text, captions.

**Never (both modes):** purple, cyan, neon. No combinations outside the palette.

### Type rules
- Display headlines: Figtree 300, `letter-spacing: -0.02em`, line-height 0.9–1.05
- Body: Figtree 400, line-height 1.6
- Mono labels: uppercase, `letter-spacing: 0.18em–0.32em`
- Roman numerals (I, II, III) Figtree 300 italic at large sizes
- Emphasis on Latin: italic 500 in brick
- For Thai script: weight 500 + brick color (NEVER `font-style: italic` on Thai — synthetic skew looks bad)
- Numbers always lead. "82–86 SCA" not "Quality: 82–86"
- **Honest ranges, not false precision** — every score is a range with a confidence band, never a single decimal. Show the breakdown of what was measured (defects, size, color uniformity, density proxy) vs what's pending (sensory cup by Q-grader, 80 of 100 SCA pts).

### Screens to build (5 — tight, two-mode mix)

Add a bottom tab nav (filled icon style like the reference) with these screens. Each should be polished, not a wireframe.

#### Screen 1 — Home / Today  *(Mode A — Friendly)*
- Top: avatar + farmer name "อุดร แซ่หม่า" (NOT "Welcome Udorn")
- Hero question card: "วันนี้สแกนล็อตอะไร?" (What lot are you scanning today?) — large rounded card with hand-drawn coffee branch illustration on the right (warm tones in palette)
- Search row: rounded pill `🔍 ค้นหาล็อต`
- "ล็อตล่าสุด" section header with "ดูทั้งหมด" link on right
- 2-up horizontal lot cards with photo thumbnails — each card shows: photo of beans with rank badge (`1`, `2` like in the reference), lot name "ล็อต 047 · ดอยช้าง", farmer + score range
- "วิดีโอสอน" (Tutorial videos) section — full-width photo card with bold title "วิธี HOW TO MAKE..." (in the reference style)
- Bottom tab nav 5 icons: Home / สแกน / สร้าง / บันทึก / โปรไฟล์ — filled icon style, brick when active

#### Screen 2 — Camera Scan & Score Reveal  *(Mode B — Editorial)*
This is where the cupping-form aesthetic lives. Mode A friendliness disappears — the user is looking at a serious evaluation document.

- Two-state screen with toggle at top to flip between "Capture" and "Result"
- **Capture state**: Faux camera viewfinder (gradient bg simulating camera) with overlay frame `ใช้กระดาษ A4 ขาว · กระจายเมล็ด 50 เม็ด`. Detected-bean count counter "47 / 50" in large mono. Big circular capture button (80px gold ring, brick center). *Stays minimal — this is a tool screen.*
- **Result state**: Pre-screening report card with corner registration ticks (small espresso L-shapes at 4 corners). Top section is **what we measured from the photo**: defect declaration row `Cat-1: 0 · Cat-2: 3 (−6 pts)`, bean size row `Sc.17 87% · Sc.16 13%`, color uniformity row `93% σ < 0.08`, density proxy `7.2/10`. Range estimate in HUGE brick numerals (72px+): **82–86 SCA** with smaller `±2 confidence band` below. Stamp in corner rotated -8°: `LIKELY SPECIALTY · ≥80 SCA` in brick border. Below that is the **PENDING** section in stone-soft type: 6 sensory criteria (fragrance, flavor, aftertaste, acidity, body, balance) shown as EMPTY text-block placeholders `· · · · · · · · · ·` with the label `Q-GRADER CUP REQUIRED · 80 of 100 pts`. This is the honest contrast — the form shows what AI did and what humans must still do.
- The result animates in: measured rows fill left-to-right with 80ms stagger; range counter ticks 80→82–86 over 800ms; the PENDING block stays empty (this is the honest visual moment, not a flaw).
- Bottom action: a single rounded-full brick pill **"ส่งไปขาย"** (Send to market) — switching back to Mode A button vocabulary because the next screen is friendly again.

#### Screen 3 — Marketplace / Lot Browse (roaster view)  *(Mode B — Editorial)*
- Switch to English for this screen (this is Pim the roaster's view — bilingual app)
- Top: filter pill chips (Origin, Altitude, Score Range, Process, Certification) — pill chip style from Mode A is allowed here even in editorial mode, because filter UI is universal
- Grid of **Lot Cards** (3–6 cards). Each Lot Card stays editorial:
  - Number plate: `LOT 047`
  - Origin line in mono: `DOI CHANG · CHIANG RAI · 1,420m`
  - Producer name in Figtree 500: `Udorn Sae-Ma`
  - Score in giant brick numerals: `82–86` (range, never single decimal). Below in mono: `±2 SCA · sensory pending`
  - Mini bar viz for 3 measured criteria (defect / size / uniformity) — using text blocks `█████░░`
  - Stamp rotated -8° in corner: `VERIFIED Q · 2026-11-14`
  - Hairline stone border, NO drop shadow, corner radius max 4px
- Hover state: card lifts 2px (translateY -2px)

#### Screen 4 — Lot Detail (roaster view)  *(Mode B base + Mode A hero)*
Inspired by the reference image's Recipe detail — large hero photo, then info chips, then structured detail below.

- **Top bar**: back arrow (circular bone bg) + "Lot Detail" centered + share icon (circular brick bg) — Mode A friendly chrome
- **Hero**: full-width photo of green beans on white A4 (or wood/burlap texture), rounded bottom corners (24px) — like the cappuccino hero in the reference. Photo lifts above the next section by ~32px
- **Lot title block** (just below hero): `LOT 047` in mono on top, then big "Doi Chang Catimor Washed" in Figtree 500, star rating "★ 84 SCA range" pulled from defect score, producer line with avatar circle: `Udorn Sae-Ma · ดอยช้าง`
- **Info chips row** (Mode A — like the reference's Arabica Beans / 25 Min Durations): 2 rounded pill chips with icon + label + value — `🫘 Catimor / Variety` and `📅 Nov 2026 / Harvest`
- **Below the fold (Mode B editorial)**: 2-column (single column on mobile)
  - **Left**: full cupping form (same as Screen 2 result, with measured + pending split), traceability box with mini map, GPS coords, altitude, harvest date
  - **Right**: producer story (single paragraph in Figtree 400, Thai with English toggle), grading notes from Q-grader, certification list (organic ✓ / fair-trade ✓)
- **Sticky bottom bar (mobile)**: price `฿1,400 / kg green` in brick + huge rounded-full **"Buy 60kg lot"** CTA in brick (Mode A friendly button) + escrow-protected badge in moss
- Desktop: buy box floats right; mobile: full-width sticky bottom

#### Screen 5 — Onboarding Splash (NEW)  *(Mode A — Friendly)*
A welcoming first-touch screen, modelled on the reference image's left phone.

- Top: full-width illustrated hero (~60% of screen) — hand-drawn warm scene of a Doi Chang farmer with green beans and the mountains in the background. Style: warm tones in palette only (bone, crema, brick, moss). NOT generic stock illustration. Hand-drawn feel.
- Below: question in Figtree 500 (centered): **"คุณปลูกกาแฟแบบไหน?"** (What kind of coffee do you grow?)
- Subtitle: "เลือกประเภทเพื่อรับคำแนะนำสายพันธุ์" (Pick a type to get variety advice)
- 3 pill chip options in a row (like Light/Medium/Strong in the reference): **"Arabica"**, **"Robusta"**, **"ผสม"** (Mix) — selected state = brick bg + bone text + soft glow
- Page indicator (3 dots) below
- Big rounded-full brick CTA at bottom: **"เริ่มต้นใช้งาน"** (Get started) — full-width with 24px side margins, 56px tall

### Interaction & polish requirements

- Smooth transitions between screens (slide-fade, 300ms ease-out-quart)
- On the score reveal screen, animate the cupping form filling in (stagger 80ms per row) — this is the hero moment
- Hover lift on Lot Cards (translateY -2px, 200ms)
- All buttons get tap-state (scale 0.98)
- Reduced-motion media query disables all motion
- Use `clamp()` for fluid typography
- Mobile-first; design at 390px wide first, then enhance for desktop

### Anti-patterns — DO NOT use any of these

- ❌ Glassmorphism / backdrop-blur on cards
- ❌ Purple-to-blue or cyan gradients
- ❌ Neon accents on dark mode
- ❌ Gradient text on metrics or headings
- ❌ Generic drop shadows on rounded rectangles in **Mode B** (Mode A photo cards CAN have soft inner shadow)
- ❌ Identical card grids with icon + heading + text repeated
- ❌ Material Design 3 styling
- ❌ Linear/Notion/Vercel-clean (good but generic — we want specific)
- ❌ Italic on Thai script (browser fakes it as skew, looks bad)
- ❌ Drop caps on Thai paragraphs (Thai leading vowels break visually)
- ❌ "Welcome to DoiBean! 👋" generic onboarding tone
- ❌ Emoji icons in UI chrome (icons should be lucide-react or custom SVG, not OS emoji)
- ❌ Stock-photography vibes for illustrations — Mode A illustrations must feel hand-drawn, in palette only
- ❌ Mixing both modes within a single screen — pick one per screen, transitions between screens are fine

### The "old scent" requirement (literal motifs)
Use at least 3 of these in the artifact:
- Corner registration ticks (small L-shapes at panel corners, espresso color)
- Hand-numbered lots: `LOT 047 · DOI CHANG · 2026-11-14`
- Stamped artifacts: rotated `PRELIMINARY` or `VERIFIED Q` stamps in brick
- Subtle paper texture (very low opacity radial gradient with bone tones)
- Hairline rules between sections (1px stone)
- Mono labels in uppercase with wide letter-spacing
- Roman numerals (I, II, III) in italic brick

### Quality test before you ship
Before finalizing the artifact, ask yourself:
- Does this feel like a coffee artifact, or like SaaS?
- Could a Q-grader recognize the cupping form vocabulary?
- Would a Doi Chang farmer with gloves on hit the buttons?
- If someone said "AI made this," would they believe it immediately?

If yes to the last question, push harder toward letterpress + hand-stamped + cupping-form vocabulary.

### Sample data to use
Use realistic Thai coffee specifics, not placeholders:
- Producer names: อุดร แซ่หม่า (Udorn Sae-Ma), อาเมะ จะสือ (Ame Jasue), หมี่หย่า (Mee Ya)
- Altitudes: 1,200m / 1,340m / 1,420m
- Varieties: Catimor, Typica, Caturra, SL28
- Processes: Washed, Honey, Natural, Anaerobic
- Similar-lot profile notes (database lookup, not AI-from-photo): floral, jasmine, citrus acidity, dark chocolate, panela, bergamot. Always label this with `(n=47 similar lots)` or `Roaster cup pending` to be honest about what's predicted vs measured.
- Score ranges (NEVER single decimals): 82–86, 84–88, 86–90, 80–84, 83–87. Always show with confidence band.
- Roasters: Counter Culture, Roar Coffee Tokyo, Bonanza Berlin, Roots Bangkok

### Final output

Single self-contained React component artifact with:
- **Bottom tab nav** with filled icons (like reference): Home / สแกน / สร้าง / บันทึก / โปรไฟล์ — brick when active, slate when inactive
- 5 polished screens (Onboarding · Home · Scan/Result · Marketplace · Lot Detail)
- Working state for the scan-to-result animation
- Both modes visibly distinct: Home/Onboarding/Tutorial = warm friendly; Scan-Result/Marketplace cards/Lot detail body = editorial cupping form
- Mobile-first responsive (works at 390px and 1440px)
- All design tokens applied via Tailwind arbitrary values or inline style
- Comments are minimal — make the code itself the documentation

Make it feel real. Make it feel grounded in Doi Chang. Make it feel like a coffee object first and an app second.

## ⤴️ COPY TO HERE ⤴️

---

## Visual reference

**Style reference for Mode A (Friendly Everyday):** see `docs/references/style-reference-recipe-app.png` in this repo (Dribbble-style coffee recipe app). Borrow:
- Warm beige background, photo cards with rounded corners
- Big rounded-full primary CTA buttons (we use brick or crema, not their yellow)
- Pill chip selectors (Light/Medium/Strong → ours: Arabica/Robusta/Mix or score-range filters)
- Bottom tab nav with filled icons + active state highlight
- Illustrated hero on splash/onboarding (warm tones, hand-drawn)
- Photo cards with rank badges (1, 2 like the reference)
- Avatar circle + creator name pattern

**Don't borrow from the reference:** their specific yellow/coral palette (use ours), their consumer copy tone (we're farmer + roaster, not coffee-recipe consumer), or any photography of finished drinks (we're green beans + farmers).

## Tips for getting the best result

1. **First reply is best**: Claude artifacts are highest quality on the first response. If unsatisfied, refine with `"Make Screen 2 cupping form feel more letterpress — register marks at corners, score range in 72px Figtree 300, larger paper texture, slight brick stamp rotated."`

2. **Iterate one screen at a time**: After the initial 4-screen artifact, ask `"Polish Screen 2 only — make the bean detection overlay feel more tactile, add subtle haptic-style scale on tap, slow the score reveal to 1200ms."`

3. **Add screens in follow-ups**: `"Add a fifth screen: Variety Advisor for the farmer. Map placeholder + 3 ranked variety recommendations + climate disclaimer."`

4. **Color drift is the most common error**: If Claude introduces a new color (a stray blue, a gray-on-gray header), call it out specifically: `"Remove all blue/cyan tones — only the palette in section 'Design tokens' is allowed. The 'Verified' badge should be moss green not teal."`

5. **The 'old scent' is the differentiator**: If output feels too clean/SaaS, paste this single line: `"Push 30% more toward letterpress and hand-stamped — registration ticks, paper grain, rotated stamps, hand-numbered lots. Right now it looks like generic SaaS."`

6. **Mode bleed — most common error**: If Mode A friendliness leaks into Mode B (e.g., the Score Reveal gets rounded-full pill buttons), call it out: `"Score Reveal screen needs to feel like a printed Q-grader form — go back to 4px corner radius, mono labels, hairline rules, rotated stamp. The friendly buttons belong only at the bottom 'Send to market' action."`

7. **Reference image guidance**: To anchor Mode A, paste: `"Look at /docs/references/style-reference-recipe-app.png for Mode A vibe — warm illustrated splash, rounded photo cards with rank badges, big rounded primary CTAs, pill chip selectors, friendly bottom tab nav. Apply that warmth to Home / Onboarding / Tutorial / Earnings screens, NOT to Score Reveal or Lot Detail body."`

---

**Source:** boardroom synthesis from `docs/DoiBean-Boardroom-Summary.pdf` and `docs/9-box-ai-brief.th.md`
**Repo:** https://github.com/Moysed/doibean-deep-dive
