# 第36届复赛理论试题整理工程

<!-- collection-audit-2026-10-13 -->
2026-10-13 总审核完成：14 处文字润色，56 项计算检查、三版内置编译与独立重建通过。当前成品和完整记录见[总审核报告](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/总审核/2026-10-13/审核报告.md)。
<!-- /collection-audit-2026-10-13 -->

第36届（2019年）全部7题、320分。原始PDF40页（试题7页、参考解答33页）保留在上一级目录。三版共用逐题教师主稿。

| 版本 | 总页数 | 正文页数 | 成品与可编辑源稿 |
| --- | --- | --- | --- |
| 试题版 | 8 | 7 | [PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第36届/整理版/output/第36届_试题版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第36届/整理版/output/第36届_试题版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第36届/整理版/latex/第36届_试题版.tex) |
| 学生详解版 | 61 | 60 | [PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第36届/整理版/output/第36届_学生详解版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第36届/整理版/output/第36届_学生详解版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第36届/整理版/latex/第36届_学生详解版.tex) |
| 教师备课版 | 78 | 77 | [PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第36届/整理版/output/第36届_教师备课版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第36届/整理版/output/第36届_教师备课版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第36届/整理版/latex/第36届_教师备课版.tex) |

各含1页简洁封面。学生正文60页、教师正文77页，满足至少56／71页标准。A4、12pt、22mm页边距、1.24倍行距、0.35em段间距；无页眉，页脚页码。

学生每题五模块：题型定位、知识点、物理图像、解题入口、解析。教师增加关键洞察、易错点、课堂讲解建议、变式训练，共九模块。每题4道完整解答变式，共28道；23幅可编辑TikZ图全部参与题面或解答。

第1题明确质心最低判据和接地限制，第2题分开碰撞与两段运动，第3题保留磁场储能，第5题区分近轴与精确光线，第6题保留速率中间精度，第7题更正电荷密度符号及密度单位。见[原卷与答案核对](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第36届/整理版/核验/原卷与答案核对.md)。

## 修改与重建

主稿为drafts/question-01.md至question-07.md，图定义为scripts/make_figures.py。三份正式LaTeX内嵌TikZ，可各自独立编译。长期修改应同步回主稿；构建会重写生成的LaTeX。

本机已有Pandoc、XeLaTeX、qpdf、pdftotext。文档脚本用Codex捆绑Python的pypdf、pypdfium2、Pillow；计算核验用现有Homebrew Python的SymPy、NumPy、SciPy。未安装额外运行时。

在本目录执行：

    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/build_all.py
    /opt/homebrew/bin/python3 scripts/verify_physics.py
    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/quality_check.py
    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/check_rebuild.py

图未修改时可用--skip-figures。重建检查从独立目录的主稿、图定义与模板开始，不复用成品。

## 核验记录

- [验收报告](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第36届/整理版/核验/验收报告.md)记录56项计算、147页审读、内置编译与独立重建。
- physics-results.json绑定7份主稿与检查脚本；document-results.json绑定模块、图稿和成品。
- native-compile-results.json保存内置编译的原始结果及源文件SHA-256。
- visual-review.json记录实际审读页码和成品校验值；preview保留逐页图像和总览。
- rebuild-results.json记录独立重建的TeX、逐页文字及逐页渲染一致性。
- CHECKPOINT.json记录逐题完成状态，SHA256清单.json记录文件校验值。
