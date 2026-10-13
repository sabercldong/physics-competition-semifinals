# 第40届复赛理论试题整理工程

<!-- collection-audit-2026-10-13 -->
2026-10-13 总审核完成：10 处文字润色，32 项计算检查、三版内置编译与独立重建通过。当前成品和完整记录见[总审核报告](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/总审核/2026-10-13/审核报告.md)。
<!-- /collection-audit-2026-10-13 -->

第40届（2023年）全部8题、320分。沿用已确认的“质心模拟题”流程：试题版、学生详解版、教师备课版共用逐题主稿。原始23页试题与参考解答保留在上一级目录。

| 版本 | 总页数 | 正文页数 | 成品与源稿 |
| --- | --- | --- | --- |
| 试题版 | 9 | 8 | [PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第40届/整理版/output/第40届_试题版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第40届/整理版/output/第40届_试题版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第40届/整理版/latex/第40届_试题版.tex) |
| 学生详解版 | 57 | 56 | [PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第40届/整理版/output/第40届_学生详解版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第40届/整理版/output/第40届_学生详解版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第40届/整理版/latex/第40届_学生详解版.tex) |
| 教师备课版 | 72 | 71 | [PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第40届/整理版/output/第40届_教师备课版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第40届/整理版/output/第40届_教师备课版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第40届/整理版/latex/第40届_教师备课版.tex) |

每版另含1页简洁封面；学生正文56页、教师正文71页，达到第101套标准。固定A4、12pt、四边22mm、1.24倍行距、0.35em段间距；无页眉，页脚保留页码。

学生版每题包含完整题面与五模块：题型定位、知识点、物理图像、解题入口、解析。教师版完整包含同一学生核心，再加关键洞察、易错点、课堂讲解建议、变式训练，共九模块。每题4道完整解答变式，共32道。18幅可编辑TikZ图用于题面和推导。

参考解答中的康普顿位移符号错误已更正；中央不稳定活塞的静止初值、偶极子径向分支、理想导体初始条件和声学近似另作说明。见[原卷与答案核对](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第40届/整理版/核验/原卷与答案核对.md)。

## 编辑与重建

内容主稿为drafts/question-01.md至question-08.md，图定义位于scripts/make_figures.py。三份正式LaTeX都内嵌TikZ，无需附带图像文件，可在内置编辑器独立编译。长期修改应同步回主稿，随后构建会重写生成的LaTeX。

现有本机工具为Pandoc、XeLaTeX、qpdf和pdftotext。文档构建使用Codex捆绑Python的pypdf、pypdfium2、Pillow；计算核验使用现有Homebrew Python中的NumPy、SciPy、SymPy，未安装额外运行时。

在本目录执行：

    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/build_all.py
    /opt/homebrew/bin/python3 scripts/verify_physics.py
    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/quality_check.py
    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/check_rebuild.py

已有图未改变时可用--skip-figures；单版内容或分页修改可同时指定--edition 教师备课版等。独立重建默认从主稿、图定义与模板重新生成全部三版，不使用当前build中的产物。

## 核验入口

- [验收报告](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第40届/整理版/核验/验收报告.md)：计算、结构、编译、138页页面审读和独立重建。
- physics-results.json绑定32项检查、当前题稿和检查脚本。
- document-results.json绑定三版PDF、模块结构、配图和页数。
- native-compile-results.json保存三版内置编译器结果。
- rebuild-results.json保存逐页文字、渲染和TeX一致性。
- visual-review.json和visual-pagination-comparison.json保存审读范围及末次分页比较。
- CHECKPOINT.json及SHA256清单.json保存当前交付状态与校验值。
