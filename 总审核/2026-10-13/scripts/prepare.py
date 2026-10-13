from pathlib import Path
import json,hashlib,re,datetime
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parents[1]
manifest=[]
for b in sorted(ROOT.glob('第*届/整理版')):
 for part in ['drafts','scripts','latex','output','核验','sources']:
  for p in (b/part).rglob('*'):
   if p.is_file() and (part!='sources' or p.suffix in ['.json','.txt']):
    dest=OUT/'修改前'/p.relative_to(ROOT)
    dest.parent.mkdir(parents=True,exist_ok=True)
    if not dest.exists(): dest.write_bytes(p.read_bytes())
    manifest.append(dict(path=str(p.relative_to(ROOT)),sha256=hashlib.sha256(dest.read_bytes()).hexdigest()))
 for name in ['README.md','CHECKPOINT.json','SHA256清单.json']:
  p=b/name
  if p.exists():
   dest=OUT/'修改前'/p.relative_to(ROOT);dest.parent.mkdir(parents=True,exist_ok=True)
   if not dest.exists():dest.write_bytes(p.read_bytes())
for name in ['README.md','接管记录.md']:
 p=ROOT/name;dest=OUT/'修改前'/name
 if not dest.exists():dest.write_bytes(p.read_bytes())
(OUT/'baseline.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
# Complete prose inventory: skip display maths and numerical tables, retain prose containing inline maths.
for exam in range(35,44):
 lines=[];flags=[]
 for p in sorted((ROOT/f'第{exam}届/整理版/drafts').glob('*.md')):
  math=False
  for n,line in enumerate(p.read_text().splitlines(),1):
   if '$$' in line:math=not math;continue
   if math or not line.strip() or line.startswith(('!','|','\\')):continue
   if re.search('[\u4e00-\u9fff]',line):
    rec=f'{p.stem}:{n} {line}';lines.append(rec)
    if re.search(r'不是|而是|真正|值得|显然|本质|一眼|牢牢|抓住|主线|链条|闭环|路线|落地|反哺|底层|高级|很好的|非常|自然地|我们|模板|漂亮|最重要|关键是|关键在|关键的一|灵魂|这正|体现|充分|巧妙|入口是|入口不|难点不是|本题不|本题的|这道题',line):flags.append(rec)
 (OUT/f'prose-{exam}.txt').write_text('\n'.join(lines)+'\n')
 (OUT/f'flags-{exam}.txt').write_text('\n'.join(flags)+'\n')
 print(exam,'prose_lines',len(lines),'flagged',len(flags))
print('baseline files',len(manifest))
