# Platform and export profiles

Verified: 2026-11-05. Recheck the exact surface, account capabilities, and upload interface before release.

| Surface | Canvas guidance | Important distinction |
| --- | --- | --- |
| YouTube video | 16:9, official current recommendation 3840 × 2160, minimum width 640. | Mobile upload ceiling is 2 MB for video thumbnails. Desktop guidance currently permits 50 MB. Do not repeat the old universal 2 MB assumption. |
| YouTube Shorts | 9:16, current recommendation 2160 × 3840. | Current desktop Studio guidance supports custom uploads for verified accounts. Availability can differ by interface. |
| YouTube podcast playlist | 1:1. | Mobile podcast thumbnail ceiling differs from video. Check the live guidance. |
| Instagram Reel or TikTok cover | Start with a vertical 9:16 composition, such as 1080 × 1920. | Grid, feed, and player crops differ. These are design canvases, not a claim that every native app accepts an arbitrary uploaded image. Verify cover selection support. |
| X or LinkedIn attached image | Match the chosen post/media placement. | A video thumbnail, link preview, and attached image are distinct products. Verify their rules separately. |

Owner portable preset: generate a large PNG, then export a 16:9 JPEG at quality 99 with a conservative ceiling of 2,000,000 bytes. Quality 99 is a JPEG encoder setting, not “99% identical” or a guarantee that a 4K image fits. If the file exceeds the ceiling, ask for or apply an already authorized change of dimensions or quality and report the final settings.

Use sRGB for typical social delivery. Preserve the master and any editable type/layout source. JPEG has no alpha channel, so flatten transparency onto a deliberate background. Do not strip a color profile without converting the pixels appropriately. Do not upscale a small source and claim it contains new detail. If the model generated a smaller master than requested, state its actual dimensions.
