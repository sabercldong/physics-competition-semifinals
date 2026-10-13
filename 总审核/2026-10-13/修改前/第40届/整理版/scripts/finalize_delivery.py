#!/usr/bin/env python3
"""Bind completed reviews and checks to current deliverables."""
from pathlib import Path
import json,hashlib,datetime
from pypdf import PdfReader
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1];PROJECT=ROOT.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(n):return json.loads((ROOT/'核验'/n).read_text())
def write(p,data):p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def main():
    now=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat(timespec='seconds')
    doc=read('document-results.json');phy=read('physics-results.json');reb=read('rebuild-results.json')
    nat=read('native-compile-results.json');comparison=read('visual-pagination-comparison.json')
    assert phy['all_passed'] and phy['check_count']==32 and reb['all_passed']
    assert len(doc['structure'])==8 and len(doc['figures'])==18 and doc['core_identical']
    assert phy['script_sha256']==sha(ROOT/'scripts/verify_physics.py')
    for p in (ROOT/'drafts').glob('*.md'):assert phy['source_sha256'][p.name]==sha(p)
    for row in doc['pdfs']:
        p=ROOT/'output'/row['name'];assert sha(p)==row['sha256']
        assert p.read_bytes()==(ROOT/'build'/p.name).read_bytes()
        assert not row['short_body_pdf_pages']
    for row in nat:
        assert row['kind']=='success';row['source_sha256']=sha(Path(row['path']))
    write(ROOT/'核验/native-compile-results.json',nat)
    source=json.loads((ROOT/'sources/原始资料清单.json').read_text())
    for row in source:
        p=Path(row['path']);assert sha(p)==row['sha256'] and len(PdfReader(p).pages)==row['pages']
    assert comparison['same_page_count'] and comparison['changed_pdf_pages']==[46,47,71,72]
    teacher=next(x for x in doc['pdfs'] if '教师' in x['name'])
    assert comparison['current_pdf_sha256']==teacher['sha256']
    # Human review: all 24 contact sheets, all 18 diagrams; the final four
    # changed teacher pages were re-read at full size after pagination edits.
    review={'all_passed':True,'reviewed_at':now,'full_document_review':True,
       'total_pdf_pages_reviewed':sum(x['pages'] for x in doc['pdfs']),'figure_count_reviewed':18,
       'method':'三版全部页面总览审读，代表页单页放大；最后教师版四页分页改动后逐页重读，其余68页经逐页像素比较确认未改变。',
       'pdfs':[{'name':x['name'],'sha256':x['sha256'],'pages':x['pages'],
                'overview_coverage_pdf_pages':list(range(1,x['pages']+1)),
                'contact_sheet_starts':list(range(1,x['pages']+1,6))} for x in doc['pdfs']],
       'single_page_reviews':{'学生详解版':[27,55],'教师备课版':[38,46,47,71,72],'试题版':[5]},
       'final_diagram_reviews':['q2-piston','q2-potential','q7-atmosphere'],
       'findings':['未见公式裁切、缺字或图文遮挡。','题末保留自然留白，不通过改变字号或行距凑页。','最后两道短变式整段排版，消除页首孤立的一行。'],
       'unresolved_visual_issues':[]}
    write(ROOT/'核验/visual-review.json',review)
    # Refresh figure overviews to the current reviewed image versions.
    figs=sorted((ROOT/'figures').glob('*.png'))
    for first in range(0,len(figs),4):
        sheet=Image.new('RGB',(1500,1250),'#eeeeee');draw=ImageDraw.Draw(sheet)
        for j,p in enumerate(figs[first:first+4]):
            im=Image.open(p).convert('RGB');im.thumbnail((710,550));x=j%2*750;y=j//2*625
            sheet.paste(im,(x+(750-im.width)//2,y+55+(550-im.height)//2));draw.text((x+20,y+15),p.stem,fill='black')
        sheet.save(ROOT/'preview'/f'figures-{first+1:02d}.jpg',quality=94)
    intro=['# 第40届复赛理论试题整理工程','',
      '第40届（2023年）全部8题、320分。沿用已确认的“质心模拟题”流程：试题版、学生详解版、教师备课版共用逐题主稿。原始23页试题与参考解答保留在上一级目录。','',
      '| 版本 | 总页数 | 正文页数 | 成品与源稿 |','| --- | --- | --- | --- |']
    for v in ['试题版','学生详解版','教师备课版']:
        x=next(x for x in doc['pdfs'] if x['name']==f'第40届_{v}.pdf')
        intro.append(f'| {v} | {x["pages"]} | {x["body_pages"]} | [PDF]({ROOT}/output/第40届_{v}.pdf) · [Markdown]({ROOT}/output/第40届_{v}.md) · [LaTeX]({ROOT}/latex/第40届_{v}.tex) |')
    intro+=['','每版另含1页简洁封面；学生正文56页、教师正文71页，达到第101套标准。固定A4、12pt、四边22mm、1.24倍行距、0.35em段间距；无页眉，页脚保留页码。','',
      '学生版每题包含完整题面与五模块：题型定位、知识点、物理图像、解题入口、解析。教师版完整包含同一学生核心，再加关键洞察、易错点、课堂讲解建议、变式训练，共九模块。每题4道完整解答变式，共32道。18幅可编辑TikZ图用于题面和推导。','',
      '参考解答中的康普顿位移符号错误已更正；中央不稳定活塞的静止初值、偶极子径向分支、理想导体初始条件和声学近似另作说明。见[原卷与答案核对]('+str(ROOT/'核验/原卷与答案核对.md')+')。','',
      '## 编辑与重建','',
      '内容主稿为drafts/question-01.md至question-08.md，图定义位于scripts/make_figures.py。三份正式LaTeX都内嵌TikZ，无需附带图像文件，可在内置编辑器独立编译。长期修改应同步回主稿，随后构建会重写生成的LaTeX。','',
      '现有本机工具为Pandoc、XeLaTeX、qpdf和pdftotext。文档构建使用Codex捆绑Python的pypdf、pypdfium2、Pillow；计算核验使用现有Homebrew Python中的NumPy、SciPy、SymPy，未安装额外运行时。','',
      '在本目录执行：','',
      '    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/build_all.py',
      '    /opt/homebrew/bin/python3 scripts/verify_physics.py',
      '    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/quality_check.py',
      '    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/check_rebuild.py','',
      '已有图未改变时可用--skip-figures；单版内容或分页修改可同时指定--edition 教师备课版等。独立重建默认从主稿、图定义与模板重新生成全部三版，不使用当前build中的产物。','',
      '## 核验入口','',
      '- [验收报告]('+str(ROOT/'核验/验收报告.md')+')：计算、结构、编译、138页页面审读和独立重建。',
      '- physics-results.json绑定32项检查、当前题稿和检查脚本。',
      '- document-results.json绑定三版PDF、模块结构、配图和页数。',
      '- native-compile-results.json保存三版内置编译器结果。',
      '- rebuild-results.json保存逐页文字、渲染和TeX一致性。',
      '- visual-review.json和visual-pagination-comparison.json保存审读范围及末次分页比较。',
      '- CHECKPOINT.json及SHA256清单.json保存当前交付状态与校验值。']
    (ROOT/'README.md').write_text('\n'.join(intro)+'\n')
    report=['# 第40届整理版验收报告','',f'完成时间：{now}。范围：第40届全部8道原题及32道教师变式。','',
      '| 版本 | 总页数 | 正文页数 |','| --- | --- | --- |']
    for x in doc['pdfs']:report.append(f'| {x["name"]} | {x["pages"]} | {x["body_pages"]} |')
    report+=['','学生正文56页、教师正文71页；各版有1页封面。18幅TikZ图，8份逐题主稿，三版Markdown、LaTeX及PDF均保存。五／九模块和变式顺序通过检查，学生与教师核心一致。','',
      '## 物理与原卷核验','',
      '已查看原卷全部5页和参考解答全部18页，核对条件、分问、方向与题图。第8题康普顿位移的加号由守恒方程独立求出，原PDF中的减号已记入更正记录。其余适用条件、舍入差异与编号问题见[原卷与答案核对]('+str(ROOT/'核验/原卷与答案核对.md')+')。','',
      '32项独立计算检查全部通过。主要采用完整地面系受力方程、全部桥梁平衡方程、Cartesian电偶极子场的运动积分、面电流及毕奥—萨伐尔积分、气体联合微分方程，以及不预设波长位移的相对论能量动量求解。','',
      '| 检查 | 结果 |','| --- | --- |']
    for x in phy['checks']:report.append(f'| {x["check"]} | 通过 |')
    report+=['','检查覆盖原题核心、关键分支及代表性变式；并非32道变式各有一份独立数值测试。所有变式均保留完整解答与适用条件。','',
      '## 文档与页面验收','',
      '三版PDF通过qpdf完整性检查；正式输出与本次build中的PDF逐字节一致。XeLaTeX日志没有Missing character或Overfull，三份自包含LaTeX均通过内置编译器。','',
      '全部138页和18幅图已实际审读。总览覆盖每一页，长公式、接触力矩、康普顿位移及短变式另做单页放大检查。末次只调整教师PDF第46、47、71、72页的整段分页，四页均重读，其余68页经逐页像素比较确认与前次审读版本一致。学生与试题PDF未改变。题末自然留白保留，没有用字号、行距或空段补页。','',
      '## 独立重建','',
      '将主稿、脚本、图定义和模板复制到独立临时目录重新生成全部图与三版PDF。生成TeX、逐页提取文字与逐页渲染图像均一致。重建使用同一本机工具环境；PDF时间等元数据不作为内容一致性的判据。','',
      '## 当前成品校验值','',
      '| PDF | SHA-256 |','| --- | --- |']
    for x in doc['pdfs']:report.append(f'| {x["name"]} | {x["sha256"]} |')
    report+=['','第40届交付已完成。其他届次的进度另见项目接管记录，本报告不重新认证第41-43届既有工程。']
    (ROOT/'核验/验收报告.md').write_text('\n'.join(report)+'\n')
    cp={'status':'已完成','stage':'第40届交付验收完成','completed_at':now,'exam':40,'questions':8,
        'completed_questions':list(range(1,9)),'total_points':320,'variants':32,'figures':18,'pdfs':doc['pdfs'],
        'checks':{'physics':True,'structure':True,'native_compile':True,'visual_review':True,'isolated_rebuild':True},
        'source_files':source,'pending_items':[]}
    write(ROOT/'CHECKPOINT.json',cp)
    parent=PROJECT/'README.md';t=parent.read_text()
    line=('\n第40届已完成教学整理：[试题版（9页）]('+str(ROOT/'output/第40届_试题版.pdf')+')、'
       '[学生详解版（57页）]('+str(ROOT/'output/第40届_学生详解版.pdf')+')、'
       '[教师备课版（72页）]('+str(ROOT/'output/第40届_教师备课版.pdf')+')。学生正文56页、教师正文71页；'
       '简洁封面、无页眉，18幅TikZ图、32道完整解答变式，32项独立检查和独立重建通过。'
       '[工程与验收入口]('+str(ROOT/'README.md')+')。\n')
    if '第40届已完成教学整理' not in t:parent.write_text(t.rstrip()+'\n'+line)
    (PROJECT/'接管记录.md').write_text(
      '# 复赛试卷接管记录\n\n'
      f'更新：{now}。\n\n'
      '原对话ID：01a12a75-8836-7c43-92a5-930bb93aee53；多次出现模型响应流中断。当前对话“复赛试卷（接管）”承接同一项目目录。\n\n'
      '## 继续执行的人工要求\n\n'
      '- 每届试题版、学生详解版、教师备课版共用一套主稿；完整题面及分问。\n'
      '- 学生五模块；教师九模块，每题四道完整解答变式。\n'
      '- 学生至少56页正文，教师至少71页正文；封面另计。\n'
      '- A4、12pt、22mm页边距、1.24倍行距；简洁封面，无页眉。\n'
      '- TikZ题图和必要解答图，独立计算、整本PDF审读与重建核验。\n'
      '- 保存逐题检查点；未决事项与完成状态分开。\n\n'
      '## 当前进度\n\n'
      '第35-43届原始资料已收齐。第41-43届既有工程的检查点均记为完成，成品保留；本次未重做其全部验收。\n\n'
      '本次已完成第40届8题：试题版9页、学生版57页（正文56）、教师版72页（正文71）；18图、32变式。32项计算检查、三版内置编译、138页审读和独立重建通过。\n\n'
      '下一届为第39届；原始资料在第39届目录，教学整理尚未开始。继续时先读学习笔记和第40届工程说明，按每届实际题数处理。\n')
    paths=[ROOT/'README.md',ROOT/'CHECKPOINT.json']
    for d in ['drafts','scripts','latex','output','figures','sources','核验']:
        paths.extend(p for p in (ROOT/d).rglob('*') if p.is_file() and p.suffix in {'.md','.tex','.tikz','.pdf','.png','.jpg','.py','.json','.txt','.log'})
    paths.extend(Path(x['path']) for x in source)
    entries=[]
    for p in sorted(set(paths)):
        try:rel=str(p.relative_to(ROOT))
        except ValueError:rel=str(p)
        entries.append({'path':rel,'bytes':p.stat().st_size,'sha256':sha(p)})
    write(ROOT/'SHA256清单.json',{'created_at':now,'scope':'本届原始资料、主稿、图稿、脚本、三版成品、源文件及核验记录；不含本清单自身、build中间文件、preview与可变化的项目总目录。','files':entries})
    for row in entries:
        p=Path(row['path']);p=p if p.is_absolute() else ROOT/p;assert sha(p)==row['sha256']
    print(json.dumps({'status':'已完成','pages':{x['name']:x['pages'] for x in doc['pdfs']},
       'checks':32,'figures':18,'variants':32,'manifest_files':len(entries)},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
