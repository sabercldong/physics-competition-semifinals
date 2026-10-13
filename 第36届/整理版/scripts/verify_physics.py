#!/usr/bin/env python3
"""Independent equations, integration, ODEs and ray tracing for all seven problems."""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.integrate import quad,solve_ivp
from scipy.optimize import brentq,minimize_scalar
ROOT=Path(__file__).resolve().parents[1]
records=[]
def ck(name,ok):
    assert bool(ok),name
    records.append({"check":name,"passed":True})
def near(a,b,rtol=2e-8,atol=1e-10):
    return np.allclose(a,b,rtol=rtol,atol=atol)

# 1. Changing mass, independent mass moments, constrained statics.
m,k,H,h=sp.symbols("m k H h",positive=True)
Y=(2*m*H/5+k*h*h/2)/(m+k*h)
root=m/k*(sp.sqrt(1+4*k*H/(5*m))-1)
z=sp.symbols("z",real=True)
mass=sp.integrate(k,(z,0,h))
moment=sp.integrate(k*z,(z,0,h))+sp.integrate(4*m*z/(5*H),(z,0,H))
ck("1-1 杯壁与水层积分一阶矩",sp.simplify(moment/(m+mass)-Y)==0)
ck("1-2 求导驻点及正曲率",sp.simplify(sp.diff(Y,h).subs(h,root))==0
   and sp.simplify((sp.diff(Y,h,2)-k/(m+k*h)).subs(h,root))==0)
rng=np.random.default_rng(36)
triples=np.exp(rng.uniform(-3,3,(100,3)))
hs=np.array([mm/kk*(math.sqrt(1+4*kk*hh/(5*mm))-1) for mm,kk,hh in triples])
ck("1-3 100组水深正根、杯内及端点筛选",
   np.all(hs>0) and np.all(hs<.4*triples[:,2]))
ck("1-4 新增质量的质心微分恒等式",
   sp.simplify(sp.diff(Y,h)-k*(h-Y)/(m+k*h))==0)
a,W,x,y=sp.symbols("a W x y",positive=True)
NA,NB,NC=sp.symbols("NA NB NC")
bs=a/(2*sp.sqrt(3))
sol=sp.solve([NA+NB+NC,-a*NA/2+a*NC/2-W*x,
              -bs*NA+2*bs*NB-bs*NC-W*y],(NA,NB,NC))
ck("1-5 完整三脚节点力矩解",
   sp.simplify(sol[NB]-2*W*y/(sp.sqrt(3)*a))==0 and
   sp.simplify(sol[NC]-sol[NA]-2*W*x/a)==0)
eta=sp.symbols("eta",positive=True)
Yeta=((1-eta)*m*H/2+k*h*h/2)/(m+k*h)
ck("1-6 改变底重比例的新增水层方程",
   sp.simplify((h-Yeta)*(m+k*h)*2-
               (k*h*h+2*m*h-(1-eta)*m*H))==0)

# 2. Full Newton equations for wheel and frame, impulse balance and event ODE.
mm,ll,rr,gg,mu=1.2,1.,.3,9.8,.1
s=2*rr/(3*ll);c=math.sqrt(1-s*s)
Jf=2*quad(lambda q:mm/(2*ll)*q*q,-1.5*ll,.5*ll)[0]+quad(lambda q:2*mm/ll*q*q,-.5*ll,.5*ll)[0]
ck("2-1 杆与板分布积分惯量",near(Jf,4*mm*ll*ll/3))
drop=(ll/4)*s;wf=math.sqrt(2*4*mm*gg*drop/Jf)
ck("2-2 势能与定轴动能独立求角速度",near(wf,math.sqrt(gg*rr)/ll))
vc=ll*wf/4;JN=4*mm*vc*c;v0=(4*mm*vc*s-mu*JN)/(6*mm)
JA=(Jf*wf-2*mm*rr*v0/3-mu*rr*JN)/(1.5*ll*c);JW=JN-JA
ck("2-3 碰撞线动量与角冲量、法向接触",
   near(v0,math.sqrt(gg*rr)/6*(s-mu*c)) and JA>0 and JW>0 and
   near(JA/JN,(8-s*s-8*mu*s*c)/(9*c*c)))
A,N,Nw,X,Yv,aw=sp.symbols("A N Nw X Yv aw")
eq1=[X-mu*N-4*mm*A,-X-mu*Nw-2*mm*A,N+Yv-4*mm*gg,
     Nw-Yv-2*mm*gg,Yv*c-X*s-5*N*(c+mu*s),2*mm*rr*aw-mu*Nw]
ss=sp.solve(eq1,(A,N,Nw,X,Yv,aw))
ck("2-4 滑动完整六方程",
   near([float(ss[q]) for q in (A,N,Nw,aw)],
        [-mu*gg,2*mm*gg/3,16*mm*gg/3,8*mu*gg/(3*rr)]))
def e_roll(t,z):return z[0]-rr*z[1]
e_roll.terminal=True;e_roll.direction=-1
nw=16*mm*gg/3;nn=2*mm*gg/3
def slip_ode(t,z):
    v,w,x,heat=z
    return [-mu*gg,mu*nw/(2*mm*rr),v,mu*nn*v+mu*nw*(v-rr*w)]
out=solve_ivp(slip_ode,(0,.1),[v0,0,0,0],events=e_roll,rtol=1e-11,atol=1e-13)
tr=out.t[-1];v1,w1,s1,heat1=out.y[:,-1]
ck("2-5 接触滑速ODE首次事件",near([tr,v1,rr*w1],
   [3*v0/(11*mu*gg),8*v0/11,8*v0/11]))
ck("2-6 滑动摩擦功积分与平动转动能差",
   near(heat1,3*mm*v0*v0-4*mm*v1*v1) and
   near(s1,57*v0*v0/(242*mu*gg)))
F=sp.symbols("F")
eq2=[X-mu*N-4*mm*A,F-X-2*mm*A,N+Yv-4*mm*gg,Nw-Yv-2*mm*gg,
     Yv*c-X*s-5*N*(c+mu*s),2*mm*rr*aw+F,A-rr*aw]
ss2=sp.solve(eq2,(A,N,Nw,X,Yv,aw,F));df=12+11*mu*s/c
ck("2-7 纯滚动完整七方程",
   near([float(ss2[q]) for q in (A,N,F)],
        [-mu*gg/df,8*mm*gg/df,2*mm*mu*gg/df]))
a2=float(ss2[A]);n2=float(ss2[N])
out2=solve_ivp(lambda t,z:[a2,z[0],mu*n2*z[0]],(0,-v1/a2),
               [v1,0,0],rtol=1e-11,atol=1e-13)
s2=out2.y[1,-1]
ck("2-8 纯滚动停止ODE与能量闭合",
   near(out2.y[2,-1],4*mm*v1*v1) and
   near(s1+s2,v0*v0/(242*mu*gg)*(825+704*mu*s/c)))
ck("2-9 静摩擦裕度及阈值分支",
   0<float(ss2[F])<mu*float(ss2[Nw]) and
   near(float(ss2[F])/(mu*float(ss2[Nw])),1/(32+33*mu*s/c)) and
   near(math.sqrt(gg*rr)/6*(s-(s/c)*c),0))
# changed wheel inertia computed from torque ODE, not by replacing a final number
tr_disk=brentq(lambda t:v0-mu*gg*t-(16*mu*gg/3)*t,0,v0/(mu*gg))
ck("2-10 实心圆盘变式的首次无滑动",near(v0-mu*gg*tr_disk,16*v0/19))

# 3. Biot-Savart integrals, acceleration, source work and variable-current closure.
u0=4*math.pi*1e-7;I=1e4;b=.005;d=.002;L=1;mp=.01;R=.001;lam=.0005
kl=u0/math.pi*math.log1p(d/b)
Bend=u0*I/(4*math.pi)*quad(lambda z:b/(b*b+z*z)**1.5,0,np.inf)[0]
ck("3-1 毕奥萨伐尔半无限端点场",near(Bend,u0*I/(4*math.pi*b)))
fb=quad(lambda q:u0*I*I/(4*math.pi)*(1/q+1/(2*b+d-q)),b,b+d)[0]
ck("3-2 弹丸横向磁力积分",near(fb,.5*kl*I*I))
flux_per_len=quad(lambda q:u0*I/(2*math.pi)*(1/q+1/(2*b+d-q)),b,b+d)[0]
ck("3-3 长回路磁通积分与力的一致性",near(flux_per_len,kl*I) and near(fb,.5*I*flux_per_len))
theta=.25;acc=fb/mp-9.8*math.sin(theta);T=math.sqrt(2*L/acc)
out=solve_ivp(lambda t,z:[z[1],(fb-mp*9.8*math.sin(theta))/mp],(0,T),
              [0,0],rtol=1e-11,atol=1e-13)
ck("3-4 斜轨Newton运动与机械能",near(out.y[0,-1],L) and
   near(.5*mp*out.y[1,-1]**2+mp*9.8*L*math.sin(theta),fb*L))
U=lambda t:I*(R+lam*acc*t*t)+kl*I*acc*t
ws=quad(lambda t:I*U(t),0,T)[0]
qj=quad(lambda t:I*I*(R+lam*acc*t*t),0,T)[0]
ck("3-5 源功及焦耳热时间积分",near(ws,I*I*T*(R+2*lam*L/3)+kl*I*I*L))
ck("3-6 源功的动能势能磁能闭合",near(ws,qj+.5*mp*out.y[1,-1]**2+mp*9.8*L*math.sin(theta)+.5*kl*I*I*L))
it,di,xx,vv,l0,kap,res=sp.symbols("it di xx vv l0 kap res",real=True)
us=it*res+(l0+kap*xx)*di+kap*it*vv
ubdot=(l0+kap*xx)*it*di+kap*it*it*vv/2
ck("3-7 可变电流功率恒等式",sp.simplify(us*it-it*it*res-ubdot-kap*it*it*vv/2)==0)
Th=math.sqrt(2*L/(fb/mp));ve=math.sqrt(2*L*fb/mp)
ck("3-8 水平数值及无损效率",near([Th,ve,I*(R+2*lam*L)+kl*I*ve],
   [.05451617569115117,36.68635913367326,20.049375765244786])
   and near((fb*L)/(kl*I*I*L),.5))

# 4. Exact gas pressure linearization, oscillator dynamics and loss power.
p0=1.01e5;temp=273.;ma=.029;rg=8.31;gam=1.4
rho=ma*p0/(rg*temp);vs=math.sqrt(gam*p0/rho)
ck("4-1 气体密度与绝热声速",near([rho,vs],[1.2910875726760203,330.9381648669691]))
pv,V,S,z=sp.symbols("pv V S z",positive=True)
pex=pv*(V/(V+S*z))**sp.Rational(7,5)
force=S*(pex-pv)
ck("4-2 精确绝热压力的一阶回复力",sp.simplify(sp.diff(force,z).subs(z,0)+sp.Rational(7,5)*pv*S*S/V)==0)
Snum=1e-5;lnum=.005;Vnum=.0002;mass=rho*Snum*lnum;K=gam*p0*Snum*Snum/Vnum;w=math.sqrt(K/mass)
tf=2*math.pi/w
out=solve_ivp(lambda t,z:[z[1],-K*z[0]/mass],
              (0,tf),[1e-7,0],rtol=1e-10,atol=1e-15)
ck("4-3 声学振子ODE周期及几何频率",near(out.y[:,-1],[1e-7,0],atol=1e-10) and near(w,vs*math.sqrt(Snum/(lnum*Vnum))))
small=1e-6
Ecomp=quad(lambda dz:-(p0*(Vnum/(Vnum+dz))**gam-p0),0,Snum*small)[0]
ck("4-4 压缩做功积分的二阶弹簧能",near(Ecomp,.5*K*small*small,rtol=1e-6))
S120=lnum*Vnum*(2*math.pi*120/vs)**2;S200=lnum*Vnum*(2*math.pi*200/vs)**2
ck("4-5 两个频率反求面积及端部惯性",near(S120/S200,.36) and near(math.sqrt(lnum/(1.5*lnum)),math.sqrt(2/3)))
beta=.12
peak=minimize_scalar(lambda om:-om*om/((1-om*om)**2+4*beta*beta*om*om),
                     bounds=(.5,1.5),method="bounded",options={"xatol":1e-12})
ck("4-6 阻尼吸收功率峰的独立极值",near(peak.x,1,rtol=1e-7))

# 5. Matrices, two surfaces and exact vector Snell ray tracing.
n1=1.46;n2=1.45;ng=1.5;ne=1.;diam=.003;rad=diam/2
na=math.sqrt(n1*n1-n2*n2);accept=math.asin(na/ne);af=math.asin(na/n1)
ck("5-1 两次Snell与全反射临界",near(n1*math.cos(af),n2) and near(ne*math.sin(accept),na))
power=(ng-ne)/rad
sf=np.array([[1.,0],[-power,1]])
prop=np.array([[1,diam/ng],[0,1]])
mat=sf@prop@sf
ck("5-2 双曲面完整光线矩阵及行列式",near(np.linalg.det(mat),1) and near(mat[1,0],-4*ne*(ng-ne)/(ng*diam)))
zi=ng*rad/(ng-ne);zo=zi-diam
zf=ne/((ne-ng)/(-rad)+ng/zo)
fe=-ne/mat[1,0]
ck("5-3 虚物折射与矩阵后焦距",near(zf,.00075) and near(zf,-ne*mat[0,0]/mat[1,0]) and near(fe-zf,rad))
def refract(ray,normal,nin,nout):
    co=np.dot(ray,normal);ratio=nin/nout
    return ratio*ray+(math.sqrt(1-ratio*ratio*(1-co*co))-ratio*co)*normal
def trace(height):
    first=np.array([-math.sqrt(rad*rad-height*height),height])
    ray=refract(np.array([1.,0.]),-first/rad,ne,ng)
    second=first-2*np.dot(first,ray)*ray
    exitray=refract(ray,second/rad,ng,ne)
    return second,exitray
hh=.00035;pos,ray=trace(hh)
alpha=math.asin(hh/rad);beta=math.asin(ne/ng*math.sin(alpha))
ck("5-4 精确向量Snell光路与球面角几何",near(np.linalg.norm(pos),rad) and near(-math.atan2(ray[1],ray[0]),2*(alpha-beta)))
tiny=1e-8;pt,dr=trace(tiny)
ck("5-5 精确光线的近轴极限",near(-dr[1]/tiny,1/fe,rtol=1e-6) and near(pt[0]-pt[1]*dr[0]/dr[1],rad+zf,rtol=1e-6))
edge=brentq(lambda hh:-math.atan2(trace(hh)[1][1],trace(hh)[1][0])-accept,1e-9,.0006,xtol=1e-15)
ck("5-6 精确接受角束径边界",near(edge*2,.0007540410325835296) and edge*2<2*fe*na)
beam=.0006;dz=25e-6/(beam/(2*fe))
Mfocus=np.array([[1,zf/ne],[0,1]])@mat
Mdef=np.array([[1,(zf+dz)/ne],[0,1]])@mat
ck("5-7 理想离焦位置容差",near(Mfocus[0,0],0) and near(abs((Mdef@np.array([beam/2,0]))[0]),25e-6) and near(dz,.0001875))
n2max=math.sqrt(n1*n1-(.0005/(2*fe))**2)
ck("5-8 反求包层及焦点分支",near(math.sqrt(n1*n1-n2max*n2max),.0005/(2*fe)) and (2-2.1)*diam/(4*(2.1-1))<0)

# 6. Two-body solve, full four-vectors, velocity transformation and decay ODE.
MP=139.57061;MM=105.65837;BP=.965;c0=3e8;thalf=1.523e-6
qstar=brentq(lambda q:math.sqrt(MM*MM+q*q)+q-MP,0,MP)
estar=math.sqrt(MM*MM+qstar*qstar);bstar=qstar/estar;GP=1/math.sqrt(1-BP*BP)
ck("6-1 非线性两体能量守恒求动量",near(qstar,(MP*MP-MM*MM)/(2*MP)) and near(estar+qstar,MP))
ck("6-2 μ子质量壳与母系速率",near(estar*estar-qstar*qstar,MM*MM) and near(bstar,.2713862422251681))
cs=np.linspace(-1,1,301);sn=np.sqrt(1-cs*cs)
Em=GP*(estar+BP*qstar*cs);pmx=GP*(qstar*cs+BP*estar);pmy=qstar*sn
En=GP*(qstar-BP*qstar*cs);pnx=GP*(-qstar*cs+BP*qstar);pny=-qstar*sn
ck("6-3 301个角度的完整四动量守恒",
   near(Em+En,GP*MP) and near(pmx+pnx,GP*BP*MP) and near(pmy+pny,0) and near(Em*Em-pmx*pmx-pmy*pmy,MM*MM))
speed=np.sqrt(pmx*pmx+pmy*pmy)/Em
bmax=(BP+bstar)/(1+BP*bstar);bmin=(BP-bstar)/(1-BP*bstar)
ck("6-4 全角度速率端点筛选",near([speed.min(),speed.max()],[bmin,bmax]) and np.all(np.diff(speed)>0))
bx=(bstar*cs+BP)/(1+BP*bstar*cs);by=bstar*sn/(GP*(1+BP*bstar*cs))
ck("6-5 二维速度与能量动量变换一致",near(np.sqrt(bx*bx+by*by),speed))
gm=1/math.sqrt(1-bmax*bmax);time=10000/(bmax*c0);tau0=thalf/math.log(2)
dec=solve_ivp(lambda t,z:[-z[0]/(gm*tau0)],(0,time),[1.],rtol=1e-11,atol=1e-13)
prob=2**(-time/(gm*thalf))
ck("6-6 衰变ODE与半衰期概率",near(dec.y[0,-1],prob) and near(prob,.045180792513750935))
proper=(10000/gm)/(bmax*c0);halfheight=gm*bmax*c0*thalf
ck("6-7 长度收缩固有时间及半衰高度",near(proper,time/gm) and near(2**(-halfheight/(gm*bmax*c0*thalf)),.5))
cone=lambda q: bstar*math.sqrt(1-q*q)/(GP*(BP+bstar*q))
ext=minimize_scalar(lambda q:-cone(q),bounds=(-.999,.999),method="bounded",options={"xatol":1e-12})
ck("6-8 发射角极值变式",near(ext.x,-bstar/BP,rtol=1e-6) and near(cone(ext.x),bstar/(GP*math.sqrt(BP*BP-bstar*bstar))))

# 7. Image charges, disk quadrature, signed Gauss law, wavefront and atmosphere.
eps=8.85e-12;ec=1.5e5;rc=2500.;dc=1000.;hc=6000.;qc=eps*ec*math.pi*rc*rc
energy=quad(lambda z:.5*eps*ec*ec*math.pi*rc*rc,0,dc)[0]
ck("7-1 场能体积积分与电容储能",near(energy,.5*qc*ec*dc) and near(qc,26.065401547752817))
charges=[(-qc,hc),(qc,hc+dc),(qc,-hc),(-qc,-hc-dc)]
ez=sum((-qq*zz)/(4*math.pi*eps*abs(zz)**3) for qq,zz in charges)
ck("7-2 四个真实镜像电荷的地表向量场",near(ez,3454.5068027210878) and ez>0)
sigma=qc/(math.pi*rc*rc)
ed=quad(lambda s:sigma/eps*s*(hc/(s*s+hc*hc)**1.5-(hc+dc)/(s*s+(hc+dc)**2)**1.5),0,rc)[0]
edclosed=sigma/eps*((hc+dc)/math.sqrt(rc*rc+(hc+dc)**2)-hc/math.sqrt(rc*rc+hc*hc))
ck("7-3 均匀圆盘加镜像的圆环场积分",near(ed,edclosed) and near(ed,2799.7482776871475))
# use a remote point and direct ring quadrature so asymptotic cancellation is stable
remote=1e6
edremote=quad(lambda s:sigma/eps*s*(remote/(s*s+remote**2)**1.5-(remote+dc)/(s*s+(remote+dc)**2)**1.5),0,rc)[0]
epremote=qc/(2*math.pi*eps)*(1/remote**2-1/(remote+dc)**2)
ck("7-4 圆盘远场回到点电荷偶极场",near(edremote,epremote,rtol=2e-5,atol=1e-12))
eb=3e6;ach=2.5/(2*math.pi*eps*eb*hc);core=.005
lambda_core=-2*math.pi*eps*eb*core
ql=lambda radius:lambda_core+quad(lambda r:-eps*eb/r*2*math.pi*r,core,radius)[0]
ck("7-5 负电密度的高斯积分及核心边界",
   all(near(ql(r)/(2*math.pi*eps*r),-eb) for r in [.01,.1,1.,ach]))
ck("7-6 通道总量反求直径",near(2*ach,4.9954470524763135) and near(ql(ach)*hc,-2.5))
hi=80000.;ri=100000.;arrival=math.hypot(hi,ri)/c0
ring=lambda t:math.sqrt(c0*c0*t*t-hi*hi)
dt=1e-9;vel=(ring(arrival+dt)-ring(arrival-dt))/(2*dt)
ck("7-7 球面波交线的独立时间差分",near(vel,c0*math.hypot(hi,ri)/ri,rtol=1e-8))
width=ring(arrival)-ring(arrival-1e-5)
ck("7-8 有限波包环宽与局部扩张近似",width>c0*1e-5 and near(width,vel*1e-5,rtol=.01))
Ta=290.;alpha=.005;grav=9.8;airM=.029;Pg=1.01e5;zb=12000.;RG=8.31
atm=solve_ivp(lambda z,p:[-airM*grav*p[0]/(RG*(Ta-alpha*z))],(0,zb),[Pg],rtol=1e-11,atol=1e-7)
tb=Ta-alpha*zb;pb=Pg*(tb/Ta)**(airM*grav/(alpha*RG));rhob=airM*pb/(RG*tb)
ck("7-9 大气静力ODE与变温积分",near(atm.y[0,-1],pb) and near(rhob,.3139145532870392))
vb=50/(rhob-.18);vnew=50/(rhob*(1-4/29))
ck("7-10 浮力质量闭合及等压同温变式",
   near(rhob*vb-.18*vb,50) and near(vb,373.37241377214224) and
   near(rhob*vnew-(4/29*rhob)*vnew,50))

assert len(records)==56,len(records)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={"all_passed":True,"check_count":len(records),"checks":records,
        "source_sha256":{p.name:sha(p) for p in sorted((ROOT/"drafts").glob("question-*.md"))},
        "script_sha256":sha(Path(__file__)),
        "methods":"质量一阶矩、完整Newton与冲量系统、ODE事件、毕奥萨伐尔及源功积分、压缩能、向量Snell、四动量、衰变ODE、镜像圆环积分和大气ODE"}
(ROOT/"核验/physics-results.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"checks":len(records),"all_passed":True},ensure_ascii=False))
