# Visual contract

## Composition
9:16, 1080×1920, 60 fps. Starter safe area: x72–1008, y180–1640; validate against the intended platform's current overlays. Keep the face outside caption/UI collision zones. One large foreground subject and one semantic artifact, with optional small supporting layers. Scale changes should reveal information or move an object between scenes.

## Approved style family
- Environment: bright blue pixel sky/meadow, mint checkerboard with gentle drift; requested red/coral and electric royal/cobalt variants are available for individual scenes. Background motion must remain visible without competing with reading.
- Cards: blue desktop title bar, square corners, pale borders, hard offset shadows; paper cards yellow/mint; terminal charcoal/mint; calendar physical hinged leaves.
- Typography: oversized condensed outlined white display headings, dark offset edge; lighter readable UI/body. Check Cyrillic glyphs, number legibility and actual font substitution. Do not bundle licensed commercial font files. Starter uses installed Impact for display and Arial for UI; if unavailable, report and agree on a replacement. Do not silently impose a different pair.
- Color tokens in the native library follow this family; retain project controls when supplied. Pixel edges should be crisp. Disable motion blur on pixel sprites; use it selectively on panels, pointers and transitions.
- No decorative English slogans, fake metrics, unrelated stickers or repeated brand labels.

## Avatar recipe for a private project
Use the supplied approved identity reference. Lock face, hair, glasses, palette and body proportions. Produce distinct action cutouts; separate props from the body when their motion matters. Generate new major-beat illustrations rather than repeatedly floating one pose. This repository deliberately contains no identifiable avatar.

## Motion grammar
Primary action 0.35–0.7 s; secondary stagger 0.06–0.14 s; readable hold usually 1.2–2.0 s, extend for unfamiliar values. Background drift continues through holds. These are starting ranges, not universal limits. Avoid every object bobbing with the same rhythm. Background, artifact and cursor react to the same event.
