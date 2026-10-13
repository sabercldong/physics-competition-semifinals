#!/usr/bin/env python3
"""Build three editions from per-question teaching masters."""
from pathlib import Path
import argparse,hashlib,json,subprocess,shutil,sys,re
ROOT=Path(__file__).resolve().parents[1]
def run(args,cwd=ROOT,log=None):
    p=subprocess.run(args,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    if log:Path(log).write_text(p.stdout)
    if p.returncode:raise RuntimeError(p.stdout[-6000:])
    return p.stdout
def split(t):
    paper=t.split('## 一、题型定位',1)[0].rstrip()+'\n'
    core=t.split('## 六、关键洞察',1)[0].rstrip()+'\n'
    return paper,core,t.rstrip()+'\n'
def inline_figs(md):
    def repl(m):
        body=(ROOT/'figures'/f'{Path(m.group(2)).stem}.tikz').read_text()
        return ('\n\n\\begin{center}\n\\begin{minipage}{\\linewidth}\n'
        '\\centering\\begingroup\\sbox{\\diagrambox}{\\small\n'+body+
        '}\n\\ifdim\\wd\\diagrambox>.88\\linewidth\n'
        '\\sbox{\\diagrambox}{\\resizebox{.88\\linewidth}{!}{\\usebox{\\diagrambox}}}\\fi\n'
        '\\ifdim\\ht\\diagrambox>.38\\textheight\n'
        '\\resizebox{!}{.38\\textheight}{\\usebox{\\diagrambox}}\n'
        '\\else\\usebox{\\diagrambox}\\fi\n\\par\\smallskip{\\small '+m.group(1)+
        '\\par}\\endgroup\\end{minipage}\\end{center}\n\n')
    return re.sub(r'!\[([^\]]+)\]\((\.\./figures/[^)]+\.png)\)',repl,md)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--skip-figures',action='store_true');ap.add_argument('--generate-only',action='store_true')
    ap.add_argument('--edition',choices=['试题版','学生详解版','教师备课版']);o=ap.parse_args()
    for d in ['build','output','latex','preview']:(ROOT/d).mkdir(exist_ok=True)
    run([sys.executable,str(ROOT/'scripts/make_figures.py')])
    if not o.skip_figures:
        import pypdfium2 as pdfium
        for p in sorted((ROOT/'figures').glob('*.tex')):
            run(['xelatex','-interaction=nonstopmode','-halt-on-error',p.name],cwd=p.parent,log=ROOT/'build'/f'{p.stem}-compile.txt')
            doc=pdfium.PdfDocument(str(p.with_suffix('.pdf')));pg=doc[0];bm=pg.render(scale=2.5);bm.to_pil().save(p.with_suffix('.png'));bm.close();pg.close();doc.close()
    files=sorted((ROOT/'drafts').glob('question-*.md'));assert len(files)==8
    parts=[split(p.read_text()) for p in files];template=(ROOT/'latex/template.tex').read_text()
    summary=ROOT/'build/build-summary.json'
    result=json.loads(summary.read_text()) if o.edition and summary.exists() else {}
    for i,v in enumerate(['试题版','学生详解版','教师备课版']):
        if o.edition and v!=o.edition:continue
        md='\n\n\\clearpage\n\n'.join(p[i] for p in parts)
        if i==0:md='本卷共8题，总分320分。考试时间：9:00-12:00。所有需要评阅的解答均须写在答题纸上。\n\n'+md
        stem=f'第40届_{v}';(ROOT/'output'/f'{stem}.md').write_text(md)
        p=subprocess.run(['pandoc','--from=markdown+tex_math_dollars+raw_tex','--to=latex','--top-level-division=section'],input=inline_figs(md),text=True,capture_output=True);assert p.returncode==0,p.stderr
        body=p.stdout.replace(r'\def\LTcaptype{none}',r'\def\LTcaptype{table}')
        # Keep short concluding arguments whole; avoid a few-line tail page.
        markers=([r'\subsubsection{12　低温与临界点的其他极限}'] if i==1 else
                 ['若改为固定像素数的绝对标准误差',
                  r'\subsubsection{变式4　有初始切向速度的定半径轨道}',
                  r'\subsubsection{变式4　有限球壳厚度的积分修正}',
                  r'\subsubsection{变式3　从波长位移反求角度}'] if i==2 else [])
        for marker in markers:
            start=body.index(marker);end=body.find(r'\clearpage',start)
            if end<0:end=len(body)
            body=body[:start]+'\\noindent\\begin{minipage}{\\linewidth}\n'+body[start:end]+'\n\\end{minipage}\n\n'+body[end:]
        tex=ROOT/'latex'/f'{stem}.tex';tex.write_text(template.replace('%%%VERSION%%%',v).replace('%%%BODY%%%',body))
        if not o.generate_only:
            for k in [1,2]:run(['xelatex','-interaction=nonstopmode','-halt-on-error','-output-directory='+str(ROOT/'build'),str(tex)],log=ROOT/'build'/f'{stem}-pass{k}.txt')
            pdf=ROOT/'build'/f'{stem}.pdf';shutil.copy2(pdf,ROOT/'output'/pdf.name)
            result[v]={'pdf':pdf.name,'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest()};print('Built '+v,flush=True)
    (ROOT/'build/build-summary.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
