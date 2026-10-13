#!/usr/bin/env python3
"""Verify bound evidence and register the three completed editions."""
from pathlib import Path
import datetime, hashlib, json, re
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT.parents[1]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(name): return json.loads((ROOT/"核验"/name).read_text())
def save(p,value): p.write_text(json.dumps(value,ensure_ascii=False,indent=2)+"\n")

def main():
    now=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat(timespec="seconds")
    doc=read("document-results.json"); phy=read("physics-results.json")
    native=read("native-compile-results.json"); review=read("visual-review.json")
    rebuild=read("rebuild-results.json")
    assert phy["all_passed"] and phy["check_count"]==48 and rebuild["all_passed"]
    assert len(doc["structure"])==8 and len(doc["figures"])==24 and doc["core_identical"]
    assert phy["script_sha256"]==sha(ROOT/"scripts/verify_physics.py")
    drafts=sorted((ROOT/"drafts").glob("question-*.md"))
    referenced=set()
    for p in drafts:
        assert phy["source_sha256"][p.name]==sha(p)
        referenced.update(Path(s).stem for s in re.findall(r"!\[[^\]]+\]\(([^)]+)\)",p.read_text()))
    assert referenced=={Path(r["name"]).stem for r in doc["figures"]}
    assert len(native)==3
    for r in native:
        assert r["kind"]=="success" and r["source_sha256"]==sha(Path(r["path"]))
    sources=json.loads((ROOT/"sources/原始资料清单.json").read_text())
    for r in sources:
        assert sha(Path(r["path"]))==r["sha256"] and len(PdfReader(r["path"]).pages)==r["pages"]
    assert review["all_passed"] and review["figure_count_reviewed"]==24
    assert not review["unresolved_visual_issues"]
    reviewed={r["name"]:r for r in review["pdfs"]}
    for r in doc["pdfs"]:
        p=ROOT/"output"/r["name"]
        assert sha(p)==r["sha256"] and p.read_bytes()==(ROOT/"build"/p.name).read_bytes()
        assert not r["short_body_pdf_pages"]
        v=reviewed[r["name"]]
        assert v["sha256"]==r["sha256"] and v["overview_coverage_pdf_pages"]==list(range(1,r["pages"]+1))
    rows={r["name"].split("_")[1].split(".")[0]:r for r in doc["pdfs"]}
    student=rows["学生详解版"]; teacher=rows["教师备课版"]; paper=rows["试题版"]
    total=sum(r["pages"] for r in doc["pdfs"])
    assert review["total_pdf_pages_reviewed"]==total
    layout=(f"各含1页简洁封面。学生正文{student['body_pages']}页、教师正文{teacher['body_pages']}页，"
            "满足至少56／71页标准。A4、12pt、22mm页边距、1.24倍行距、0.35em段间距；无页眉，页脚页码。")
    intro=["# 第37届复赛理论试题整理工程","",
        "第37届（2020年）全部8题、320分。原始PDF21页（试题5页、参考解答16页）保留在上一级目录。三版共用逐题教师主稿。","",
        "| 版本 | 总页数 | 正文页数 | 成品与可编辑源稿 |","| --- | --- | --- | --- |"]
    for v in ["试题版","学生详解版","教师备课版"]:
        r=rows[v]; stem=f"第37届_{v}"
        intro.append(f"| {v} | {r['pages']} | {r['body_pages']} | [PDF]({ROOT}/output/{stem}.pdf) · [Markdown]({ROOT}/output/{stem}.md) · [LaTeX]({ROOT}/latex/{stem}.tex) |")
    intro+=["",layout,"",
        "学生每题五模块：题型定位、知识点、物理图像、解题入口、解析。教师增加关键洞察、易错点、课堂讲解建议、变式训练，共九模块。每题4道完整解答变式，共32道；24幅可编辑TikZ图全部参与题面或解答。","",
        "第1题区分热交换与气路流动时间尺度，第3题补上电容初始电压，第4题更正半径不等号，第6题并列参考路径替代与共旋介质腔相位闭合的频差，第7题筛选一整圈时间分支，第8题保留谐振与负载条件。"
        f"见[原卷与答案核对]({ROOT}/核验/原卷与答案核对.md)。","",
        "## 修改与重建","",
        "主稿为drafts/question-01.md至question-08.md，图定义为scripts/make_figures.py。三份正式LaTeX内嵌TikZ，可各自独立编译。长期修改应同步回主稿；构建会重写生成的LaTeX。","",
        "本机已有Pandoc、XeLaTeX、qpdf、pdftotext。文档脚本用Codex捆绑Python的pypdf、pypdfium2、Pillow；计算核验用现有Homebrew Python的SymPy、NumPy、SciPy。未安装额外运行时。","",
        "在本目录执行：","",
        "    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/build_all.py",
        "    /opt/homebrew/bin/python3 scripts/verify_physics.py",
        "    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/quality_check.py",
        "    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/check_rebuild.py","",
        "图未修改时可用--skip-figures。重建检查从独立目录的主稿、图定义与模板开始，不复用成品。","",
        "## 核验记录","",
        f"- [验收报告]({ROOT}/核验/验收报告.md)记录48项计算、{total}页审读、内置编译与独立重建。",
        "- physics-results.json绑定8份主稿与检查脚本；document-results.json绑定模块、图稿和成品。",
        "- native-compile-results.json保存内置编译的原始结果及源文件SHA-256。",
        "- visual-review.json记录实际审读页码和成品校验值；preview保留逐页图像和总览。",
        "- rebuild-results.json记录独立重建的TeX、逐页文字及逐页渲染一致性。",
        "- CHECKPOINT.json记录逐题完成状态，SHA256清单.json记录文件校验值。"]
    (ROOT/"README.md").write_text("\n".join(intro)+"\n")
    report=["# 第37届整理版验收报告","",f"完成时间：{now}。范围：全部8题、32道完整解答变式。","",
        "| 版本 | 总页数 | 正文页数 |","| --- | --- | --- |"]
    for v in ["试题版","学生详解版","教师备课版"]:
        r=rows[v]; report.append(f"| {v} | {r['pages']} | {r['body_pages']} |")
    report+=["",layout,"",
        "完整题面、学生五模块／教师九模块、每题4变式、解答核心一致性均通过检查。24幅图全部引用。","",
        "## 物理核验","",
        "原卷5页及参考解答16页均已逐页查看。原PDF正文无可用文字层，题面与公式按扫描图像核对。原PDF校验值未变。","",
        "48项独立检查覆盖气体状态求导和双室压差矩阵、台球滑动终止ODE及摩擦功、负电阻双状态电路及耗散积分、相对论磁运动和反应阈值四动量、世界线交点和异地事件变换、旋转介质速度合成与共振相位、双体缩距角运动ODE及角位移积分、Jones矩阵和电路节点功率闭合。检查项目按物理关系分组，项目数不是变式数。","",
        "第3题参考积分式遗漏电容初始常数，已补vC(0)=−Lβ；第4题半径上限不等号已更正，场值按题给常数为3.25 T。第6题共旋介质腔相位闭合给Δf≈mΩ/(πn²)，参考路径替代给mΩ/π，两者明确并列。第7题与第8题补齐有效分支、谐振调谐及负载限制。详见原卷与答案核对.md。","",
        "| 检查 | 结果 |","| --- | --- |"]
    report.extend(f"| {r['check']} | 通过 |" for r in phy["checks"])
    report+=["","## 排版与编译","",
        "三版PDF通过qpdf检查；XeLaTeX日志无缺字、无Overfull。数学式百分号转义另作源码检查；编号和单位缺字已修正。三份自包含LaTeX均通过内置编译，记录与源文件SHA-256绑定。成品与build中PDF逐字节一致。","",
        f"实际审读全部{total}页，页面总览覆盖每页，关键长公式与图文页另作单页放大。24幅图逐一查看，挤叠标注修正后复读。台球加速度与触地点论证、反质子结尾、频差相位核对及两道短变式保持整段，消除孤立末行。字号、行距、页边距固定，没有空段补页。","",
        "## 独立重建","",
        "从复制到独立临时目录的主稿、脚本与模板重新生成全部图和三版PDF。TeX、逐页文字和每页渲染均一致。此项验证基于同一已安装工具环境，PDF时间戳等元数据不作为内容判据。","",
        "## 成品SHA-256","","| 文件 | SHA-256 |","| --- | --- |"]
    report.extend(f"| {r['name']} | {r['sha256']} |" for r in doc["pdfs"])
    report+=["","第37届交付完成，下一届为第36届。本报告不重新认证此前已交付的其他届次。"]
    (ROOT/"核验/验收报告.md").write_text("\n".join(report)+"\n")
    audit=ROOT/"核验/原卷与答案核对.md"; s=audit.read_text().replace("（进行中）","（已完成）")
    s=s.replace("状态：逐题主稿、独立计算及三版成品尚待完成。",f"状态：8题、32变式、24图、48项计算、{total}页审读、三版内置编译和独立重建已完成。见验收报告.md。")
    audit.write_text(s)
    cp={"exam":37,"status":"已完成","stage":"三版交付验收完成","completed_at":now,
        "questions":8,"completed_questions":list(range(1,9)),"total_points":320,
        "variants":32,"figures":24,"physics_checks":48,"pdfs":doc["pdfs"],
        "per_question":[{"question":i,"status":"已完成","modules":9,"variants":4,
                         "master_sha256":sha(p)} for i,p in enumerate(drafts,1)],
        "checks":{"physics":True,"structure":True,"native_compile":True,"visual_review":True,"isolated_rebuild":True},
        "source_files":sources,"pending_items":[],"next_exam":36}
    save(ROOT/"CHECKPOINT.json",cp)
    line=(f"第37届已完成教学整理：[试题版（{paper['pages']}页）]({ROOT}/output/第37届_试题版.pdf)、"
          f"[学生详解版（{student['pages']}页）]({ROOT}/output/第37届_学生详解版.pdf)、"
          f"[教师备课版（{teacher['pages']}页）]({ROOT}/output/第37届_教师备课版.pdf)。"
          f"学生正文{student['body_pages']}页、教师正文{teacher['body_pages']}页；24幅TikZ图、32道完整解答变式，"
          f"48项计算、{total}页审读、内置编译和独立重建通过。[工程与验收入口]({ROOT}/README.md)。")
    p=PROJECT/"README.md";s=p.read_text()
    if "第37届已完成教学整理" not in s: p.write_text(s.rstrip()+"\n\n"+line+"\n")
    p=PROJECT/"接管记录.md";s=p.read_text()
    s=re.sub(r"更新：.+?。",f"更新：{now}。",s,count=1)
    old="下一届为第37届；原始资料在第37届目录。继续时读学习笔记和第38届工程说明，按每届实际题数处理。"
    new=(f"第37届已完成8题：试题{paper['pages']}页、学生{student['pages']}页（正文{student['body_pages']}）、"
         f"教师{teacher['pages']}页（正文{teacher['body_pages']}）；24图、32变式。48项计算检查、三版内置编译、"
         f"{total}页审读和独立重建通过。\n\n"
         "下一届为第36届；原始资料在第36届目录。继续时读学习笔记和第37届工程说明，按每届实际题数处理。")
    assert old in s or "第37届已完成8题" in s
    if old in s:s=s.replace(old,new)
    p.write_text(s)
    paths=[ROOT/"README.md",ROOT/"CHECKPOINT.json"]
    for d in ["drafts","scripts","latex","output","figures","sources","核验"]:
        paths.extend(p for p in (ROOT/d).rglob("*") if p.is_file() and p.suffix in
                     {".md",".tex",".tikz",".pdf",".png",".jpg",".py",".json",".txt",".log"})
    paths.extend(Path(r["path"]) for r in sources)
    entries=[]
    for p in sorted(set(paths)):
        try:rel=str(p.relative_to(ROOT))
        except ValueError:rel=str(p)
        entries.append({"path":rel,"bytes":p.stat().st_size,"sha256":sha(p)})
    save(ROOT/"SHA256清单.json",{"created_at":now,
         "scope":"原始资料、逐题主稿、三版成品、源文件、脚本、图稿、核验记录；不含本清单、build、preview及项目总目录。",
         "files":entries})
    for r in entries:
        p=Path(r["path"]); assert sha(p if p.is_absolute() else ROOT/p)==r["sha256"]
    print(json.dumps({"status":"已完成","pages":{v:r["pages"] for v,r in rows.items()},
                      "physics_checks":48,"variants":32,"figures":24,"reviewed_pages":total,
                      "manifest_files":len(entries)},ensure_ascii=False,indent=2))

if __name__=="__main__":main()
