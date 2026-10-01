# Native library

Load `assets/ae/pixel-vibe.jsx` with `$.evalFile`; its namespace is `PV`. The demo shows every template/cut. All templates produce native editable compositions. No remote assets, plugins or network requests.

## Cards — `PV.card(kind, duration, options)`
| kind | Visible action / intended use |
|---|---|
| brief | Paper brief: question becomes a concrete task |
| window | Desktop window: staggered modules appear |
| terminal | Command changes, progress completes |
| diff | Removed line changes into a resolved patch |
| calendar | Ordered 26→27→28→29 hinged leaves |
| invoice | Separate two prices; no quota/API equivalence |
| compare | Two equal visual columns; no invented winner |
| checklist | Checks draw one at a time |
| task | Same artifact moves between two panes |
| portal | Resource selection opens its contents |

Options: `background` (native environment or any ID from [backgrounds.md](backgrounds.md)), `title` (short, explicit copy), `font` (installed display font name), `seed` (reserved; current patterns deterministic). Bodies are neutral schematic samples, not production claims. Replace content and layout with the actual beat. Every kind is covered in the demo; scenes retain 0.8s handles.

## Environments — `PV.background(comp, 'checker'|'sky'|'red-checker'|'blue-checker')`
Procedural moving checkerboard; geometric pixel sky/clouds/meadow. Original construction, no photo or third-party game asset. Red/coral and royal/cobalt variants keep the same drifting checker geometry.

`PV.plateBackground(comp, 'red-checker'|'blue-checker')` imports the included AI-generated PNG and animates its pan/rotation with 20% overscan. Use it on a fresh composition before adding foreground layers. These are static source plates with AE motion tracks, not baked animated clips. The adapter also accepts all 20 new scene IDs; see [backgrounds.md](backgrounds.md). Native rendering of this adapter is pending.

## Cuts — `PV.cut(master, outgoingComp, start, cutTime, kind)`
| kind | Motion / meaning |
|---|---|
| shatter | 3×4 tiles split the actual outgoing scene |
| strips | Six strips cascade away |
| page | Whole scene hinges on its left edge |
| drag | Pointer pulls the actual scene out |
| zoom | Object/scene punch with opacity clearance |
| wipe | Staggered palette bars cover then reveal |

`start` is the outgoing scene's master start time; `cutTime` is its end. Incoming scene must already be below outgoing cut layers. End all cut layers at cutTime+0.7, keep outgoing source handles at least that long. Change cut family between adjacent beats. Page transitions must not expose unintentionally mirrored copy.

## Primitives
`PV.comp`, `PV.rect`, `PV.text`, `PV.keys`, `PV.enter`, `PV.pop`, `PV.path`, `PV.pointer`, `PV.burst`, `PV.mask`, `PV.bar`. `keys` handles spatial properties' single ease dimension. `path` uses native Trim Paths. `pointer` is a drawn cursor; the calling beat must create target reaction. `burst` is an accent, not a substitute for storytelling.

## Build example
Run `scripts/build-demo.jsx` from AE. It builds a 40-second catalog (ten four-second beats) with every card and transition. It stops if the current project is unsaved, never silently discards it. Project saves to ignored `output/` beside this package. Read the source before running scripts from any repository.
