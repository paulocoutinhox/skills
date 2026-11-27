# Typesetting, export, and preflight

## Reproducible source

Use a real paginated typesetting engine that supports the chosen features. LuaLaTeX with fitting packages is one way to handle references, footnotes, contents, and tables. A supported paged-media engine or another tool is fine when it covers every required feature. Do not assume a browser's basic print dialog gives you footnotes, tagged PDF, accurate cross-references, or press color management.

The bundled [starting document](../assets/main.tex) is an A4 editorial starting point. It needs LuaLaTeX and Arial installed and licensed. It fails on purpose if the chosen font is missing. It sets mirrored inner/outer margins for duplex print, chapters opening on a recto, blank versos that count without a printed number, indentation of every paragraph including the first after a heading, and empty PDF creator/producer metadata so the file does not name the production tools. For a digital-only reader PDF, switch to `oneside` with `left`/`right` margins. Its fixed English words, such as the acknowledgments heading, the chapter title and the copyright line, are placeholders too, so write them in the book's language. Its front matter follows the default ABNT-based order from [book anatomy](editorial.md#book-anatomy-and-order): title page, copyright page, dedication, acknowledgments, list of figures, list of tables and then the contents as the last pre-textual element. For the commercial order, move `\tableofcontents` before `\listoffigures`, place the acknowledgments chapter after the lists and any foreword or preface, and update the brief's `front-matter` array to the same sequence. Ask for an approved font substitution instead of quietly changing the book. Replace or delete every `PLACEHOLDER` marker, and remove front-matter elements the brief does not choose, including empty lists of figures or tables.

## Justified text and language

Body text is justified to both margins. LaTeX justifies paragraphs by default, so do not add `\raggedright`, `ragged2e` or `\RaggedRight` to body text. Other engines need explicit settings, such as CSS `text-align: justify` with `hyphens: auto` and a `lang` attribute, or the layout application's full-justify paragraph style with the last line aligned left.

Justification needs hyphenation in the correct language. Change the template's `babel` option from `english` to the book's language, for example `brazilian` for Brazilian Portuguese, and set `pdflang` to the matching tag, such as `pt-BR`. Check the rendered names of generated headings, such as the contents, list of figures and references. Override a name the chosen style requires through the language's caption hook, for example `\addto\captionsbrazilian{\renewcommand{\bibname}{Referências}}` for ABNT. Keep `microtype` enabled for character protrusion and font expansion, which reduce uneven word spacing.

Check justified pages for rivers, loose or tight lines, more than two consecutive hyphenated line ends and overfull boxes reported in the log. Fix a bad paragraph with hyphenation exceptions, `\hyphenation{...}` entries for unknown words, or careful rewording approved by the author. Do not fix it by switching that paragraph to left alignment. Keep the ABNT reference list left-aligned in ABNT mode, as the template does. Install the required TeX packages in the real environment, and run LuaLaTeX until the contents and cross-references stop changing. For automatic bibliographies, set up a verified current style and test typical entries. The template's manual bibliography is only a structural example.

Keep chapters, bibliography metadata, illustration sources, generated masters, print profiles, and reader exports apart. Use semantic headings and stable labels. Any final page insertion changes the count and can change margins and spine. Freeze the interior before finalizing the cover.

## Avoid layout failures

- Keep headings with following content, captions with images, source notes with the appropriate figure, and table titles with the table.
- Review widows, orphans, overfull lines, missing glyphs, hyphenation, justified spacing, footnote overflow, and excessive blank space.
- Never overlap text frames, images, running heads, folios, or barcode regions.
- Do not split an image, graph, formula, or important callout across pages by accident.
- Keep core text and essential image details inside the template's text-safe area. Keep them clear of trim lines, bleed, gutter, fold, punch, and board-joint exclusion areas. Only intentional bleed artwork extends beyond trim.
- For planned multi-page tables, repeat headers and clearly mark that the table continues. Do not quietly drop rows.

## Navigation and references

Generate contents from real headings and link each entry to its final destination. Generate figure and table lists from captions when chosen. Resolve chapter, figure, table, equation, note, and bibliography references after all pages stop moving. Open and click sample first, middle, and last links, then check every internal destination with a program where supported.

Reader PDFs keep links, useful bookmarks, language, author/title metadata, searchable text, and accessibility structure supported by the engine. A proof may need a different PDF tagging toolchain. Do not claim PDF/UA compliance without the right validation. A print service may forbid annotations and bookmarks, so strip those only from its production copy and keep navigation in the reader PDF.

## Preflight sequence

1. Check physical page dimensions and page boxes, orientation, final count, intended blank pages, and reading order.
2. Check font embedding and missing glyphs. Confirm every font license permits the export.
3. Check effective image resolution, aspect ratios, crop behavior, color spaces, intended black-only text, and transparency handling.
4. Render every page at a readable resolution. Check a contact sheet, then each page at normal size, and close-up crops where needed.
5. Check all first and last chapter pages, large figures, long tables, block quotes, footnotes, bibliography, and front matter. Confirm white backgrounds throughout and justified body paragraphs on every page.
6. Extract the exported text, for example with `pdftotext`, and search it for `PLACEHOLDER`, `TODO`, template sentences and production terms such as AI, artificial intelligence, model, prompt, generated, agent, LaTeX, template and every tool name used. Search in the book's language as well, for example "inteligência artificial", "gerado" and "modelo". Read the PDF Title, Author, Subject and Keywords metadata too. Remove every hit that describes how the book was produced. Keep a hit only when it is real subject matter of the book.
7. Check the cover against the final template, spine, author/title, bleed, safe zones, barcode, and marks policy. Remove guides from production files.
8. Reopen the real exported PDFs and PNGs. Decode the barcode, test reader links, and compare page count with the geometry calculation.
9. Record the commands and checks you really ran. If the printer preview or physical proof is unavailable, state that approval remains pending.

Useful local tools include `pdfinfo`, `pdffonts`, `pdftoppm`, a PDF inspection library, an image inspector, and a barcode decoder. Check that they are available before you call them. A successful PDF parse does not detect all visual defects. Never label an unrendered manuscript “visually verified.”
