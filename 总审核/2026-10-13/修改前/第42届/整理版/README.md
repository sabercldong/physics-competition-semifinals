# 第42届复赛理论试题整理工程

第42届（2025年）全部7题、320分，按“质心模拟题”项目流程完成三版整理。原卷与参考解答保留在上一级目录。

| 版本 | 总页数 | 正文页数 | 文件 |
| --- | --- | --- | --- |
| 试题版 | 10 | 9 | [PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第42届/整理版/output/第42届_试题版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第42届/整理版/output/第42届_试题版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第42届/整理版/latex/第42届_试题版.tex) |
| 学生详解版 | 59 | 58 | [PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第42届/整理版/output/第42届_学生详解版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第42届/整理版/output/第42届_学生详解版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第42届/整理版/latex/第42届_学生详解版.tex) |
| 教师备课版 | 73 | 72 | [PDF](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第42届/整理版/output/第42届_教师备课版.pdf) · [Markdown](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第42届/整理版/output/第42届_教师备课版.md) · [LaTeX](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第42届/整理版/latex/第42届_教师备课版.tex) |

各版含1页封面。学生正文58页、教师正文72页，达到第101套至少56／71页正文的要求。A4、12pt、22mm页边距、1.24倍行距保持固定；封面仅留名称与版本，正文无页眉，页脚保留页码。

学生每题含完整题面、题型定位、知识点、物理图像、解题入口、解析五个模块。教师保留同一核心，再增加关键洞察、易错点、课堂讲解建议、变式训练，共九个模块；每题4道带完整解答的变式，共28道。全工程有21张可编辑TikZ图。

第1题严格向下单向通量与参考答案净通量的积分域区别已明确说明。符号、接线、临界条件、数值舍入及模型范围详见[原卷与答案核对](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第42届/整理版/核验/原卷与答案核对.md)。

## 编辑与重建

长期维护以drafts/question-01.md至question-07.md为主稿，图定义位于scripts/make_figures.py。生成的三份LaTeX均内嵌TikZ，自包含，可用Codex内置LaTeX编辑器打开修改和预览。直接改生成文件可临时编辑，但后续构建会重新从主稿生成。

在本目录执行：

    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/build_all.py
    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/verify_physics.py
    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/quality_check.py
    /Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/check_rebuild.py

构建使用本机已有Pandoc、XeLaTeX；检查使用qpdf、pdftotext与Python的numpy、pypdf、pypdfium2、Pillow。独立目录从主稿、脚本、模板重新生成全部图与PDF，不使用当前构建中间文件。

## 核验与索引

- [验收报告](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第42届/整理版/核验/验收报告.md)：原卷、30项独立数值检查、分版、编译、整本页面审读及重建结果。
- [页数与版式说明](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/第42届/整理版/核验/页数与版式说明.md)：内容补充、正文标准及分页处理。
- 核验/physics-results.json、document-results.json、native-compile-results.json、rebuild-results.json、visual-review.json保存当前成品证据。
- SHA256清单.json包含原始资料、主稿、图源、构建脚本、成品与核验记录的校验值。
- preview保存所有PDF页面和总览图；build保存编译日志及中间文件；CHECKPOINT.json保存完成状态。

方法依据见[流程学习笔记](/Users/dongxingxi/Documents/ChatGPT/复赛试卷/质心模拟题处理流程_学习笔记.md)。
