#!/usr/bin/env python3
"""Rebuild copied source in an independent directory and compare rendered PDFs."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,tempfile
from pypdf import PdfReader
import pypdfium2 as pdfium
ROOT=Path(__file__).resolve().parents[1]
def pixhash(p):
    hashes=[];doc=pdfium.PdfDocument(str(p))
    for i in range(len(doc)):
        page=doc[i];bm=page.render(scale=.7)
        im=bm.to_pil().convert("RGB");hashes.append(hashlib.sha256(im.tobytes()).hexdigest())
        bm.close();page.close()
    doc.close();return hashes
def main():
    dest=Path(tempfile.mkdtemp(prefix="codex-37-rebuild-"))
    for d in ("drafts","scripts"):shutil.copytree(ROOT/d,dest/d)
    (dest/"latex").mkdir();shutil.copy2(ROOT/"latex/template.tex",dest/"latex/template.tex")
    log=ROOT/"核验/rebuild-command.log"
    with log.open("w") as f:
        p=subprocess.run([sys.executable,str(dest/"scripts/build_all.py")],stdout=f,stderr=subprocess.STDOUT)
    assert p.returncode==0,"rebuild failed: "+str(log)
    results=[]
    for p in sorted((ROOT/"output").glob("*.pdf")):
        other=dest/"output"/p.name
        r1=PdfReader(p);r2=PdfReader(other)
        tex1=(ROOT/"latex"/(p.stem+".tex")).read_bytes()
        tex2=(dest/"latex"/(p.stem+".tex")).read_bytes()
        same_text=[q.extract_text() for q in r1.pages]==[q.extract_text() for q in r2.pages]
        same_pixels=pixhash(p)==pixhash(other)
        assert tex1==tex2 and same_text and same_pixels,p.name
        results.append({"pdf":p.name,"pages":len(r1.pages),"TeX_identical":True,
                        "page_text_identical":same_text,"every_page_render_identical":same_pixels})
    (ROOT/"核验/rebuild-results.json").write_text(json.dumps(
        {"all_passed":True,"isolated_directory":str(dest),"results":results},ensure_ascii=False,indent=2))
    print(json.dumps(results,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
