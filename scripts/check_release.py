"""Read-only candidate audit. Reports filenames/counts, never matched values."""
import argparse,re
from pathlib import Path
ALLOWED={'.md','.py','.js','.jsx','.yaml','.json'}
EXACT={'.gitignore','LICENSE'}
PLATES={'assets/backgrounds/07-yellow-sun-clouds.png', 'assets/backgrounds/08-pink-cloud-coast.png', 'assets/backgrounds/red-checker.png', 'assets/backgrounds/03-cobalt-cloud-stairs.png', 'assets/backgrounds/15-lime-diagonal-tiles.png', 'assets/backgrounds/09-teal-cloud-horizon.png', 'assets/backgrounds/12-ice-blue-snow-clouds.png', 'assets/backgrounds/02-red-sunset-clouds.png', 'assets/backgrounds/11-violet-night-clouds.png', 'assets/backgrounds/04-lavender-cloud-sea.png', 'assets/backgrounds/10-orange-desert-clouds.png', 'assets/backgrounds/19-aqua-pixel-ripples.png', 'assets/backgrounds/16-magenta-cloud-portals.png', 'assets/backgrounds/06-mint-cloud-window.png', 'assets/backgrounds/blue-checker.png', 'assets/backgrounds/17-indigo-moon-clouds.png', 'assets/backgrounds/20-ruby-cloud-mountains.png', 'assets/backgrounds/18-cream-green-clouds.png', 'assets/backgrounds/01-cyan-cloud-meadow.png', 'assets/backgrounds/13-red-pixel-checker.png', 'assets/backgrounds/05-peach-floating-islands.png', 'assets/backgrounds/14-blue-pixel-checker.png'}
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
        if str(rel) in PLATES or str(rel)=='assets/backgrounds/gallery.jpg':
            raw=p.read_bytes()
            if str(rel) in PLATES and not raw.startswith(b'\x89PNG\r\n\x1a\n'):issues.append((str(rel),'invalid PNG'))
            if str(rel).endswith('.jpg') and not raw.startswith(b'\xff\xd8'):issues.append((str(rel),'invalid JPEG'))
            if any(literal.encode().lower() in raw.lower() for literal in denied if literal):issues.append((str(rel),'confidential literal in binary'))
            continue
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
