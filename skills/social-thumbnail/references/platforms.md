# Platform and export profiles

Checked: 2026-11-18 for the YouTube rows. Check the exact surface, account capabilities and upload interface again before release.

| Surface | Canvas guidance | Important distinction |
| --- | --- | --- |
| YouTube video | 16:9, official current recommendation 3840 × 2160, minimum width 640, JPG or PNG. | Mobile upload limit is 2 MB for video thumbnails. Desktop guidance currently allows 50 MB. Do not apply the 2 MB mobile limit to every upload path. Custom thumbnails need a verified account. |
| YouTube Shorts | 9:16, current recommendation 2160 × 3840, minimum height 640. | Current guidance documents custom uploads only in desktop Studio for verified accounts. |
| YouTube podcast playlist | 1:1. | 10 MB on mobile and 50 MB on desktop. |
| Instagram Reel or TikTok cover | Start with a vertical 9:16 layout, such as 1080 × 1920. | Grid, feed and player crops differ. These are design canvases, not a claim that every native app accepts any uploaded image. Check cover selection support. |
| X or LinkedIn attached image | Match the chosen post/media placement. | A video thumbnail, link preview and attached image are separate products. Check their rules separately. |

Owner portable preset: generate a large PNG, then export a 16:9 JPEG at quality 99 with a cautious limit of 2,000,000 bytes. Quality 99 is a JPEG encoder setting, not “99% identical” or a promise that a 4K image fits. If the file goes over the limit, ask for or apply an already approved change of dimensions or quality, and report the final settings.

Use sRGB for normal social delivery. Keep the master and any editable type/layout source. JPEG has no alpha channel, so flatten transparency onto a chosen background. Do not strip a color profile without converting the pixels properly. Do not upscale a small source and claim it has new detail. If the model made a smaller master than requested, state its real dimensions.
