from pathlib import Path
import subprocess,concurrent.futures,json,time
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parents[1];LOG=OUT/'logs'
PYDOC='/Users/dongxingxi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3'
def one(n):
 b=ROOT/f'第{n}届/整理版';result={'exam':n,'steps':[]}
 jobs=[('build',PYDOC,'build_all.py',['--skip-figures']),('physics','/opt/homebrew/bin/python3','verify_physics.py',[])]
 if n==43:jobs.append(('enrichment','/opt/homebrew/bin/python3','verify_enrichment.py',[]))
 jobs.append(('quality',PYDOC,'quality_check.py',[]))
 for name,py,script,args in jobs:
  start=time.time()
  with (LOG/f'{name}-{n}.log').open('w') as f:r=subprocess.run([py,str(b/'scripts'/script)]+args,cwd=b,stdout=f,stderr=subprocess.STDOUT)
  step=dict(name=name,exit=r.returncode,seconds=round(time.time()-start,1));result['steps'].append(step)
  print(n,name,r.returncode,flush=True)
  if r.returncode:
   result['error']=(LOG/f'{name}-{n}.log').read_text()[-3500:];break
 (OUT/f'checks-{n}.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
 return result
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:rs=list(ex.map(one,range(35,44)))
(OUT/'checks.json').write_text(json.dumps(rs,ensure_ascii=False,indent=2));print('completed',all(not r.get('error') for r in rs),flush=True)
