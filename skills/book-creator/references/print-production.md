# Print production and geometry

## Two manufacturing paths

Keep a generic commercial-printer path and an on-demand paperback path apart. Never mix one printer's crop-mark requirements with another printer's ban on marks. The current job template overrides a generic preset.

| Decision | On-demand paperback baseline | Commercial printer |
| --- | --- | --- |
| Manufacturing files | Separate interior PDF and full-wrap cover PDF. | Separate files unless the supplied specification says otherwise. |
| Cover bleed | 0.125 in = 3.175 mm on the outside perimeter. | Use supplied template. |
| Crop/fold marks | Leave out marks, template labels, and guide layers. | Include only required marks outside bleed. Get exact offset and media-box instructions. |
| Interior bleed | Only if real artwork reaches trim. Width = trim width + 3.175 mm, height = trim height + 6.35 mm. No extra bleed at the binding edge. | Use the supplied template and page-box rules. |
| No-bleed interior | Trim-size single pages with no imposition. | Usually single pages. The printer controls signatures and imposition unless it clearly hands that job over. |
| Color and PDF standard | Embedded fonts, high-resolution images, supported flattened transparency and color handling. | The published commercial profile requests PDF/X-1a, CMYK, outlined text, marks/bleed, and images at least 300 ppi. Confirm the real job's current requirements before export. |

Interior page backgrounds stay white even when the paper stock is cream, such as pólen. Interior illustrations may contain color, but that does not allow a page-sized tinted background. Choose black-only or color production on purpose. Make sure text meant to be black-only does not turn into unwanted rich black.

The commercial help lists trim sizes of 110 × 180, 140 × 210, 150 × 220, 160 × 230, 170 × 240, 200 × 200, 210 × 280, landscape 280 × 210, and 210 × 297 mm. A separate summary also mentions A5, which is 148 × 210 mm and is not interchangeable with 140 × 210 mm. Confirm the exact dimensions in the job. Custom sizes need a clear, supported production agreement. These are candidate sizes that do not depend on one provider. They do not claim that all bindings and stocks support every size.

Convert text to outlines only in the print copy, and only when that requirement is confirmed. Keep editable typography in the source and searchable, selectable text in the digital reader PDF. A PDF/X-1a export needs the proper output intent and compatible transparency and color handling. Renaming a PDF does not make it compliant. Check the exported profile with a suitable preflight tool.

## Paperback calculation

For left-to-right binding, the flat cover reads back cover, spine, front cover. For right-to-left binding, follow the real template instead of mirroring text by habit.

```text
spine = final interior page count × verified thickness per page
wrap width = 2 × trim width + spine + 2 × outer bleed
wrap height = trim height + 2 × outer bleed
```

A paperback base profile uses these thicknesses:

| Paper and ink | Millimeters per interior page |
| --- | --- |
| White, black ink | 0.0572008 |
| Cream, black ink | 0.0635 |
| Standard color | 0.0572008 |
| Premium color | 0.0596138 |

These are conversions from the documented inch coefficients. They apply to that production profile only. Groundwood, different weights, coated stocks, glued versus sewn blocks, hardcover boards, flaps, spiral, and other printers need their own template or measured caliper (thickness). If the caliper is given per sheet, tell sheets and pages apart before you multiply. Do not reuse a per-page multiplier as a per-sheet one.

Apply the formulas with the real supplied values, and check the result against the printer's final template. For example, 240 pages at 0.0635 mm per page yields a 15.24 mm spine. A 152.4×228.6 mm trim with 3.175 mm outside bleed yields a 326.39×234.95 mm wrap. This is a worked number example for that profile. It is not an approval or proof that the product is available.

No geometry program is bundled. Hardcover boards, creep, flaps, spiral and different paper calipers need their real contracts, not a reuse of this paperback example.

## Margins and spine lettering

For the paperback base profile, minimum inner margins by final page count are 9.525 mm for 24–150 pages, 12.7 mm for 151–300, 15.875 mm for 301–500, 19.05 mm for 501–700, and 22.225 mm for 701–828. Outside, top, and bottom minimums are 6.35 mm without bleed and 9.525 mm with bleed. These are printing minimums, not advice to shrink the chosen editorial margins. Use the larger margin that applies. Check page limits for each product separately.

Require room for both the title and the author on a printable spine. Use the final template's text-safe region and production tolerance. The documents disagree on the threshold, giving 79 pages in one place and 80 in another, so use 80 pages as the safe base and confirm the template. Do not add spine text below the verified threshold or squeeze it into a narrow spine. Keep at least 1.5875 mm between spine lettering and each fold in this profile.

## Stock and finishing specification

Record the real stock names and weights in g/m², not just “good paper.” Options to discuss include offset white, cream (pólen), coated illustration stock where supported, coated cover card, hardcover board, matte/gloss lamination, and other supported finishes. Record 1/1 black interior, 4/4 color interior, 4/0 or 4/4 cover as applicable. Confirm inside-cover printing, flap widths, binding side, spine orientation, and whether lamination affects fold zones. Do not guess stock availability or thickness from weight alone.

For hardcover, request the exact board/joint/turn-in template. For spiral, request punch-safe margins and front/back panels. For saddle stitch, confirm page multiple, creep, and maximum block thickness. These cannot be calculated from the paperback formula alone.

## ISBN and barcode

Ask for the ISBN-13 and which edition and format it identifies. Normalize separators, check for 13 digits and the 978/979 prefix, and verify the alternating 1/3 check-digit sum. Do not invent an ISBN or reuse one for a different publication format without confirming its assignment.

Generate a standards-compliant EAN-13 with a real barcode library or vector tool. Keep quiet zones, high contrast, and clear human-readable digits. Place it in the template's back-cover barcode region. Keep a clean white patch behind it. If the printer assigns the barcode, reserve its region instead of printing a second code. Never render a barcode with an image model. Decode the exported barcode at final size and compare the exact payload with the supplied ISBN. Add a price supplement only when it is clearly required.
