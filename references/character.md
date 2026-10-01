# Make your own 2D pixel character

This is an identity-preserving workflow using the user's own photo and an approved master. The public package contains instructions, not anyone's face or portrait. Keep photos, masters, pose cutouts and metadata in a separate private production project. Do not commit them to this repository.

## 1. Private identity and proportions
Inspect the supplied photo before generation. Record visible face silhouette, cheekbones, eyes, nose, mouth, hair, glasses if present and the user's chosen clothes. Ask only about missing choices that affect the requested result. Do not invent accessories or change age/body type. Use the already approved character if one exists.

Generate one master first with the built-in image tool: reference photo = identity input; approved style image = style input. Explicitly label their roles. Target clean 2D pixel sprite, consistent square pixel grid, readable face, compact game body, natural leg stance and loose clothing when selected. No glossy 3D, smooth anime body or arbitrary exaggerated muscles. Request genuine transparent background; a drawn checkerboard is not transparency. Generate the full figure with margins; don't cut off shoes, hands or head.

**Master prompt template**
```text
Create one full-body 2D pixel-art character using the supplied photo as the identity reference and the selected Pixel Vibe image as the style reference. Preserve recognizable face silhouette, cheekbones, hair and eyewear actually present in the photo. Use the user's selected body proportions and clothing. Crisp consistent square pixel edges, limited coherent palette, clear compact game silhouette, readable natural stance. Genuine transparent background, generous margin around the entire figure. No text, watermark, props, UI, fake transparent checkerboard, glossy 3D or invented accessories.
```
The template requires actual references. Without them, request the missing photo/master instead of inventing a substitute person.

## 2. Approve and lock the master
Inspect full size: does it resemble the photo, is the face stable, are hands/glasses plausible, is the body acceptable? Correct the master before producing poses. Save it as a private identity control. A successful generation does not mean the user approved the character.

## 3. Generate each pose using that same master
Use the approved master as the identity AND style anchor for every pose. One pose per image, same scale/palette/proportions, transparent background. If a local reference has not been viewed, inspect it first. Use image editing/reference inputs rather than repeatedly regenerating the person from a textual description.

**Pose prompt template**
```text
Use the approved master character as the identity and style reference. Change only the pose to: [ACTION]. Preserve the same face silhouette, cheekbones, hair, eyewear, head/body ratio, body build, outfit, shoes and square pixel-grid scale. Keep every limb inside frame with transparent margins. Genuine transparent background. No additional text or logos. Place a requested prop on a separate transparent asset when it needs its own motion.
```

| Pose | ACTION / purpose |
|---|---|
| idle | Relaxed standing, neutral expression; readable introductions |
| question | One palm up, mildly curious; question mark is a separate asset |
| think | Hand to chin, thoughtful expression; preserve cheeks/face |
| explain-left | Gesture toward the left, face toward viewer |
| explain-right | Gesture toward the right, face toward viewer |
| work | Typing at the selected laptop; laptop as separate prop if needed |
| result | Confident open posture, presenting a result card separately |
| CTA | Point toward resource/profile; no channel URL baked into sprite |

For unique major-beat illustrations, keep the master identity but change the actual action/prop/environment. Do not make eight versions of the same sitting image. No automatic mirror of asymmetrical outfit/face details.

## 4. 2D animation in After Effects
Separate body, hands and props when actions require it. A one-piece cutout can enter/tilt but cannot produce real typing, walking or talking by itself. For an actual sprite cycle, generate/edit consistent discrete frames from the master, inspect each frame and build an explicit image sequence. Verify total frame count and looping seam. Do not advertise a still as a fully rigged character.

Keep square edges deliberate: pixel sprites without motion blur, integer-friendly scaling where possible; avoid repeated resampling. Native props/UI may use selective blur. Animate anticipation → gesture/action → artifact response → hold. Match eye/hand direction to the target. The final pose should not obstruct the narrated value or CTA.

## 5. Delivery and privacy
Private character folder: master, separate pose PNGs, transparent prop assets, optional approved frame sequences, identity/style notes. Public Pixel Vibe: only this generic recipe. Publishing the skill never implies permission to publish the person's identity assets.
