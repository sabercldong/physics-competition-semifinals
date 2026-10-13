from pathlib import Path
import json,hashlib
import pypdfium2 as pdfium
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parents[1]
def hashes(p):
 doc=pdfium.PdfDocument(str(p));h=[]
 for pg in doc:
  bm=pg.render(scale=1);h.append(hashlib.sha256(bm.to_pil().convert('RGB').tobytes()).hexdigest());bm.close();pg.close()
 doc.close();return h
rows=[]
for n in range(35,44):
 b=ROOT/f'第{n}届/整理版'
 for p in sorted((b/'output').glob('*.pdf')):
  baseline=OUT/'修改前'/p.relative_to(ROOT)
  old,new=hashes(baseline),hashes(p)
  assert len(old)==len(new),(p,len(old),len(new))
  changed=[i+1 for i,(a,z) in enumerate(zip(old,new)) if a!=z]
  preview=OUT/'changed-pages'/p.stem;preview.mkdir(parents=True,exist_ok=True)
  # Six per contact, same scale as each exam's established review sheets.
  sheets=[]
  for start in range(0,len(changed),6):
   canvas=Image.new('RGB',(1200,1830),'#eeeeee');draw=ImageDraw.Draw(canvas)
   for k,page in enumerate(changed[start:start+6]):
    img=Image.open(b/'preview'/p.stem/f'page-{page:03d}.jpg');img.thumbnail((570,565))
    x=(k%2)*600;y=(k//2)*610;canvas.paste(img,(x+(600-img.width)//2,y+32));draw.text((x+16,y+10),f'{n} {p.stem} page {page}',fill='black')
   name=preview/f'contact-{start//6+1:02d}.jpg';canvas.save(name,quality=90);sheets.append(str(name.relative_to(ROOT)))
  row=dict(exam=n,name=p.name,path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),pages=len(new),changed_pages=changed,unchanged_pages=[i+1 for i,(a,z) in enumerate(zip(old,new)) if a==z],contact_sheets=sheets,page_pixel_hashes=new,baseline_sha256=hashlib.sha256(baseline.read_bytes()).hexdigest())
  rows.append(row);print(n,p.stem.split('_')[1],len(changed),'changed',flush=True)
(OUT/'page-comparison.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print('total pages',sum(r['pages'] for r in rows),'changed',sum(len(r['changed_pages']) for r in rows),'sheets',sum(len(r['contact_sheets']) for r in rows),flush=True)
