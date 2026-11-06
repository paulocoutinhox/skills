# Typesetting, export, and preflight

## Reproducible source

Use a real paginated typesetting engine with support for the selected features. LuaLaTeX with suitable packages is one route for references, footnotes, contents, and tables. A supported paged-media engine or another tool is acceptable when it implements every required feature. Do not assume a browser's basic print dialog supplies footnotes, tagged PDF, accurate cross-references, or press color management.

The bundled `assets/main.tex` is an A4 editorial starting point. It needs LuaLaTeX and Arial installed and licensed. It intentionally fails if the selected font is absent. Ask for an approved font substitution rather than silently changing the book. Install the required TeX packages in the actual environment and run LuaLaTeX until the contents and cross-references settle. For bibliography automation, configure a verified current style and test representative entries. The template's manual bibliography is only a structural example.

Keep chapters, bibliography metadata, illustration sources, generated masters, print profiles, and reader exports separately. Use semantic headings and stable labels. Any final page insertion changes the count and can change margins and spine. Freeze the interior before finalizing the cover.

## Avoid layout failures

- Keep headings with following content, captions with images, source notes with the appropriate figure, and table titles with the table.
- Review widows, orphans, overfull lines, missing glyphs, hyphenation, justified spacing, footnote overflow, and excessive blank space.
- Never overlap text frames, images, running heads, folios, or barcode regions.
- Do not split an image, graph, formula, or important callout across pages accidentally.
- Keep core text and essential image details inside the template's text-safe area. Keep them clear of trim lines, bleed, gutter, fold, punch, and board-joint exclusion areas. Only intentional bleed artwork extends beyond trim.
- For deliberate multi-page tables, repeat headers and add a clear continuation treatment. Do not silently drop rows.

## Navigation and references

Generate contents from real headings and link each entry to its final destination. Generate figure/table lists from captions when selected. Resolve chapter, figure, table, equation, note, and bibliography references after all page movements. Open and click representative first, middle, and last links, then verify every internal destination programmatically where supported.

Reader PDFs retain links, useful bookmarks, language, author/title metadata, searchable text, and accessibility structure supported by the engine. A proof may need a different PDF tagging toolchain. Do not claim PDF/UA compliance without the appropriate validation. A manufacturing service may forbid annotations and bookmarks, so strip those only from its production derivative and keep navigation in the reader PDF.

## Preflight sequence

1. Inspect physical page dimensions and page boxes, orientation, final count, intended blank pages, and reading order.
2. Inspect font embedding and missing glyphs. Confirm every font license permits the export.
3. Check effective image resolution, aspect ratios, crop behavior, color spaces, intended black-only text, and transparency handling.
4. Render every page at a readable resolution. Inspect a contact sheet, then each page at normal size and detailed crops where necessary.
5. Inspect all first/last chapter pages, large figures, long tables, block quotes, footnotes, bibliography, and front matter. Verify white backgrounds throughout.
6. Check the cover against the final template, spine, author/title, bleed, safe zones, barcode, and marks policy. Remove guides from production files.
7. Reopen the actual exported PDFs and PNGs. Decode the barcode, test reader links, and compare page count with the geometry calculation.
8. Record commands and checks actually performed. If the printer preview or physical proof is unavailable, state that approval remains pending.

Useful local tools include `pdfinfo`, `pdffonts`, `pdftoppm`, a PDF inspection library, an image inspector, and a barcode decoder. Verify availability before calling them. A successful PDF parse does not detect all visual defects. Never label an unrendered manuscript “visually verified.”
