/* Pixel Vibe backgrounds only; no personal media. */
(function(){
var root=new File($.fileName).parent.parent;
if(app.project&&app.project.dirty){alert('Save current project first.');return;}
var out=new Folder(root.fsName+'/output');if(!out.exists&&!out.create()){alert('Cannot create output folder');return;}
var grouped=false;
try{
$.evalFile(new File(root.fsName+'/assets/ae/pixel-vibe.jsx'));
app.newProject();app.beginUndoGroup('Pixel Vibe background catalog');grouped=true;
var names=["01-cyan-cloud-meadow", "02-red-sunset-clouds", "03-cobalt-cloud-stairs", "04-lavender-cloud-sea", "05-peach-floating-islands", "06-mint-cloud-window", "07-yellow-sun-clouds", "08-pink-cloud-coast", "09-teal-cloud-horizon", "10-orange-desert-clouds", "11-violet-night-clouds", "12-ice-blue-snow-clouds", "13-red-pixel-checker", "14-blue-pixel-checker", "15-lime-diagonal-tiles", "16-magenta-cloud-portals", "17-indigo-moon-clouds", "18-cream-green-clouds", "19-aqua-pixel-ripples", "20-ruby-cloud-mountains"];
var m=PV.comp('Pixel Vibe Backgrounds',1080,1920,40);
for(var i=0;i<names.length;i++){var c=PV.comp(names[i],1080,1920,2);PV.background(c,names[i]);var l=m.layers.add(c);l.startTime=i*2;l.inPoint=i*2;l.outPoint=(i+1)*2;}
m.time=0;m.openInViewer();app.project.save(new File(out.fsName+'/pixel-vibe-backgrounds.aep'));
app.endUndoGroup();grouped=false;
}catch(e){if(grouped)app.endUndoGroup();alert('Pixel Vibe backgrounds: '+e.toString()+' line '+e.line);}
})();
