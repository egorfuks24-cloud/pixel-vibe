/* Trusted local demo. Review before execution. Does not fetch remote content. */
(function(){
var root=new File($.fileName).parent.parent;
if(app.project&&app.project.dirty){alert('Save your current project before running Pixel Vibe.');return;}
var out=new Folder(root.fsName+'/output');if(!out.exists&&!out.create()){alert('Cannot create output folder.');return;}
var opened=false;
try{
$.evalFile(new File(root.fsName+'/assets/ae/pixel-vibe.jsx'));
app.newProject();app.beginUndoGroup('Pixel Vibe catalog');opened=true;
var kinds=['brief','window','terminal','diff','calendar','invoice','compare','checklist','task','portal'];
var cuts=['shatter','strips','page','drag','zoom','wipe'];
var m=PV.comp('Pixel Vibe Catalog',1080,1920,40),scenes=[],i,l;
for(i=0;i<kinds.length;i++){var c=PV.card(kinds[i],4.8,{});scenes.push(c);l=m.layers.add(c);l.startTime=i*4;l.inPoint=i*4;l.outPoint=(i+1)*4;}
for(i=0;i<9;i++)PV.cut(m,scenes[i],i*4,(i+1)*4,cuts[i%cuts.length]);
m.time=1.5;m.openInViewer();app.project.save(new File(out.fsName+'/pixel-vibe-demo.aep'));
app.endUndoGroup();opened=false;
}catch(e){if(opened)app.endUndoGroup();alert('Pixel Vibe: '+e.toString()+' line '+e.line);}
})();
