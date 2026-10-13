#!/usr/bin/env python3
"""Bind actual review/compile/rebuild evidence and register the completed last collected paper."""
from pathlib import Path
import hashlib,json,datetime,re
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(n):return json.loads((ROOT/"核验"/n).read_text())
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+"\n")
def main():
    now=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat(timespec="seconds")
    doc=read("document-results.json");phys=read("physics-results.json")
    native=read("native-compile-results.json");review=read("visual-review.json")
    rebuild=read("rebuild-results.json")
    assert phys["all_passed"] and phys["check_count"]==64 and rebuild["all_passed"]
    assert len(doc["structure"])==8 and len(doc["figures"])==25 and doc["core_identical"]
    assert len(doc["measurement_photos"])==2 and all(p["original_bytes_preserved"] for p in doc["measurement_photos"])
    assert phys["script_sha256"]==sha(ROOT/"scripts/verify_physics.py")
    drafts=sorted((ROOT/"drafts").glob("question-*.md"))
    refs=set()
    for p in drafts:
        assert phys["source_sha256"][p.name]==sha(p)
        refs.update(Path(n).stem for n in re.findall(r"!\[[^\]]+\]\(([^)]+)\)",p.read_text()))
    assert refs=={Path(f["name"]).stem for f in doc["figures"]}
    assert len(native)==3
    for r in native:assert r["kind"]=="success" and r["source_sha256"]==sha(Path(r["path"]))
    originals=json.loads((ROOT/"sources/原始资料清单.json").read_text())
    for r in originals:assert sha(Path(r["path"]))==r["sha256"] and len(PdfReader(r["path"]).pages)==r["pages"]
    assert review["all_passed"] and review["figure_count_reviewed"]==25 and not review["unresolved_visual_issues"]
    reviewed={r["name"]:r for r in review["pdfs"]}
    for r in doc["pdfs"]:
        p=ROOT/"output"/r["name"];v=reviewed[r["name"]]
        assert sha(p)==r["sha256"]==v["sha256"] and p.read_bytes()==(ROOT/"build"/p.name).read_bytes()
        assert not r["short_body_pdf_pages"]
        assert v["overview_coverage_pdf_pages"]==list(range(1,r["pages"]+1))
    total=sum(r["pages"] for r in doc["pdfs"])
    assert review["total_pdf_pages_reviewed"]==total
    rows={r["name"].split("_")[1].split(".")[0]:r for r in doc["pdfs"]}
    assert rows["学生详解版"]["body_pages"]>=56 and rows["教师备课版"]["body_pages"]>=71
    layout="A4、12pt、22mm页边距、1.24倍行距、0.35em段间距；无页眉，页脚页码。各含1页简洁封面。"
    table=["| 版本 | 总页数 | 正文页数 |","| --- | --- | --- |"]
    table.extend(f"| {v} | {rows[v]['pages']} | {rows[v]['body_pages']} |" for v in ["试题版","学生详解版","教师备课版"])
    paths=[]
    for v in ["试题版","学生详解版","教师备课版"]:
        stem=f"第35届_{v}"
        paths.append(f"- {v}：[PDF]({ROOT}/output/{stem}.pdf) · [Markdown]({ROOT}/output/{stem}.md) · [LaTeX]({ROOT}/latex/{stem}.tex)")
    readme=["# 第35届复赛理论试题整理工程","",
        "第35届（2018年）全部8题、320分。两份原始PDF保留在上一级目录，未改写。",
        "三版共用逐题教师主稿；学生每题五模块，教师每题九模块及4道完整解答变式，共32道。",""]+table+["",layout,""]+paths+["",
        "25幅图包含23幅可编辑TikZ示意图与2幅原始测量照片；照片、标尺和缺失阶次说明完整。",
        "第6题用完整灰体辐射度方程修正参考内球温度227K为约217K；第5题保留一般初始条件，不把旋转系角动量常数强置零。",
        f"见[原卷与答案核对]({ROOT}/核验/原卷与答案核对.md)与[验收报告]({ROOT}/核验/验收报告.md)。","",
        "主稿为drafts/question-01.md至question-08.md，图定义为scripts/make_figures.py。正式TeX各自独立、自包含：内嵌TikZ和原始JPEG流，无需外部图片文件。",
        "长期修改须同步回主稿；build_all.py会重新生成正式LaTeX。独立重建还复制sources以从原JPEG重新生成图稿。","",
        "本机使用已有Pandoc、XeLaTeX、qpdf、pdftotext；文档脚本使用Codex捆绑Python的pypdf、pypdfium2、Pillow，计算核验使用已有Homebrew Python的SymPy、NumPy、SciPy。没有安装额外运行时。","",
        "在本目录执行：","",
        "    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/build_all.py",
        "    /opt/homebrew/bin/python3 scripts/verify_physics.py",
        "    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/quality_check.py",
        "    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/check_rebuild.py","",
        f"64项独立计算、{total}页实际审读、三版内置编译和独立目录重建均通过。核验JSON与源文件和成品SHA-256绑定；preview保留逐页图像及总览。","",
        "已收集的第35—43届已有整理工程。本次完成最后待处理的第35届；第41—43届沿用既有工程，本次未重做其全部核验。当前没有已收集的下一届原卷，不自动推定为第34届。"]
    (ROOT/"README.md").write_text("\n".join(readme)+"\n")
    report=["# 第35届整理版验收报告","",f"完成时间：{now}。范围：8题、32道完整解答变式。",""]+table+["",layout,"",
        "题面、学生五模块、教师九模块、每题4变式、解答核心一致性与25幅图引用检查通过。",
        "短尾页已通过保持完整解答段落和相邻变式解决；未降低字号或增加空段补页。试题版DNA照片单列一页，属于必要的测量图页，文字较少但图面完整。","",
        "合并版原卷38页逐页查看，参考解答版23—25页另行放大查看以修复两照片及核对读数容差。两原PDF字节未变，测量照片JPEG字节与原PDF中的图像流逐一相同，并在三版PDF和TeX中逐一验证嵌入。","",
        "第6题修正：包含球壳内表面自照后，辐射阻因子为1/e+(r/R1)²(1/E−1)，得到T0=216.9062K。辐射度线性系统、两表面净流和完整吸收Markov链独立一致。第5题修正：一般旋转系角动量常数可非零，直角坐标六常数通解保留全部初始条件。","",
        "第1题两种落地时间和Newton事件相符；第2题按过零而非转向计数；第3题明确固定O及有限时间顶部条件；第4题证明最小逃逸路径并检查鞍点；第7题保留原照片、标尺和缺失阶次；第8题核反冲与线宽的比较及补偿方向一致。","",
        "| 独立检查 | 结果 |","| --- | --- |"]
    report.extend(f"| {r['check']} | 通过 |" for r in phys["checks"])
    report+=["","三版qpdf、日志缺字和Overfull检查通过。三份自包含LaTeX均通过内置编译；记录绑定当前源SHA-256，未另开编辑器或替换原第40届编辑器。",
        f"实际审读全部{total}页，6页总览覆盖每一页，关键公式和照片另作单页放大。25幅图逐一查看，轴反力标注、自由飞行转向、频率圆模方向及辐射图单位经修正后复读。","",
        "独立重建从新临时目录的主稿、脚本、模板及原JPEG开始，重新生成所有图和三版PDF。TeX、每页文字和每页渲染与交付版一致；同一工具环境中的PDF元数据不作为内容判据。","",
        "| 成品 | SHA-256 |","| --- | --- |"]
    report.extend(f"| {r['name']} | {r['sha256']} |" for r in doc["pdfs"])
    (ROOT/"核验/验收报告.md").write_text("\n".join(report)+"\n")
    cp=dict(exam=35,status="已完成",completed_at=now,questions=8,completed_questions=list(range(1,9)),
        total_points=320,variants=32,figures=25,editable_schematics=23,measurement_photos=2,
        physics_checks=64,pdfs=doc["pdfs"],source_files=originals,pending_items=[],next_exam=None,
        next_status="已收集第35—43届整理工程齐备；第41—43届为既有工程，本次不重新认证。",
        per_question=[dict(question=i,status="已完成",modules=9,variants=4,master_sha256=sha(p)) for i,p in enumerate(drafts,1)],
        checks=dict(physics=True,structure=True,native_compile=True,visual_review=True,isolated_rebuild=True))
    save(ROOT/"CHECKPOINT.json",cp)
    line=(f"第35届已完成教学整理：试题{rows['试题版']['pages']}页、学生{rows['学生详解版']['pages']}页（正文{rows['学生详解版']['body_pages']}页）、"
          f"教师{rows['教师备课版']['pages']}页（正文{rows['教师备课版']['body_pages']}页）；8题、32变式、23幅可编辑示意图及2幅原测量照片。"
          f"64项计算、{total}页审读、三版内置编译和独立重建通过。[工程与验收入口]({ROOT}/README.md)。")
    p=PROJECT/"README.md";st=p.read_text()
    if "第35届已完成教学整理" not in st:p.write_text(st.rstrip()+"\n\n"+line+"\n")
    p=PROJECT/"接管记录.md";st=p.read_text()
    st=re.sub(r"更新：.+?。",f"更新：{now}。",st,count=1)
    old="下一届为第35届；原始资料在第35届目录。继续时读学习笔记和第36届工程说明，按每届实际题数处理。"
    new=line+"\n\n已收集的第35—43届整理工程齐备。当前没有待接续的已收集原卷，不自动推定第34届。第41—43届为此前既有工程，本次接管未重新执行其全部核验。"
    assert old in st or "第35届已完成教学整理" in st
    if old in st:st=st.replace(old,new)
    p.write_text(st)
    paths=[ROOT/"README.md",ROOT/"CHECKPOINT.json"]
    for d in ["drafts","scripts","latex","output","figures","sources","核验"]:
        paths.extend(p for p in (ROOT/d).rglob("*") if p.is_file() and p.suffix in
                     {".md",".tex",".tikz",".pdf",".png",".jpg",".py",".json",".txt",".log"})
    paths.extend(Path(r["path"]) for r in originals)
    entries=[]
    for p in sorted(set(paths)):
        try:rel=str(p.relative_to(ROOT))
        except ValueError:rel=str(p)
        entries.append(dict(path=rel,bytes=p.stat().st_size,sha256=sha(p)))
    save(ROOT/"SHA256清单.json",dict(created_at=now,scope="原卷、主稿、成品、源文件、脚本、图稿及核验；不含本清单、build、preview及项目总目录",files=entries))
    for r in entries:
        p=Path(r["path"]);assert sha(p if p.is_absolute() else ROOT/p)==r["sha256"]
    print(json.dumps(dict(status="已完成",pages={v:r["pages"] for v,r in rows.items()},
        checks=64,variants=32,figures=25,reviewed_pages=total,manifest_files=len(entries)),ensure_ascii=False,indent=2))
if __name__=="__main__":main()
