#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,re,subprocess,shutil
from pypdf import PdfReader
import pypdfium2 as pdfium
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    results={"structure":[],"pdfs":[],"figures":[]}
    modules=["一、题型定位","二、知识点","三、物理图像","四、解题入口","五、解析",
             "六、关键洞察","七、易错点","八、课堂讲解建议","九、变式训练"]
    for p in sorted((ROOT/"drafts").glob("question-*.md")):
        t=p.read_text()
        headers=re.findall(r"^## (.+)$",t,re.M)
        assert headers==modules,(p,headers)
        assert len(re.findall(r"^### 变式[1-4]",t,re.M))==4
        for img in re.findall(r"!\[[^\]]+\]\(([^)]+)\)",t):
            assert (p.parent/img).is_file(),img
        results["structure"].append({"question":p.stem,"modules":9,"variants":4,"sha256":sha(p)})
    student=(ROOT/"output/第40届_学生详解版.md").read_text()
    teacher=(ROOT/"output/第40届_教师备课版.md").read_text()
    assert "## 六、关键洞察" not in student
    assert len(re.findall(r"^# 第 [1-8] 题",student,re.M))==8
    for p in sorted((ROOT/"drafts").glob("question-*.md")):
        core=p.read_text().split("## 六、关键洞察")[0].strip()
        assert core in student and core in teacher
    results["core_identical"]=True
    for p in sorted((ROOT/"output").glob("*.pdf")):
        check=subprocess.run(["qpdf","--check",str(p)],text=True,capture_output=True)
        assert check.returncode==0,check.stdout+check.stderr
        log=(ROOT/"build"/(p.stem+".log")).read_text()
        bad=re.findall(r"^.*(?:Overfull|Missing character|^! ).*$",log,re.M)
        assert not bad,(p.name,bad)
        reader=PdfReader(p)
        minima={"第40届_学生详解版.pdf":56,"第40届_教师备课版.pdf":71}
        if p.name in minima:
            assert len(reader.pages)-1>=minima[p.name],(p.name,"正文页数未达第101套标准",len(reader.pages)-1)
        # Poppler correctly decodes CJK ToUnicode here; pypdf drops some Fandol glyph mappings.
        extracted=subprocess.run(["pdftotext","-layout",str(p),"-"],text=True,capture_output=True,check=True)
        texts=extracted.stdout.split("\f")
        if not texts[-1].strip():texts.pop()
        assert len(texts)==len(reader.pages)
        start_pages=[i+1 for i,t in enumerate(texts) if re.search(r"第\s*[1-8]\s*题",t)]
        assert len(start_pages)==8,(p.name,"题数或生成内容重复",start_pages)
        cover=re.sub(r"\s+","",texts[0])
        assert len(cover)<80 and "考试时间" not in cover and "包含" not in cover
        tex=(ROOT/"latex"/(p.stem+".tex")).read_text()
        assert "\\fancyhead" not in tex and "\\renewcommand{\\headrulewidth}{0pt}" in tex
        preview=ROOT/"preview"/p.stem
        if preview.exists():shutil.rmtree(preview)
        preview.mkdir(exist_ok=True)
        doc=pdfium.PdfDocument(str(p))
        renders=[]
        for i in range(len(doc)):
            pg=doc[i];bm=pg.render(scale=1.35);im=bm.to_pil().convert("RGB")
            imgpath=preview/f"page-{i+1:03d}.jpg";im.save(imgpath,quality=90)
            renders.append(im);bm.close();pg.close()
        doc.close()
        for first in range(0,len(renders),6):
            sheet=Image.new("RGB",(1200,3*610),"#eeeeee");draw=ImageDraw.Draw(sheet)
            for j,im in enumerate(renders[first:first+6]):
                im=im.copy();im.thumbnail((570,565));xx=(j%2)*600;yy=(j//2)*610
                sheet.paste(im,(xx+(600-im.width)//2,yy+32))
                draw.text((xx+16,yy+10),f"{p.stem} PDF page {first+j+1}",fill="black")
            sheet.save(preview/f"contact-{first+1:03d}.jpg",quality=88)
        results["pdfs"].append({"name":p.name,"pages":len(reader.pages),"body_pages":len(reader.pages)-1,
             "required_body_pages":minima.get(p.name),"simple_cover":True,"page_headers":False,
             "sha256":sha(p),"qpdf":"passed","missing_glyphs":0,"overfull_boxes":0,
             "question_start_pdf_pages":[i+1 for i,t in enumerate(texts)
                                       if re.search(r"第\s*[1-8]\s*题",t)],
             "short_body_pdf_pages":[i+1 for i,t in enumerate(texts)
                                    if i>0 and len(re.sub(r"\s+","",t))<160]})
    for p in sorted((ROOT/"figures").glob("*.tikz")):
        results["figures"].append({"name":p.name,"sha256":sha(p),
                                  "vector_pdf_sha256":sha(p.with_suffix(".pdf"))})
    (ROOT/"核验/document-results.json").write_text(json.dumps(results,ensure_ascii=False,indent=2))
    print(json.dumps({"pdfs":results["pdfs"],"figures":len(results["figures"]),
                      "core_identical":True},ensure_ascii=False,indent=2))
if __name__=="__main__":main()
