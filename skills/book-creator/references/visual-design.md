# Images and cover design

## Art direction

Derive the cover from the book's genre, promise, audience, tone, and title hierarchy. Select readable licensed display typography. Arial 12 for body text does not dictate cover typography. Keep the title, subtitle, author, series information, and spine legible at their actual physical and thumbnail sizes.

Use a deliberate palette and a clear focal point. Keep front and back composition cohesive across the spine without placing critical faces or lettering on folds. Put descriptive back-cover copy, author biography, optional publisher mark, and a reserved barcode patch into distinct safe areas. Match exact author and title metadata across every output.

## Image-model workflow

Create an image list with purpose, placement, aspect ratio, generation prompt, target physical size, resolution, caption, credit, and alternative text. Generate original illustrative artwork using the available image model. If none is available, report that dependency and request a supported image-generation path rather than claiming images were generated.

Use the same visual direction across a series. Ask for reference images when identity or specific object fidelity matters. Inspect faces, hands, perspective, object proportions, repeated motifs, unwanted text, and artifacts. Regenerate or edit flaws. Avoid stretching or squeezing an image. Crop intentionally or use proportional containment. Do not claim that setting DPI metadata adds missing pixel detail.

Set body text, precise labels, formulas, charts, and barcodes with deterministic layout tools. A generated image can supply the cover artwork while editable typography supplies reliable spelling and spacing. A chart showing actual measurements must come from validated data rather than an invented model illustration.

## Resolution and placement

For print, calculate effective resolution as source pixels divided by placed inches. Target at least 300 ppi for continuous-tone artwork in the supported production profile. Line art may need higher resolution or vector output. Generate a large PNG master, preserve it, and export color-managed print and RGB digital derivatives separately. PNG uses RGB or grayscale and is not a CMYK press container.

Keep captions attached to their figures. Prevent a page break inside an ordinary image/caption block. Move the block or redesign a large figure rather than clipping it. Multi-page diagrams need deliberate panels with continuity labels. Large tables need readable repeated headers, not rasterization or microscopic scaling. Review crop-safe, fold-safe, and binding-safe regions independently.
