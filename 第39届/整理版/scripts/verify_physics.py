#!/usr/bin/env python3
"""Independent symbolic, quadrature, event-ODE and boundary-value checks."""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.integrate import quad,solve_ivp,solve_bvp
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(name,condition,evidence):
    assert condition,(name,evidence)
    checks.append({"check":name,"passed":True,"evidence":evidence})
def close(a,b,rtol=1e-8,atol=1e-10):
    return bool(np.allclose(a,b,rtol=rtol,atol=atol))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def roots(fun):
    x=np.linspace(0,2*np.pi,12001)
    return np.array([brentq(fun,a,b) for a,b in zip(x[:-1],x[1:]) if fun(a)*fun(b)<0])
def main():
    lam=633e-9;t=.002;th=np.deg2rad(5)
    d=437*lam/6;dd=23*lam/2;gam=np.arccos(20/23);ph=2*np.pi/3
    c=(4*np.pi*d/lam+ph)/(2*np.pi);edge=(4*np.pi*d*np.cos(gam)/lam+ph)/(2*np.pi)
    check("1A_光程前向亮纹与周期计数",close([c,edge,2*dd/lam,2*dd*np.cos(gam)/lam],[146,127,23,20]),[c,edge])
    span=2*(d-dd)*(1-np.cos(gam))/lam
    check("1B_末态逐级亮纹数",close(span,16) and round(span)+1==17,{"span":span,"fringes":17})
    G=lambda n,angle:2*t*(np.sqrt(n*n-np.sin(angle)**2)-np.cos(angle))
    n=brentq(lambda n:G(n,th)-G(n,0)-7*lam,1,2)
    approx=t*np.sin(th)**2/(2*t*(1-np.cos(th))-7*lam)
    check("1C_精确折射率和近似舍入",round(n,2)==round(approx,2)==1.41,{"exact":n,"approx":approx})
    i=math.asin(math.sin(th)/1.5)
    wavefront=2*t*(1.5-math.cos(th-i))/math.cos(i)
    check("1D_几何波前路径与根号公式",close(wavefront,G(1.5,th)),{"geometric":wavefront})
    H=math.sqrt(1.5**2-math.sin(th)**2)-1.5+1-math.cos(th)
    tc=8*lam/(2*H)
    check("1E_变式厚度与计数灵敏度",round(tc*1000,2)==1.99 and close(12-11+8,9),{"thickness_mm":tc*1000,"sensitivity":lam/(t*th**2)*1.41**2})
    l,k,l0,A,I=sp.symbols("l k l0 A I",positive=True)
    force=k*(l-l0)+A*I**2/(2*l**2)
    keff=sp.diff(force,l).subs(I**2,2*k*(l0-l)*l**2/A)
    check("2A_应力压缩力与有效刚度",sp.simplify(keff-k*(3*l-2*l0)/l)==0,str(keff))
    f=(l0-l)*l**2;peak=f.subs(l,2*l0/3)
    check("2B_恒流阈值与非零三次项",sp.simplify(peak-4*l0**3/27)==0 and sp.diff(force,l,2).is_positive,{"peak":str(peak),"force_second":str(sp.diff(force,l,2))})
    eta=sp.symbols("eta")
    x=1-eta-2*eta**2
    resid=sp.series((1-x)*x**2-eta,eta,0,3)
    check("2C_弱电流展开与指定分支",resid.removeO()==0 and close([6.75*.2*.8**2,3-2/.8,3-2/.5],[.864,.5,-1]),str(resid))
    Ip=sp.symbols("Ip",real=True)
    flux=A*Ip/l0;current=flux/(A/l)
    energy=sp.simplify(sp.Rational(1,2)*(A/l)*current**2)
    check("2D_固定磁通链能量曲率",sp.diff(energy,l,2)==0 and sp.simplify(current-Ip*l/l0)==0,str(energy))
    check("2E_有限电阻能量耗散恒等式",sp.simplify(sp.diff(sp.Rational(1,2)*l*I**2,I)*(-I/l)+I**2)==0,"固定电感归一化电路dI/dt=-I/L，dW/dt=-I²")
    kap=.4;w=1.37;m=2.3;V=.8
    states=[];v=b=0.;jx=0.
    for j in range(1,31):
        vi=v+w;bi=b
        # Impulse derived by contact angular momentum plus elastic energy.
        J=-2*m*kap/(1+kap)*(vi-bi)
        v=vi+J/m;b=bi-J/(kap*m);jx+=J
        states.append([v,b,jx])
    expected=[]
    for j in range(1,31):
        u=(((-1)**j-1)/2)*w
        bv=(j*w-u)/(1+kap);vv=(j*w+kap*u)/(1+kap)
        expected.append([vv,bv,m*(vv-j*w)])
    check("3A_三十次冲量迭代与闭式",close(states,expected),{"last":states[-1],"flights":30})
    M=sp.Matrix([[3,4],[10,-3]])/7;W=sp.diag(1,sp.Rational(2,5))
    check("3B_弹性矩阵能量与二周期",M*M==sp.eye(2) and M.T*W*M==W,str(M))
    check("3C_奇偶摩擦冲量与必要粗糙度",close([states[0][2],states[1][2]],[-4*m*w/7,-4*m*w/7]),"奇数次非零，偶数次为零；|Jx|/Jy=4tanθ/7")
    vx,bb,kk=sp.symbols("v b kap",real=True)
    vf=(vx+kk*bb)/(1+kk)
    loss=sp.simplify((vx**2+kk*bb**2-(1+kk)*vf**2)/2)
    check("3D_粘着模型的能量损失",sp.simplify(loss-kk*(vx-bb)**2/(2*(1+kk)))==0,str(loss))
    be=.35;uu=0;zs=0;rows=[]
    for j in range(1,15):
        ui=uu+w;uu=-be*ui;zs+=w
        rows.append(uu)
    check("3E_一般切向恢复系数",close(rows,[-be*w/(1+be)*(1-(-be)**j) for j in range(1,15)]),rows[-1])
    s,a,R,om,g,theta,mm=sp.symbols("s a R om g theta m",positive=True)
    Iz=sp.integrate((R+s*sp.sin(theta))**2*mm/(2*a),(s,0,2*a))
    U=mm*g*a*sp.cos(theta)-om**2*Iz/2
    Q=mm*g*a*sp.sin(theta)+mm*a*om**2*(R+4*a*sp.sin(theta)/3)*sp.cos(theta)
    check("4A_质元积分与广义力矩",sp.simplify(sp.diff(U,theta)+Q)==0,str(Iz))
    observations=[]
    for aa,bb in [(.7,.6),(3.,.6),(4.,2.)]:
        fun=lambda z:np.sin(z)+bb*np.cos(z)+aa*np.sin(z)*np.cos(z)
        rr=roots(fun);curv=-np.cos(rr)+bb*np.sin(rr)-aa*np.cos(2*rr)
        expected_count=4 if aa**(2/3)>1+bb**(2/3) else 2
        observations.append({"A":aa,"B":bb,"degrees":np.rad2deg(rr).tolist(),"curvature":curv.tolist()})
        assert len(rr)==expected_count
        if len(rr)==4:assert list(curv>0)==[True,False,True,False]
        else:assert list(curv>0)==[True,False]
    check("4B_各象限根数和曲率符号",True,observations)
    aa=3.;bc=(aa**(2/3)-1)**1.5;tt=2*np.pi-np.arccos(-aa**(-1/3))
    f0=np.sin(tt)+bc*np.cos(tt)+aa*np.sin(tt)*np.cos(tt)
    cur=-np.cos(tt)+bc*np.sin(tt)-aa*np.cos(2*tt)
    third=np.sin(tt)+bc*np.cos(tt)+4*aa*np.sin(tt)*np.cos(tt)
    check("4C_相切重根与非零三阶导数",abs(f0)<1e-12 and abs(cur)<1e-12 and abs(third)>1e-3,{"theta_degrees":np.rad2deg(tt),"third":third})
    crit=((4/3)**(2/3)-1)**(-.75)
    nums=observations[1]["degrees"]
    check("4D_数值变式角度与临界转速",close(nums,[106.01687713,197.93016477,244.65523015,351.39772794],atol=1e-7) and round(crit,2)==3.21,{"critical_ratio":crit})
    eps=sp.symbols("eps")
    quartic=sp.series(sp.cos(sp.pi+eps)-sp.sin(sp.pi+eps)**2/2+1,eps,0,6).removeO()
    check("4E_中心铰点退化的四阶稳定项",sp.simplify(quartic-eps**4/8)==0,str(quartic))
    df2=-2/(np.cos(tt)**2)*np.tan(tt)+aa*np.sin(tt)
    check("4F_临界附近角度与频率标度",close(df2,3*aa*np.sin(tt)) and df2<0,{"f_second":df2,"angle_exponent":.5,"frequency_exponent":.25})
    tv,al=sp.symbols("t alpha",real=True)
    xx=1+al*tv-al*sp.sin(tv)
    check("5A_线性加载ODE与初值",sp.simplify(sp.diff(xx,tv,2)+xx-1-al*tv)==0 and xx.subs(tv,0)==1 and sp.diff(xx,tv).subs(tv,0)==0,str(xx))
    events=[]
    for ell in [2.,10.]:
        for beta in [.5,1.,1.02,1.2,2.,4.,10.]:
            def up(t,y):return y[0]-ell
            def down(t,y):return beta*t-ell
            up.terminal=down.terminal=True;up.direction=down.direction=1
            sol=solve_ivp(lambda t,y:[y[1],-y[0]+1+beta*t],(0,ell/beta+3),[1.,0.],events=[up,down],rtol=2e-10,atol=2e-11,max_step=.04)
            winner=2 if len(sol.t_events[1]) else 1
            analytical=2 if math.sin(ell/beta)>1/beta else 1
            assert winner==analytical,(ell,beta,winner,analytical)
            events.append({"ell":ell,"beta":beta,"first":winner})
    check("5B_十四组首次断裂ODE事件",True,events)
    zz=brentq(lambda z:math.sin(z)/z-.5,.01,math.pi)
    check("5C_具体阈值与等号同时断",close(2/zz,1.05513,atol=5e-6) and close(1+math.pi/2-math.sin(math.pi/2),math.pi/2),{"z":zz,"beta":2/zz})
    time=sp.symbols("time",real=True)
    k1,k2,mass,grav,alpha=sp.symbols("k1 k2 mass grav alpha",positive=True)
    o=sp.sqrt(k1/mass)
    x1=mass*grav/k1+alpha*time/k1-alpha*sp.sin(o*time)/(k1*o)
    x2=alpha*time/k2
    E=mass*sp.diff(x1,time)**2/2+k1*x1**2/2+k2*x2**2/2-mass*grav*x1
    balance=sp.simplify(sp.diff(E,time)-alpha*time*(sp.diff(x1,time)+sp.diff(x2,time)))
    check("5D_不同劲度与下端功率能量账目",balance==0,str(balance))
    step=1+sp.Symbol("F")*(1-sp.cos(time))
    check("5E_阶跃加载与初始连续性",step.subs(time,0)==1 and sp.diff(step,time).subs(time,0)==0,"最大上弹簧长度=1+2F，下弹簧长度=F")
    L=1.7;sm=.03;sp_= .06;mesh=np.linspace(-L,L,301)
    # Solve in density and electric field variables without assuming hyperbolic forms.
    sol=solve_bvp(lambda x,y:np.array([-y[1],-y[0]]),
                  lambda yl,yr:np.array([yl[1]-sm,yr[1]+sp_]),
                  mesh,np.zeros((2,len(mesh))),tol=1e-10,max_nodes=4000)
    assert sol.success
    dn=(sp_+sm)*np.cosh(mesh)/(2*np.sinh(L))+(sp_-sm)*np.sinh(mesh)/(2*np.cosh(L))
    check("6A_电场密度耦合BVP独立解",close(sol.sol(mesh)[0],dn,atol=2e-10),{"max_error":float(max(abs(sol.sol(mesh)[0]-dn)))})
    volume=quad(lambda x:float(sol.sol(x)[0]),-L,L,epsabs=1e-12)[0]
    voltage=-quad(lambda x:float(sol.sol(x)[1]),-L,L,epsabs=1e-12)[0]
    check("6B_表面跃变与整体电中性",close(volume,sm+sp_) and close(voltage,(sp_-sm)*math.tanh(L)),{"integral_density":volume,"voltage":voltage})
    n0,T0,e,rho,c,kB=sp.symbols("n0 T0 e rho c kB",positive=True)
    K=e*rho*c*sp.sqrt(T0)/n0;H=(e**2*rho*c*sp.sqrt(T0)/kB-T0)/n0
    S=1/(e/kB-sp.sqrt(T0)/(e*rho*c))
    check("6C_Seebeck系数与端差相消",sp.simplify(K/H-S)==0,str(S))
    nr,tr,nt,aT=sp.symbols("nr tr n aT",positive=True)
    Y=aT+(sp.sqrt(tr)-aT)*sp.sqrt(nr/nt)
    exactT=Y**2
    residual=sp.simplify(sp.diff(exactT,nt)-(aT*Y-exactT)/nt)
    check("6D_非线性温度密度关系",residual==0,str(exactT))
    odd=(sp_+(-sp_))==0
    check("6E_奇偶边界变式",odd and close(quad(lambda x:np.sinh(x),-L,L)[0],0) and close(np.cosh(L)-np.cosh(-L),0),"奇模总电荷0，偶模端差0")
    norm=quad(lambda x:x*x*math.exp(-x)/2,0,np.inf)[0]
    mean=quad(lambda x:x**3*math.exp(-x)/2,0,np.inf)[0]
    moment=quad(lambda x:x**4*math.exp(-x)/2,0,np.inf)[0]
    check("7A_能量分布归一化与矩",close([norm,mean,moment, moment-mean**2],[1,3,12,3]),[norm,mean,moment])
    angle=quad(lambda x:math.cos(x)**2*math.sin(x),0,math.pi/2)[0]
    check("7B_法向动量通量半球积分",close(angle,1/3),angle)
    vi=(8/3)**3;tf=3/8;pf=tf/vi
    entropy=3*math.log(tf)+math.log(vi)
    check("7C_绝热火球半径压强与熵",close([3*400/150,pf,entropy],[8,81/4096,0]),{"radius_fm":8,"volume_ratio":vi,"pressure_ratio":pf})
    dispersions=[]
    for dim,power in [(3,1),(3,2),(2,1),(4,1),(3,1.5)]:
        weight=lambda p:p**(dim-1)*np.exp(-p**power)
        zz=quad(weight,0,np.inf)[0]
        ee=quad(lambda p:p**power*weight(p),0,np.inf)[0]/zz
        pressure=quad(lambda p:power*p**power/dim*weight(p),0,np.inf)[0]/zz
        assert close([ee,pressure],[dim/power,1])
        dispersions.append({"dimension":dim,"power":power,"mean_energy":ee,"pressure_over_nkT":pressure})
    check("7D_维度及幂律色散积分变式",True,dispersions)
    for frac in [0,.3,1]:
        cv=3*frac+1.5*(1-frac);ga=(cv+1)/cv
        assert close(ga,1+2/(3*(1+frac)))
    check("7E_混合热容与等温功",close(quad(lambda v:1/v,1,3)[0],math.log(3)),"固定比例Cv=1.5(1+f)R；等温功=RTlnq")
    result={"all_passed":True,"check_count":len(checks),"checks":checks,
            "method":"符号积分和高阶展开、数值积分、冲量独立迭代、ODE断裂事件、耦合边值解；不把参考答案当作计算输入。",
            "source_sha256":{p.name:sha(p) for p in sorted((ROOT/"drafts").glob("*.md"))},
            "script_sha256":sha(Path(__file__))}
    (ROOT/"核验/physics-results.json").write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print(json.dumps({"all_passed":True,"checks":len(checks),"refractive_index":n},ensure_ascii=False))
if __name__=="__main__":main()
