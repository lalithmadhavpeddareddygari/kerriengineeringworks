# Kerri Engineering Works — Brand Guidelines

Version 2.0 · November 2026
Status: Approved for website, technical documents, presentations, product video and all brand assets. Logo approved (receiver-loop mark, option 3a).

**Files that travel with this document**
- `brand-kit/logo/` — master logo SVGs (see §5.6)
- `Kerri Brand System` — visual version of these rules

> **For AI assistants and designers:** This file is the single source of truth for the Kerri visual identity. Follow every rule marked **MUST**. Use only the colour values, fonts and sizes defined here. If a situation is not covered, choose the most restrained option: white background, Kerri Navy text, no accent.

---

## 1. Brand overview

**Company:** Kerri Engineering Works
**What we do:** Pneumatic sample conveying systems and laboratory equipment for the steel, cement, foundry and aluminium industries, supplied worldwide.
**Primary audiences:**
1. OEM and B2B procurement buyers comparing suppliers.
2. Engineers and plant operators checking specifications and operation.

**Brand character:** Established and dependable · Precise and engineering-led · Modern and automated.

**Design principles**
1. **White first.** Every layout starts on white. Structure comes from spacing and thin rules, not colour.
2. **Data is the hero.** Specifications, numbers and drawings are presented clearly and never decorated.
3. **One signal per view.** Each screen, page, slide or video frame has at most one element in the accent colour.
4. **Engineered, not styled.** Square corners, straight lines, consistent grid. No gradients, glows, bevels or decorative illustration.

---

## 2. Voice and copy

- Plain, factual, confident. Write like an engineer explaining to a buyer.
- Lead with the measurable benefit, then the specification. Example: "Sample in the lab in 40 seconds. Transfer distance up to 1200 m."
- Use SI units with a space before the unit: `4.5 bar`, `76 mm`, `65 °C`. Use `Ø` for diameter.
- Use British/International English spelling (colour, aluminium) for global material.
- Sentence case for all headings and buttons. UPPERCASE only for short labels set in Condensed (see 4.4).
- No exclamation marks, no superlatives without evidence ("world's best"), no emoji.
- Product naming: `Product Type Model` — e.g. "Transfer Station PS-1200". Part numbers: `KEW-PS-1200`, always in the mono font.

---

## 3. Colour

### 3.1 Palette

| Token | Name | HEX | RGB | CMYK (approx.*) | Role |
|---|---|---|---|---|---|
| `--kew-white` | White | `#FFFFFF` | 255 255 255 | 0 0 0 0 | Default background for everything |
| `--kew-navy` | Kerri Navy | `#0E2A47` | 14 42 71 | 100 75 35 50 | Headings, header/footer bars, dark video backgrounds, table header rules |
| `--kew-blue` | Kerri Blue | `#2470C9` | 36 112 201 | 85 48 0 0 | Primary buttons, links, active/selected states, diagram flow lines |
| `--kew-sky` | Sky Tint | `#E6F0FB` | 230 240 251 | 8 3 0 0 | Highlight panels, selected table rows, info callouts |
| `--kew-molten` | Molten (accent) | `#E8641B` | 232 100 27 | 0 70 95 0 | Single attention point: marker bars, key figure, "New" tag |
| `--kew-graphite` | Graphite | `#1C2430` | 28 36 48 | 75 60 45 70 | Body text |
| `--kew-steel` | Steel | `#5A6676` | 90 102 118 | 60 45 30 15 | Secondary text, captions, icons |
| `--kew-alloy` | Alloy | `#C8D0DA` | 200 208 218 | 20 12 8 0 | Borders, dividers, table rules |
| `--kew-mist` | Mist | `#F3F5F8` | 243 245 248 | 4 2 1 0 | Section backgrounds, cards, zebra rows |

\* CMYK values are starting points. Confirm against a printed proof before a print run.

**Supporting tints (on-dark text only):** `#8DB8EA` (light blue label on Navy), `#C9DCF3` (secondary text on Navy).

### 3.2 Status colours (UI and documents only)

These are **functional**, never decorative. They MUST NOT be replaced by Molten.

| Purpose | Text / icon | Background |
|---|---|---|
| Error | `#C8191F` | `#FCE8E8` |
| Warning | `#E0A100` (icon) / `#7A5300` (text) | `#FFF4D6` |
| Success | `#1E8A4C` | `#E3F4EA` |
| Info | `#2470C9` | `#E6F0FB` |

### 3.3 Proportion

Across any page, slide set or video sequence, aim for:

- White ~62%
- Mist ~12%
- Kerri Navy ~14%
- Kerri Blue ~7%
- Steel / Graphite (text) ~2%
- Molten **≤ 3%**

### 3.4 Approved text/background pairings (WCAG 2.1)

| Text | Background | Contrast | Allowed for |
|---|---|---|---|
| Navy `#0E2A47` | White | 14.6 : 1 | All text |
| Graphite `#1C2430` | White | 15.5 : 1 | All text |
| Steel `#5A6676` | White | 5.8 : 1 | All text |
| Kerri Blue `#2470C9` | White | 4.9 : 1 | All text, links |
| White | Navy | 14.6 : 1 | All text |
| White | Kerri Blue | 4.9 : 1 | Buttons, all text |
| Navy | Sky Tint | 13.0 : 1 | All text |
| Navy | Molten | 4.4 : 1 | Large/bold text only (≥ 18 px bold or ≥ 24 px) |

### 3.5 Colour rules

- MUST start every layout on White.
- MUST use Molten at most once per screen, page, slide or video frame.
- MUST NOT set body or small text in Molten, and MUST NOT put white text on Molten.
- MUST NOT use Molten for warnings, errors or status (avoids confusion with safety colours on the plant floor).
- MUST NOT use gradients, transparency effects on brand colours, or colours outside this palette (except photography and the status set).
- Charts: series order Navy → Kerri Blue → `#8DB8EA` → Steel → Alloy. Highlight one series in Molten only if it is the point of the chart.

---

## 4. Typography

### 4.1 Typefaces

| Role | Font | Weights | Licence |
|---|---|---|---|
| All text (headings, body, UI) | **IBM Plex Sans** | 400, 500, 600, 700 | SIL Open Font License (free) |
| Labels, lower thirds, tight columns | **IBM Plex Sans Condensed** | 500, 600, 700 | SIL OFL (free) |
| Numbers, part numbers, specifications, code | **IBM Plex Mono** | 400, 500 | SIL OFL (free) |

**Why IBM Plex:** an open-source superfamily designed for engineering and technical documentation, with matching Sans, Condensed and Mono styles so all text shares one rhythm. It is free for commercial use and available in Google Fonts, Google Docs/Slides, Canva, Figma and Adobe Fonts, and can be installed on Windows, macOS and Linux.

**Get the fonts:** https://fonts.google.com/specimen/IBM+Plex+Sans · https://github.com/IBM/plex

**Fallback stacks** (use when Plex cannot be installed, e.g. a client's PowerPoint):

```css
--kew-font: 'IBM Plex Sans', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
--kew-font-condensed: 'IBM Plex Sans Condensed', 'Arial Narrow', 'IBM Plex Sans', sans-serif;
--kew-mono: 'IBM Plex Mono', Consolas, 'Courier New', monospace;
```

In Microsoft Office without Plex installed, use **Arial** (text) and **Consolas** (numbers).

### 4.2 Type scale — web and screen (px)

| Token | Size | Line height | Weight | Letter spacing | Colour | Use |
|---|---|---|---|---|---|---|
| `display` | 64 | 1.0 | 700 | −3% | Navy | Hero headline, one per page |
| `h1` | 44 | 1.05 | 700 | −2.5% | Navy | Page title |
| `h2` | 30 | 1.15 | 600 | −1.5% | Navy | Section title |
| `h3` | 21 | 1.3 | 600 | 0 | Graphite | Card / sub-section title |
| `body-lg` | 19 | 1.6 | 400 | 0 | Steel | Intro paragraphs |
| `body` | 17 | 1.6 | 400 | 0 | Graphite | Default paragraph |
| `small` | 14 | 1.5 | 400 | 0 | Steel | Captions, footnotes |
| `label` | 13 | 1.2 | 700 Condensed | +8% UPPERCASE | Steel or Kerri Blue | Eyebrows, tags, table headers |
| `data` | 14 | 1.5 | 400 Mono | 0 | Graphite | Spec values, part numbers |
| `data-lg` | 28 | 1.1 | 500 Mono | 0 | Navy | Key figures in stat blocks |

Mobile: scale `display` to 40, `h1` to 32, `h2` to 24. Body stays 17.

### 4.3 Type scale — print documents (pt)

| Element | Size | Weight |
|---|---|---|
| Document title | 24 pt | 700 |
| Section heading | 14 pt | 600 |
| Body | 9.5–10 pt / 14 pt leading | 400 |
| Table text | 8.5 pt | 400 (values in Mono) |
| Labels | 7.5 pt Condensed | 700 uppercase |
| Footer | 7 pt Mono | 400 |

Minimum print size: 7 pt.

### 4.4 Typography rules

- MUST use sentence case for headings and buttons.
- UPPERCASE only in Condensed `label` style, max ~6 words.
- All numbers with units in specs and tables MUST use IBM Plex Mono.
- Left-align text. Never justify. Never centre paragraphs (centring is allowed only for end cards and single short lines).
- Max line length 70 characters for body text.
- Do not use italics for emphasis; use weight 600.

---

## 5. Logo

### 5.1 The mark

The Kerri mark is drawn from the receiving station of a Kerri pneumatic system:

- **The ring is the receiver loop.** The tube runs in straight along the top, bends round a large circular loop and ends in an open trough at the lower right. It is a path, not a closed circle.
- **The K sits inside the loop.** Its lower leg is the sample carrier: a rounded cylinder with two wear bands, pointing towards the trough opening the way a carrier leaves the loop.
- One stroke weight, flat single colour, no gradients or shading.

**Meaning in one line:** "Every sample arrives."

### 5.2 Lockups

| Lockup | Use | File |
|---|---|---|
| Horizontal (primary) | Website header, letterhead, email, datasheets, slides | `kerri-logo-horizontal-*.svg` |
| Stacked | Square spaces: end cards, social avatars with name, nameplates, packaging | `kerri-logo-stacked-*.svg` |
| Mark only | Favicon, app icon, social avatar, equipment decals, embroidery, watermarks | `kerri-mark-*.svg` |

Wordmark: "KERRI" in IBM Plex Sans Bold, +3% tracking. "ENGINEERING WORKS" in IBM Plex Sans Condensed Semibold, +24% tracking, ~28% of the KERRI size, aligned to the left edge of KERRI (horizontal) or centred (stacked). In the horizontal lockup the mark height equals the full height of the two text lines.

### 5.3 Colour versions

| Version | Mark + KERRI | Sub-line | Background |
|---|---|---|---|
| Primary | Navy `#0E2A47` | Steel `#5A6676` | White, Mist, Sky Tint |
| Reversed | White | `#8DB8EA` | Navy, dark photos on a solid Navy plate |
| One colour | Black `#000000` | Black | Fax, stamps, laser etching, engraving, single-colour print |
| Embroidery / decal | Navy or White thread / vinyl | same | Workwear, equipment panels |

The logo is never in Kerri Blue, Molten, or more than one colour inside the mark.

### 5.4 Clear space and minimum size

- Clear space: at least the height of the K stem (≈ 40% of the mark height) on all sides. Nothing else enters this space.
- Full mark (with carrier bands): **≥ 40 px** on screen, **≥ 12 mm** in print.
- Below 40 px use the **small-size mark** (`kerri-mark-small-*.svg`): heavier ring, no bands. Works down to 16 px.
- Horizontal lockup minimum width: 120 px on screen, 30 mm in print.

### 5.5 Logo rules

- MUST use the supplied files. Never redraw, retype or trace the logo.
- MUST NOT close the ring, rotate, stretch, outline, add shadows, glows, bevels or 3D effects.
- MUST NOT recolour outside §5.3, place the full-colour logo on busy photos without a solid plate, or add a tagline inside the clear space.
- MUST NOT put the mark inside another shape (circle, square badge) except an app icon tile: Navy square, White mark, mark at 70% of tile width.
- The mark is the company symbol. Product lines MUST NOT get their own mark; they use the Kerri logo + product name in IBM Plex Sans.

### 5.6 Logo files (`brand-kit/logo/`)

| File | Content |
|---|---|
| `kerri-mark-navy.svg` | Mark, Navy, full detail |
| `kerri-mark-white.svg` | Mark, White, for dark backgrounds |
| `kerri-mark-black.svg` | Mark, one-colour black |
| `kerri-mark-small-navy.svg` | Small-size mark (≤ 40 px), Navy |
| `kerri-mark-small-white.svg` | Small-size mark, White |
| `kerri-logo-horizontal-navy.svg` / `-white.svg` | Primary horizontal lockup |
| `kerri-logo-stacked-navy.svg` / `-white.svg` | Stacked lockup |

The lockup SVGs use live IBM Plex text. Before sending to a printer, sign maker or embroiderer, open in Illustrator / Inkscape / Figma and convert text to outlines. Export PNG at 2× and 4× and PDF from these masters as needed.

**Mark geometry (SVG, 100 × 100 viewBox)** — for developers and AI tools that need to rebuild it in code:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <defs>
    <mask id="k" maskUnits="userSpaceOnUse" x="0" y="0" width="100" height="100"><rect width="100" height="100" fill="#fff"/><rect x="40.5" y="58" width="30" height="11" rx="5.5" transform="rotate(38 55.5 63.5)" fill="#000" stroke="#000" stroke-width="6"/></mask>
    <mask id="b" maskUnits="userSpaceOnUse" x="0" y="0" width="100" height="100"><rect width="100" height="100" fill="#fff"/><g transform="rotate(38 55.5 63.5)" stroke="#000" stroke-width="1.8"><line x1="48" y1="56" x2="48" y2="71"/><line x1="63" y1="56" x2="63" y2="71"/></g></mask>
  </defs>
  <g fill="#0E2A47">
    <path d="M88 12 L48 12 A38 38 0 1 0 80.9 69" fill="none" stroke="#0E2A47" stroke-width="7"/>
    <g transform="translate(48 50) scale(0.9) translate(-48 -50)">
      <g mask="url(#k)"><rect x="29" y="30" width="10" height="40"/><polygon points="39,48 55,30 67,30 39,61"/></g>
      <rect x="40.5" y="58" width="30" height="11" rx="5.5" transform="rotate(38 55.5 63.5)" mask="url(#b)"/>
    </g>
  </g>
</svg>
```

### 5.7 Trademark

File in Nice **Class 7** (pneumatic conveying machinery) as both word mark (KERRI) and device mark. Before filing, complete an IP India public search (word + Vienna-code device search in Class 7) and obtain an attorney opinion. Keep the ring open in every use; it is part of what distinguishes the mark from circle-enclosed letter marks.

---

## 6. Layout, grid and spacing

### 6.1 Spacing scale (px)

`4 · 8 · 16 · 24 · 32 · 48 · 64 · 88`

- Inside components: 8–24.
- Between components: 24–48.
- Between page sections: 88 (desktop), 56 (mobile).

### 6.2 Grids

- **Web:** 12 columns, 1180 px max content width, 24 px gutters, 48 px outer margin (20 px on mobile).
- **A4 / Letter documents:** 20 mm margins, 6 columns, 5 mm gutters.
- **Slides (16:9, 1920×1080):** 96 px margins, 12 columns, 32 px gutters.
- **Video (1920×1080):** keep all text inside the 8% title-safe area (154 px left/right, 86 px top/bottom).

### 6.3 Shape and structure

- Corner radius: **0–2 px maximum**. No pills, no rounded cards.
- Borders: 1 px Alloy `#C8D0DA`. Emphasis rules: 2–3 px Navy.
- Shadows: none. Use Mist backgrounds or Alloy borders to separate.
- Section backgrounds alternate White and Mist. Use Navy sections sparingly (max one per page) for key figures or CTAs.

---

## 7. Components

### Buttons
| Type | Style |
|---|---|
| Primary | Kerri Blue fill, White text, 15 px / 600, padding 13×22, radius 2. Hover: Navy fill. |
| Secondary | White fill, 1 px Navy border, Navy text. Hover: Mist fill. |
| Text link | Kerri Blue, 600, trailing " →". Hover: Navy, underline. |

One primary button per view. Labels are verbs: "Request a quote", "Download datasheet", "Book a demo".

### Tags
Condensed 12 px / 700 uppercase, +8% tracking, padding 4×9, square corners.
- Default: Mist fill, Steel text, Alloy border.
- Industry: Sky Tint fill, Navy text.
- New: Molten fill, Navy text (counts as the one accent).

### Product card
White, 1 px Alloy border. Image area on Mist (product on white seamless background). Content: `label` category → `h3` product name → `data` key specs in a single line separated by " · " → text link.

### Stat block
Navy background, 4 px × 32 px Molten bar above the number, figure in Plex Sans 64 px / 700 White (or `data-lg` Mono), description 16 px `#C9DCF3`.

### Callout / note
Sky Tint background, `label` in Kerri Blue, text 18 px Navy. No left-border accents.

### Specification table
- Header row: Condensed label, bottom border 1–2 px Navy.
- Rows: 1 px Alloy dividers, optional Mist zebra striping.
- Parameter left (Sans), value right-aligned (Mono). Units always included.

### Form fields
Label 13 px / 600 Graphite above field. Field: 1 px Alloy border, radius 2, padding 12×14, placeholder in Steel. Focus: 2 px Kerri Blue border. Error: `#C8191F` border and message below.

### Navigation (web)
White bar, 1 px Alloy bottom border. Horizontal logo left (32–40 px mark height), links 15 px Graphite, one primary button right. Sticky on scroll.

---

## 8. Iconography

- Line icons, 1.5 px stroke at 24 px, square caps and joins, no fills.
- Colour: Steel by default, Kerri Blue when interactive, Navy on light emphasis.
- Recommended open-source set: **Lucide** (https://lucide.dev) or **IBM Carbon icons**. Do not mix sets.
- No emoji, no 3D or filled cartoon icons.

---

## 9. Photography and imagery

- **Product shots:** equipment on pure white or Mist seamless background, even soft light, 3/4 angle, no props.
- **In-plant shots:** real Kerri installations in steel, cement, foundry and aluminium plants. Daylight or neutral light, sharp, uncluttered. People shown wearing correct PPE.
- **Colour treatment:** natural colour, slightly cool white balance. No heavy filters, duotones or colour overlays.
- **Technical drawings:** Navy lines on white, Kerri Blue for flow paths, Molten only for the single point being explained.
- MUST NOT use generic stock imagery of unrelated factories, abstract tech graphics, or AI-generated equipment images.

---

## 10. Applications

### 10.1 Website
- Header: navigation as in §7.
- Hero: two columns. Left: `label` (industries) → `display` headline (one key figure may be in Molten) → `body-lg` → primary + secondary button. Right: photo.
- Below hero: row of 3 key figures in `data-lg` Mono with `small` captions, separated by Alloy rules.
- Sections alternate White / Mist, 88 px vertical padding.
- Footer: Navy background, White and `#C9DCF3` text, reversed horizontal logo.
- Favicon: `kerri-mark-small-navy.svg` (SVG favicon) plus 32 px and 180 px PNG (Apple touch icon: Navy tile, White mark).
- Open Graph image: 1200×630, White background, horizontal logo top-left, headline in `h1` style, one product photo right.

**Website page structure (recommended)**

| Page | Purpose | Key content |
|---|---|---|
| Home | Who we are, what we make, proof | Hero, 3 key figures, product lines, industries, installations, CTA |
| Products / [product line] | Compare and specify | Product cards, spec tables, datasheet downloads |
| Product detail | Convince the engineer | Photo, how it works diagram, spec table, video, related products, quote CTA |
| Industries (steel, cement, foundry, aluminium) | Relevance to the buyer's plant | Typical layout, installations, case study |
| Installations / case studies | Proof | Plant, country, problem, system, measured result |
| Service & support | Reassurance after purchase | AMC, spares, commissioning, contact |
| About | Heritage and capability | Year founded, facility, team, certifications |
| Contact / Request a quote | Conversion | Short form (name, company, country, industry, requirement), phone, email, address |

**Website HTML starter** (use with the tokens in §13):

```html
<header style="display:flex;align-items:center;gap:32px;padding:16px 48px;border-bottom:1px solid #C8D0DA;background:#fff">
  <img src="/brand/kerri-logo-horizontal-navy.svg" alt="Kerri Engineering Works" height="40">
  <nav style="display:flex;gap:28px;font:400 15px var(--kew-font);color:#1C2430">…</nav>
  <a href="/quote" style="margin-left:auto;background:#2470C9;color:#fff;padding:13px 22px;border-radius:2px;font:600 15px var(--kew-font);text-decoration:none">Request a quote</a>
</header>
```

### 10.2 Technical data sheet (A4)
1. Header: wordmark left; document code right in Mono (`TDS · KEW-PS-1200 · REV C`); 3 px Navy rule beneath.
2. `label` category in Kerri Blue → product title 24 pt → one-sentence description.
3. Dimensioned drawing on Mist panel.
4. Specification table (§7).
5. Footer: website + email in Mono, page number "1 / 4", 1 px Alloy rule above.

### 10.3 Presentations (16:9)
- Title slide: Navy background, Molten bar, white title in Plex Sans Bold 72–88 px.
- Content slides: White background, Navy title 48 px, body ≥ 24 px.
- Section divider: Mist background, large Mono number ("02") in Kerri Blue + section title.
- Max one accent per slide. Max 3 bullet points per slide.

### 10.4 Product demo video (1920×1080)

| Element | Specification | Duration |
|---|---|---|
| Title card | Navy background, Molten bar 44×6 px, product name Plex Sans Bold 88 px White, `label` "Product demonstration" in `#8DB8EA` | 3 s |
| Lower third | White plate bottom-left inside safe area, 6 px Molten left bar, title 36 px / 700 Navy, step label Condensed 24 px Steel ("Step 2 of 5") | 4–6 s |
| Spec callout | Navy plate, 4 px Kerri Blue top rule, value Plex Mono 64 px White, label Condensed 24 px `#8DB8EA`. One on screen at a time | 3–4 s |
| Diagram overlay | Navy lines, Kerri Blue animated flow path, Molten for current point only | as needed |
| End card | White background, centred wordmark, product URL in Kerri Blue Mono | 4 s |

**Motion:** elements slide in 12–24 px with opacity, 300 ms, ease-out (`cubic-bezier(0.2, 0, 0, 1)`); exit 200 ms. No bounce, spin, zoom-blur or 3D flips.
**Audio:** calm, neutral music; voice-over in clear international English.
**Captions:** always provide burned-in or SRT subtitles in Plex Sans 600, White on 80% Navy plate.

### 10.5 Email and social
- Email: 600 px wide, White background, Navy header bar with reversed horizontal logo (PNG, 2×), one Kerri Blue button.
- Email signature: name 14 px / 600 Navy, title 13 px Steel, phone and email in Plex Mono 13 px, horizontal logo 28 px high below. No quotes, banners or extra colours.
- Social avatar: White mark on Navy square. Social post: logo bottom-left at ~8% of image width.
- Social (LinkedIn): 1200×1200 or 1200×627. White or Navy background, one key figure or product photo, Molten used once.

---

## 11. Accessibility

- All text MUST meet WCAG 2.1 AA (4.5:1, or 3:1 for large text). Use only pairings in §3.4.
- Never rely on colour alone; pair status colours with icons or text.
- Interactive targets ≥ 44×44 px.
- Visible focus state: 2 px Kerri Blue outline, 2 px offset.
- Videos MUST have captions.

---

## 12. Do and don't — quick reference

**Do**
- Use white space generously.
- Put numbers in IBM Plex Mono.
- Keep one accent per view.
- Use square corners and thin rules.

**Don't**
- Use gradients, shadows, glows or rounded "bubbly" shapes.
- Use Molten for text, warnings or more than one element.
- Introduce new colours or fonts.
- Use emoji, stock factory photos or decorative illustrations.

---

## 13. Design tokens

### CSS
```css
:root {
  --kew-white: #FFFFFF;
  --kew-navy: #0E2A47;
  --kew-blue: #2470C9;
  --kew-sky: #E6F0FB;
  --kew-molten: #E8641B;
  --kew-graphite: #1C2430;
  --kew-steel: #5A6676;
  --kew-alloy: #C8D0DA;
  --kew-mist: #F3F5F8;
  --kew-on-navy-label: #8DB8EA;
  --kew-on-navy-text: #C9DCF3;
  --kew-error: #C8191F;
  --kew-warning: #E0A100;
  --kew-success: #1E8A4C;

  --kew-font: 'IBM Plex Sans', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
  --kew-font-condensed: 'IBM Plex Sans Condensed', 'Arial Narrow', sans-serif;
  --kew-mono: 'IBM Plex Mono', Consolas, 'Courier New', monospace;

  --kew-radius: 2px;
  --kew-border: 1px solid #C8D0DA;
  --kew-space-1: 4px;  --kew-space-2: 8px;  --kew-space-3: 16px;
  --kew-space-4: 24px; --kew-space-5: 32px; --kew-space-6: 48px;
  --kew-space-7: 64px; --kew-space-8: 88px;
  --kew-content-max: 1180px;
  --kew-ease: cubic-bezier(0.2, 0, 0, 1);
}
```

Google Fonts embed:
```html
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Sans+Condensed:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
```

### JSON
```json
{
  "color": {
    "white": "#FFFFFF", "navy": "#0E2A47", "blue": "#2470C9", "sky": "#E6F0FB",
    "molten": "#E8641B", "graphite": "#1C2430", "steel": "#5A6676",
    "alloy": "#C8D0DA", "mist": "#F3F5F8",
    "onNavyLabel": "#8DB8EA", "onNavyText": "#C9DCF3",
    "error": "#C8191F", "warning": "#E0A100", "success": "#1E8A4C"
  },
  "font": {
    "sans": "IBM Plex Sans", "condensed": "IBM Plex Sans Condensed", "mono": "IBM Plex Mono"
  },
  "radius": 2,
  "space": [4, 8, 16, 24, 32, 48, 64, 88]
}
```

---

## 14. Prompt snippet for AI tools

Attach this file (and the logo SVGs if the tool accepts files), then paste this at the start of any request to an AI design, writing or coding tool:

> Design for Kerri Engineering Works using the attached Kerri Brand Guidelines. Follow every MUST rule. Use the supplied logo files exactly; never redraw the logo. The logo is a Navy open ring (the receiver loop of a pneumatic tube) with a K inside whose lower leg is a sample carrier; the ring must stay open. White background first. Colours: Kerri Navy #0E2A47 (headings, dark areas), Kerri Blue #2470C9 (buttons, links), Sky Tint #E6F0FB (highlight panels), greys #1C2430 / #5A6676 / #C8D0DA / #F3F5F8, and Molten #E8641B as a single accent used once per view, never for text or warnings. Fonts: IBM Plex Sans for all text, IBM Plex Sans Condensed for uppercase labels, IBM Plex Mono for numbers and part numbers. Square corners (max 2 px), 1 px grey rules, no gradients or shadows, no emoji. Tone: plain, factual, engineering-led; SI units with a space (4.5 bar). If something is not covered, choose the most restrained option: white background, Navy text, no accent.

**Task-specific additions**
- *Website:* "Follow §10.1. Output semantic HTML with the CSS variables in §13. Mobile-first, 1180 px max width, WCAG AA."
- *Presentation:* "Follow §10.3. 1920×1080, horizontal logo bottom-left on content slides, reversed logo on the Navy title slide."
- *Datasheet / document:* "Follow §10.2. A4, 20 mm margins, specs in IBM Plex Mono."
- *Video:* "Follow §10.4. Title card 3 s, end card with stacked logo 4 s."
- *Social post:* "Follow §10.5. One key figure or one product photo, Molten used once."

---

## 15. Change log

| Version | Date | Change |
|---|---|---|
| 2.0 | Nov 2026 | Official logo (receiver-loop mark) replaces interim wordmark. Logo files, clear space, minimum sizes, trademark note, website structure and task prompts added. |
| 1.0 | Nov 2026 | Colour, type, layout, components, applications. |
