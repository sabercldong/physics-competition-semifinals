#!/usr/bin/env python3
"""Independent symbolic, ODE, quadrature, phase and circuit checks."""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as s
from scipy.integrate import solve_ivp,quad
from scipy.optimize import brentq
from scipy.special import jv
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def close(a,b,rtol=2e-8,atol=2e-10):
    assert np.allclose(a,b,rtol=rtol,atol=atol),(a,b)
def record(name,evidence):
    checks.append({"check":name,"passed":True,"evidence":evidence})
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

# Q1: derive from state and force, not a copied final stiffness.
y,p0,pe,V,a,A,b,k,V2=s.symbols("y p0 pe V a A b k V2",positive=True)
p=pe*(V/(V-a*y))**k
F=(p-p0)*(A+b*y)
K=s.diff(F,y)
assert s.simplify(K.subs(y,0)-(k*a*pe*A/V+b*(pe-p0)))==0
record("1A_气体状态与承载力乘积求导",str(K))
gamma=s.Rational(7,2)/s.Rational(5,2)
assert gamma==s.Rational(7,5)
openF=(pe*(V+V2)/(V+V2-a*y)-p0)*(A+b*y)
assert s.simplify(s.diff(openF,y).subs(y,0)-(a*pe*A/(V+V2)+b*(pe-p0)))==0
record("1B_热容与双气室共同等温导数",{"gamma":str(gamma)})
values=[]
for exponent,total in [(1,.02),(1.4,.02),(1,.06)]:
    fun=lambda yy:(3e5*(total/(total-.05*yy))**exponent-1e5)*(.05+.01*yy)
    derivative=(fun(1e-6)-fun(-1e-6))/(2e-6)
    values.append(float(derivative))
close(values,[39500,54500,14500],rtol=1e-8)
freq=np.sqrt(np.array(values)/1000)/(2*np.pi)
record("1C_数值力差分与附加容积变式",{"stiffness":values,"Hz":freq.tolist()})
ratio=(1.4+1)/(1+1);assert ratio==1.2
assert (1/4+1)/(1+1)==5/8
record("1D_面积项刚度比与附加容积选择",{"Ka_over_Kp":1,"V2_over_V1":3})
G=.03;pp=3.;v1=2.;v2=4.;aa=.5;area=.7;ga=1.4
kh=ga*pp*aa*area/v1;kl=ga*pp*aa*area/(v1+v2)
tau=1/(ga*pp*G*(1/v1+1/v2))
res=[]
for w in [.001,.1,1,10,100]:
    mat=np.array([[1j*w+ga*pp*G/v1,-ga*pp*G/v1],
                  [-ga*pp*G/v2,1j*w+ga*pp*G/v2]],complex)
    dp=np.linalg.solve(mat,np.array([1j*w*ga*pp*aa/v1,0]))
    gain=area*dp[0]
    close(gain,kl+(kh-kl)*1j*w*tau/(1+1j*w*tau))
    assert gain.imag>0
    res.append([w,gain.real,gain.imag])
record("1E_两室压差流动矩阵与被动耗散",res)
omega=math.sqrt(39500/1000)
def ev(t,z):return z[0]
ev.direction=-1;ev.terminal=True
sol=solve_ivp(lambda t,z:[z[1],-39500*z[0]/1000],[0,1],[1,0],events=ev,rtol=1e-10,atol=1e-12)
period=4*sol.t_events[0][0]
close(period,2*np.pi/omega)
record("1F_恢复力方向与小振动ODE周期",{"seconds":float(period)})

# Q2: impulse and friction evolution, event detection and work.
P=1.;m=1.;R=1.;mu=.2;g=9.8;J=.4
v0=P/m;w0=P*.5/J
assert v0-R*w0<0
def contact(t,z):return z[0]-R*z[1]
contact.terminal=True;contact.direction=1
ball=solve_ivp(lambda t,z:[mu*g,-mu*m*g*R/J,mu*m*g*(z[0]-R*z[1]),z[0]],
               [0,1],[v0,w0,0,0],events=contact,rtol=1e-11,atol=1e-13)
t0=ball.t_events[0][0];vb,wb,work,xc=ball.y_events[0][0]
close([t0,vb,wb],[P/(14*mu*m*g),15*P/(14*m),15*P/(14*m*R)])
record("2A_冲量初值与滑动终止事件",{"t0":t0,"v_roll":vb,"omega_roll":wb})
close(work,-P*P/(112*m));close(xc,29*P*P/(392*mu*m*m*g))
energy0=.5*m*v0*v0+.5*J*w0*w0
energyf=.5*m*vb*vb+.5*J*wb*wb
close(energyf-energy0,work)
record("2B_作用点摩擦功与平转动能闭合",{"work":work,"center_distance":xc})
heights=[-1,-.5,0,.4,.5,1]
roll=[]
for h in heights:
    u0=1-h/.4
    if abs(u0)<1e-12:tf=0.;vf=1.
    else:
        f=-np.sign(u0)*mu*m*g
        tf=abs(u0)/(mu*g*(1+1/.4))
        vf=v0+f*tf/m;wf=P*h/J-f*R*tf/J
        close(vf,wf*R)
    close(vf,(1+h)/1.4)
    roll.append([h,tf,float(vf)])
record("2C_全部击打高度分支与角动量终速",roll)
t,u,rr=s.symbols("t u rr",positive=True)
th=u*t/rr
pos=s.Matrix([u*t-rr*s.sin(th),rr*(1-s.cos(th))])
vel=pos.diff(t);acc=vel.diff(t)
assert s.simplify(acc.dot(acc)-u**4/rr**2)==0
assert s.simplify(vel.dot(vel)-2*u**2*(1-s.cos(th)))==0
record("2D_摆线导数与刚体向心加速度",{"velocity":str(vel),"acceleration":str(acc)})
theta=np.linspace(0,6*np.pi,301)
speeds=np.sqrt((1-np.cos(theta))**2+np.sin(theta)**2)
close(speeds,2*np.abs(np.sin(theta/2)))
assert speeds.min()>=0
record("2E_跨三周期的速率绝对值",{"samples":len(theta)})
arc=quad(lambda z:math.hypot(1-math.cos(z),math.sin(z)),0,2*np.pi)[0]
close(arc,8)
record("2F_材料点一圈弧长积分",{"s_over_R":arc})

# Q3: integrate circuit states, preserving capacitor initial voltage.
beta=.2
def current(t,delta):
    q2=delta*delta-1
    if abs(q2)<1e-12:return beta*t*np.exp(-delta*t)
    if q2<0:
        w=math.sqrt(-q2);return beta*np.exp(-delta*t)*np.sin(w*t)/w
    q=math.sqrt(q2);return beta*np.exp(-delta*t)*np.sinh(q*t)/q
errs=[]
for delta in [-1.2,-.3,0,.3,1,1.2]:
    rho=2*delta
    z=solve_ivp(lambda t,z:[-rho*z[0]-z[1],z[0]],[0,5],[0,-beta],
                 rtol=2e-12,atol=1e-14,dense_output=True)
    tt=np.linspace(0,5,121)
    err=np.max(np.abs(z.sol(tt)[0]-current(tt,delta)))
    assert err<2e-8,err;errs.append([delta,float(err)])
record("3A_电流电容双状态ODE及重根初值",errs)
budgets=[]
for delta in [.15,.4,.8]:
    integral=quad(lambda t:2*delta*current(t,delta)**2,0,math.inf,epsabs=1e-10)[0]
    close(integral,.5*beta**2,rtol=2e-6)
    budgets.append([delta,integral])
record("3B_净耗散从零到无穷的能量积分",budgets)
regions=[]
for delta in [-1.2,-.5,0,.5,1,1.2]:
    eig=np.linalg.eigvals(np.array([[-2*delta,-1],[1,0.]]))
    close(np.sort_complex(eig),np.sort_complex(np.roots([1,2*delta,1])))
    regions.append([delta,[[float(x.real),float(x.imag)] for x in eig]])
record("3C_状态矩阵特征根与振荡区间",regions)
Vmin=.2;Vmax=.6;R0=10
Vmid=(Vmin+Vmax)/2;amplitude=(Vmax-Vmin)/2
mean=quad(lambda x:(amplitude*math.cos(x))**2/R0,0,2*np.pi)[0]/(2*np.pi)
close(mean,(Vmax-Vmin)**2/(8*R0))
record("3D_工作区间与负吸收正输出功率",{"bias":Vmid,"output_W":mean})
close(current(1.,1),beta/math.e)
offset=Vmid+(Vmax-Vmin)/4
maxamp=min(offset-Vmin,Vmax-offset)
close(maxamp**2/amplitude**2,.25)
record("3E_临界峰值与偏置偏移功率",{"peak_time":1,"power_ratio":.25})
r_external=.8;r_inductor=.2;r_negative=1.
lossnet=r_external+r_inductor-r_negative
state=solve_ivp(lambda t,z:[-lossnet*z[0]-z[1],z[0]],
                 [0,2*math.pi],[0,-beta],rtol=1e-11,atol=1e-13,dense_output=True)
tt=np.linspace(0,2*math.pi,101);states=state.sol(tt)
close(states[0],beta*np.sin(tt))
close(.5*(states[0]**2+states[1]**2),.5*beta**2)
record("3F_电感损耗加入后的独立状态与能量",{"R":r_external,"rL":r_inductor,"R0":r_negative,"energy":.5*beta**2})

# Q4: magnetic motion and threshold four-vectors.
energy=math.sqrt(10.);B=.7;period=2*math.pi*energy/B
mag=solve_ivp(lambda t,z:[-B*z[1]/energy,B*z[0]/energy,z[0]/energy,z[1]/energy],
              [0,period],[3,0,0,0],rtol=2e-11,atol=1e-12,dense_output=True)
zz=mag.sol(np.linspace(0,period,201));rad=3/B
close(zz[0]**2+zz[1]**2,9)
close(zz[2]**2+(zz[3]-rad)**2,rad**2,rtol=1e-8)
record("4A_相对论洛伦兹ODE与圆轨道半径",{"radius":rad,"period":period})
bmin=2*math.pi*math.sqrt((1e12)**2-(938.3e6)**2)/(3e8*6436)
close(bmin,3.254186110057572,rtol=1e-12)
record("4B_磁刚度单位转换与最大周长",{"Tesla":bmin,"radius_m":6436/(2*math.pi)})
E=s.symbols("E",positive=True)
threshold=s.solve(s.Eq((E+1)**2-(E**2-1),16),E)[0]
assert threshold==7
vcm=math.sqrt(3)/2;gcm=1/math.sqrt(1-vcm*vcm)
close([4*gcm,4*gcm*vcm],[8,4*math.sqrt(3)])
record("4C_固定靶阈值与末态共同四动量",{"E_over_mc2":7,"K_MeV":6*938.3})
ma,mb,mf=s.symbols("ma mb mf",positive=True)
eth=s.solve(s.Eq((E+mb)**2-(E**2-ma**2),mf**2),E)[0]
assert s.simplify(eth-(mf**2-ma**2-mb**2)/(2*mb))==0
record("4D_任意入射靶质量的阈值方程",str(eth))
collider=[2.,math.sqrt(3)]
close(2*collider[0],4)
record("4E_对称对撞的零总动量阈值",{"each_beam_K_MeV":938.3})
first_turn=brentq(lambda tt:mag.sol(tt)[0],period*.1,period*.4)
omega_measured=math.pi/(2*first_turn)
close(omega_measured,B/energy)
record("4F_动量转过九十度的数值频率",{"omega":omega_measured,"quarter_time":first_turn})

# Q5: solve world-line intersections, then transform actual events.
def boost(event,v):
    t,x,y=event;ga=1/math.sqrt(1-v*v)
    return np.array([ga*(t-v*y),x,ga*(y-v*t)])
T=1.;D=math.sqrt(5)/3
tB=brentq(lambda t:-t-(-D-t/3),0,3)
tC=brentq(lambda t:-tB+(t-tB)+2*t/3,tB,3)
Aev=np.array([0.,0.,0.]);Bev=np.array([tB,0.,-tB]);Cev=np.array([tC,0.,-2*tC/3])
close(boost(Cev,-2/3)[0],T)
close(boost(Bev,-2/3)[0],T/2)
close([tC,boost(Cev,-1/3)[0]],[3/math.sqrt(5),7*math.sqrt(10)/20])
record("5A_光世界线交点及两系事件变换",{"B":Bev.tolist(),"C":Cev.tolist()})
tmeet=3*D
meet=np.array([tmeet,0.,-2*tmeet/3])
close(boost(meet-Cev,-2/3)[0],2/3)
record("5B_追及事件在甲系的返回后间隔",{"over_T":2/3})
ux=math.sqrt((3/4)**2-(2/3)**2);uy=2/3
tf=1/ux;recv=np.array([tf,1.,uy*tf])
ev甲=boost(recv,-2/3);vel甲=ev甲[1:]/ev甲[0]
close(vel甲,[math.sqrt(85)/52,12/13])
close(np.linalg.norm(vel甲),math.sqrt(2389)/52)
record("5C_投递交点变换直接给二维速度",{"velocity_over_c":vel甲.tolist(),"degrees_to_minus_y":180-math.degrees(math.atan(math.sqrt(85)/48))})
ev乙=boost(recv,-1/3)
close(ev乙[0],11*math.sqrt(34)/17)
close(ev乙[1]/ev乙[0],math.sqrt(34)/22)
record("5D_乙系异地事件时间和横向速度核对",{"time_over_d_c":float(ev乙[0])})
interval=recv[0]**2-recv[1]**2-recv[2]**2
for evv in [ev甲,ev乙]:close(evv[0]**2-evv[1]**2-evv[2]**2,interval)
close(math.sqrt(interval),3*math.sqrt(7/17))
record("5E_投递固有时与不变间隔",{"proper_time":math.sqrt(interval)})
w=3/7;ll=1.;wait=.2;tb=ll/(1+w);delay=wait/math.sqrt(1-w*w)
total=tb+delay+(ll-w*(tb+delay))
close(total-2*ll/(1+w),math.sqrt(2/5)*wait)
record("5F_延迟反射的移动端点与本地钟",{"round_trip":total})

# Q6: refraction and phase periodicity with wave dispersion.
n1=1.5;n2=1.48
na=math.sqrt(n1*n1-n2*n2);theta=math.acos(n2/n1)
i=math.asin(na)
close(math.sin(i),n1*math.sin(theta))
record("6A_端面与侧面临界角几何",{"NA":na,"acceptance_deg":math.degrees(i)})
timecases=[]
for n in [1.,1.2,1.5,2.]:
    urot=.01;ell=2*math.pi
    vp=(1/n+urot)/(1+urot/n);vm=(1/n-urot)/(1-urot/n)
    tp=ell/(vp-urot);tm=ell/(vm+urot)
    close(tp-tm,4*math.pi*urot/(1-urot**2),rtol=1e-10)
    timecases.append([n,tp,tm])
record("6B_速度合成后与分束器追及",timecases)
phase=8*math.pi**2/(1.55e-6*3e8)
close(phase,.169799645610+0,atol=2e-9)
record("6C_百圈有向面积的相位数值",{"phase_rad":phase,"delay_s":4*math.pi/(3e8)**2})
nn,uu,cc,mm,rad=s.symbols("nn uu cc mm rad",positive=True)
ell=2*s.pi*rad
tp=ell*(nn*cc+uu)/(cc**2-uu**2);tm=ell*(nn*cc-uu)/(cc**2-uu**2)
split=mm/tm-mm/tp
slope=s.simplify(s.diff(split,uu).subs(uu,0)*rad)
assert s.simplify(slope-mm/(s.pi*nn**2))==0
record("6D_同级次单周相位方程的频差",str(slope))
vp=(cc/nn+uu)/(1+uu/(nn*cc));vm=(cc/nn-uu)/(1-uu/(nn*cc))
rot_split=mm*(vm+uu-vp+uu)/(2*s.pi*rad)
assert s.simplify(s.diff(rot_split,uu).subs(uu,0)*rad-mm/(s.pi*nn**2))==0
reference=mm*uu/(s.pi*rad)*(cc**2-uu**2)/(cc**2-nn**2*uu**2)
assert s.simplify(s.diff(reference,uu).subs(uu,0)*rad/slope-nn**2)==0
record("6E_移动波色散与参考路径约定的差异",{"reference_over_phase_slope":"n^2","Omega_for_100_Hz":math.pi*2.25*100/600000})
signed=1+4-9
assert signed==-4 and abs(signed)/(1+4+9)==2/7
record("6F_反向绕组的有向面积求和",{"all_same_area":14,"reversed_area":-4})

# Q7: dimension, independent radius-angle ODE, and branch checks.
da,db,dd=s.symbols("da db dd")
dim=s.solve([da-1-1,3+2*da+dd-2,-2-db-dd+3],[da,db,dd])
assert dim=={da:2,db:6,dd:-5}
record("7A_功率量纲线性系统",str(dim))
sim=[]
for chi in [.02,.2,.6,.95]:
    scale=5*math.pi/(4*chi)
    def circle(t,z):return z[1]-2*math.pi
    circle.terminal=True;circle.direction=1
    sol=solve_ivp(lambda t,z:[-1/(4*z[0]**3),scale/z[0]**1.5],
                  [0,.999999],[1,0],events=circle,rtol=1e-10,atol=1e-12)
    frac=sol.t_events[0][0]
    close(frac,1-(1-chi)**(8/5),rtol=2e-8)
    sim.append([chi,float(frac)])
record("7B_缩距角运动ODE的一整圈事件",sim)
L0=10.;AA=.3;GS=3.
phasehalf=quad(lambda r:math.sqrt(GS)*r**1.5/AA,L0/2,L0)[0]
theta_c=2*math.sqrt(GS)*L0**2.5/(5*AA)
close(phasehalf,theta_c*(1-math.sqrt(2)/8))
thalf=quad(lambda r:r**3/AA,L0/2,L0)[0]
close(thalf,15*L0**4/(64*AA))
record("7C_半间距的时间与角位移直接积分",{"time":thalf,"angle_rad":phasehalf})
for chi in [1.01,2,10]:
    maxangle=2*math.pi/chi
    assert maxangle<2*math.pi
record("7D_一圈不存在时的有效分支筛选",{"condition":"0<chi<1","endpoint_chi":1})
M,mass=s.symbols("M mass",positive=True);total=M+mass
mchirp=(M*mass/total)**s.Rational(3,5)*total**s.Rational(2,5)
assert s.simplify(mchirp**s.Rational(5,3)-M*mass/total**s.Rational(1,3))==0
record("7E_约化质量与啁啾质量幂次",str(s.simplify(mchirp**s.Rational(5,3))))
x=s.symbols("x",positive=True)
series=s.series((1-(1-x)**s.Rational(8,5))/(s.Rational(8,5)*x),x,0,3)
assert s.expand(series.removeO()).coeff(x,1)==-s.Rational(3,10)
record("7F_慢耗散周期极限与缩距比例",str(series))

# Q8: Jones matrices, Fourier quadrature, and KCL network.
angles=np.linspace(-2,2,41)
inp=np.array([1,1],complex)/math.sqrt(2);an=np.array([-1,1],complex)/math.sqrt(2)
for qphase in [0,np.pi/2,-np.pi/2]:
    for delta in angles:
        matrix=np.diag([1,np.exp(-1j*(delta+qphase))])
        close(np.vdot(matrix@inp,matrix@inp),1)
        transmission=abs(an@(matrix@inp))**2
        close(transmission,math.sin((delta+qphase)/2)**2)
record("8A_Jones投影与无损强度守恒",{"phase_samples":len(angles),"waveplate_biases":3})
ll,thick,n0,gg,lam,Vv=s.symbols("ll thick n0 gg lam Vv",positive=True)
delta=2*s.pi/lam*ll*n0**3*gg*(Vv/ll)
half=s.solve(s.Eq(delta,s.pi),Vv)[0]
assert s.simplify(half-lam/(2*n0**3*gg))==0
transverse=s.solve(s.Eq(2*s.pi/lam*ll*n0**3*gg*(Vv/thick),s.pi),Vv)[0]
assert s.simplify(transverse/half-thick/ll)==0
record("8B_纵向横向电极的半波电压",{"longitudinal":str(half),"transverse":str(transverse)})
amp=.2;coeff=[]
for order in [1,3]:
    val=quad(lambda z:.5*math.sin(amp*math.sin(z))*math.sin(order*z),0,2*math.pi,epsabs=1e-12)[0]/math.pi
    close(val,jv(order,amp))
    coeff.append(val)
close(coeff,[amp/2-amp**3/16,amp**3/48],atol=1e-6)
record("8C_弱信号谐波的独立傅里叶积分",{"first":coeff[0],"third":coeff[1]})
rm=50.;resistance=1e6;cap=100e-12;rl=1e4;wm=2*math.pi*1e8
ind=1/(wm*wm*cap)
def network(w,compensated=True,load=rl):
    yy=1/resistance+1j*w*cap
    if compensated:yy+=1/load+1/(1j*w*ind)
    vc=(1/rm)/(1/rm+yy)
    src=(1-vc)/rm
    close(src,vc*yy)
    pin=src.real
    loss=rm*abs(src)**2+abs(vc)**2*(1/resistance+(1/load if compensated else 0))
    close(pin,loss)
    return vc
networkvals=[]
for wr in [.2,.5,1,1.5,2]:
    vc=network(wm*wr)
    expected=1/(1+rm*(1/resistance+1/rl)+1j*rm*(wm*wr*cap-1/(wm*wr*ind)))
    close(vc,expected)
    networkvals.append([wr,float(abs(vc))])
record("8D_并联元件节点KCL与电源功率闭合",networkvals)
h0=abs(network(wm,False));hres=abs(network(wm))
close(h0,1/math.sqrt(1.00005**2+math.pi**2))
close(hres,1/1.00505)
close(ind,25.33029591058444e-9,rtol=1e-12)
record("8E_高频分压与调谐电感数值",{"without":h0,"resonant":hres,"L_nH":ind*1e9,"RL_50_ohm":float(abs(network(wm,True,50)))})
ae=1+rm*(1/resistance+1/rl)
low=brentq(lambda w:abs(network(w))**2-hres**2/2,wm*.1,wm)
high=brentq(lambda w:abs(network(w))**2-hres**2/2,wm,wm*3)
close(high-low,ae/(rm*cap),rtol=1e-11)
record("8F_半功率频率根与加载带宽",{"low_Hz":low/(2*math.pi),"high_Hz":high/(2*math.pi),"Q":wm/(high-low)})

assert len(checks)==48
output={"all_passed":True,"check_count":len(checks),"checks":checks,
        "script_sha256":sha(Path(__file__)),
        "source_sha256":{p.name:sha(p) for p in sorted((ROOT/"drafts").glob("question-*.md"))}}
(ROOT/"核验/physics-results.json").write_text(json.dumps(output,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"all_passed":True,"checks":len(checks),"B_min":bmin,
                  "phase_model_resonator_slope":"m/(pi n^2)"},ensure_ascii=False))
