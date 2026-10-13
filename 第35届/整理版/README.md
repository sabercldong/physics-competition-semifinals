# 第35届复赛理论试题整理工程

<!-- collection-audit-2026-10-13 -->
2026-10-13 总审核完成：20 处文字润色，64 项计算检查、三版内置编译与独立重建通过。当前成品和完整记录见[总审核报告](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/总审核/2026-10-13/审核报告.md)。
<!-- /collection-audit-2026-10-13 -->

第35届（2018年）全部8题、320分。两份原始PDF保留在上一级目录，未改写。
三版共用逐题教师主稿；学生每题五模块，教师每题九模块及4道完整解答变式，共32道。

| 版本 | 总页数 | 正文页数 |
| --- | --- | --- |
| 试题版 | 10 | 9 |
| 学生详解版 | 57 | 56 |
| 教师备课版 | 74 | 73 |

A4、12pt、22mm页边距、1.24倍行距、0.35em段间距；无页眉，页脚页码。各含1页简洁封面。

- 试题版：[PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第35届/整理版/output/第35届_试题版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第35届/整理版/output/第35届_试题版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第35届/整理版/latex/第35届_试题版.tex)
- 学生详解版：[PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第35届/整理版/output/第35届_学生详解版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第35届/整理版/output/第35届_学生详解版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第35届/整理版/latex/第35届_学生详解版.tex)
- 教师备课版：[PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第35届/整理版/output/第35届_教师备课版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第35届/整理版/output/第35届_教师备课版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第35届/整理版/latex/第35届_教师备课版.tex)

25幅图包含23幅可编辑TikZ示意图与2幅原始测量照片；照片、标尺和缺失阶次说明完整。
第6题用完整灰体辐射度方程修正参考内球温度227K为约217K；第5题保留一般初始条件，不把旋转系角动量常数强置零。
见[原卷与答案核对](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第35届/整理版/核验/原卷与答案核对.md)与[验收报告](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第35届/整理版/核验/验收报告.md)。

主稿为drafts/question-01.md至question-08.md，图定义为scripts/make_figures.py。正式TeX各自独立、自包含：内嵌TikZ和原始JPEG流，无需外部图片文件。
长期修改须同步回主稿；build_all.py会重新生成正式LaTeX。独立重建还复制sources以从原JPEG重新生成图稿。

本机使用已有Pandoc、XeLaTeX、qpdf、pdftotext；文档脚本使用Codex捆绑Python的pypdf、pypdfium2、Pillow，计算核验使用已有Homebrew Python的SymPy、NumPy、SciPy。没有安装额外运行时。

在本目录执行：

    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/build_all.py
    /opt/homebrew/bin/python3 scripts/verify_physics.py
    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/quality_check.py
    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/check_rebuild.py

64项独立计算、141页实际审读、三版内置编译和独立目录重建均通过。核验JSON与源文件和成品SHA-256绑定；preview保留逐页图像及总览。

已收集的第35—43届已有整理工程。第35届完成后，已对第35—43届全部重新执行计算、结构、编译、页面比对与独立重建核验，并完成文字润色。当前没有已收集的下一届原卷，不自动推定为第34届。
