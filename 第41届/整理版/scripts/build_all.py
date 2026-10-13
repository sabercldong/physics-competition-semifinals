#!/usr/bin/env python3
"""Single-source three-version build with editable, self-contained TeX."""
from pathlib import Path
import argparse, hashlib, json, re, shutil, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]
VERSIONS = {"试题版": "paper", "学生详解版": "student", "教师备课版": "teacher"}
def run(args, cwd=ROOT, log=None):
    p = subprocess.run(args,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    if log: Path(log).write_text(p.stdout,encoding="utf-8")
    if p.returncode: raise RuntimeError(f"Command failed: {args}\n{p.stdout[-6000:]}")
    return p.stdout
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def split(text):
    paper, core = text.split("## 一、题型定位",1)
    student = (paper+"## 一、题型定位"+core).split("## 六、关键洞察",1)[0].rstrip()+"\n"
    return paper.rstrip()+"\n",student,text.rstrip()+"\n"
def inline_figs(md,compact=False):
    def repl(m):
        caption,name=m.group(1),Path(m.group(2)).stem
        body=(ROOT/"figures"/f"{name}.tikz").read_text(encoding="utf-8")
        if compact and name.startswith("q2-"):
            body=r"\scalebox{.85}{"+body+"}\n"
        return ("\n\n\\begin{center}\n\\begin{minipage}{\\linewidth}\n"
                "\\centering\\begingroup\n\\sbox{\\diagrambox}{\\small\n"+body+
                "}\n\\ifdim\\wd\\diagrambox>.88\\linewidth\n"
                "\\sbox{\\diagrambox}{\\resizebox{.88\\linewidth}{!}{\\usebox{\\diagrambox}}}\n\\fi\n"
                "\\ifdim\\ht\\diagrambox>.40\\textheight\n"
                "\\resizebox{!}{.40\\textheight}{\\usebox{\\diagrambox}}\n"
                "\\else\\usebox{\\diagrambox}\\fi\n"
                "\\par\\smallskip{\\small "+caption+"\\par}\n"
                "\\endgroup\\end{minipage}\n\\end{center}\n\n")
    return re.sub(r"!\[([^\]]+)\]\((\.\./figures/[^)]+\.png)\)",repl,md)
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--skip-figures",action="store_true")
    ap.add_argument("--generate-only",action="store_true")
    opts=ap.parse_args()
    for d in ("build","output","latex","preview"): (ROOT/d).mkdir(exist_ok=True)
    run([sys.executable,str(ROOT/"scripts/make_figures.py")])
    if not opts.skip_figures:
        import pypdfium2 as pdfium
        for tex in sorted((ROOT/"figures").glob("*.tex")):
            run(["xelatex","-interaction=nonstopmode","-halt-on-error",
                 "-output-directory=.",tex.name],cwd=tex.parent,
                 log=ROOT/"build"/f"{tex.stem}-compile.txt")
            doc=pdfium.PdfDocument(str(tex.with_suffix(".pdf")))
            pg=doc[0]; bm=pg.render(scale=2.5); bm.to_pil().save(tex.with_suffix(".png"))
            bm.close(); pg.close(); doc.close()
        print("Figures compiled",flush=True)
    texts=[p.read_text(encoding="utf-8") for p in sorted((ROOT/"drafts").glob("question-*.md"))]
    assert len(texts)==7, "本届应为7题"
    parts=[split(t) for t in texts]
    template=(ROOT/"latex/template.tex").read_text(encoding="utf-8")
    summary={}
    for vi,(v,key) in enumerate(VERSIONS.items()):
        md=parts[0][vi]
        for qi in range(1,len(parts)):
            sep="\n\n\\clearpage\n\n"
            md+=sep+parts[qi][vi]
        if vi==0:
            # The long billiard question continues with its impact-height and
            # 30-degree-rule parts on a second substantive question page.
            marker="（3）击球者在开球时"
            assert marker in md
            md=md.replace(marker,"\\clearpage\n\n"+marker,1)
        if vi==0:
            md=("本卷共7题，总分320分。考试时间：9:00—12:00。所有需要评阅的"
                "解答均须写在答题纸上。\n\n"+md)
        fname=f"第41届_{v}"
        (ROOT/"output"/f"{fname}.md").write_text(md,encoding="utf-8")
        texmd=md
        texmd=inline_figs(texmd,compact=(vi==0))
        p=subprocess.run(["pandoc","--from=markdown+tex_math_dollars+raw_tex",
                          "--to=latex","--top-level-division=section"],
                         input=texmd,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        if p.returncode: raise RuntimeError(p.stderr)
        note={"paper":"题面与题图整理稿",
              "student":"完整题面、物理模型与逐步推导",
              "teacher":"包含学生核心解析与每题四道完整变式"}[key]
        # Pandoc 3.9 emits LTcaptype=none, unsupported by this TeX Live
        # longtable version; these uncaptained tables can use the table counter.
        body=p.stdout.replace(r"\def\LTcaptype{none}",r"\def\LTcaptype{table}")
        if vi==1:
            start=body.index(r"\subsubsection{11　端点与一个数值过程}")
            end=body.index(r"\clearpage",start)
            body=body[:start]+"\\noindent\\begin{minipage}{\\linewidth}\n"+body[start:end]+"\n\\end{minipage}\n\n"+body[end:]
        if vi==2:
            # Keep these short concluding variants intact, so their final
            # paragraphs do not form sparse three-line question-tail pages.
            for marker in ("变式4　风停止后的机械能下降",
                           "变式4　表面粒子间距改变",
                           "变式4　任意磁通的基态计算"):
                start=body.index(r"\subsubsection{"+marker)
                end=body.find(r"\clearpage",start)
                if end<0:end=len(body)
                body=body[:start]+"\\noindent\\begin{minipage}{\\linewidth}\n"+body[start:end]+"\n\\end{minipage}\n\n"+body[end:]
        source=template.replace("%%%VERSION%%%",v).replace("%%%COVERNOTE%%%",note).replace("%%%BODY%%%",body)
        texpath=ROOT/"latex"/f"{fname}.tex"
        texpath.write_text(source,encoding="utf-8")
        if not opts.generate_only:
            for turn in range(2):
                run(["xelatex","-interaction=nonstopmode","-halt-on-error",
                     "-output-directory="+str(ROOT/"build"),str(texpath)],
                    log=ROOT/"build"/f"{fname}-pass{turn+1}.txt")
            pdf=ROOT/"build"/f"{fname}.pdf"
            shutil.copy2(pdf,ROOT/"output"/pdf.name)
            summary[key]={"pdf":pdf.name,"sha256":sha(pdf)}
            print(f"Built {v}",flush=True)
    (ROOT/"build/build-summary.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8")
if __name__=="__main__": main()
