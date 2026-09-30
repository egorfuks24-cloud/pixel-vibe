"""Validate declared beat timing and provenance; no rendering or file mutation."""
import argparse,json,math
from pathlib import Path

def validate(data):
    errors=[]
    def number(v):return isinstance(v,(int,float)) and not isinstance(v,bool) and math.isfinite(v)
    total=data.get('duration');fps=data.get('fps')
    if not number(total) or total<=0:errors.append('duration must be positive');total=0
    if not number(fps) or fps<=0:errors.append('fps must be positive')
    beats=data.get('beats',[])
    if not isinstance(beats,list) or not beats:return errors+['nonempty beats list required']
    end=0;ids=set();heroes=set();previous=None
    for i,b in enumerate(beats):
        prefix='beat '+str(i)+': '
        if not isinstance(b,dict):errors.append(prefix+'object required');continue
        bid=b.get('id')
        if not isinstance(bid,str) or not bid or bid in ids:errors.append(prefix+'unique nonempty id required')
        else:ids.add(bid)
        start=b.get('start');dur=b.get('duration');hold=b.get('hold');handle=b.get('handle')
        if not all(number(v) for v in (start,dur,hold,handle)):errors.append(prefix+'numeric start/duration/hold/handle required');continue
        if abs(start-end)>1e-5:errors.append(prefix+'gap or overlap')
        if dur<=0 or hold<1 or hold>dur:errors.append(prefix+'invalid duration or readable hold')
        if handle<.7:errors.append(prefix+'transition source handle under 0.7s')
        end=start+dur
        for k in ('point','action','result','background','transition'):
            if not isinstance(b.get(k),str) or not b[k].strip():errors.append(prefix+k+' required')
        cut=b.get('transition')
        if cut not in ('shatter','strips','page','drag','zoom','wipe','none'):errors.append(prefix+'unknown cut')
        if cut=='none' and i!=len(beats)-1:errors.append(prefix+'missing transition')
        if previous==cut and cut!='none' and not b.get('intentional_recall'):errors.append(prefix+'repeated adjacent cut')
        previous=cut
        assets=b.get('assets',[])
        if not isinstance(assets,list) or not assets:errors.append(prefix+'asset provenance required');continue
        for a in assets:
            if not isinstance(a,dict) or not all(isinstance(a.get(k),str) and a[k].strip() for k in ('id','source','license','role')):errors.append(prefix+'incomplete asset provenance');continue
            if a['role']=='hero':
                if a['id'] in heroes and not b.get('intentional_recall'):errors.append(prefix+'hero reused without deliberate recall')
                heroes.add(a['id'])
    if abs(end-total)>1e-5:errors.append('beats do not cover declared duration')
    return errors

def main():
    p=argparse.ArgumentParser();p.add_argument('file',type=Path);a=p.parse_args()
    try:errors=validate(json.loads(a.file.read_text(encoding='utf-8')))
    except (OSError,ValueError,AttributeError) as e:print('FAIL: '+str(e));return 1
    for e in errors:print('FAIL: '+e)
    if not errors:print('PASS: declared timing, actions, holds and asset provenance')
    return bool(errors)
if __name__=='__main__':raise SystemExit(main())
