#!/usr/bin/env python3
"""Checks from full equations, field integrals and conservation laws."""
from pathlib import Path
import hashlib,json
import numpy as np
import sympy as s
from scipy.integrate import quad,solve_ivp
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(name,ok,detail=None):
    if not bool(ok):raise AssertionError((name,detail))
    checks.append({'check':name,'passed':True,'detail':detail})
def close(a,b,tol=1e-9):return np.allclose(a,b,rtol=tol,atol=tol)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
# 1: forward images, then recover focal length from measurable lengths.
F=6.;l=20.;u=np.array([66.,126.]);v=1/(1/F-1/u);li=l*v/u
rec=(u[1]-u[0])*li[0]*li[1]/(l*(li[0]-li[1]))
check('单透镜正向成像与两位置焦距反演',close(rec,F) and close(li,[2,1]))
f1,f2,d=s.symbols('f1 f2 d',nonzero=True)
T=lambda q:s.Matrix([[1,q],[0,1]])
L=lambda f:s.Matrix([[1,0],[-1/f,1]])
M=L(f2)*T(d)*L(f1);FF=f1*f2/(f1+f2-d);p=FF*d/f2;q=FF*d/f1
check('两透镜矩阵与主平面分解',all(s.simplify(x)==0 for x in M-T(q)*L(FF)*T(p)))
check('透镜矩阵行列式及无焦组合',s.simplify(M.det())==1 and close(np.array(M.subs({f1:80,f2:-30,d:50})).astype(float),[[.375,50],[0,8/3]]))
# 2: actual pressure force, Taylor coefficients, equilibrium derivatives.
x,tau=s.symbols('x tau',real=True);a=s.pi/2
force=s.sin(x)-tau*x/(1-4*x*x/s.pi**2)
c=s.Rational(1,6)+4/s.pi**2
critical=s.series(force.subs(tau,1),x,0,5).removeO()
check('临界活塞完整压强力的三次展开',s.simplify(critical+c*x**3)==0)
U=s.cos(x)-1-tau*s.pi**2/8*s.log(1-4*x*x/s.pi**2)
check('等温自由能势与完整动力学一致',s.simplify(s.diff(U,x)+force)==0)
fun=s.lambdify((x,tau),force,'numpy');der=s.lambdify((x,tau),s.diff(force,x),'numpy')
eqs=[]
for tv in [.2,.7,.95,.99]:
    root=brentq(lambda v:fun(v,tv),1e-7,np.pi/2-1e-6)
    omega=(np.sin(root)/root)*((np.pi**2/4+root**2)/(np.pi**2/4-root**2))-np.cos(root)
    eqs.append([tv,root,omega])
    assert close(-der(root,tv),omega) and omega>0
check('非中央平衡的完整求根与导数频率',True,eqs)
cn=float(c);small=1e-5
rt=brentq(lambda v:fun(v,1-small),1e-7,.1)
check('近平衡分支及低温频率的渐近系数',close(rt**2/small,1/cn,1e-4) and close(-der(rt,1-small)/small,2,1e-4))
pot=s.lambdify((x,tau),U,'numpy')
sol=solve_ivp(lambda z,y:[y[1],fun(y[0],.7)],(0,12),[.15,0],rtol=2e-11,atol=2e-12,max_step=.03)
ener=sol.y[1]**2/2+pot(sol.y[0],.7)
check('完整活塞方程积分的自由能第一积分',np.max(abs(ener-ener[0]))<2e-10)
I=quad(lambda z:1/np.sqrt(1-z**4),0,1)[0]
check('临界四次振子周期积分',close(I,1.311028777146,1e-9),{'integral':I,'period_coefficient':4*np.sqrt(2)*I})
# 3: solve ground-frame absolute translation, wedge equation, torque.
for mode in ['rolling','sliding']:
    errors=[]
    for MM in [.25,1.,10.]:
      for th in np.deg2rad([10,45,70]):
        ss,cc=np.sin(th),np.cos(th);mu0=2*(MM+1)/(7*MM+2)*np.tan(th);mu=.5*mu0
        # unknowns ac,a0,N1,f; mass m=g=1
        A=np.array([[cc,-1,-ss,cc],[-ss,0,-cc,-ss],[0,MM,-ss,cc],
                    [-.4,0,0,1] if mode=='rolling' else [0,0,-mu,1]])
        rhs=np.array([0,-1,0,0]);ac,a0,nn,ff=np.linalg.solve(A,rhs)
        if mode=='rolling':
            Dr=7*(MM+1)-5*cc**2
            target=[5*(MM+1)*ss/Dr,5*ss*cc/Dr,(7*MM+2)*cc/Dr,2*(MM+1)*ss/Dr]
            assert close(ff/nn,mu0)
        else:
            Ds=MM+1-cc**2-mu*ss*cc
            target=[(MM+1)*(ss-mu*cc)/Ds,cc*(ss-mu*cc)/Ds,MM*cc/Ds,mu*MM*cc/Ds]
            ap=ac-ff/.4
            assert ap>0
            # t=1, s=.5 ac, mechanical energy vs gravitational drop.
            vc=ac;v0=a0;wr=ff/.4
            kinetic=.5*MM*v0*v0+.5*((vc*cc-v0)**2+(vc*ss)**2)+.2*wr*wr
            heat=.5*ff*ap
            assert close(.5*ac*ss,kinetic+heat)
        errors.append(float(np.max(abs(np.array(target)-[ac,a0,nn,ff]))))
    check('球楔块'+('纯滚动：地面系完整受力与摩擦阈值' if mode=='rolling' else '滑动：地面系解、接触速度与耗散'),max(errors)<1e-10)
# 4: all eight statics equations solved together, including torque.
th=np.pi/4;cc,ss=np.cos(th),np.sin(th);R=2*(np.sqrt(2)-1);aa=16;bb=aa+4*R/np.tan(th/2);LL=30;mass=6
def bridge(W=0):
    # N1,N2,N3,N4,N5,f1,f2,f5
    A=np.array([[1,-cc,0,0,0,0,-ss,0],
        [0,-ss,0,0,0,1,cc,0],[0,0,0,0,0,1,-1,0],
        [0,0,1,-2*cc,0,0,0,0],[2,0,-1,0,0,0,0,0],
        [0,-cc,0,cc,1,0,-ss,0],[0,ss,0,-ss,0,0,-cc,1],
        [0,aa,0,-bb,0,0,-2*R,0]])
    b=np.array([-1,0,0,1,mass+W,mass,0,-mass*(LL/2*cc-R*ss)])
    out=np.linalg.solve(A,b);assert close(A@out,b)
    return out
n1,n2,n3,n4,n5,f_1,f_2,f5=bridge()
check('编木桥八个静力学方程的完整线性求解',
      close(bb,24) and min(n1,n2,n3,n4,n5)>0 and close(f_1,f_2),
      {'N1_over_mg':n1,'f_over_mg':f_1,'N5_over_mg':n5,'f5_over_mg':f5,'mu':f_1/n1,'mu_prime':abs(f5)/n5})
Dm=bb/cc+2*R*np.tan(th/2)-aa;alpha=bb/(2*cc*Dm)
nw=bridge(2)
check('编木桥中央附加载荷的完整重算',close(nw[0],n1+2*alpha) and close(nw[4],n5+1))
# exact tangency geometry for editable figure, scale 1/4.
rv=R/4;tv=np.array([cc,ss]);nv=np.array([-ss,cc]);ca=aa/4*tv+3*rv*nv;cb=bb/4*tv-rv*nv
check('编木桥圆柱接触几何与图稿坐标',close(cb[1]-ca[1],4*rv) and close(ca,[2.3890873,3.267767],1e-6) and close(cb,[4.3890873,4.096194],1e-6))
# 5: integrate Cartesian force, compare invariants and all radial branches.
for th in [.4,np.pi/2,2.0]:
    r0=2.;start=np.array([r0*np.sin(th),r0*np.cos(th),0,0])
    def field(t,y):
        pos=y[:2];rr=np.linalg.norm(pos)
        f=3*pos[1]*pos/rr**5-np.array([0.,1.])/rr**3
        return [y[2],y[3],f[0],f[1]]
    sol=solve_ivp(field,(0,2),start,rtol=2e-11,atol=2e-12,max_step=.015)
    rr=np.linalg.norm(sol.y[:2],axis=0);co=sol.y[1]/rr
    LLv=sol.y[0]*sol.y[3]-sol.y[1]*sol.y[2]
    en=.5*(sol.y[2]**2+sol.y[3]**2)+co/rr**2
    check(f'偶极子二维完整场积分：初角{th:.4f}',
       close(rr**2,r0*r0+2*np.cos(th)*sol.t**2/r0**2,2e-9)
       and close(LLv**2,2*(np.cos(th)-co),2e-9)
       and close(en,np.cos(th)/r0**2,2e-9))
th=np.arccos(-1/np.sqrt(3));pos=np.array([np.sin(th),np.cos(th)]);force=3*pos[1]*pos-np.array([0.,1.])
check('绕轴圆轨道：场投影、根筛选与向心速度',close(force[1],0) and force[0]<0 and close(-force[0]*pos[0],2/np.sqrt(3)))
J=quad(lambda u:(1-.5*np.sin(u)**2)**(-.5),0,np.pi/2)[0]
check('定半径半圆轨道的非小振幅周期积分',close(J,1.8540746773,1e-9))
# 6: currents and field integrals.
moment=.5*quad(lambda th:(-1.5*np.sin(th))*np.sin(th)**2,0,np.pi)[0]*2*np.pi
check('球面电流独立积分给出磁矩',close(moment,-2*np.pi))
axis=[]
for zz in [0,.7,3.]:
    # mu0=I=b=1; direct differential cross product z component.
    integ=quad(lambda phi:1/(1+zz*zz)**1.5,0,2*np.pi)[0]/(4*np.pi)
    axis.append(close(integ,1/(2*(1+zz*zz)**1.5)))
check('毕奥萨伐尔线积分复核轴上场',all(axis))
z,b=s.symbols('z b',positive=True)
B2=b**4/(4*(b*b+z*z)**3)
Favg=s.simplify(-s.pi*s.diff(B2,z)/2)
check('感应磁矩平均力由外场梯度推出',s.simplify(Favg-3*s.pi*b**4*z/(4*(b*b+z*z)**4))==0)
dp=s.diff(z/(b*b+z*z)**4,z)
check('平均力竖直稳定性与最优高度',s.simplify(dp-(b*b-7*z*z)/(b*b+z*z)**5)==0)
angular=quad(lambda th:np.sin(th)**3,0,np.pi)[0]*2*np.pi
check('趋肤层焦耳热的角积分',close(angular,8*np.pi/3))
delta=.05;radial=quad(lambda rr:rr*rr,1-delta,1)[0]
check('有限壳层体积与功率修正',close(radial/delta,1-delta+delta*delta/3))
# 7: solve pressure-temperature equations jointly.
gamma=1.4;mu=.029;g=9.8;RR=8.314;T0=288.;p0=101325.;Gamma=(gamma-1)*mu*g/(gamma*RR)
sol=solve_ivp(lambda z,y:[-mu*g*y[0]/(RR*y[1]),(gamma-1)/gamma*y[1]/y[0]*(-mu*g*y[0]/(RR*y[1]))],(0,10000),[p0,T0],rtol=2e-11,atol=2e-9)
Temp=T0-Gamma*sol.t;Pres=p0*(Temp/T0)**(gamma/(gamma-1))
check('大气静力学与绝热过程的联合积分',close(sol.y[0],Pres,2e-9) and close(sol.y[1],Temp,2e-9))
ratio=np.sqrt(263.15/218.15);crit=np.arcsin(1/ratio)
check('声速温度比与临界角',close(np.rad2deg(crit),65.5733692632,1e-9),{'speed_ratio':ratio,'critical_angle_degrees':float(np.rad2deg(crit))})
Re=6371.;hor=lambda hh:np.sqrt((Re+hh)**2-Re**2)
check('球面地平线距离的精确量级',2*hor(10)<1000 and hor(10)+hor(20)<1000,
      {'same_layer_km':2*hor(10),'mixed_layer_bound_km':hor(10)+hor(20)})
r1=Re+10;r2=Re+20;impact=.5*(r2/ratio+r1)
check('球面上下界面持续全反射的可行区间',impact<r1 and impact/r2>1/ratio and impact/r1>1/ratio)
# 8: solve conservation equations without using the wavelength shift.
Eka=17440.;hc=1240.;ryd=10973731.;Zeff=np.sqrt(4*Eka/(3*hc*ryd*1e-9))
check('X射线阈值、截止与有效核电荷数',close(hc/20100,.0616915423,1e-9) and 41<Zeff<42,{'Z_effective':Zeff,'Z':42,'lambda0_nm':hc/Eka})
errors=[]
for en in [.001,.034129,.7,10.]:
  for ang in [.01,.7,np.pi/2,np.pi]:
    cos=np.cos(ang)
    def conserved(out):return en+1-out-np.sqrt(1+en*en+out*out-2*en*out*cos)
    out=brentq(conserved,0,en,xtol=1e-14)
    errors.append(abs((1/out-1/en)-(1-cos)))
    electron=np.array([en-out*cos,-out*np.sin(ang)])
    kinetic=en-out
    assert close((1+kinetic)**2,1+electron@electron,1e-9)
    recoil=np.arctan2(abs(electron[1]),electron[0])
    assert close(np.tan(recoil),1/((1+en)*np.tan(ang/2)),1e-8)
check('相对论散射：直接求解能量动量与波长位移',max(errors)<2e-6,{'maximum_absolute_shift_error':max(errors)})
lambda0=hc/Eka;lc=.002426;angle=3*np.pi/4;lambda1=lambda0+lc*(1-np.cos(angle))
check('135度散射的峰位与电子能量',lambda1>lambda0 and hc/lambda1<Eka,
      {'lambda1_nm':lambda1,'electron_kinetic_eV':Eka-hc/lambda1})
data={'all_passed':True,'check_count':len(checks),'checks':checks,'script_sha256':sha(Path(__file__)),
      'source_sha256':{p.name:sha(p) for p in sorted((ROOT/'drafts').glob('*.md'))}}
(ROOT/'核验/physics-results.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
print(json.dumps({'all_passed':True,'check_count':len(checks),'details':[r for r in checks if r['detail']]},ensure_ascii=False,indent=2))
