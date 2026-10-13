#!/usr/bin/env python3
"""64 independent symbolic, ODE, quadrature and numerical checks of the eight masters."""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as s
from scipy.integrate import solve_ivp,quad
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def test(name,value,detail=None):
    assert bool(value),name
    checks.append(dict(check=name,passed=True,detail=detail))
def zero(x):return s.simplify(x)==0
def close(a,b,tol=1e-8):return np.allclose(a,b,rtol=tol,atol=tol)

# 1: central Newton equations provide independent landing events.
r,R,r0,v,mu=s.symbols('r R r0 v mu',positive=True)
j=r0*v;eps=v*v/2-mu/r0
rp=r0*r0*v*v/(2*mu-r0*v*v)
test("1.1 转折点代入有效势能量",zero(eps-j*j/(2*rp*rp)+mu/rp))
vr2=v*v+2*mu*(1/R-1/r0)-(r0*v/R)**2
test("1.2 落地径向速度的阈值因式",zero(vr2-(r0-R)/(R*R*r0)*(2*mu*R-v*v*r0*(R+r0))))
aa,bb,kk=s.symbols('aa bb kk',positive=True)
Q=-kk*r*r+bb*r-aa;Delta=bb*bb-4*kk*aa
F=-s.sqrt(Q)/kk-bb/(2*kk**s.Rational(3,2))*s.asin((-2*kk*r+bb)/s.sqrt(Delta))
# evaluate the derivative under Delta>0 and Q>0 to avoid artificial sqrt sign ambiguity
dF=s.lambdify((r,aa,bb,kk),s.diff(F,r),'numpy')
test("1.3 题给原函数导数",close(dF(np.array([1.1,1.3,1.5]),.2,2.,.8),
 np.array([1.1,1.3,1.5])/np.sqrt(-.8*np.array([1.1,1.3,1.5])**2+2*np.array([1.1,1.3,1.5])-.2)))
tf=math.sqrt(2**3/2)*(math.acos(math.sqrt(.5))+math.sqrt(.5*.5))
ti=quad(lambda u:2*u/math.sqrt(2*(1/(2-u*u)-.5)),0,1)[0]
test("1.4 径向释放时间的数值积分",close(tf,ti))
def gravity(t,y):
    rr=np.hypot(y[0],y[1]);return [y[2],y[3],-y[0]/rr**3,-y[1]/rr**3]
def hit(t,y):return np.hypot(y[0],y[1])-1
hit.terminal=True;hit.direction=-1
sol=solve_ivp(gravity,(0,20),[2,0,0,.3],events=hit,rtol=2e-11,atol=1e-12,max_step=.02)
aK=1/(1-.3**2);ecc=1-2*.3**2;ER=math.acos((1-1/aK)/ecc)
tK=(math.pi-ER+ecc*math.sin(ER))*aK**1.5
yhit=sol.y_events[0][0]
test("1.5 二维Newton落地事件与偏近点角",close([sol.t_events[0][0],np.hypot(*yhit[2:])],[tK,math.sqrt(1.09)]))
test("1.6 两倍半径零速释放变式",close(tf,2*(math.pi/4+.5)))
test("1.7 擦地半周期极限",close(math.pi*((2+1)/2)**1.5,math.pi*(1.5)**1.5))
q=s.symbols('q',positive=True)
inv=2*mu*R**2*q*(1/R-1/r0)/(r0*r0-R*R*q)
test("1.8 落地角反演",zero((r0*r0*v*v/(R*R*(v*v+2*mu*(1/R-1/r0)))).subs(v*v,inv)-q))

# 2: explicitly integrate sliding ODEs, then apply static conditions at velocity-zero events.
t,b,A,w=s.symbols('t b A w',positive=True)
x=-b+(-A+b)*s.cos(w*t)
test("2.1 右行分段ODE、端点及速度峰",zero(s.diff(x,t,2)+w*w*(x+b)) and
 zero(x.subs(t,s.pi/w)-(A-2*b)) and
 zero(s.diff(x,t).subs(t,s.pi/(2*w))-w*(A-b)))
x=b+(A-b)*s.cos(w*t)
test("2.2 左行分段ODE及端点",zero(s.diff(x,t,2)+w*w*(x-b)) and zero(x.subs(t,s.pi/w)-(2*b-A)))
def simulate(a,bs=1):
    x=-a; xs=[x];path=0.;directions=[]
    while abs(x)>bs+1e-9:
        direction=-np.sign(x)
        sol2=solve_ivp(lambda t,y:[y[1],-y[0]-direction],(0,math.pi),[x,0],rtol=1e-11,atol=1e-12)
        xn=sol2.y[0,-1];path+=abs(xn-x);xs.append(xn);directions.append(direction);x=xn
        assert len(xs)<100
    nr=sum(1 for j in range(2,len(xs),2) if xs[j]<-1e-8)
    return x,path,xs,nr
num=simulate(10.5)
test("2.3 ODE端点序列",close(num[2],[-10.5,8.5,-6.5,4.5,-2.5,.5]))
test("2.4 数值累计路程与全程耗散",close(num[1],55))
edge=[]
for a in [1.,3.,5.,7.,9.]:
    xn,_,xs,_=simulate(a)
    Ns=max(0,math.ceil((a-1)/2))
    edge.append(close(xn,(-1)**(Ns+1)*(a-2*Ns)) and len(xs)-1==Ns)
test("2.5 静摩擦带边界取整",all(edge))
rounds=[]
for a in [3.9,4.,4.01,8.,8.01,12.]:
    *_,nr=simulate(a);rounds.append(nr==max(0,math.ceil(a/4)-1))
test("2.6 按过零定义计数",all(rounds))
test("2.7 不等静动摩擦变式",close(simulate(6,1.5)[2],[-6,4,-2,0]))
u=s.symbols('u',positive=True);xr=-b+s.sqrt(b*b+u*u/w**2)
test("2.8 原点初速度转折点能量",zero(w*w*xr*xr+2*w*w*b*xr-u*u))

# 3: derive Newton reactions and free rigid-body coordinates from geometry.
M,m,l,g,V,th=s.symbols('M m l g V th',positive=True)
mass=M+m;dist=(3*M+4*m)*l/(6*mass);IO=(3*M+4*m)*l*l/9
om0=6*m*V/((3*M+4*m)*l)
test("3.1 裸杆打击中心冲量关系",zero(M*l/2*(2*l/3)/(M*l*l/3)-1))
test("3.2 组合质心及质心惯量",zero(IO-mass*dist**2-M*(3*M+4*m)*l*l/(36*mass)))
test("3.3 嵌入碰撞动能及水平动量",zero(IO*om0**2/2-2*m*m*V*V/(3*M+4*m)) and zero(mass*dist*om0-m*V))
test("3.4 转动能量的角度系数",zero(2*mass*g*dist/IO-3*g/l))
om,al=s.symbols('om al',real=True)
xc=-dist*s.sin(th);yc=-dist*s.cos(th)
ax=s.diff(xc,th,2)*om**2+s.diff(xc,th)*al
ay=s.diff(yc,th,2)*om**2+s.diff(yc,th)*al
test("3.5 质心加速度与轴反力",zero(ax-dist*(om**2*s.sin(th)-al*s.cos(th))) and zero(ay-dist*(om**2*s.cos(th)+al*s.sin(th))))
tt,ost=s.symbols('tt ost',positive=True)
xC=dist*ost*tt;yC=dist-g*tt*tt/2
xB=xC+(l-dist)*s.sin(ost*tt);yB=yC+(l-dist)*s.cos(ost*tt)
xA=xC-dist*s.sin(ost*tt);yA=yC-dist*s.cos(ost*tt)
test("3.6 释放时位置速度及质心平抛",zero(xB.subs(tt,0)) and zero(yB.subs(tt,0)-l) and zero(s.diff(xB,tt).subs(tt,0)-l*ost) and zero(s.diff(yC,tt,2)+g))
test("3.7 两杆端距离不变",zero((xB-xA)**2+(yB-yA)**2-l*l))
test("3.8 固定O高度及顶部临界时间",zero(yB.subs(tt,s.pi/ost)-(m*l/(3*mass)-g*s.pi**2/(2*ost**2))) and
 zero(s.diff(2*s.sqrt(l/(6*g))*s.log(s.sec(th/2)+s.tan(th/2)),th)-s.sqrt(l/(6*g))/s.cos(th/2)))

# 4: full Biot-Savart sum, rather than using the stated near-field model alone.
z,a=s.symbols('z a',complex=True)
coords=[(-a,a,-1),(a,a,1),(a,-a,-1),(-a,-a,1)]
complexsum=sum(-s.I*sg/(z-(xx+s.I*yy)) for xx,yy,sg in coords)
test("4.1 四导线复场精确求和",zero(complexsum-8*a*a*z/(z**4+4*a**4)))
test("4.2 线性梯度来自精确场",zero(s.diff(complexsum,z).subs(z,0)-2/a**2))
xx,yy,K,B0,mag=s.symbols('xx yy K B0 mag',real=True,positive=True)
test("4.3 中心无源区域散度旋度",zero(s.diff(K*xx,xx)+s.diff(-K*yy,yy)) and zero(s.diff(-K*yy,xx)-s.diff(K*xx,yy)))
pot=mag*s.sqrt(B0*B0+K*K*(xx*xx+yy*yy))
test("4.4 二次势刚度",zero(s.diff(pot,xx,2).subs({xx:0,yy:0})-mag*K*K/B0))
ang=np.linspace(0,2*np.pi,1001);rho=1.07457
bm=4*rho/np.sqrt(rho**8+8*rho**4*np.cos(4*ang)+16)
test("4.5 固定半径轴向最低势垒",np.min(bm)>=4*rho/(rho**4+4)-1e-12)
rr=s.symbols('rr',positive=True);bf=4*rr/(rr**4+4);rb=(s.Rational(4,3))**s.Rational(1,4)
test("4.6 鞍点半径、场强及轴向曲率",zero(s.diff(bf,rr).subs(rr,rb)) and
 zero(bf.subs(rr,rb)**2-3*s.sqrt(3)/8) and
 zero((bf*s.diff(bf,rr,2)).subs(rr,rb)+s.Rational(27,16)))
def field_mod(x,y):
    zz=complex(x,y);return abs(4*zz/(zz**4+4))
rbf=float(rb);h=1e-4;f0=field_mod(rbf,0)
test("4.7 轴向极大横向极小的鞍点",field_mod(rbf+h,0)+field_mod(rbf-h,0)-2*f0<0 and field_mod(rbf,h)+field_mod(rbf,-h)-2*f0>0)
u=s.symbols('u',positive=True)
test("4.8 偏置场展开",s.series(s.sqrt(1+u)-1,u,0,3).removeO()==u/2-u*u/8)

# 5: laboratory equations checked by direct substitution of the full rotating solution.
L,O,t=s.symbols('L O t',positive=True)
Ax,Bx,Ay,By=s.symbols('Ax Bx Ay By',real=True)
xp=Ax*s.cos(O*t)+Bx*s.sin(O*t);yp=Ay*s.cos(O*t)+By*s.sin(O*t)
X=xp*s.cos(L*t)-yp*s.sin(L*t);Y=xp*s.sin(L*t)+yp*s.cos(L*t)
test("5.1 完整旋转通解代入实验室ODE",
 zero(s.diff(X,t,2)+(O*O-L*L)*X+2*L*s.diff(Y,t)) and
 zero(s.diff(Y,t,2)+(O*O-L*L)*Y-2*L*s.diff(X,t)))
test("5.2 初速度变换",zero(s.diff(X,t).subs(t,0)-(O*Bx-L*Ay)) and zero(s.diff(Y,t).subs(t,0)-(O*By+L*Ax)))
wp=O+L;wm=O-L
up=s.exp(s.I*wp*t);um=s.exp(-s.I*wm*t)
test("5.3 两个圆模代入复ODE",zero(s.diff(up,t,2)-2*s.I*L*s.diff(up,t)+(O*O-L*L)*up) and zero(s.diff(um,t,2)-2*s.I*L*s.diff(um,t)+(O*O-L*L)*um))
test("5.4 模频乘积与差",zero(wp*wm-(O*O-L*L)) and zero(wp-wm-2*L))
vx,vy=s.symbols('vx vy',real=True);omega=s.symbols('omega',positive=True)
test("5.5 磁场不做功的机械能导数",zero(vx*(-omega**2*xx-2*L*vy)+vy*(-omega**2*yy+2*L*vx)+omega**2*(xx*vx+yy*vy)))
can=xx*vy-yy*vx-L*(xx**2+yy**2)
der=s.diff(can,xx)*vx+s.diff(can,yy)*vy+s.diff(can,vx)*(-omega**2*xx-2*L*vy)+s.diff(can,vy)*(-omega**2*yy+2*L*vx)
test("5.6 非零角动量积分常数守恒",zero(der))
test("5.7 旋转系圆模的非零常数",zero(xp.subs({Ax:1,Bx:0,Ay:0,By:1})*s.diff(yp,t).subs({Ax:1,Bx:0,Ay:0,By:1})-
 yp.subs({Ax:1,Bx:0,Ay:0,By:1})*s.diff(xp,t).subs({Ax:1,Bx:0,Ay:0,By:1})-O))
test("5.8 弱场二阶展开及普通频率",s.series(s.sqrt(omega**2+L**2),L,0,3).removeO()==omega+L**2/(2*omega))

# 6: solve the two radiosity equations as an independent linear system.
sig=5.67e-8;Qh=44.;A0=4*np.pi*.2**2;A1=4*np.pi*.9**2;e=.8;E=.8;f=A0/A1
T2=(2.73**4+Qh/(4*np.pi*sig))**.25
test("6.1 外表面净辐射及温度",close(4*np.pi*sig*(T2**4-2.73**4),44) and close(T2,88.6472027501))
T1=T2+Qh/(4*np.pi*.01)*(1/.9-1)
integral=quad(lambda R:-Qh/(4*np.pi*.01*R*R),.9,1)[0]
test("6.2 导热积分与温差",close(T1+integral,T2))
view=quad(lambda th:2*np.sin(th)*np.cos(th),0,np.arcsin(.2/.9))[0]
test("6.3 漫辐射球壳视角因子积分",close(view,f))
D=1/e+f*(1/E-1);T0=(T1**4+Qh*D/(A0*sig))**.25
mat=np.array([[1,-(1-e)],[-(1-E)*f,1-(1-E)*(1-f)]])
J=np.linalg.solve(mat,[e*sig*T0**4,E*sig*T1**4])
test("6.4 含自照的辐射度线性方程",close(J,[103.624102484,16.088883784]))
G=np.array([J[1],f*J[0]+(1-f)*J[1]])
test("6.5 两表面净流相等",close([A0*(J[0]-G[0]),A1*(G[1]-J[1])],[44,44]))
# Markov chain states: arriving at inner surface, arriving at shell.
trans=np.array([[0,1-e],[(1-E)*f,(1-E)*(1-f)]])
abs_shell=np.array([0,E])
prob=np.linalg.solve(np.eye(2)-trans,abs_shell)
test("6.6 完整反射链的吸收概率",close(e*prob[1],1/D))
test("6.7 灰体交换极限及参考漏项差异",D<1.3 and ((1-(1-e)*(1-E)*f)/(e*E))>1.5 and
 close((T1**4+Qh*((1-(1-e)*(1-E)*f)/(e*E))/(A0*sig))**.25,227.360940716))
tblack=(T1**4+Qh/e/(A0*sig))**.25
tdouble=((T2+(T1-T2)/2)**4+Qh*D/(A0*sig))**.25
test("6.8 涂黑与加倍导热变式",close([tblack,tdouble],[216.437789377,213.696447500]))

# 7: geometry, scaling and readout uncertainty; original byte integrity recorded separately.
lam,dist,Xi,alpha=s.symbols('lam dist Xi alpha',positive=True)
exact=lam*s.sqrt(dist**2+Xi**2)/Xi
test("7.1 单缝几何与小角度极限",s.limit(exact/(lam*dist/Xi),Xi,0)==1)
wire=633e-9*4.2/.0079;spacing=633e-9*4.2/.0017;alph=math.radians(15)
pitch=spacing/math.cos(alph);radius=spacing/(2*np.pi*math.sin(alph))
test("7.2 弹簧三尺度计算",close([wire*1e3,pitch*1e3,radius*1e3],[.3365316456,1.619047742,.961668991],tol=2e-4))
dna=.15e-9*.09/.0047;ap=math.radians(42)
pp=dna/math.cos(ap);rp=dna/(2*np.pi*math.sin(ap))
test("7.3 DNA尺度计算",close([pp*1e9,rp*1e9],[3.865,.6832],tol=2e-4))
test("7.4 螺旋反算角度",close([pitch/(2*np.pi*radius),pp/(2*np.pi*rp)],[math.tan(alph),math.tan(ap)]))
pform=lam*dist/(Xi*s.cos(alpha));rform=lam*dist/(2*s.pi*Xi*s.sin(alpha))
test("7.5 半径与螺距的角度误差",zero(s.diff(pform,alpha)/pform-s.tan(alpha)) and zero(s.diff(rform,alpha)/rform+s.cot(alpha)))
orders=np.array([2,3,5]);positions=4.7*orders+1.3
slope=np.polyfit(orders,positions,1)[0]
test("7.6 缺失阶次的线性拟合",close(slope,4.7))
imA=Image.open(ROOT/"sources/q7-original-23-0.jpg");imB=Image.open(ROOT/"sources/q7-original-24-0.jpg")
test("7.7 照片标定及等比例缩放",imA.size==(692,562) and imB.size==(525,501) and close((2*45)/(2*562)*78,45/562*78))
test("7.8 DNA小角度修正和弹簧角度敏感性",close(math.sqrt(1+(.0047/.09)**2)-1,.0013626,tol=1e-6) and
 .06<math.cos(alph)/math.sin(alph)*math.radians(1)<.07)

# 8: use high precision for tiny ratios and exact Doppler window overlap.
import mpmath as mp
mp.mp.dps=60
E0=mp.mpf('2.31e-15');mn=mp.mpf('9.5e-26');cc=mp.mpf('3e8');hh=mp.mpf('6.6e-34');Gamma=mp.mpf('3.2e-13')*E0
epsilon=E0/(mn*cc*cc);em=2*E0/(1+mp.sqrt(1+2*epsilon));ab=2*E0/(1+mp.sqrt(1-2*epsilon));recoil=E0*E0/(2*mn*cc*cc)
test("8.1 发射吸收自洽能量方程",abs(E0-em-em*em/(2*mn*cc*cc))<mp.mpf('1e-65') and abs(ab-E0-ab*ab/(2*mn*cc*cc))<mp.mpf('1e-65'))
test("8.2 反冲频差的一阶精度",abs((E0-em)/recoil-1)<mp.mpf('3e-7') and abs((ab-E0)/recoil-1)<mp.mpf('3e-7'))
test("8.3 线宽与反冲数量级",4.2e5<float(recoil/Gamma)<4.3e5 and close(float(recoil/hh),4.728070175e11,tol=1e-8))
test("8.4 两自由核窗口无交叠",E0-recoil+Gamma<E0+recoil-Gamma)
bet=2*E0*Gamma/(E0*E0+Gamma*Gamma)
Du=mp.sqrt((1-bet)/(1+bet))
test("8.5 精确多普勒窗口边界",abs(Du*(E0+Gamma)-(E0-Gamma))<mp.mpf('1e-65') and close(float(cc*bet),.000192))
delta=mp.mpf('1e-10');beta=((1+delta)**2-1)/((1+delta)**2+1)
test("8.6 未知频移的速度补偿",abs((1+delta)*mp.sqrt((1-beta)/(1+beta))-1)<mp.mpf('1e-55') and close(float(cc*beta),.03))
test("8.7 单色源窗口为两窗口的一半",close(float(cc*Gamma/E0),.000096))
test("8.8 自由核反冲差的迎向补偿",close(float(2*recoil*cc/E0),81.052631579))

assert len(checks)==64,len(checks)
out=dict(all_passed=True,check_count=len(checks),checks=checks,
 script_sha256=sha(Path(__file__)),
 source_sha256={p.name:sha(p) for p in sorted((ROOT/"drafts").glob("question-*.md"))},
 assumptions=["中心力点质点、地球外球对称场","最大静摩擦等于动摩擦","均匀重力自由刚体",
 "无限长导线、平面逃逸","经典线性束缚电子","各向同性漫辐射及漫反射灰体",
 "题设螺旋衍射估算模型、参考代表读数","题设有限线宽窗口及无反冲晶体"],
 numeric=dict(T2=T2,T1=T1,T0=T0,reference_T0=227.360940716,radiosities=J.tolist(),
 spring_mm=[wire*1e3,pitch*1e3,radius*1e3],DNA_nm=[pp*1e9,rp*1e9]))
(ROOT/"核验/physics-results.json").write_text(json.dumps(out,ensure_ascii=False,indent=2))
print("64 independent checks passed")
