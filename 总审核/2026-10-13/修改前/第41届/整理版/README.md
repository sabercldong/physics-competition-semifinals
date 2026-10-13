# 第41届复赛理论试题整理工程

第41届（2024年）全部7题、320分，沿用“质心模拟题”项目流程完成三版。原始5页试题和19页参考解答保留在上一级目录。

| 版本 | 总页数 | 正文页数 | 文件 |
| --- | --- | --- | --- |
| 试题版 | 9 | 8 | [PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第41届/整理版/output/第41届_试题版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第41届/整理版/output/第41届_试题版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第41届/整理版/latex/第41届_试题版.tex) |
| 学生详解版 | 62 | 61 | [PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第41届/整理版/output/第41届_学生详解版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第41届/整理版/output/第41届_学生详解版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第41届/整理版/latex/第41届_学生详解版.tex) |
| 教师备课版 | 74 | 73 | [PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第41届/整理版/output/第41届_教师备课版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第41届/整理版/output/第41届_教师备课版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第41届/整理版/latex/第41届_教师备课版.tex) |

学生正文61页、教师正文73页，达到第101套至少56／71页正文标准。各版另含1页简洁封面，无页眉；正文页脚保留页码。A4、12pt、22mm页边距、1.24倍行距固定。

学生每题五模块：题型定位、知识点、物理图像、解题入口、解析。教师保留完全一致的核心，再加关键洞察、易错点、课堂讲解建议、变式训练，共九模块。每题4道完整解答变式，共28道；有17张可编辑TikZ图。试题版不含解析和答案图。

注水原系数计算与参考答案中途舍入、电子能量指数笔误、量子估算适用条件和环态奇偶规则见[原卷与答案核对](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第41届/整理版/核验/原卷与答案核对.md)。

## 编辑与重建

长期维护以drafts/question-01.md至question-07.md为主稿，图定义在scripts/make_figures.py。三份LaTeX均内嵌TikZ并自包含，可在内置编辑器单独编译。直接编辑生成的TeX后，后续从主稿构建会重写它；正式修改宜同步回主稿。

在本目录执行：

    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/build_all.py
    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/verify_physics.py
    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/quality_check.py
    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/check_rebuild.py

构建使用已有Pandoc和XeLaTeX，不安装运行时。依赖numpy、pypdf、pypdfium2、Pillow与qpdf、pdftotext。独立目录重建从主稿、脚本、模板重新生成全部图和三版PDF，不使用当前build中间文件。

## 核验入口

- [验收报告](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第41届/整理版/核验/验收报告.md)：当前52项计算检查、三版编译、145页审读和独立重建。
- [页数与版式说明](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第41届/整理版/核验/页数与版式说明.md)：正文标准、真实推导内容与分页。
- 核验目录保存physics-results.json、document-results.json、native-compile-results.json、rebuild-results.json、visual-review.json。
- sources保存原始页渲染与解答文本，figures保存TikZ、独立TeX、矢量PDF和PNG；preview保存所有页面及总览，build保存日志。
- SHA256清单.json绑定原始资料、主稿、图源、脚本、成品和核验证据；CHECKPOINT.json记录完成状态。

流程依据见[学习笔记](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/质心模拟题处理流程_学习笔记.md)。
