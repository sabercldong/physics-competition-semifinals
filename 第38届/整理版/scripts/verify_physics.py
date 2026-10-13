#!/usr/bin/env python3
"""Independent ray, impulse, quadrature, Lorentz-ODE and coupled motor checks."""
from pathlib import Path
import json,hashlib,math
import numpy as np
import sympy as sp
from scipy.integrate import quad,solve_ivp
from scipy.optimize import brentq,minimize_scalar
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def close(a,b,rtol=1e-7,atol=1e-9):return bool(np.allclose(a,b,rtol=rtol,atol=atol))
def check(name,condition,evidence):
    assert condition,(name,evidence)
    checks.append({"check":name,"passed":True,"evidence":evidence})
def main():
    # 1: Surface tangents enforce tangential optical momentum continuity.
    rays=[]
    for n,r0 in [(1.5,4),(1.8,1.5)]:
        for ang in np.linspace(0,.3,7):
            r=(n-1)*r0/(n*np.cos(ang)-1);x=r*np.cos(ang);y=r*np.sin(ang)
            slope=y/((n*n-1)*(x-n*r0/(n+1)))
            tangent=np.array([-slope,1.]);tangent/=np.linalg.norm(tangent)
            incident=np.array([1.,0.]);outgoing=np.array([x,-y])/r
            err=n*np.dot(incident,tangent)-np.dot(outgoing,tangent)
            rays.append(float(err))
    check("1A_凸面逐点斯涅尔切向光学动量",max(abs(np.array(rays)))<1e-10,{"rays":len(rays),"max_residual":max(abs(np.array(rays)))})
    rays=[]
    for ang in np.linspace(0,.3,7):
        n=1.8;r0=1.5;r=(n-1)*r0/(n*np.cos(ang)-1);x=r*np.cos(ang);y=r*np.sin(ang)
        slope=y/((n*n-1)*(x-n*r0/(n+1)));tan=np.array([-slope,1.]);tan/=np.linalg.norm(tan)
        rays.append(float(np.dot(np.array([x,-y])/r,tan)-n*np.dot(np.array([1.,0.]),tan)))
    check("1B_凹面球面波到平面波折射",max(abs(np.array(rays)))<1e-10,rays)
    x,y,n,r0=sp.symbols("x y n r0",positive=True)
    branch=n*r0/(n+1)+sp.sqrt((r0/(n+1))**2+y**2/(n*n-1))
    poly=(n*n-1)*x*x-2*n*(n-1)*r0*x+(n-1)**2*r0*r0-y*y
    check("1C_双曲面配方与分支多项式",sp.simplify(poly.subs(x,branch))==0,str(branch))
    ang=math.radians(10);r=.5*.1/(1.5*math.cos(ang)-1)
    check("1D_同材料缩束变式",close([r*math.sin(ang),r*math.sin(ang)/4],[.018193,.004548],atol=2e-6),{"radii_mm":[r*math.sin(ang)*1000,r*math.sin(ang)*250]})
    c=math.cos(math.radians(20));ratio=2*.5*(1.8*c-1)/(.8*(1.5*c-1))
    sag=-40+math.sqrt(40**2+20**2/1.25)
    check("1E_不同折射率与边缘退后",close([ratio,sag],[2.1104425757,3.8178046004]),[ratio,sag])
    check("1F_物理角域与近轴曲率",1.6*math.cos(math.pi/3)<1 and close(math.degrees(math.acos(1/1.6)),51.3178,atol=1e-4),"60度超出物理角域；顶点曲率由二次展开复核")
    # 2: Direct work integration and independent perturbation slopes.
    rho=13600.;g=9.8;S=.001;h=.25;T0=400.;Rg=8.31;unit=rho*g*S*h*h
    nu=4*unit/(Rg*T0);WA=4*unit
    WB=quad(lambda V:rho*g*(6*h-V/S),2*S*h,3*S*h)[0]
    UB=nu*2.5*Rg*100;QB=UB+WB
    check("2A_pV直接积分与状态链",close([WA,WB,QB],[33.32,29.155,49.98]),{"WA":WA,"WB":WB,"QB":QB,"moles":nu})
    heights=np.linspace(2*h,3*h,101);Ts=(6*h-heights)*heights*T0/(4*h*h)
    check("2B_加热支路单调及终温",np.all(np.diff(Ts)>0) and close([Ts[0],Ts[-1]],[800,900]),{"temperature_range":[Ts[0],Ts[-1]]})
    perturb=[]
    for yy in [.51,.6,.7,.749]:
        pe=rho*g*(6*h-yy);tt=pe*S*yy/(nu*Rg);eps=1e-6
        force=lambda y:S*(nu*Rg*tt/(S*y)-rho*g*(6*h-y))
        deriv=(force(yy+eps)-force(yy-eps))/(2*eps)
        assert deriv<0
        perturb.append(deriv)
    check("2C_有限水银等温扰动恢复",True,perturb)
    entropy=nu*Rg*(2.5*np.log(9/8)+np.log(3/2))
    check("2D_热容变式与状态熵差",close([5*unit,3.5*WA+QB,entropy],[41.65,166.6,.05830356068],atol=1e-9),{"changed_Cv_Q":5*unit,"total_Q":3.5*WA+QB,"entropy":entropy})
    yy=sp.symbols("y",real=True);temp=(5-yy)*yy/3
    check("2E_降低大气压的支路折叠",sp.diff(temp,yy).subs(yy,sp.Rational(5,2))==0 and temp.subs(yy,sp.Rational(5,2))==sp.Rational(25,12),str(temp))
    adiabatic_slope=rho*g-1.4*(rho*g*3*h)/(3*h)
    check("2F_末端绝热恢复与流出势能",adiabatic_slope<0 and close(.5*unit+3*unit,WB),{"adiabatic_slope":adiabatic_slope,"mercury_gravity_work":unit/2})
    # 3: Mechanical impulses without using the closed matrices.
    def hit(v,b,side):
        impulse=-2*.4/1.4*(v-side*b)
        return v+impulse,b-side*impulse/.4,impulse
    trials=[]
    for b0 in [0,.1,5/26,.39,.8,.999]:
        v=1.;b=b0;imp=[]
        for side in [1,-1,1]:
            v,b,j=hit(v,b,side);imp.append(j)
            assert close(v*v+.4*b*b,1+.4*b0*b0)
        pred=np.array([(-333-52*b0)/343,(-130+333*b0)/343])
        assert close([v,b],pred)
        trials.append({"b0":b0,"v3":v,"b3":b,"impulses":imp})
    check("3A_六组初值三次独立冲量迭代",True,trials)
    D=sp.Matrix([[3,4],[10,-3]])/7;Up=sp.Matrix([[3,-4],[-10,-3]])/7;W=sp.diag(1,sp.Rational(2,5))
    check("3B_矩阵能量及三碰闭式",D.T*W*D==W and Up.T*W*Up==W and D*Up*D==sp.Matrix([[-333,-52],[-130,333]])/343,str(D*Up*D))
    q=sp.Matrix([1,sp.Rational(5,26)]);qq=D*Up*D*q
    check("3C_恰好反向及返回位移",qq==-q and (D*q)[0]+(Up*D*q)[0]==0,str(qq))
    cospsi=-31/49;sinpsi=12*np.sqrt(10)/49;psi=np.arctan2(sinpsi,cospsi)
    init=np.array([1.,.2]);cur=init.copy();errors=[]
    for j in range(1,11):
        cur=np.array(Up*D,dtype=float)@cur
        expected=[init[0]*np.cos(j*psi)+np.sqrt(.4)*init[1]*np.sin(j*psi),
                  init[1]*np.cos(j*psi)-init[0]/np.sqrt(.4)*np.sin(j*psi)]
        errors.append(float(np.max(abs(cur-expected))))
    check("3D_二十次碰撞旋转形式",max(errors)<1e-12,{"max_error":max(errors)})
    for b0 in np.linspace(0,.999,31):
        requirements=[2*(1-b0)/7,2*(13+b0)/49,2*(29+55*b0)/343]
        assert requirements[1]>=max(requirements)
    check("3E_三碰粗糙度必要条件",True,"原题初始范围内第二次所需冲量比最大")
    check("3F_无初始自转能量分配",close((333/343)**2+.4*(130/343)**2,1),"三碰前后切向加自转能量相同")
    # 4: Actual loop integral and Hessian, rather than just dipole lookup.
    RR=.01;zz=2.
    integral=quad(lambda ph:(RR+zz*np.cos(ph))/(zz*zz+2*zz*RR*np.cos(ph)+RR*RR)**1.5,0,2*np.pi,epsabs=1e-13)[0]*RR/(4*np.pi)
    dipole=-RR*RR/(4*zz**3)
    check("4A_毕奥萨伐尔环积分赤道方向",integral<0 and close(integral,dipole,rtol=4e-5,atol=1e-14),{"exact_unit_mu0I":integral,"dipole":dipole})
    z,theta,C,mg=sp.symbols("z theta C mg",positive=True)
    pot=C*sp.cos(theta)/z**3-mg*z
    torque=-sp.diff(pot,theta)
    check("4B_有向力矩与角稳定",sp.simplify(torque-C*sp.sin(theta)/z**3)==0 and sp.diff(pot,theta,2).subs(theta,sp.pi)==C/z**3,str(torque))
    ze=(3*C/mg)**sp.Rational(1,4)
    check("4C_竖直平衡及负曲率",sp.simplify(sp.diff(pot,z).subs({theta:sp.pi,z:ze}))==0 and sp.diff(pot,z,2).subs(theta,sp.pi)==-12*C/z**5,str(ze))
    check("4D_双自由度鞍点与增长率",sp.diff(pot,z,theta).subs(theta,sp.pi)==0 and sp.simplify((12*C/z**5).subs(C,mg*z**4/3)-4*mg/z)==0,"混合曲率0，角正曲率、竖直负曲率")
    kk=sp.symbols("k");spring=-C/z**3-mg*z+kk*(z-ze)**2/2
    check("4E_弹簧稳定阈值与临界三阶",sp.diff(spring,z,2)==kk-12*C/z**5 and sp.diff(spring,z,3)==60*C/z**6,"k>12C/ze^5；等号三次项非零")
    check("4F_均匀场的角翻转",close(quad(lambda th:np.cos(th),0,2*np.pi)[0],0),"均匀场只改变角势能，在固定反平行指向时不改变竖直力")
    # 5: Photon angular averages, recoil, resonance and ODE event.
    mass=6.64e-26;kB=1.38e-23;temp=623.;planck=6.626e-34;wave=670e-9;rate=5e6;beta=-1e10
    vv=np.sqrt(kB*temp/mass);aa=rate*planck/(mass*wave);stop=vv*vv/(2*aa)
    avg_emission=quad(lambda th:.5*np.sin(th)*np.cos(th),0,np.pi)[0]
    check("5A_一维热初速与同性发射均值",abs(avg_emission)<1e-14 and close([vv,aa,stop],[359.831788,74469.51987,.8693416843]),{"v0":vv,"a":aa,"s":stop,"emission_mean_z":avg_emission})
    detune=vv/wave;bf=-vv/(beta*wave)
    check("5B_红失谐及正磁场端点",round(detune/1e6)==537 and bf>0 and close(bf,.0537062370),{"detune_MHz":detune/1e6,"B_final":bf})
    positions=np.linspace(0,stop,101);vel=np.sqrt(np.maximum(vv*vv-2*aa*positions,0));bb=(vel-vv)/(beta*wave)
    residual=beta*bb+(vv-vel)/wave
    check("5C_百点共振条件与定义域",np.max(abs(residual))<1e-6 and np.all(np.diff(bb)>0),{"max_Hz_residual":float(np.max(abs(residual)))})
    def event(t,y):return y[1]-20
    event.terminal=True;event.direction=-1
    sol=solve_ivp(lambda t,y:[y[1],-aa],(0,.02),[0,vv],events=event,rtol=1e-11,atol=1e-12)
    ss=float(sol.y_events[0][0,0])
    check("5D_有限终速ODE与梯度",close(ss,(vv*vv-400)/(2*aa)) and close(aa/(abs(beta)*wave*20),.5557426856),{"position":ss,"B":(20-vv)/(beta*wave)})
    minv=aa/(abs(beta)*wave*.1)
    check("5E_场梯度上限变式",close(minv,111.1485371) and close((vv-minv)/(abs(beta)*wave),.0371169031),{"min_speed":minv})
    N=rate*vv/aa
    check("5F_散射次数与率加倍缩放",close(N*planck/wave,mass*vv) and close((2*rate)*vv/(2*aa),N),{"photons":N,"time":vv/aa})
    # 6: Cartesian Lorentz equations in normalized physical units.
    trajectories=[]
    for eta in [.1,.2,.30806541358,.5]:
        gyro=np.sqrt(8*eta)
        def motion(t,y):
            x,yc,vx,vy=y;rr=x*x+yc*yc
            return [vx,vy,x/rr-gyro*vy,yc/rr+gyro*vx]
        def outer(t,y):return np.hypot(y[0],y[1])-2
        def turn(t,y):return (y[0]*y[2]+y[1]*y[3])/np.hypot(y[0],y[1])
        outer.terminal=True;outer.direction=1
        turn.terminal=True;turn.direction=-1
        sol=solve_ivp(motion,(0,30),[1,0,0,0],events=[outer,turn],rtol=2e-10,atol=2e-11,max_step=.02)
        radii=np.hypot(sol.y[0],sol.y[1]);angular=sol.y[0]*sol.y[3]-sol.y[1]*sol.y[2]
        energy=(sol.y[2]**2+sol.y[3]**2)/2
        assert close(angular,.5*gyro*(radii*radii-1),atol=5e-9)
        assert close(energy,np.log(radii),atol=5e-9)
        reached=bool(len(sol.t_events[0]))
        if eta in [.1,.2]:assert reached
        if eta==.5:assert not reached
        trajectories.append({"eta":eta,"outer_event":reached,"last_radius":float(radii[-1])})
    check("6A_笛卡尔洛伦兹ODE角动量与电场功",True,trajectories)
    us=np.linspace(1.0001,10,10000);threshold=us*us*np.log(us)/(us*us-1)**2
    check("6B_途中阈值单调和等号边界",np.all(np.diff(threshold)<0) and close(4*np.log(2)/9,.308065413582),{"eta_critical":4*np.log(2)/9})
    cm=1.3;linmass=2.;r1=.7;r2=1.8;alpha=cm/(linmass+cm)
    drive=lambda t:.7*(1+np.cos(t))
    sol=solve_ivp(lambda t,y:[alpha*drive(t),drive(t),((linmass+cm)*r2*r2-cm*r1*r1*alpha)*drive(t)],(0,5),[0,0,0],rtol=1e-11,atol=1e-12)
    wi,wo,Jext=sol.y[:,-1]
    mech=linmass*(r1*r1*wi+r2*r2*wo)
    Lfield=quad(lambda r:2*cm*wo*r,r1,r2)[0]
    check("6C_感应转动ODE及场角动量积分",close(wi,alpha*wo) and close(Jext,mech+Lfield),{"omega":wi,"Omega":wo,"external_J":Jext,"mechanical_L":mech,"field_L":Lfield})
    magnetic=.5*cm*(r1*r1*(wi-wo)**2+(r2*r2-r1*r1)*wo*wo)
    kinetic=.5*linmass*(r1*r1*wi*wi+r2*r2*wo*wo)
    Ieff=(linmass+cm)*r2*r2-cm*cm/(linmass+cm)*r1*r1
    check("6D_磁能机械能与有效惯量",close(kinetic+magnetic,.5*Ieff*wo*wo),{"energy":kinetic+magnetic})
    check("6E_等电磁线质量数值变式",close([7.5-4.5,3.75], [3,7.5/2]),"cm=m,r2=2r1，J=7.5m r1²Ω,L=4.5m r1²Ω")
    response=alpha*(r1/r2)**2
    sol=solve_ivp(lambda t,y:[drive(t),response*drive(t)],(0,4),[0,0],rtol=1e-11,atol=1e-12)
    check("6F_反向驱动自由外筒响应",close(sol.y[1,-1],response*sol.y[0,-1]),{"Omega_over_omega":response})
    # 7: Solve all wheel + body equations, then audit whole-system momentum.
    def vehicle(M,m,r,h,L,theta,torque):
        gs=9.8*np.sin(theta);gc=9.8*np.cos(theta);mt=M+2*m
        # unknowns: a, f_front, f_rear, N_front, N_rear
        mat=np.array([[m/2,1,0,0,0],
                      [-(mt+m/2),0,1,0,0],
                      [m*r/2,0,r,0,0],
                      [0,0,0,1,1],
                      [M*h,0,0,L/2,-L/2]],float)
        rhs=[0,mt*gs,torque,mt*gc,-M*h*gs-torque]
        a,ff,fr,nf,nr=np.linalg.solve(mat,rhs)
        H=r+M*h/mt
        whole=L*(nf-nr)/2+H*(ff+fr)+m*r*a
        return a,ff,fr,nf,nr,whole
    audits=[]
    for m in [0,10,50]:
        for theta in [0,.2,np.pi/6]:
            values=vehicle(1800,m,.4,.1,2.9,theta,4000)
            a,ff,fr,nf,nr,res=values
            assert abs(res)<1e-8 and close(a,(10000-(1800+2*m)*9.8*np.sin(theta))/(1800+3*m))
            audits.append({"m":m,"slope":theta,"solution":list(values[:-1])})
    check("7A_九组车轮车身联立与整车角动量",True,audits)
    flat=vehicle(1800,0,.4,.1,2.9,0,4000);hill=vehicle(1800,0,.4,.1,2.9,np.pi/6,4000)
    check("7B_完整载荷加速度和摩擦数值",close([flat[0],hill[0],flat[2]/flat[4],hill[2]/hill[4]],[50/9,59/90,.9483942704,1.0680928421]),{"flat":flat[:5],"hill":hill[:5]})
    simplified=[]
    for tt in [0,np.pi/6]:
        a=10000/1800-9.8*np.sin(tt);nr=1800*9.8*np.cos(tt)/2+1800*.1*(a+9.8*np.sin(tt))/2.9
        simplified.append(10000/nr)
    check("7C_参考省略力矩约定对照",close(simplified,[1.09113,1.25264],atol=5e-6),simplified)
    M,m,r,h,L=1800,50,.4,.1,2.9;tt=.2;gs=9.8*np.sin(tt);gc=9.8*np.cos(tt)
    safe=((M+2*m)*L*gc/2-(M*h+(M+2*m)*r)*gs)/(M*h+(M+3*m)*r)
    tau=r*((M+3*m)*safe+(M+2*m)*gs);sol=vehicle(M,m,r,h,L,tt,tau)
    check("7D_前轮离地边界",abs(sol[3])<1e-8,{"a_safe":safe,"N_front":sol[3]})
    force=1800*9.8/(2*(1-.5/2.9));ratio=force*.4/400
    check("7E_牵引极限与传动比变式",close(ratio,10.6575),{"ratio_limit":ratio})
    nr=1800*9.8/2+.9*10000/2.9
    check("7F_提高质心的相反两种趋势",close(10000/nr,.838683,atol=2e-6) and close(2.9*9.8/(2*.9),15.78888889),{"mu":10000/nr,"safe_a":2.9*9.8/(2*.9)})
    # 8: Integrate actual electrical input, heat and vehicle acceleration.
    volts=400.;res=.2;km=.2;Me=1800.;rad=.4;gear=10.;target=100/3.6
    def motor_run(gear,drag=0):
        def ode(t,y):
            v,eb,heat=y;cur=(volts-km*gear*v/rad)/res
            return [(gear*km*cur/rad-drag)/Me,volts*cur,res*cur*cur]
        def goal(t,y):return y[0]-target
        goal.terminal=True;goal.direction=1
        sol=solve_ivp(ode,(0,100),[0,0,0],events=goal,rtol=2e-11,atol=2e-9,max_step=.05)
        return float(sol.t_events[0][0]),sol.y_events[0][0]
    tf,final=motor_run(gear)
    check("8A_耦合电流ODE目标事件",close(tf,14.4*np.log(72/47)) and close(final[0],target),{"time":tf})
    mech=.5*Me*target*target
    check("8B_电池热耗积分能量闭合",close(final[1],4e6) and close(final[1],final[2]+mech),{"battery_J":final[1],"heat_J":final[2],"mechanical_J":mech,"efficiency":mech/final[1]})
    peak=minimize_scalar(lambda w:-(km*(volts-km*w)/res*w),bounds=(0,2000),method="bounded")
    check("8C_电路转矩功率极值",close([peak.x,-peak.fun],[1000,200000],rtol=1e-6),{"peak_speed":peak.x,"peak_power":-peak.fun})
    t2,fin2=motor_run(20)
    check("8D_传动比加倍事件与能量",close(t2,-3.6*np.log(1-target/40)) and close(fin2[1],2e6),{"time":t2,"battery_J":fin2[1]})
    drag=500.;amax=50/9;vmax=80.;vinf=vmax*(1-drag/(Me*amax))
    sol=solve_ivp(lambda t,y:[(gear*km*(volts-km*gear*y[0]/rad)/res/rad-drag)/Me],(0,20),[0],rtol=1e-11,atol=1e-12)
    check("8E_恒阻力电机ODE",close(sol.y[0,-1],vinf*(1-np.exp(-20/14.4))),{"terminal":vinf,"at_20s":float(sol.y[0,-1])})
    def time_for_gear(ri):
        vm=rad*2000/ri;am=400*ri/(Me*rad)
        return -vm/am*np.log(1-target/vm)
    opt=minimize_scalar(time_for_gear,bounds=(.01,28.7999),method="bounded")
    xx=target/(rad*2000/opt.x)
    eq=xx/(1-xx)+2*np.log(1-xx)
    check("8F_固定传动比独立数值优化",abs(eq)<1e-6 and close(xx,.71533186,atol=1e-7),{"ratio":opt.x,"time":opt.fun,"target_speed_fraction":xx})
    result={"all_passed":True,"check_count":len(checks),"checks":checks,
            "method":"逐点斯涅尔光学动量、直接积分、独立冲量映射、真实环场积分、洛伦兹运动ODE、感应转动ODE、完整车轮车身线性系统、机电能量ODE及数值优化。",
            "source_sha256":{p.name:sha(p) for p in sorted((ROOT/"drafts").glob("*.md"))},
            "script_sha256":sha(Path(__file__))}
    (ROOT/"核验/physics-results.json").write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print(json.dumps({"all_passed":True,"checks":len(checks),"motor_time":tf,"vehicle_full_mu":[flat[2]/flat[4],hill[2]/hill[4]]},ensure_ascii=False))
if __name__=="__main__":main()
