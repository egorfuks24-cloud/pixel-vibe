import copy,importlib.util,json,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def module(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/('check_'+name+'.py'));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
B=module('beats');R=module('release')
class Checks(unittest.TestCase):
    def setUp(self):self.data=json.loads((ROOT/'assets/beat-sheet.example.json').read_text())
    def test_example(self):self.assertEqual(B.validate(self.data),[])
    def test_gap(self):self.data['beats'][1]['start']+=.2;self.assertTrue(B.validate(self.data))
    def test_handle(self):self.data['beats'][0]['handle']=.1;self.assertTrue(B.validate(self.data))
    def test_provenance(self):self.data['beats'][0]['assets'][0]['license']='';self.assertTrue(B.validate(self.data))
    def test_reuse(self):self.data['beats'][1]['assets'][0]['id']=self.data['beats'][0]['assets'][0]['id'];self.assertTrue(B.validate(self.data))
    def test_invalid(self):self.data['beats'][0]['start']=float('nan');self.assertTrue(B.validate(self.data))
    def test_private_literal_and_binary(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'safe.md').write_text('Neutral content');self.assertEqual(R.audit(p)[1],[])
            (p/'safe.md').write_text('CONFIDENTIAL_FIXTURE');self.assertTrue(R.audit(p,['CONFIDENTIAL_FIXTURE'])[1])
            (p/'asset.aep').write_bytes(b'project');self.assertTrue(R.audit(p)[1])
    def test_png_allowlist(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);a=p/'assets/backgrounds';a.mkdir(parents=True);(a/'red-checker.png').write_bytes(b'not a png');self.assertTrue(R.audit(p)[1])
    def test_symlink(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'safe.md').write_text('Neutral');(p/'alias.md').symlink_to(p/'safe.md');self.assertTrue(R.audit(p)[1])
if __name__=='__main__':unittest.main()
