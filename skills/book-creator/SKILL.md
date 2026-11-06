---
name: book-creator
description: Prepare complete books and A4 workbooks for print, digital delivery or both, with coherent editorial styles, navigable PDFs, verified citations, original artwork and manufacturing-aware covers. Use for manuscript-to-publication production.
license: MIT
---

# Book Creator

Produce an editorially coherent and physically usable publication. A generated PDF, an attractive cover and a compliant manufacturing package are different achievements. Explain the actual production choices and verify the final artifacts.

Keep finished book content and delivery language provider-neutral. Source notes can identify evidence, but do not put production service names into the book or cover unless the user requests that credit.

## Establish the publication brief

Collect title/subtitle, exact author name, language, audience, manuscript/outline, rights, edition, ISBN status and delivery mode. Ask whether this is a book or an A4 workbook. A workbook defaults to 210×297 mm. A book needs its actual trim dimensions.

Confirm print, digital or both. Ask whether the reader PDF includes a cover. Manufacturing normally separates interior and cover, even when the digital reader file combines them. Confirm desired front matter, internal cover sides, title/copyright pages, dedication, acknowledgments, preface, appendices, glossary, references and subject index.

Confirm ABNT-based editorial style, strict institutional academic compliance or another named style. Arial 12 is the owner's default, not an ABNT-mandated font family. Strict academic pagination and presentation cannot be replaced by arbitrary decorative choices while retaining a compliance claim.

For print, record exact paper stock/weight, interior ink, cover stock/color, lamination, binding, spine type, flaps, trim, bleed, safe zones, inside-cover printing and the current job template. Weight alone does not determine paper thickness. Paperback, hardcover, spiral, hardcover-with-spiral and saddle stitch need different manufacturing geometry.

Use [the intake guidance](references/intake.md) and [brief template](assets/publication-brief.json) to collect these choices. Do not begin final cover geometry before the interior is stable.

## Edit before typesetting

Establish a style sheet for terminology, spelling, capitalization, numerals, dates, quotations, emphasis and references. Review structure, chapter progression, factual claims, permissions and missing source material. Distinguish substantive editing from silently rewriting the author's position.

Maintain a source record for quotations, images and factual claims. Do not invent citations, page numbers, ISBNs, cataloging data or legal notices. A bibliography records sources. A table of contents follows headings. A subject index is a curated set of concepts with locators. A list of figures is generated from captions. These are different editorial products.

For ABNT-related work, the researched baseline includes NBR 14724:2024 for academic presentation, NBR 10520:2023 for citations and NBR 6023:2025 for references. Institutional rules and the authorized full standard govern strict compliance. Check the selected bibliography style's edition instead of assuming a familiar software style implements the latest standard.

## Define actual styles

| Element | Working editorial default | Important qualification |
| --- | --- | --- |
| Body | Arial 12, black, white/unpainted page, 1.5 spacing | Owner/academic-oriented preset, not universal commercial typography |
| A4 margins | Top/inner 30 mm, bottom/outer 20 mm | Mirror for duplex and respect binding needs |
| Paragraph | 12.5 mm first-line indent, no extra ordinary-paragraph spacing | Selected convention, not a universal ABNT measurement |
| Headings | Consistent levels, spacing and numbering | Keep heading with following content |
| Short quote | Inline quotation marks with precise locator | Follow selected citation system |
| Long quote | Distinct indented block, smaller type, single spacing | Current standard/institution controls exact treatment |
| Figure/table | Number/title, content, source and notes as separate elements | Keep logically related material together |
| Footnote/reference | Smaller, readable, consistent style | Do not mix incompatible citation systems |
| Code/equation | Suitable font, preserved symbols and clear numbering | Avoid tinted full-page/background treatments |

For thematic commercial design, choose a readable licensed body face, line length, leading and hierarchy based on the actual trim and audience. A decorative cover face need not be the body face. Inspect a real spread at reading size rather than deciding from a zoomed-in page.

Apply author-date or the explicitly selected citation system consistently. Give direct quotations a page or other precise locator when available. Handle corporate/no-author sources, multiple authors, same-author/year collisions, translations and indirect citations according to the chosen standard. Match every citation to a real reference and every listed source to its intended editorial role.

## Layout and navigation

Use a paginated layout system capable of the selected footnotes, tables, references and links. [The LuaLaTeX starting document](assets/main.tex) requires the actual engine, packages and licensed Arial installation. Its structural examples are not completed content or an ABNT certification.

Keep chapters, sources, image masters, captions and exports organized. Use stable labels and real cross-references. Generate contents/bookmarks from headings and selected lists from captions. Rebuild after pagination changes and verify the first, middle and last destinations. Check all links where the tool supports it.

Review widows/orphans, overfull lines, missing glyphs, hyphenation, long URLs, footnote overflow and excessive gaps. Do not fix a paragraph by scattering manual blank lines throughout the source. A full-page figure must remain within the intended page area. Multi-page tables need repeated headers and continuation treatment, without dropped rows or unreadable scaling.

Pagination can be lower center, lower outer/right or upper outer/right when the selected editorial mode allows it. Strict academic mode follows its own counting/display rules. Suppressing a number on a title/blank/chapter-opening page must not accidentally remove that page from the physical count.

## Images and cover composition

Generate requested original illustrative artwork with the available image model. Keep factual charts tied to real data. Inspect geometry, anatomy, lettering, branding and proportions. Never stretch a source to fit another aspect ratio. Recompose or crop deliberately.

Ask whether figures have titles above them and should enter a list of figures. Keep credits/source notes distinct from display captions. Judge effective resolution at final placed size, not merely a file's DPI metadata. A 1200px image placed 100mm wide has a different effective resolution from the same image spread across an A4 page.

Interior pages remain white/unpainted, including blank pages. Cream/pollen is a physical paper choice, not a full-page color fill. Cover/back-cover art can have backgrounds. Inspect every page for collisions, cut graphics and unsafe placement near binding/trim.

## Final page count and manufacturing geometry

Freeze the final interior count, including intentional blank pages. For a left-to-right paperback, the wrap is back → spine → front. Use the actual template for direction, bleed and lettering orientation.

For a verified paperback profile:

```text
spine = final interior pages × verified thickness per page
wrap width = 2 × trim width + spine + 2 × outside bleed
wrap height = trim height + 2 × outside bleed
```

A worked example with explicitly supplied values: 240 pages × 0.0635 mm/page gives a 15.24 mm spine. With 152.4×228.6 mm trim and 3.175 mm outside bleed, the wrap is 326.39×234.95 mm. This is arithmetic for that profile, not evidence that any printer offers the combination. A per-sheet caliper must not be multiplied as a per-page coefficient.

Hardcover requires board, joint and turn-in allowances. Spiral requires punch-safe margins and separate panels. Saddle stitch requires page-multiple/creep and thickness checks. Do not reuse the paperback equation to manufacture those bindings. Put title/author on a spine only when the template's actual printable/safe area permits it.

Crop/fold marks are job-specific. Some services prohibit them. Others require them outside bleed with defined offsets. PDF/X output requires the correct color/output-intent/transparency rules, not just a renamed file. Keep searchable digital text even if a confirmed manufacturing derivative requires outlined text.

Ask for a real ISBN-13, validate its prefix/check digit and edition/format assignment, and generate any barcode through an appropriate existing barcode tool. Preserve quiet zones, contrast and the back-cover safe region. Decode the final exported barcode and compare its payload. Do not ask an image model to draw a scannable barcode or create an ISBN.

## Proof and delivery

Inspect actual page boxes/dimensions, fonts, glyphs, image quality, color, links, references and page count. Render and inspect every page, with detailed review of tables, quotes, chapter openings, figures and notes. Reopen the actual export, not only its editable source. Record unavailable tools instead of claiming visual or standards validation.

Deliver the selected reader/manufacturing PDFs, front/back PNGs and full-wrap PNG when requested, editable sources and a production manifest. A PNG is artwork, not a substitute for a required press PDF. Record what awaits printer preview/physical proof. Do not claim production approval from successful local rendering.

[Editorial detail](references/editorial.md), [typesetting/preflight](references/typesetting.md), [print production](references/print-production.md) and [visual design](references/visual-design.md) expand these decisions. This skill contains no geometry script, image converter or automated rule updater.

## Foundations

Matthew Butterick's openly available [Practical Typography](https://practicaltypography.com/summary-of-key-rules.html) informs attention to readable text and layout variables. His [widow/orphan discussion](https://practicaltypography.com/widow-and-orphan-control.html) explains why a setting still needs visual judgment. Robin Williams's [The Non-Designer's Design Book, fourth edition](https://www.peachpit.com/store/non-designers-design-book-9780133966152) is professional further reading on visual organization, verified through its publisher record. [UFES normalization guidance](https://sibpesquisa.ufes.br/normas.html) identifies current academic standard editions. These references have different scopes and do not override the actual manufacturing contract. See [sources](references/sources.md) and [license](LICENSE.md).
