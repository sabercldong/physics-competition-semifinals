# 第38届复赛理论试题整理工程

第38届（2021年）全部8题、320分。原始PDF20页（试题4页、参考解答16页）保留在上一级目录。三版共用逐题教师主稿。

| 版本 | 总页数 | 正文页数 | 成品与可编辑源稿 |
| --- | --- | --- | --- |
| 试题版 | 9 | 8 | [PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第38届/整理版/output/第38届_试题版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第38届/整理版/output/第38届_试题版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第38届/整理版/latex/第38届_试题版.tex) |
| 学生详解版 | 62 | 61 | [PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第38届/整理版/output/第38届_学生详解版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第38届/整理版/output/第38届_学生详解版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第38届/整理版/latex/第38届_学生详解版.tex) |
| 教师备课版 | 75 | 74 | [PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第38届/整理版/output/第38届_教师备课版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第38届/整理版/output/第38届_教师备课版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第38届/整理版/latex/第38届_教师备课版.tex) |

各含1页简洁封面。学生正文61页、教师正文74页，满足至少56／71页标准。A4、12pt、22mm页边距、1.24倍行距、0.35em段间距；无页眉，页脚页码。

学生每题五模块：题型定位、知识点、物理图像、解题入口、解析。教师增加关键洞察、易错点、课堂讲解建议、变式训练，共九模块。每题4道完整解答变式，共32道；22幅可编辑TikZ图全部参与题面或解答。

第7题保留完整车载驱动的反作用力矩，同时列出参考解答省略该项的约定及相应数字。第4题统一角力矩与势能导数的方向，第8题保持未舍入中间值以解释17%／18%的差异。见[原卷与答案核对](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第38届/整理版/核验/原卷与答案核对.md)。

## 修改与重建

主稿为drafts/question-01.md至question-08.md，图定义为scripts/make_figures.py。三份正式LaTeX内嵌TikZ，可各自独立编译。长期修改应同步回主稿；构建会重写生成的LaTeX。

本机已有Pandoc、XeLaTeX、qpdf、pdftotext。文档脚本用Codex捆绑Python的pypdf、pypdfium2、Pillow；计算核验用现有Homebrew Python的SymPy、NumPy、SciPy。未安装额外运行时。

在本目录执行：

    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/build_all.py
    /opt/homebrew/bin/python3 scripts/verify_physics.py
    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/quality_check.py
    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/check_rebuild.py

图未修改时可用--skip-figures。重建检查从独立目录的主稿、图定义与模板开始，不复用成品。

## 核验记录

- [验收报告](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第38届/整理版/核验/验收报告.md)记录48项计算、146页审读、内置编译与独立重建。
- physics-results.json绑定8份主稿与检查脚本；document-results.json绑定模块、图稿和成品。
- native-compile-results.json保存内置编译的原始结果及源文件SHA-256。
- visual-review.json记录实际审读页码和成品校验值；preview保留逐页图像和总览。
- rebuild-results.json记录独立重建的TeX、逐页文字及逐页渲染一致性。
- CHECKPOINT.json记录逐题完成状态，SHA256清单.json记录文件校验值。
