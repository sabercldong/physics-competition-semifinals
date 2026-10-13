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
def inline_figs(md):
    def repl(m):
        caption,name=m.group(1),Path(m.group(2)).stem
        body=(ROOT/"figures"/f"{name}.tikz").read_text(encoding="utf-8")
        return ("\n\n\\begin{center}\n\\begin{minipage}{\\linewidth}\n"
                "\\centering\\begingroup\n\\sbox{\\diagrambox}{\\small\n"+body+
                "}\n\\ifdim\\wd\\diagrambox>.88\\linewidth\n"
                "\\sbox{\\diagrambox}{\\resizebox{.88\\linewidth}{!}{\\usebox{\\diagrambox}}}\n\\fi\n"
                "\\ifdim\\ht\\diagrambox>.29\\textheight\n"
                "\\resizebox{!}{.29\\textheight}{\\usebox{\\diagrambox}}\n"
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
    assert len(texts)==7
    parts=[split(t) for t in texts]
    template=(ROOT/"latex/template.tex").read_text(encoding="utf-8")
    summary={}
    for vi,(v,key) in enumerate(VERSIONS.items()):
        md=parts[0][vi]
        for qi in range(1,len(parts)):
            sep="\n\n\\bigskip\n\n" if key=="paper" and qi==6 else "\n\n\\clearpage\n\n"
            md+=sep+parts[qi][vi]
        if vi==0:
            md=("本卷共7题，总分320分。考试时间：9:00—12:00。所有需要评阅的"
                "解答均须写在答题纸上。\n\n"+md)
        fname=f"第43届_{v}"
        (ROOT/"output"/f"{fname}.md").write_text(md,encoding="utf-8")
        texmd=md
        if key=="paper":
            # Place the model next to its introducing paragraph, before lengthy subquestions.
            for num in (4,6):
                match=re.search(r"!\[[^\]]+\]\(\.\./figures/q"+str(num)+r"-[^)]+\.png\)",texmd)
                if match:
                    img=match.group(0);texmd=texmd.replace(img,"")
                    qstart=texmd.index("# 第 "+str(num)+" 题")
                    substart=texmd.index("（1）",qstart)
                    texmd=texmd[:substart]+img+"\n\n"+texmd[substart:]
        texmd=inline_figs(texmd)
        p=subprocess.run(["pandoc","--from=markdown+tex_math_dollars+raw_tex",
                          "--to=latex","--top-level-division=section"],
                         input=texmd,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        if p.returncode: raise RuntimeError(p.stderr)
        note={"paper":"题面与题图整理稿",
              "student":"完整题面、物理模型与逐步推导",
              "teacher":"包含学生核心解析与每题四道完整变式"}[key]
        body=p.stdout
        # Apply no-break groups after Markdown conversion, so math still gets parsed.
        if key=="teacher":
            chunks=body.split("\\clearpage")
            for qi in (0,1,3,4,6):
                pos=chunks[qi].index("\\subsubsection{变式4")
                anchor=chunks[qi].rfind("\\hypertarget",0,pos)
                if anchor>=0:pos=anchor
                if qi in (3,6):
                    # Keep a short complete final variant together, including displays.
                    chunks[qi]=(chunks[qi][:pos]+"\\par\\noindent\\begin{minipage}{\\linewidth}\n"
                                "\\setlength{\\parindent}{2em}\\setlength{\\parskip}{.35em}\n"
                                +chunks[qi][pos:]+"\n\\end{minipage}\\par\n")
                else:
                    chunks[qi]=chunks[qi][:pos]+"\\begin{samepage}\n"+chunks[qi][pos:]+"\n\\end{samepage}\n"
            body="\\clearpage".join(chunks)
        if key=="student":
            # A short final derivation should end as a complete block, without a sparse tail.
            endings=["（9）区分缩放规律、交换对称与电流统计。",
                     "（11）分别估计形变和角度近似。",
                     "（10）阻尼选择取向的能量依据。",
                     "（2.8）从角动量损失复核轨道下降率。",
                     "（7）为什么横摇与升沉在一阶可以分别求解。",
                     "（7）从麦克斯韦方程推出横向色散。",
                     "（6）矩阵如何解释缺级与周期结构。"]
            chunks=body.split("\\clearpage")
            for qi,marker in enumerate(endings):
                pos=chunks[qi].index(marker)
                chunks[qi]=(chunks[qi][:pos]+"\\par\\noindent\\begin{minipage}{\\linewidth}\n"
                            "\\setlength{\\parindent}{2em}\\setlength{\\parskip}{.35em}\n"
                            +chunks[qi][pos:]+"\n\\end{minipage}\\par\n")
            body="\\clearpage".join(chunks)
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
