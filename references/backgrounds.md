# Color backgrounds

Built-in image generation produced two original 9:16 source plates: `assets/backgrounds/red-checker.png` and `blue-checker.png`. No private reference images were used. These contain no characters, logos or personal identifiers.

Prompt set: clean full-bleed retro pixel/collage checkerboard, crisp square edges, no text/UI/frame/objects, calm center for overlays; red uses cherry/coral, blue uses electric royal/cobalt. Medium-small consistent squares and restrained tonal variation.

Use native `PV.background(comp, 'red-checker')` or `'blue-checker'` for editable geometric tiles. Use `PV.plateBackground` for the generated raster with pan/rotation; this is AE animation applied to a still PNG, not an already animated video. Never assume a generated texture is perfectly seamless; do not tile the PNG. Use overscan and inspect all output edges.
