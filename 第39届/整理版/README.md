# 第39届复赛理论试题整理工程

<!-- collection-audit-2026-10-13 -->
2026-10-13 总审核完成：15 处文字润色，36 项计算检查、三版内置编译与独立重建通过。当前成品和完整记录见[总审核报告](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/总审核/2026-10-13/审核报告.md)。
<!-- /collection-audit-2026-10-13 -->

第39届（2022年）全部7题、320分。原始PDF29页（试题4页、参考解答25页）保留在上一级目录。三版共用逐题教师主稿，题面与解答核心一致。

| 版本 | 总页数 | 正文页数 | 成品与可编辑源稿 |
| --- | --- | --- | --- |
| 试题版 | 8 | 7 | [PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第39届/整理版/output/第39届_试题版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第39届/整理版/output/第39届_试题版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第39届/整理版/latex/第39届_试题版.tex) |
| 学生详解版 | 58 | 57 | [PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第39届/整理版/output/第39届_学生详解版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第39届/整理版/output/第39届_学生详解版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第39届/整理版/latex/第39届_学生详解版.tex) |
| 教师备课版 | 73 | 72 | [PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第39届/整理版/output/第39届_教师备课版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第39届/整理版/output/第39届_教师备课版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第39届/整理版/latex/第39届_教师备课版.tex) |

各含1页简洁封面。学生正文57页、教师正文72页，满足至少56／71页标准。A4、12pt、22mm页边距、1.24倍行距、0.35em段间距；无页眉，页脚页码。

学生每题五模块：题型定位、知识点、物理图像、解题入口、解析。教师增加关键洞察、易错点、课堂讲解建议、变式训练，共九模块。每题4道完整解答变式，共28道；18幅可编辑TikZ图用于题面或推导。

恒流弹簧的临界稳定性、粗糙弹性碰撞的接触模型、转动系能量与力矩等效、断裂判据的严格边界、温度积分常数及Seebeck量纲另作说明。见[原卷与答案核对](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第39届/整理版/核验/原卷与答案核对.md)。

## 修改与重建

主稿为drafts/question-01.md至question-07.md。图定义在scripts/make_figures.py。三份正式LaTeX内嵌TikZ，为可独立编译的单文件。生成文件的长期修改应同步回主稿，再运行构建；构建会重写生成的LaTeX。

本机已有Pandoc、XeLaTeX、qpdf、pdftotext。文档工作使用Codex捆绑Python的pypdf、pypdfium2、Pillow；物理核验使用现有Homebrew Python的SymPy、NumPy、SciPy。未安装额外运行时。

在本目录执行：

    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/build_all.py
    /opt/homebrew/bin/python3 scripts/verify_physics.py
    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/quality_check.py
    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/check_rebuild.py

图未修改时可用--skip-figures；仅一版修改可用--edition。独立重建从主稿、图定义与模板开始，不复用当前PDF。

## 核验记录

- [验收报告](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第39届/整理版/核验/验收报告.md)记录36项计算、139页审读、三版内置编译及独立重建。
- physics-results.json绑定当前7份主稿和检查脚本；document-results.json绑定模块、图、页数和PDF。
- native-compile-results.json保存内置编译器结果和源文件校验值。
- visual-review.json保存实际审读范围；preview保留逐页图像、页面总览和图稿总览。
- rebuild-results.json保存独立目录生成的TeX、逐页文字、逐页渲染一致性。
- CHECKPOINT.json和SHA256清单.json保存完成状态与文件校验值。
