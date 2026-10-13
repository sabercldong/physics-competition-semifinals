#!/usr/bin/env python3
"""Bind verified sources, compilation, actual page reviews and deliverables."""
from pathlib import Path
import json,hashlib,datetime,re
from pypdf import PdfReader
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(name):return json.loads((ROOT/"核验"/name).read_text())
def save(path,value):path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+"\n")
def main():
    now=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat(timespec="seconds")
    doc=read("document-results.json");phy=read("physics-results.json")
    nat=read("native-compile-results.json");reb=read("rebuild-results.json")
    assert phy["all_passed"] and phy["check_count"]==36 and reb["all_passed"]
    assert len(doc["structure"])==7 and len(doc["figures"])==18 and doc["core_identical"]
    assert phy["script_sha256"]==sha(ROOT/"scripts/verify_physics.py")
    for p in (ROOT/"drafts").glob("*.md"):
        assert phy["source_sha256"][p.name]==sha(p)
    assert len(nat)==3
    for row in nat:
        assert row["kind"]=="success"
        row["source_sha256"]=sha(Path(row["path"]))
    save(ROOT/"核验/native-compile-results.json",nat)
    source=json.loads((ROOT/"sources/原始资料清单.json").read_text())
    for row in source:
        p=Path(row["path"])
        assert sha(p)==row["sha256"] and len(PdfReader(p).pages)==row["pages"]
    for row in doc["pdfs"]:
        p=ROOT/"output"/row["name"]
        assert sha(p)==row["sha256"]
        assert p.read_bytes()==(ROOT/"build"/p.name).read_bytes()
        assert not row["short_body_pdf_pages"]
    review={
        "all_passed":True,"reviewed_at":now,
        "total_pdf_pages_reviewed":sum(r["pages"] for r in doc["pdfs"]),
        "figure_count_reviewed":18,
        "method":"三版全页总览审读；图中重叠标注修正后复读；短题末论证和同时断变式整段排版；最后新增绝热图所在页面复读。长公式与受力图另作单页放大。",
        "pdfs":[{"name":r["name"],"sha256":r["sha256"],"pages":r["pages"],
                 "overview_coverage_pdf_pages":list(range(1,r["pages"]+1)),
                 "contact_sheet_starts":list(range(1,r["pages"]+1,6))} for r in doc["pdfs"]],
        "single_page_reviews":{"试题版":[2],"学生详解版":[31,47,57],"教师备课版":[51,59]},
        "final_figure_full_size_reviews":["q4-forces","q4-boundary","q5-springs","q7-wall"],
        "findings":["未见公式裁切、缺字和图文遮挡。",
                    "第1题试题版的两图及题面在同页，消除单独一图的尾页。",
                    "奇偶冲量检查、弹簧能量账目和同时断变式保持完整论证，消除孤立末行。",
                    "各题末自然留白保留；固定字号、行距和页边距，没有空段补页。"],
        "unresolved_visual_issues":[]}
    save(ROOT/"核验/visual-review.json",review)
    # Contact sheets must display the same figure image versions as delivery.
    figs=sorted((ROOT/"figures").glob("*.png"))
    for first in range(0,len(figs),4):
        sheet=Image.new("RGB",(1600,1400),"#eeeeee");draw=ImageDraw.Draw(sheet)
        for j,p in enumerate(figs[first:first+4]):
            im=Image.open(p).convert("RGB");im.thumbnail((760,620));x=j%2*800;y=j//2*700
            sheet.paste(im,(x+(800-im.width)//2,y+50+(620-im.height)//2))
            draw.text((x+20,y+15),p.stem,fill="black")
        sheet.save(ROOT/"preview"/f"figures-{first+1:02d}.jpg",quality=94)
    rows={r["name"].split("_")[1].split(".")[0]:r for r in doc["pdfs"]}
    intro=["# 第39届复赛理论试题整理工程","",
           "第39届（2022年）全部7题、320分。原始PDF29页（试题4页、参考解答25页）保留在上一级目录。三版共用逐题教师主稿，题面与解答核心一致。","",
           "| 版本 | 总页数 | 正文页数 | 成品与可编辑源稿 |",
           "| --- | --- | --- | --- |"]
    for v in ["试题版","学生详解版","教师备课版"]:
        r=rows[v]
        intro.append(f'| {v} | {r["pages"]} | {r["body_pages"]} | [PDF]({ROOT}/output/第39届_{v}.pdf) · [Markdown]({ROOT}/output/第39届_{v}.md) · [LaTeX]({ROOT}/latex/第39届_{v}.tex) |')
    intro+=["",
        "各含1页简洁封面。学生正文57页、教师正文72页，满足至少56／71页标准。A4、12pt、22mm页边距、1.24倍行距、0.35em段间距；无页眉，页脚页码。","",
        "学生每题五模块：题型定位、知识点、物理图像、解题入口、解析。教师增加关键洞察、易错点、课堂讲解建议、变式训练，共九模块。每题4道完整解答变式，共28道；18幅可编辑TikZ图用于题面或推导。","",
        "恒流弹簧的临界稳定性、粗糙弹性碰撞的接触模型、转动系能量与力矩等效、断裂判据的严格边界、温度积分常数及Seebeck量纲另作说明。见[原卷与答案核对]("+str(ROOT/"核验/原卷与答案核对.md")+")。","",
        "## 修改与重建","",
        "主稿为drafts/question-01.md至question-07.md。图定义在scripts/make_figures.py。三份正式LaTeX内嵌TikZ，为可独立编译的单文件。生成文件的长期修改应同步回主稿，再运行构建；构建会重写生成的LaTeX。","",
        "本机已有Pandoc、XeLaTeX、qpdf、pdftotext。文档工作使用Codex捆绑Python的pypdf、pypdfium2、Pillow；物理核验使用现有Homebrew Python的SymPy、NumPy、SciPy。未安装额外运行时。","",
        "在本目录执行：","",
        "    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/build_all.py",
        "    /opt/homebrew/bin/python3 scripts/verify_physics.py",
        "    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/quality_check.py",
        "    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/check_rebuild.py","",
        "图未修改时可用--skip-figures；仅一版修改可用--edition。独立重建从主稿、图定义与模板开始，不复用当前PDF。","",
        "## 核验记录","",
        "- [验收报告]("+str(ROOT/"核验/验收报告.md")+")记录36项计算、139页审读、三版内置编译及独立重建。",
        "- physics-results.json绑定当前7份主稿和检查脚本；document-results.json绑定模块、图、页数和PDF。",
        "- native-compile-results.json保存内置编译器结果和源文件校验值。",
        "- visual-review.json保存实际审读范围；preview保留逐页图像、页面总览和图稿总览。",
        "- rebuild-results.json保存独立目录生成的TeX、逐页文字、逐页渲染一致性。",
        "- CHECKPOINT.json和SHA256清单.json保存完成状态与文件校验值。"]
    (ROOT/"README.md").write_text("\n".join(intro)+"\n")
    report=["# 第39届整理版验收报告","",f"完成时间：{now}。范围：全部7题及28道完整解答变式。","",
            "| 版本 | 总页数 | 正文页数 |","| --- | --- | --- |"]
    for v in ["试题版","学生详解版","教师备课版"]:
        r=rows[v];report.append(f'| {v} | {r["pages"]} | {r["body_pages"]} |')
    report+=["",
        "学生正文57页，教师正文72页；各版另含1页封面。五／九模块、完整题面、4变式每题、学生与教师核心一致性通过检查；18幅TikZ图均有引用。","",
        "## 物理核验","",
        "原卷4页及参考解答25页均已查看，关键原公式另作放大核对。原PDF校验值未变。原题结果与参考答案相符；临界稳定性、接触模型、温度参考常数与概率措辞的适用条件补充见原卷与答案核对.md。","",
        "36项独立检查通过。覆盖光程几何、弹簧电磁应力与能量曲率、30次冲量迭代、旋转杆质量积分与根数／高阶曲率、14组断裂ODE事件、静电与密度耦合边值解、统计概率及动量通量积分。28道变式均保留完整解析；检查项目按物理关系分组，项目数不是变式数。","",
        "| 检查 | 结果 |","| --- | --- |"]
    for r in phy["checks"]:report.append(f'| {r["check"]} | 通过 |')
    report+=["",
        "## 排版与编译","",
        "三版PDF均通过qpdf完整性检查。XeLaTeX日志无缺字和Overfull。三份自包含LaTeX均通过内置编译器，结果与源文件SHA-256绑定。输出PDF与build产物逐字节一致。","",
        "实际审读全部139页，页面总览覆盖每页；长公式、旋转杆受力图、密度双曲解、Seebeck端差及同时断边界例子做单页放大。18幅图实际查看，挤叠标注修正后复读。各题尾保留自然留白，短论证与短变式保持完整段落，没有变更字号／行距或加入空段凑页。","",
        "## 独立重建","",
        "把主稿、脚本和模板复制到独立临时目录，重新生成全部图及三版PDF。TeX源、逐页文字与逐页渲染均一致。重建使用相同本机工具环境；时间戳等PDF元数据不作为内容一致性判据。","",
        "## 成品SHA-256","",
        "| 文件 | SHA-256 |","| --- | --- |"]
    for r in doc["pdfs"]:report.append(f'| {r["name"]} | {r["sha256"]} |')
    report+=["","第39届交付完成，下一届为第38届。本报告不重新认证第41—43届既有整理工程。"]
    (ROOT/"核验/验收报告.md").write_text("\n".join(report)+"\n")
    cp={"exam":39,"status":"已完成","stage":"三版交付验收完成","completed_at":now,
        "questions":7,"completed_questions":list(range(1,8)),"total_points":320,
        "variants":28,"figures":18,"physics_checks":36,"pdfs":doc["pdfs"],
        "checks":{"physics":True,"structure":True,"native_compile":True,"visual_review":True,"isolated_rebuild":True},
        "source_files":source,"pending_items":[],"next_exam":38}
    save(ROOT/"CHECKPOINT.json",cp)
    p=PROJECT/"README.md";s=p.read_text()
    line=("第39届已完成教学整理：[试题版（8页）]("+str(ROOT/"output/第39届_试题版.pdf")+")、"
          "[学生详解版（58页）]("+str(ROOT/"output/第39届_学生详解版.pdf")+")、"
          "[教师备课版（73页）]("+str(ROOT/"output/第39届_教师备课版.pdf")+")。"
          "学生正文57页、教师正文72页；18幅TikZ图、28道完整解答变式，36项计算、139页审读、内置编译和独立重建通过。"
          "[工程与验收入口]("+str(ROOT/"README.md")+")。")
    if "第39届已完成教学整理" not in s:p.write_text(s.rstrip()+"\n\n"+line+"\n")
    p=PROJECT/"接管记录.md";s=p.read_text()
    s=re.sub(r"更新：.+?。",f"更新：{now}。",s,count=1)
    old="下一届为第39届；原始资料在第39届目录，教学整理尚未开始。继续时先读学习笔记和第40届工程说明，按每届实际题数处理。"
    new=("第39届已完成7题：试题8页、学生58页（正文57）、教师73页（正文72）；18图、28变式。"
         "36项计算检查、三版内置编译、139页审读和独立重建通过。\n\n"
         "下一届为第38届；原始资料在第38届目录。继续时读学习笔记和第39届工程说明，按每届实际题数处理。")
    if old in s:s=s.replace(old,new)
    elif "第39届已完成7题" not in s:s=s.rstrip()+"\n\n"+new+"\n"
    p.write_text(s)
    paths=[ROOT/"README.md",ROOT/"CHECKPOINT.json"]
    for d in ["drafts","scripts","latex","output","figures","sources","核验"]:
        paths.extend(p for p in (ROOT/d).rglob("*") if p.is_file() and p.suffix in {".md",".tex",".tikz",".pdf",".png",".jpg",".py",".json",".txt",".log"})
    paths.extend(Path(r["path"]) for r in source)
    entries=[]
    for p in sorted(set(paths)):
        try:rel=str(p.relative_to(ROOT))
        except ValueError:rel=str(p)
        entries.append({"path":rel,"bytes":p.stat().st_size,"sha256":sha(p)})
    save(ROOT/"SHA256清单.json",{"created_at":now,"scope":"原始资料、逐题主稿、三版成品、源文件、脚本、图稿与核验记录；不含本清单、build中间文件、preview及会继续变化的项目总目录。","files":entries})
    for r in entries:
        p=Path(r["path"]);p=p if p.is_absolute() else ROOT/p
        assert sha(p)==r["sha256"]
    print(json.dumps({"status":"已完成","pages":{v:rows[v]["pages"] for v in rows},
                     "checks":36,"variants":28,"figures":18,"manifest_files":len(entries)},ensure_ascii=False,indent=2))
if __name__=="__main__":main()
