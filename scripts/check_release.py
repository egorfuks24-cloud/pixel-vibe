"""Read-only candidate audit. Reports filenames/counts, never matched values."""
import argparse,re
from pathlib import Path
ALLOWED={'.md','.py','.js','.jsx','.yaml','.json'}
EXACT={'.gitignore','LICENSE'}
IGNORED={'.git','__pycache__'}
PATTERNS=[r'/'+'Users'+r'/[^\s]+',r'/'+'home'+r'/[^\s]+',r'/'+'private'+r'/var/[^\s]+',r'(?i)\b(?:ghp|github_pat|sk_live|xoxb)[_-][A-Za-z0-9_-]{12,}',r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----',r'(?i)https?://t\.me/[A-Za-z0-9_]+',r'(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b']

def audit(root,denied=()):
    issues=[];count=0
    for p in sorted(root.rglob('*')):
        rel=p.relative_to(root)
        if any(part in IGNORED for part in rel.parts):continue
        if p.is_symlink():issues.append((str(rel),'symlink'));continue
        if not p.is_file():continue
        count+=1
        if p.name not in EXACT and p.suffix not in ALLOWED:issues.append((str(rel),'not in public text-file allowlist'));continue
        try:s=p.read_text(encoding='utf-8')
        except (OSError,UnicodeError):issues.append((str(rel),'unreadable text'));continue
        # Scanner regex definitions are patterns, not exposed credentials/paths.
        found=sum(bool(re.search(pattern,s)) for pattern in PATTERNS)
        found+=sum(bool(literal and literal.casefold() in s.casefold()) for literal in denied)
        if found:issues.append((str(rel),'sensitive pattern count '+str(found)))
    return count,issues

def main():
    p=argparse.ArgumentParser();p.add_argument('root',type=Path);p.add_argument('--deny-file',type=Path);a=p.parse_args()
    if not a.root.is_dir():p.error('root must be a directory')
    denied=a.deny_file.read_text(encoding='utf-8').splitlines() if a.deny_file else []
    count,issues=audit(a.root,denied)
    for f,reason in issues:print('FAIL: '+f+' — '+reason)
    print(('FAIL' if issues else 'PASS')+': '+str(count)+' public candidate files; '+str(len(issues))+' findings. Manual inventory review still required.')
    return bool(issues)
if __name__=='__main__':raise SystemExit(main())
