"""Bind the completed editorial and visual audit to the verified delivery files."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[3]
AUDIT = ROOT / '总审核/2026-10-13'
NOW = datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(timespec='seconds')


def read(path):
    return json.loads(path.read_text())


def write(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def link(label, path):
    return f'[{label}]({path})'


def insert_note(path, text):
    content = path.read_text()
    marker = '<!-- collection-audit-2026-10-13 -->'
    end = '<!-- /collection-audit-2026-10-13 -->'
    note = f'{marker}\n{text}\n{end}\n'
    if marker in content:
        content = re.sub(re.escape(marker) + r'.*?' + re.escape(end) + r'\n?', lambda _: note, content, flags=re.S)
    else:
        first, rest = content.split('\n', 1)
        content = first + '\n\n' + note + rest
    path.write_text(content)


comparison = read(AUDIT / 'page-comparison.json')
native = read(AUDIT / 'native-compile.json')
invariants = read(AUDIT / 'content-invariants.json')
edits = read(AUDIT / 'prose-edits.json')
assert len(native) == 27 and len(comparison) == 27
assert len(edits) == len(invariants['questions']) == 67
assert sum(len(e['edits']) for e in edits) == 106
assert sum(q['formulas'] for q in invariants['questions']) == 12104
assert sum(q['variants'] for q in invariants['questions']) == 268
assert invariants['all_passed']
for q in invariants['questions']:
    assert sha(ROOT / q['path']) == q['sha256'], q['path']
for source in invariants['original_files']:
    assert source['unchanged'] and sha(Path(source['path'])) == source['sha256']
for item in native:
    assert item['kind'] == 'success'
    assert sha(Path(item['path'])) == item['source_sha256']
for item in comparison:
    assert sha(Path(item['path'])) == item['sha256']
    assert sorted(item['changed_pages'] + item['unchanged_pages']) == list(range(1, item['pages'] + 1))
    if '试题版' in item['name']:
        assert not item['changed_pages']
assert all(s['exit'] == 0 for exam in read(AUDIT / 'checks.json') for s in exam['steps'])
assert all(s['exit'] == 0 for s in read(AUDIT / 'rebuild-run.json'))

# These are actual single-page visual inspections, supplementary to all 32 contact sheets.
single_pages = {
    35: ('教师备课版', 64), 36: ('学生详解版', 27), 37: ('教师备课版', 29),
    38: ('教师备课版', 35), 39: ('学生详解版', 3), 40: ('学生详解版', 2),
    41: ('学生详解版', 40), 42: ('教师备课版', 32), 43: ('学生详解版', 4),
}
rows, all_figures, all_visuals = [], [], []
for n in range(35, 44):
    base = ROOT / f'第{n}届/整理版'
    old = AUDIT / '修改前' / f'第{n}届/整理版'
    doc = read(base / '核验/document-results.json')
    baseline_doc = read(old / '核验/document-results.json')
    physics = read(base / '核验/physics-results.json')
    rebuild = read(base / '核验/rebuild-results.json')
    assert physics['all_passed'] and all(x['passed'] for x in physics['checks'])
    assert rebuild['all_passed'] and len(rebuild['results']) == 3
    assert all(x['TeX_identical'] and x['page_text_identical'] and x['every_page_render_identical'] for x in rebuild['results'])
    assert doc['core_identical'] and all(x['modules'] == 9 and x['variants'] == 4 for x in doc['structure'])
    for pdf in doc['pdfs']:
        assert pdf['sha256'] == sha(base / 'output' / pdf['name'])
        assert pdf['qpdf'] == 'passed' and pdf['missing_glyphs'] == pdf['overfull_boxes'] == 0
        assert not pdf['short_body_pdf_pages']
        if pdf['required_body_pages'] is not None:
            assert pdf['body_pages'] >= pdf['required_body_pages']
    count = len(physics['checks'])
    extra = 0
    if n == 43:
        enrich = read(base / '核验/enrichment-results.json')
        assert enrich['all_passed'] and all(x['passed'] for x in enrich['checks'])
        extra = len(enrich['checks'])
    old_fig = {f['name']: f for f in baseline_doc['figures']}
    assert len(old_fig) == len(doc['figures'])
    for f in doc['figures']:
        assert f == old_fig[f['name']], f
        assert sha(base / 'figures' / f['name']) == f['sha256']
        all_figures.append({'exam': n, **f, 'unchanged': True})
    if n == 35:
        assert doc['measurement_photos'] == baseline_doc['measurement_photos']
        assert all(p['original_bytes_preserved'] and all(e['original_JPEG_bytes_embedded'] for e in p['editions']) for p in doc['measurement_photos'])

    compiled = [r for r in native if f'/第{n}届/' in r['path']]
    assert len(compiled) == 3
    write(base / '核验/native-compile-results.json', {'all_passed': True, 'verified_at': NOW, 'results': compiled})
    pages = [p for p in comparison if p['exam'] == n]
    changed = sum(len(p['changed_pages']) for p in pages)
    unchanged = sum(len(p['unchanged_pages']) for p in pages)
    v, pno = single_pages[n]
    visual = {
        'all_passed': True, 'reviewed_at': NOW,
        'method': '本轮逐页比较全部页面；重新审看所有变化页的六页总览，每届另放大一页。逐像素相同的页面沿用修改前已有视觉审读记录。',
        'total_pdf_pages_covered': changed + unchanged,
        'changed_pdf_pages_visually_reviewed_this_pass': changed,
        'pixel_identical_pages_inheriting_prior_review': unchanged,
        'baseline_review_path': str(old / '核验/visual-review.json'),
        'baseline_review_sha256': sha(old / '核验/visual-review.json'),
        'comparison_record': str(AUDIT / 'page-comparison.json'),
        'comparison_record_sha256': sha(AUDIT / 'page-comparison.json'),
        'pdfs': [{k: p[k] for k in ['name', 'sha256', 'pages', 'baseline_sha256', 'changed_pages', 'unchanged_pages', 'contact_sheets']} for p in pages],
        'single_page_reviews': [{'name': f'第{n}届_{v}.pdf', 'pdf_page': pno,
                                 'image': str(base / 'preview' / f'第{n}届_{v}' / f'page-{pno:03}.jpg')}],
        'findings': ['变化页未见公式裁切、缺字或图文遮挡。', '页数、题号、模块、图稿及原题版页面内容保持一致。'],
        'unresolved_visual_issues': [],
    }
    write(base / '核验/visual-review.json', visual)
    all_visuals.append({'exam': n, **visual})
    n_edits = sum(len(e['edits']) for e in edits if e['exam'] == n)
    cp = read(base / 'CHECKPOINT.json')
    cp.update(status='已完成', stage=f'第{n}届完成总审核及文字润色', exam=n, pending_items=[], pdfs=doc['pdfs'])
    cp['physics_checks'] = count + extra
    if 'independent_calculation_checks' in cp:
        cp['independent_calculation_checks'] = count + extra
    cp['per_question'] = [{'question': int(q['question'].split('-')[-1]), 'status': '已完成', 'modules': q['modules'], 'variants': q['variants'], 'master_sha256': q['sha256']} for q in doc['structure']]
    cp['checks'].update(physics=True, structure=True, native_compile=True, visual_review=True, isolated_rebuild=True, originals_unchanged=True, editorial_invariants=True)
    cp['collection_audit'] = {'completed_at': NOW, 'report': str(AUDIT / '审核报告.md'),
                              'prose_edits': n_edits, 'physics_checks': count + extra,
                              'changed_pages_reviewed': changed, 'pixel_identical_pages': unchanged,
                              'skill': '/Users/dongxingxi/.codex/skills/humanizer-zh/SKILL.md'}
    write(base / 'CHECKPOINT.json', cp)
    table = '\n'.join(f"| {x['name'].removesuffix('.pdf')} | {x['pages']} | {x['body_pages']} | `{x['sha256']}` |" for x in doc['pdfs'])
    report = f'''# 第{n}届验收报告

复核时间：{NOW}。本报告对应当前源稿和成品；修改前记录保存在{link('总审核备份', old / '核验/验收报告.md')}。

本轮按 humanizer-zh 技能完成 {n_edits} 处文字修改，保留题面、全部数学表达式、图稿和变式题目。学生五模块、教师九模块及每题四道带解答变式检查通过；两版共有解析内容一致。

重新执行 {count + extra} 项计算检查、三版文档结构与排版检查、三版内置编译，以及隔离目录重建，均通过。独立重建的 TeX、逐页文字和逐页像素与当前成品一致。

本届共 {changed + unchanged} 页，本轮重新审看 {changed} 个变化页，并放大检查{v}第 {pno} 个 PDF 页面；其余 {unchanged} 页与修改前逐像素相同，沿用此前审读记录。未见新增公式裁切、缺字或图文遮挡。

| 成品 | 总页数 | 正文页数 | SHA-256 |
| --- | ---: | ---: | --- |
{table}

页数包含一页封面；正文仍满足学生至少 56 页、教师至少 71 页的要求。PDF 结构检查通过，编译日志无缺字及 Overfull 记录。

原卷模型差异及参考答案的处理依据仍见{link('原卷与答案核对', base / '核验/原卷与答案核对.md')}；本轮文字润色未改变这些结论。完整范围、修改对照和全部成品见{link('总审核报告', AUDIT / '审核报告.md')}。

当前核验依据：document-results.json、physics-results.json、native-compile-results.json、visual-review.json、rebuild-results.json，以及本目录上一级 SHA256清单.json。第 43 届另包含 enrichment-results.json。较早专项核验记录作为历史记录保留。
'''
    (base / '核验/验收报告.md').write_text(report)
    insert_note(base / 'README.md', f"2026-10-13 总审核完成：{n_edits} 处文字润色，{count + extra} 项计算检查、三版内置编译与独立重建通过。当前成品和完整记录见{link('总审核报告', AUDIT / '审核报告.md')}。")
    if n == 35:
        text = (base / 'README.md').read_text()
        text = text.replace('本次完成最后待处理的第35届；第41—43届沿用既有工程，本次未重做其全部核验。', '第35届完成后，已对第35—43届全部重新执行计算、结构、编译、页面比对与独立重建核验，并完成文字润色。')
        (base / 'README.md').write_text(text)
    rows.append({'exam': n, 'questions': len(doc['structure']), 'variants': sum(x['variants'] for x in doc['structure']),
                 'figures': len(doc['figures']),
                 'physics_checks': count + extra, 'prose_edits': n_edits,
                 'changed_pages': changed, 'unchanged_pages': unchanged, 'pdfs': doc['pdfs']})

assert sum(r['physics_checks'] for r in rows) == 392
assert sum(r['changed_pages'] for r in rows) == 158
assert sum(r['unchanged_pages'] for r in rows) == 1143
assert len(all_figures) == 184
assert len([f for f in all_figures if f['name'] not in ['q7-photo-a.tikz', 'q7-photo-b.tikz']]) == 182
write(AUDIT / 'figure-invariants.json', {'all_passed': True, 'schematic_count': 182, 'photo_wrapper_count': 2, 'figures': all_figures,
                                      'measurement_photos': read(ROOT / '第35届/整理版/核验/document-results.json')['measurement_photos']})
write(AUDIT / 'visual-review.json', {'all_passed': True, 'reviewed_at': NOW,
                                    'changed_pages_reviewed': 158, 'pixel_identical_pages': 1143,
                                    'contact_sheets_reviewed': 32, 'single_pages_reviewed': 9, 'exams': all_visuals})
write(AUDIT / 'collection-results.json', {'all_passed': True, 'completed_at': NOW, 'exams': rows})

table_rows = []
for row in rows:
    n = row['exam']
    p = {x['name'].split('_')[1].removesuffix('.pdf'): x['pages'] for x in row['pdfs']}
    cells = [link(f"{p[v]} 页", ROOT / f'第{n}届/整理版/output/第{n}届_{v}.pdf') for v in ['试题版', '学生详解版', '教师备课版']]
    table_rows.append(f"| 第{n}届 | {row['questions']} | {' | '.join(cells)} | {row['physics_checks']} | {row['prose_edits']} |")
table = '\n'.join(table_rows)
examples = []
for n, q in [(35, 3), (36, 4), (36, 6), (39, 5), (43, 2)]:
    item = next(e for e in edits if e['exam'] == n and e['question'] == q)
    e = item['edits'][-1] if (n, q) == (36, 6) else item['edits'][0]
    examples.append(f"| 第{n}届第{q}题 | {e['before']} | {e['after'] or '删除重复句'} |")
report = f'''# 第35—43届复赛试卷总审核

完成时间：{NOW}。

9 届全部处理完成，共 67 道原题、268 道带解答变式、27 份 PDF、1,301 页。本轮按 {link('humanizer-zh 技能', Path('/Users/dongxingxi/.codex/skills/humanizer-zh/SKILL.md'))} 审读教学文字，在 67 份逐题主稿中完成 106 处修改，并同步生成学生、教师两版。全部 392 项计算检查、27 次内置编译、9 套工程独立重建通过。

## 全部成品

下表页数均含一页封面。学生正文均不少于 56 页，教师正文均不少于 71 页；三版继续使用原定的 A4、12pt、22mm 页边距、1.24 倍行距，无页眉。

| 届次 | 原题 | 试题版 | 学生详解版 | 教师备课版 | 计算检查 | 文字修改 |
| --- | ---: | --- | --- | --- | ---: | ---: |
{table}

{link('打包下载全部 27 份 PDF', AUDIT / '第35—43届_审核后PDF.zip')}。可编辑的逐题主稿、LaTeX 和绘图脚本仍在各届原工程目录中。

## 本轮核验

- **原卷与内容：** 13 个原始 PDF 的 SHA-256 均一致。67 道题的题面、12,104 段数学表达式、图引用及 268 道变式标题与修改前一致；每道变式保留解答。学生五模块、教师九模块齐全，两版共有解析一致。
- **独立计算：** 重跑各届现有符号及数值核验，共 384 项；另重跑第 43 届 8 项补充核验，合计 392 项。检查涵盖方程、数值求解、守恒关系和选定变式；检查项及参数完整记录在各届核验 JSON 中。
- **编译与重建：** 27 份当前 TeX 均通过桌面内置编译；9 套工程分别从独立目录重建图稿和三版文档。重建的 TeX、逐页文字、逐页渲染像素与当前成品一致。当前成品通过 PDF 结构检查，无缺字、Overfull 或不足 160 字符的正文页。
- **页面审读：** 对全部 1,301 页做逐页像素比对；本轮实际审看 158 个变化页的 32 张总览，并放大检查 9 个代表页。其余 1,143 页逐像素相同，沿用此前整本视觉审读记录。未发现新增公式裁切、缺字或图文遮挡。9 份试题版全部页面均与修改前一致。
- **图稿：** 182 幅可编辑示意图的源码和图形 PDF 校验值均保持一致；第 35 届两幅原始测量照片继续保留原 JPEG 字节，标尺和原始测量信息未改。

本轮沿用并重跑已有物理核验，对修改后的文字检查条件、因果及符号含义；原卷与参考答案存在模型差异的处理依据仍保留在各届“原卷与答案核对.md”中。第 35 届灰体辐射、第 37 届旋转谐振腔、第 38 届驱动反作用力矩、第 43 届参考系等已有辨析未作改动。

## 文字修改

删去重复铺垫和泛泛强调，把抽象比喻改为可直接使用的物理描述，修正不贴合题意的措辞。必要的条件对比、参考系区别、适用范围及推导步骤保留。没有为改变语气而改写公式或添入个人感想。

| 位置 | 修改前 | 修改后 |
| --- | --- | --- |
{chr(10).join(examples)}

完整记录见{link('106 处文字修改对照', AUDIT / '文字修改.diff')}和{link('逐题修改记录', AUDIT / 'prose-edits.json')}。修改前源稿、成品和核验记录保存在“修改前”目录中，可逐项回溯。

按技能五个维度作编辑自评：直接性 9/10、节奏 8/10、信任度 9/10、真实性 9/10、精炼度 9/10，总计 44/50。教学讲义保留了统一模块和必要的推导复述；评分属于编辑判断，不是文本来源鉴定或检测概率。

## 核验记录

- {link('各届结果汇总', AUDIT / 'collection-results.json')}
- {link('数学表达式、题面及原始资料一致性', AUDIT / 'content-invariants.json')}
- {link('图稿与原照片一致性', AUDIT / 'figure-invariants.json')}
- {link('27 次内置编译及源码哈希', AUDIT / 'native-compile.json')}
- {link('逐页像素比对', AUDIT / 'page-comparison.json')}与{link('实际视觉审读记录', AUDIT / 'visual-review.json')}
- {link('独立重建执行记录', AUDIT / 'rebuild-run.json')}；具体逐版结果在各届“核验/rebuild-results.json”
- {link('原工程构建、计算与排版检查', AUDIT / 'checks.json')}
- {link('修改前文件清单', AUDIT / 'baseline.json')}

各届 CHECKPOINT.json、验收报告、内置编译记录、视觉审读记录与 SHA256清单.json 已更新到当前成品；旧专项检查作为历史记录保留。当前无待处理的已收集试卷。
'''
(AUDIT / '审核报告.md').write_text(report)
insert_note(ROOT / 'README.md', f"第35—43届全部完成整理及总审核（2026-10-13）：9 届、27 份成品、1,301 页；106 处文字润色，392 项计算检查、27 次内置编译及9套独立重建通过。{link('审核报告及全部成品', AUDIT / '审核报告.md')} · {link('27份PDF合集', AUDIT / '第35—43届_审核后PDF.zip')}。")
takeover = ROOT / '接管记录.md'
text = takeover.read_text()
text = re.sub(r'更新：[^。\n]+。', f'更新：{NOW}。', text, count=1)
text = text.replace('第35-43届原始资料已收齐。第41-43届既有工程的检查点均记为完成，成品保留；本次未重做其全部验收。', '第35—43届全部完成整理。2026-10-13 已对全部 9 届重跑计算、结构、编译、页面比对和独立重建，并调用 humanizer-zh 完成文字润色。')
text = text.replace('第41—43届为此前既有工程，本次接管未重新执行其全部核验。', '第41—43届此前已有的工程也已纳入本轮总审核。')
takeover.write_text(text)
insert_note(takeover, f"总审核完成：67 道原题、268 道变式、27 份 PDF；106 处文字修改。392 项计算检查全部通过。1,301 页中重新审看 158 个变化页，其余 1,143 页与此前审读版逐像素相同。{link('总审核报告', AUDIT / '审核报告.md')}。")

# Refresh existing manifest coverage; this preserves each project's original file scope.
for n in range(35, 44):
    base = ROOT / f'第{n}届/整理版'
    path = base / 'SHA256清单.json'
    data = read(path)
    for item in data['files']:
        target = Path(item['path'])
        if not target.is_absolute():
            target = base / target
        assert target.is_file(), target
        item.update(bytes=target.stat().st_size, sha256=sha(target))
    data['created_at'] = NOW
    data['collection_audit_refreshed_at'] = NOW
    write(path, data)

bundle = AUDIT / '第35—43届_审核后PDF.zip'
with zipfile.ZipFile(bundle, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    z.write(AUDIT / '审核报告.md', '审核报告.md')
    for n in range(35, 44):
        for p in sorted((ROOT / f'第{n}届/整理版/output').glob('*.pdf')):
            z.write(p, f'第{n}届/{p.name}')

checkpoint = {'status': '已完成', 'completed_at': NOW, 'exams': list(range(35, 44)),
              'questions': 67, 'variants': 268, 'pdfs': 27, 'pages': 1301,
              'prose_edits': 106, 'physics_checks': 392, 'native_compiles': 27,
              'isolated_rebuilds': 9, 'changed_pages_visually_reviewed': 158,
              'pixel_identical_pages': 1143, 'pending_items': [],
              'report_sha256': sha(AUDIT / '审核报告.md'), 'bundle_sha256': sha(bundle)}
write(AUDIT / 'CHECKPOINT.json', checkpoint)
audit_files = [p for p in sorted(AUDIT.iterdir()) if p.is_file() and p.name != 'SHA256清单.json']
write(AUDIT / 'SHA256清单.json', {'created_at': NOW, 'scope': '总审核顶层报告、数据与PDF合集；修改前文件由baseline.json记录。',
                                'files': [{'path': p.name, 'bytes': p.stat().st_size, 'sha256': sha(p)} for p in audit_files]})
print(json.dumps(checkpoint, ensure_ascii=False, indent=2))
