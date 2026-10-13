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
def inline_figs(md,compact=False):
    def repl(m):
        body=(ROOT/'figures'/f'{Path(m.group(2)).stem}.tikz').read_text()
        cap=('.39' if Path(m.group(2)).stem.startswith('q7-photo') else '.20') if compact else '.38'
        return ('\n\n\\begin{center}\n\\begin{minipage}{\\linewidth}\n'
        '\\centering\\begingroup\\sbox{\\diagrambox}{\\small\n'+body+
        '}\n\\ifdim\\wd\\diagrambox>.88\\linewidth\n'
        '\\sbox{\\diagrambox}{\\resizebox{.88\\linewidth}{!}{\\usebox{\\diagrambox}}}\\fi\n'
        '\\ifdim\\ht\\diagrambox>'+cap+'\\textheight\n'
        '\\resizebox{!}{'+cap+'\\textheight}{\\usebox{\\diagrambox}}\n'
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
        if i==0:md='本卷共8题，总分320分。\n\n'+md
        stem=f'第35届_{v}';(ROOT/'output'/f'{stem}.md').write_text(md)
        p=subprocess.run(['pandoc','--from=markdown+tex_math_dollars+raw_tex','--to=latex','--top-level-division=section'],input=inline_figs(md,compact=i==0),text=True,capture_output=True);assert p.returncode==0,p.stderr
        body=p.stdout.replace(r'\def\LTcaptype{none}',r'\def\LTcaptype{table}')
        # A complete final variant is shorter than a page; preserve its
        # conclusion instead of carrying a few lines onto a separate tail page.
        if i==2:
            pat=r'(\\subsubsection\{(?:\\texorpdfstring\{)?变式3.*?)(?=\\clearpage|\Z)'
            body=re.sub(pat,lambda m:r'\par\noindent\begin{minipage}{\linewidth}'+'\n'+m.group(1)+r'\end{minipage}\par'+'\n',body,flags=re.S)
        if i>0:
            # Keep the final orbital worked example together instead of
            # leaving its last equation and closing paragraph on a tail page.
            pat=r'(\\subsubsection\{7\.\s*无量纲化后的具体算例\}.*?)(?=\\subsection\{六、|\\clearpage|\Z)'
            body=re.sub(pat,lambda m:r'\par\noindent\begin{minipage}{\linewidth}'+'\n'+m.group(1)+r'\end{minipage}\par'+'\n',body,flags=re.S)
            for title in []:
                pat=r'(\\subsubsection\{'+re.escape(title)+r'\}.*?)(?=\\subsection\{六、|\\clearpage|\Z)'
                body=re.sub(pat,lambda m:r'\par\noindent\begin{minipage}{\linewidth}'+'\n'+m.group(1)+r'\end{minipage}\par'+'\n',body,flags=re.S)
        tex=ROOT/'latex'/f'{stem}.tex';tex.write_text(template.replace('%%%VERSION%%%',v).replace('%%%BODY%%%',body))
        if not o.generate_only:
            for k in [1,2]:run(['xelatex','-interaction=nonstopmode','-halt-on-error','-output-directory='+str(ROOT/'build'),str(tex)],log=ROOT/'build'/f'{stem}-pass{k}.txt')
            pdf=ROOT/'build'/f'{stem}.pdf'
            # Publish by replacing a fully written file, avoiding a partial
            # destination when macOS fast-copy encounters an I/O failure.
            temp_pdf=ROOT/'output'/f'{stem}.pdf.tmp'
            temp_pdf.write_bytes(pdf.read_bytes())
            temp_pdf.replace(ROOT/'output'/pdf.name)
            result[v]={'pdf':pdf.name,'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest()};print('Built '+v,flush=True)
    (ROOT/'build/build-summary.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
