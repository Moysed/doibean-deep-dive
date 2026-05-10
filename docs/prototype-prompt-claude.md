# DoiBean — Claude Artifact Prompt

> Paste this entire prompt into a fresh Claude.ai conversation. It will produce a working interactive prototype as a single artifact.

---

## ⤵️ COPY FROM HERE ⤵️

Build a working interactive prototype of **DoiBean** — a mobile-first AI app for Thai specialty coffee farmers. Single React + Tailwind artifact with screen-switching navigation. Use the exact design tokens below; do not invent new colors or fonts.

### What it is

DoiBean lets a Thai hill-tribe farmer scan their green coffee beans with a phone camera, get an instant SCA quality score, then sell directly to international roasters at 14× the co-op price. The hero interaction is the camera scan that turns 50 beans on a white A4 paper into a live cupping form filling in.

### Aesthetic direction (read carefully)

**"Hand-stamped coffee bag meets Q-grader cupping form."**

Modern mobile UI with vintage paper warmth. Generous whitespace, sharp typography, but with tactile coffee-shop heritage — letterpress feel, hand-stamped corner marks, hand-numbered lots, coffee artifact references. Think Cereal Magazine layouts crossed with a real Q-grader cupping evaluation form, not Linear or Notion.

Every screen should feel like a small physical object — a logbook page, a lot tag, a cupping form — not a generic SaaS interface.

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
- Bone is the dominant surface (70%+).
- Espresso is the dominant ink. Never pure black.
- Brick ONLY for emphasis: score numbers, primary CTAs, errors.
- Moss ONLY for verified/certified/passed states.
- Crema for numerals, large display numbers, verified marks.
- Slate for secondary text, captions.
- Never combinations not on this list. No purple, no cyan, no neon.

### Type rules
- Display headlines: Figtree 300, `letter-spacing: -0.02em`, line-height 0.9–1.05
- Body: Figtree 400, line-height 1.6
- Mono labels: uppercase, `letter-spacing: 0.18em–0.32em`
- Roman numerals (I, II, III) Figtree 300 italic at large sizes
- Emphasis on Latin: italic 500 in brick
- For Thai script: weight 500 + brick color (NEVER `font-style: italic` on Thai — synthetic skew looks bad)
- Numbers always lead. "82–86 SCA" not "Quality: 82–86"
- **Honest ranges, not false precision** — every score is a range with a confidence band, never a single decimal. Show the breakdown of what was measured (defects, size, color uniformity, density proxy) vs what's pending (sensory cup by Q-grader, 80 of 100 SCA pts).

### Screens to build (4 — keep tight)

Add a top tab nav with these 4 screens. Each should be polished, not a wireframe.

#### Screen 1 — Home / Today
- Greeting: "สวัสดี อุดร" (no English "Welcome")
- Today's harvest window status card: "เก็บเกี่ยวพรุ่งนี้ดี · ฝนวันพฤหัส" with a small temperature/forecast strip
- Latest lot status card: shows last scanned lot with score, status (รอ roaster / มี offer / ขายแล้ว)
- Big primary action button: **"ถ่ายเมล็ด"** (Scan Beans), 80px tall, brick bg, bone text, gold ring
- Bottom: 3 mini stats (this month income / lots sold / avg score)

#### Screen 2 — Camera Scan & Score Reveal
- Two-state screen with toggle button at top to flip between "Capture" and "Result"
- **Capture state**: Faux camera viewfinder (gradient bg simulating camera) with overlay frame `ใช้กระดาษ A4 ขาว · กระจายเมล็ด 50 เม็ด`. Detected-bean count counter "47 / 50" in large mono. Big circular capture button (80px gold ring, brick center).
- **Result state**: Pre-screening report card. Top section is **what we measured from the photo**: defect declaration row `Cat-1: 0 · Cat-2: 3 (−6 pts)`, bean size row `Sc.17 87% · Sc.16 13%`, color uniformity row `93% σ < 0.08`, density proxy `7.2/10`. Range estimate in HUGE brick numerals (72px+): **82–86 SCA** with smaller `±2 confidence band` below. Stamp in corner rotated -8°: `LIKELY SPECIALTY · ≥80 SCA` in brick border. Below that is the **PENDING** section in stone-soft type: 6 sensory criteria (fragrance, flavor, aftertaste, acidity, body, balance) shown as EMPTY text-block placeholders `· · · · · · · · · ·` with the label `Q-GRADER CUP REQUIRED · 80 of 100 pts`. This is the honest contrast — the form shows what AI did and what humans must still do.
- The result animates in: measured rows fill left-to-right with 80ms stagger; range counter ticks 80→82–86 over 800ms; the PENDING block stays empty (this is the honest visual moment, not a flaw).

#### Screen 3 — Marketplace / Lot Browse (roaster view)
- Switch to English for this screen (this is Pim the roaster's view)
- Top: filter chips (Origin, Altitude, Score, Process, Certification)
- Grid of **Lot Cards** (3–6 cards). Each Lot Card:
  - Number plate: `LOT 047`
  - Origin line in mono: `DOI CHANG · CHIANG RAI · 1,420m`
  - Producer name in Figtree 500: `Udorn Sae-Ma`
  - Score in giant brick numerals: `82–86` (range, never single decimal). Below in mono: `±2 SCA · sensory pending`
  - Mini bar viz for 3 cupping criteria using text blocks
  - Stamp rotated -8° in corner: `VERIFIED Q · 2026-11-14`
  - Hairline stone border, NO drop shadow, NO rounded corners over 4px
- Hover state: card lifts 2px (translateY)

#### Screen 4 — Lot Detail (roaster view)
- Hero: full-width "photo placeholder" — a textured div using bone+stone gradient with a subtle coffee-bean SVG silhouette pattern
- Below hero: 2-column layout
  - **Left**: cupping form (same as Screen 2 result), traceability box with mini map placeholder, GPS coords, altitude, harvest date
  - **Right**: producer story (single paragraph in Figtree 400), grading notes from Q-grader, certification list (organic ✓ / fair-trade ✓)
- Sticky buy box bottom-right: price `฿1,400 / kg green` in huge brick, "Buy 60kg lot" CTA, escrow-protected badge in moss

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
- ❌ Generic drop shadows on rounded rectangles (use hairline borders instead)
- ❌ Identical card grids with icon + heading + text
- ❌ Material Design 3 styling
- ❌ Linear/Notion/Vercel-clean (good but generic — we want specific)
- ❌ Italic on Thai script (browser fakes it as skew, looks bad)
- ❌ Drop caps on Thai paragraphs (Thai leading vowels break visually)
- ❌ "Welcome to DoiBean! 👋" generic onboarding tone
- ❌ Emoji icons in UI chrome
- ❌ Stock-photography vibes — use textured divs and SVG placeholders, not generic stock images

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
- Top tab nav (Home / Scan / Marketplace / Lot Detail)
- 4 polished screens
- Working state for the scan-to-result animation
- Mobile-first responsive (works at 390px and 1440px)
- All design tokens applied via Tailwind arbitrary values or inline style
- Comments are minimal — make the code itself the documentation

Make it feel real. Make it feel grounded in Doi Chang. Make it feel like a coffee object first and an app second.

## ⤴️ COPY TO HERE ⤴️

---

## Tips for getting the best result

1. **First reply is best**: Claude artifacts are highest quality on the first response. If unsatisfied, refine with `"Make the cupping form on Screen 2 feel more letterpress — register marks at corners, score number in 72px italic Figtree 300, larger paper texture, slight brick stamp rotated."`

2. **Iterate one screen at a time**: After the initial 4-screen artifact, ask `"Polish Screen 2 only — make the bean detection overlay feel more tactile, add subtle haptic-style scale on tap, slow the score reveal to 1200ms."`

3. **Add screens in follow-ups**: `"Add a fifth screen: Variety Advisor for the farmer. Map placeholder + 3 ranked variety recommendations + climate disclaimer."`

4. **Color drift is the most common error**: If Claude introduces a new color (a stray blue, a gray-on-gray header), call it out specifically: `"Remove all blue/cyan tones — only the palette in section 'Design tokens' is allowed. The 'Verified' badge should be moss green not teal."`

5. **The 'old scent' is the differentiator**: If output feels too clean/SaaS, paste this single line: `"Push 30% more toward letterpress and hand-stamped — registration ticks, paper grain, rotated stamps, hand-numbered lots. Right now it looks like generic SaaS."`

---

**Source:** boardroom synthesis from `docs/DoiBean-Boardroom-Summary.pdf` and `docs/9-box-ai-brief.th.md`
**Repo:** https://github.com/Moysed/doibean-deep-dive
