# Public distribution

The reusable code/library is MIT. Adobe software, installed fonts, product trademarks and outside artwork retain their own licenses. Included environments and schematic cards are original code; no game sprites, portraits, private avatar, vendor footage or commercial font files are shipped.

Keep personal production assets under a separate `private/` project directory. NEVER ship local AEPs (embedded absolute paths), renders of private projects, voice recordings, project journals, auth files, user/channel names or downloaded references without a separate rights/privacy decision.

Run `python3 scripts/check_release.py .` on the exact candidate directory. Optional `--deny-file PATH` takes one confidential literal per line; keep that deny file outside the package. The scanner reports counts and relative filenames, never secret values. It detects only listed patterns/forbidden files; inspect the complete file inventory and any visual assets manually. Review tracked files and Git author metadata before a public push. The ZIP release uses an explicit clean inventory, excluding outputs and .git.

A screenshot/demo built exclusively from the neutral procedural catalog may be distributed after visual/privacy review. An AEP stays local; JSX rebuilds it portably on the recipient's machine.

Publishing or changing a remote repository requires user authorization. A skill invocation alone does not authorize publication, installation, account login or messaging a channel.
