# After Effects connection

This is a JSX scripting workflow, not a built-in Codex↔AE plugin or verified MCP bridge. Requires a separately installed and licensed Adobe After Effects. No paid animation plugins required.

1. Keep the complete skill folder together. Save your current AE project first.
2. In After Effects choose **File → Scripts → Run Script File…** and select `scripts/build-demo.jsx`. Russian UI: **Файл → Сценарии → Выполнить файл сценария…**. It loads the included library, creates the editable catalog and saves `output/pixel-vibe-demo.aep`.
3. Open **Pixel Vibe Catalog**. Preview at half/quarter resolution; inspect cuts and type before a full export. Save any changes.
4. For an actual reel, ask Codex to create a project-specific build JSX using `PV` and your approved beat sheet. Run it through the same menu. Native UI automation is optional and depends on the host's available controls; manual script execution is sufficient.
5. Export through AE Render Queue, or the installed `aerender`. Output templates and H.264 availability depend on the installed AE version. Do not assume a template name exists; inspect the queue's available modules. A PNG sequence is a portable fallback, but calculate disk usage first.

Conservative command pattern (replace executable/project/output with your own paths):
```text
aerender -reuse -project PROJECT.aep -comp "Pixel Vibe Catalog" -mem_usage 10 40 -mfr OFF 20 -output OUTPUT
```
Use one render at a time. `-reuse` reuses a running AE instance. Tune memory for the actual machine; these settings are a starting profile, not a memory guarantee. Leave free disk space for cache and output. Do not kill AE or remove caches automatically.

This package uses project save and AE objects; it does not run shell commands or fetch network content. Do not enable “Allow Scripts to Write Files and Access Network” preemptively. If a later authorized script genuinely needs file/network access, inspect its code and enable only what that workflow requires.

If a build fails: preserve current project, record the error and line, repair only the named component, try once more. If a script stalls, cancel through AE and save a recovery copy; do not rerun the same unbounded script. An editor screenshot is not proof of a completed render.

Official references: [Adobe scripts](https://helpx.adobe.com/after-effects/using/scripts.html), [Adobe automated rendering](https://helpx.adobe.com/after-effects/using/automated-rendering-network-rendering.html). Library runtime coverage is recorded in `TESTING.md`; do not claim another AE version was tested.
