# 第43届复赛理论试题整理工程

<!-- collection-audit-2026-10-13 -->
2026-10-13 总审核完成：10 处文字润色，26 项计算检查、三版内置编译与独立重建通过。当前成品和完整记录见[总审核报告](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/总审核/2026-10-13/审核报告.md)。
<!-- /collection-audit-2026-10-13 -->

7道题、总分320分，已按“质心模拟题”项目的方法完成三版整理。原卷及参考解答保留在上一级目录；本目录保存教学整理稿、逐题主稿、配图及核验记录。

| 版本 | 页数（含1页封面） | 文件 |
| --- | --- | --- |
| 试题版 | 8页 | [PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第43届/整理版/output/第43届_试题版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第43届/整理版/output/第43届_试题版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第43届/整理版/latex/第43届_试题版.tex) |
| 学生详解版 | 60页 | [PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第43届/整理版/output/第43届_学生详解版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第43届/整理版/output/第43届_学生详解版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第43届/整理版/latex/第43届_学生详解版.tex) |
| 教师备课版 | 74页 | [PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第43届/整理版/output/第43届_教师备课版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第43届/整理版/output/第43届_教师备课版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第43届/整理版/latex/第43届_教师备课版.tex) |

学生版每题包括题型定位、知识点、物理图像、解题入口和逐步解析。教师版保留同一核心内容，并增加关键洞察、易错点、课堂讲解建议、变式训练；每题4道带完整解答的变式，共28道。16张TikZ配图用于题面及推导。

按用户要求，第43届采用第101套的正文页数标准：学生至少56页、教师至少71页，封面另计。当前学生正文59页、教师正文73页，均达标。通过补充独立推导、替代解法及近似适用条件增加内容；A4、12pt、22mm页边距、1.24倍行距保持一致。封面仅保留试卷名称与版本名称，正文没有页眉，页脚保留页码。详见[页数与版式修订说明](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第43届/整理版/核验/页数与版式修订说明.md)。

第4题原卷的参考系表述存在冲突，解析分别给出平动参考系和旋转参考系中的力，并说明两者的力矩关系。其余排印、符号、舍入及近似适用条件的处理见[原卷与答案核对](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第43届/整理版/核验/原卷与答案核对.md)。

## 编辑与重建

内容主稿为 drafts/question-01.md 至 question-07.md；配图定义在 scripts/make_figures.py，生成的图源位于 figures。scripts/build_all.py 从逐题主稿提取三版内容，调用Pandoc和XeLaTeX生成成品。正式三份LaTeX均已内嵌TikZ图，可直接在Codex内置LaTeX编辑器中打开、修改和预览。

继续长期维护时应修改逐题主稿或配图定义，再运行构建，避免随后构建覆盖对生成文件的单独修改。完整重建命令（在本目录执行）：

    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/build_all.py

计算、结构／PDF检查、独立目录重建：

    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/verify_physics.py
    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/verify_enrichment.py
    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/quality_check.py
    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/check_rebuild.py

当前环境已有Pandoc、XeLaTeX、qpdf、pdftotext及Python所需的numpy、pypdf、pypdfium2、Pillow。独立重建使用同一工具环境，但不依赖当前构建目录中的中间文件。

## 核验与文件索引

- [验收报告](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第43届/整理版/核验/验收报告.md)：交付范围、26项独立计算、结构、编译、页面审读和重建结果。
- 核验/physics-results.json、enrichment-results.json、document-results.json、native-compile-results.json、rebuild-results.json：机器检查证据。
- 核验/visual-review.json：页面审读范围及当前PDF校验值。
- SHA256清单.json：原始资料、主稿、图源、脚本、成品和核验文件的交付校验值。
- preview：全部PDF页面及总览图；build：编译日志与中间产物。
- 历史版本：页数修订前的首次交付工程压缩包及对应旧编译记录。
- [流程学习笔记](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/质心模拟题处理流程_学习笔记.md)：所学“质心模拟题”处理方法及依据。
