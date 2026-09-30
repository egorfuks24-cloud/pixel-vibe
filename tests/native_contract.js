/* Pure contract harness, NOT the After Effects runtime or renderer. */
const fs=require('fs'), vm=require('vm'), path=require('path'), assert=require('assert');
const root=path.resolve(__dirname,'..');let propertyCount=0;
class Prop {
 constructor(name){this.name=name;this.children={};this.numKeys=0;this.value=name==='ADBE Text Document'?{}:name==='scale'?[100,100]:name==='position'?[0,0]:0;this.propertyValueType=name==='position'?2:0;}
 property(n){return this.children[n]||(this.children[n]=new Prop(n));}
 addProperty(n){propertyCount++;return new Prop(n);}
 setValue(v){this.value=v;}
 setValueAtTime(t,v){assert(Number.isFinite(t)&&t>=0,'invalid time');this.value=v;this.numKeys++;}
 setTemporalEaseAtKey(i,a,b){assert(i>0&&a.length===b.length);}
}
class Layer extends Prop{
 constructor(c,s){super('layer');this.containingComp=c;this.source=s;this.transform={};for(const p of ['position','scale','rotation','opacity','anchorPoint','xRotation','yRotation'])this.transform[p]=new Prop(p);}
}
class Comp{constructor(n,w,h,d){this.name=n;this.width=w;this.height=h;this.duration=d;this.created=[];this.layers={addShape:()=>this.add(),addText:()=>this.add(),add:s=>this.add(s)};}add(s){const l=new Layer(this,s);this.created.push(l);return l;}openInViewer(){}}
let made=[];const sandbox={app:{project:{items:{addComp:(n,w,h,p,d,fps)=>{assert(fps===60);const c=new Comp(n,w,h,d);made.push(c);return c;}}}},Shape:function(){},KeyframeEase:function(){},PropertyValueType:{TwoD_SPATIAL:2,ThreeD_SPATIAL:3},console};
vm.createContext(sandbox);vm.runInContext(fs.readFileSync(path.join(root,'assets/ae/pixel-vibe.jsx'),'utf8'),sandbox);
const pv=sandbox.PV,kinds=['brief','window','terminal','diff','calendar','invoice','compare','checklist','task','portal'];
const scenes=kinds.map(k=>pv.card(k,4.8,{}));const master=pv.comp('catalog',1080,1920,40);
for(const cut of ['shatter','strips','page','drag','zoom','wipe'])pv.cut(master,scenes[0],0,4,cut);
assert.throws(()=>pv.card('unknown',4.8,{}));assert.throws(()=>pv.card('brief',2,{}));
assert.throws(()=>pv.cut(master,scenes[0],0,4,'unknown'));
for(const c of made)for(const l of c.created){if(l.outPoint!==undefined){assert(l.outPoint<=c.duration+.0001,c.name+' overlong layer');if(l.inPoint!==undefined)assert(l.inPoint<l.outPoint,'invalid layer interval');}}
assert(propertyCount>100);assert(made.filter(c=>c.name.startsWith('PV calendar leaf')).length===3);
console.log('PASS: ten card constructors, six cuts, invalid input guards, layer bounds; mock contract only.');
