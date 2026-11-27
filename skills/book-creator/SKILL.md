---
name: book-creator
description: Prepare complete books and A4 workbooks for print, digital delivery or both, with consistent editorial styles, navigable PDFs, verified citations, original artwork and covers that fit the printer's needs. Use for manuscript-to-publication production.
license: MIT
---

# Book Creator

Produce a publication that is consistent as a text and usable as a physical object. A generated PDF, an attractive cover and a printer package that meets the job's rules are three different results. Explain the real production choices to the user in the delivery report, never inside the book, and check the final files.

## The book contains only the book

The finished publication must read as an ordinary, professionally published book. Its pages hold the author's work and the usual parts of a book: cover, half-title, title page, copyright page, dedication, epigraph, acknowledgments, preface or introduction, contents, list of figures, list of tables, abbreviations, chapters, conclusion, appendices, glossary, references, index and an author biography, as chosen in the brief. [Book anatomy](references/editorial.md#book-anatomy-and-order) gives the order and purpose of each part.

Never write the production process into the book, cover, captions, alternative text, running heads or PDF metadata:

- Do not mention artificial intelligence, language or image models, agents, prompts, skills, templates, typesetting software, build commands, file names or production services.
- Do not add a "how this book was made" section, a tool colophon, a methodology note about writing the book, an editor's note addressed to the author, or a disclaimer about generated content.
- Credit original illustrations as the brief specifies, for example "Source: prepared by the author (2026)" in ABNT style or "Illustration by Author Name". Never write "AI-generated image" or name the image tool.
- Remove every placeholder, `TODO`, bracketed instruction, review comment and template sentence before export.

A book about a technology can discuss that technology as content. The rule forbids describing how this particular book was made. If a distribution platform asks whether content was generated with artificial intelligence, answer in that platform's submission form, as the owner decides. That declaration does not go into the book. Keep source notes, production manifests and tool records outside the publication. Do not put production service names into the book or cover unless the user requests that credit.

## Establish the publication brief

Collect the title and subtitle, exact author name, language, audience, manuscript or outline, rights, edition, ISBN status and delivery mode. Ask whether this is a book or an A4 workbook. A workbook defaults to 210×297 mm. A book needs its real trim dimensions.

Confirm print, digital or both. Ask whether the reader PDF includes a cover. Printers usually take the interior and cover as separate files, even when the digital reader file combines them. Confirm the wanted front matter, internal cover sides, title and copyright pages, dedication, acknowledgments, preface, appendices, glossary, references and subject index.

Confirm an ABNT-based editorial style, strict institutional academic compliance or another named style. Arial 12 is the owner's default, not a font family that ABNT requires. You cannot swap strict academic pagination and presentation for free decorative choices and still claim compliance.

For print, record the exact paper stock and weight, interior ink, cover stock and color, lamination, binding, spine type, flaps, trim, bleed, safe zones, inside-cover printing and the current job template. Weight alone does not tell you paper thickness. Paperback, hardcover, spiral, hardcover-with-spiral and saddle stitch each need different print geometry.

Use [the intake guidance](references/intake.md) and [brief template](assets/publication-brief.json) to collect these choices. Do not begin final cover geometry before the interior is stable.

## Edit before typesetting

Set up a style sheet for terms, spelling, capitalization, numbers, dates, quotations, emphasis and references. Review structure, chapter flow, factual claims, permissions and missing source material. Keep real editing apart from quietly rewriting the author's position.

Keep a source record for quotations, images and factual claims. Do not invent citations, page numbers, ISBNs, cataloging data or legal notices. A bibliography records sources. A table of contents follows headings. A subject index is a hand-picked set of concepts with locators (page or section pointers). A list of figures is generated from captions. These are different editorial products.

For ABNT-related work, the researched base includes NBR 14724:2024 for academic presentation, NBR 10520:2023 for citations and NBR 6023:2025 for references. Institutional rules and the licensed full standard decide strict compliance. Check the edition of the chosen bibliography style. Do not assume a familiar software style follows the latest standard.

## Define real styles

| Element | Working editorial default | Important qualification |
| --- | --- | --- |
| Body | Arial 12, black, white/unpainted page, 1.5 spacing | Owner preset aimed at academic work, not universal commercial typography |
| Alignment | Body text justified to both margins, never ragged-right, with hyphenation in the book's language | Required owner rule. The last line of each paragraph stays flush left |
| A4 margins | Top/inner 30 mm, bottom/outer 20 mm | Mirror for duplex and respect binding needs |
| Paragraph | 12.5 mm first-line indent, no extra ordinary-paragraph spacing | Chosen convention, not a universal ABNT measurement |
| Headings | Consistent levels, spacing and numbering | Keep heading with following content |
| Short quote | Inline quotation marks with precise locator | Follow the chosen citation system |
| Long quote | Separate indented block, smaller type, single spacing | The current standard or institution sets the exact treatment |
| Figure/table | Number/title, content, source and notes as separate elements | Keep logically related material together |
| Footnote/reference | Smaller, readable, consistent style | Do not mix incompatible citation systems |
| Code/equation | Fitting font, intact symbols and clear numbering | Avoid tinted full-page or background treatments |

Justify body paragraphs, footnotes, block quotations, list-item text and back-cover copy so the text lines up with both the left and right margins. Set the document language so hyphenation follows that language's rules, and enable fine spacing control such as LaTeX `microtype` or the tool's equivalent. Check justified pages for rivers (gaps that run down the page), stretched word spacing and stacks of hyphens. Fix them with hyphenation, tracking within the tool's limits or careful rewording, never by switching to left alignment. Headings, captions, tables, code, equations, the title page and the dedication follow their own chosen alignment. ABNT reference lists are aligned left by the standard, so keep that exception in ABNT mode and justify references only in a style that requires it.

For themed commercial design, choose a readable licensed body font, line length, leading (line spacing) and hierarchy based on the real trim and audience. A decorative cover font does not have to be the body font. Check a real spread at reading size instead of deciding from a zoomed-in page.

Apply author-date or the citation system the user chose, the same way throughout. Give direct quotations a page or other precise locator when available. Handle corporate and no-author sources, multiple authors, same-author/year collisions, translations and indirect citations according to the chosen standard. Match every citation to a real reference and every listed source to its intended editorial role.

## Layout and navigation

Use a paginated layout system that can handle the chosen footnotes, tables, references and links. [The LuaLaTeX starting document](assets/main.tex) needs the real engine, packages and a licensed Arial install. It sets justified text, language hyphenation and the common front matter. Replace every `PLACEHOLDER` marker with real content, or remove the element. Its structural examples are not finished content or an ABNT certification.

Keep chapters, sources, image masters, captions and exports organized. Use stable labels and real cross-references. Generate contents and bookmarks from headings, and the chosen lists from captions. Rebuild after pagination changes and check the first, middle and last destinations. Check all links where the tool supports it.

Review widows and orphans (lone lines at the top or bottom of a page), overfull lines, missing glyphs, hyphenation, long URLs, footnote overflow and excessive gaps. Do not fix a paragraph by scattering manual blank lines throughout the source. A full-page figure must stay inside the intended page area. Multi-page tables need repeated headers and continuation treatment, without dropped rows or unreadable scaling.

Page numbers can be lower center, lower outer/right or upper outer/right when the chosen editorial mode allows it. Strict academic mode follows its own counting and display rules. Hiding a number on a title, blank or chapter-opening page must not remove that page from the physical count by accident.

## Images and cover composition

Generate requested original illustrative artwork with the available image model. Keep factual charts tied to real data. Inspect geometry, anatomy, lettering, branding and proportions. Never stretch a source to fit another aspect ratio. Recompose or crop on purpose.

Ask whether figures have titles above them and should enter a list of figures. Keep credits and source notes apart from display captions. Judge effective resolution at the final placed size, not only by a file's DPI metadata. A 1200px image placed 100mm wide has a different effective resolution from the same image spread across an A4 page.

Interior pages remain white/unpainted, including blank pages. Cream paper, such as pólen, is a physical paper choice, not a full-page color fill. Cover/back-cover art can have backgrounds. Check every page for overlaps, cut graphics and unsafe placement near binding/trim.

## Final page count and manufacturing geometry

Freeze the final interior count, including intentional blank pages. For a left-to-right paperback, the wrap is back → spine → front. Use the real template for direction, bleed and lettering orientation.

For a verified paperback profile:

```text
spine = final interior pages × verified thickness per page
wrap width = 2 × trim width + spine + 2 × outside bleed
wrap height = trim height + 2 × outside bleed
```

A worked example with values the user supplied: 240 pages × 0.0635 mm/page gives a 15.24 mm spine. With 152.4×228.6 mm trim and 3.175 mm outside bleed, the wrap is 326.39×234.95 mm. This is arithmetic for that profile, not proof that any printer offers the combination. Do not use a per-sheet caliper (thickness) as if it were a per-page value.

Hardcover requires board, joint and turn-in allowances. Spiral requires punch-safe margins and separate panels. Saddle stitch requires page-multiple, creep and thickness checks. Do not reuse the paperback formula to make those bindings. Put the title and author on a spine only when the template's real printable and safe area allows it.

Crop and fold marks depend on the job. Some services forbid them. Others require them outside the bleed with set offsets. PDF/X output needs the correct color, output-intent and transparency rules, not just a renamed file. Keep searchable digital text even if a confirmed manufacturing derivative requires outlined text.

Ask for a real ISBN-13, check its prefix, check digit and the edition and format it is assigned to, and generate any barcode with a suitable existing barcode tool. Keep quiet zones, contrast and the back-cover safe region. Decode the final exported barcode and compare its payload. Do not ask an image model to draw a scannable barcode or create an ISBN.

## Proof and delivery

Check the real page boxes and dimensions, fonts, glyphs, image quality, color, links, references and page count. Extract the exported text and search it in the book's language for placeholders, `TODO`, template instructions and production words such as artificial intelligence, AI, model, prompt, generated, agent, LaTeX, template and the names of the tools used. Review each hit and remove it unless it is legitimate subject matter. Confirm that body paragraphs are justified on every page. Render and check every page, with close review of tables, quotes, chapter openings, figures and notes. Reopen the real export, not only its editable source. Note tools that were not available instead of claiming visual or standards checks.

Deliver the chosen reader and print PDFs, front/back PNGs and full-wrap PNG when requested, editable sources and a production manifest. A PNG is artwork, not a substitute for a required press PDF. Note what still waits for the printer preview or a physical proof. Do not claim production approval from successful local rendering.

[Editorial detail](references/editorial.md), [typesetting/preflight](references/typesetting.md), [print production](references/print-production.md) and [visual design](references/visual-design.md) cover these decisions in more depth. This skill contains no geometry script, image converter or automated rule updater.

## Foundations

Matthew Butterick's openly available [Practical Typography](https://practicaltypography.com/summary-of-key-rules.html) guides attention to readable text and layout settings. His [widow/orphan discussion](https://practicaltypography.com/widow-and-orphan-control.html) explains why a setting still needs a visual check. Robin Williams's [The Non-Designer's Design Book, fourth edition](https://www.peachpit.com/store/non-designers-design-book-9780133966152) is good further reading on visual layout, checked through its publisher record. [UFES normalization guidance](https://sibpesquisa.ufes.br/normas.html) names the current editions of academic standards. These references cover different things and do not override the real print contract. See [sources](references/sources.md) and [license](LICENSE.md).
