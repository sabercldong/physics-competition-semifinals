#!/usr/bin/env python3
"""Independent equation solves, integrations and state enumeration.
Checks sampled parameters and the stated estimation conventions; it does
not turn heuristic uncertainty estimates into exact scattering predictions.
"""
from pathlib import Path
import hashlib,json,math
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
ROWS=[]
def check(name,actual,expected,rtol=2e-7,atol=1e-9,method=''):
    a=np.asarray(actual,dtype=float);e=np.asarray(expected,dtype=float)
    passed=bool(np.allclose(a,e,rtol=rtol,atol=atol))
    ROWS.append({'name':name,'method':method,'actual':a.tolist(),
                 'expected':e.tolist(),'rtol':rtol,'atol':atol,'passed':passed})
    assert passed,(name,a,e)
def golden(fun,a,b):
    g=(math.sqrt(5)-1)/2;c=b-g*(b-a);d=a+g*(b-a)
    for _ in range(140):
        if fun(c)<fun(d):b=d;d=c;c=b-g*(b-a)
        else:a=c;c=d;d=a+g*(b-a)
    return (a+b)/2
def rk4(fun,state,T,steps=8000):
    state=np.array(state,dtype=float);h=T/steps;t=0
    for _ in range(steps):
        k1=fun(t,state);k2=fun(t+h/2,state+h*k1/2)
        k3=fun(t+h/2,state+h*k2/2);k4=fun(t+h,state+h*k3)
        state+=h*(k1+2*k2+2*k3+k4)/6;t+=h
    return state
def main():
    # Q1: full two-coordinate mass/stiffness solve, not just a response formula.
    M,m,k,l,g,H=8.,.7,20.,3.2,9.8,1.3;w0=g/l
    mass=np.array([[M+m,m],[m,m]]);stiff=np.diag([k,m*w0])
    for w in [.2,.8,1.3,2.2]:
        xy=np.linalg.solve(stiff-w*w*mass,[H,0])
        D=(w0-w*w)*(k-M*w*w)-m*w0*w*w
        check(f'Q1 两自由度矩阵响应 ω={w}',xy,
              [H*(w0-w*w)/D,H*w*w/D],method='全质量矩阵与刚度矩阵线性求解')
    l=g*M/k;w=math.sqrt(k/M);w0=g/l
    xy=np.linalg.solve(np.diag([k,m*w0])-w*w*mass,[H,0])
    check('Q1 调谐反共振矩阵解',xy,[0,-H/(m*w0)])
    eta=101/9900;m2=eta*M;mass2=np.array([[M+m2,m2],[m2,m2]])
    eig=np.sort(np.linalg.eigvals(np.linalg.solve(mass2,np.diag([k,m2*w0]))))
    s=[(2+eta-math.sqrt(eta*eta+4*eta))/2,(2+eta+math.sqrt(eta*eta+4*eta))/2]
    check('Q1 调谐系统两固有频率',eig,w0*np.array(s),method='广义特征值求解')
    xy=np.linalg.solve(np.diag([k,m2*w0])-.99*w0*mass2,[H,0])
    check('Q1 百分之一振幅质量比',abs(xy[0])/(100*H/k),.01)
    # Nonlinear dissipative evolution, integrate external work and heating too.
    gamma=.25;nu=1.2
    def en(z):
        x,v,th,om=z[:4]
        return .5*(M+m)*v*v+m*l*v*om*math.cos(th)+.5*m*l*l*om*om+.5*k*x*x+m*g*l*(1-math.cos(th))
    def flow(t,z):
        x,v,th,om=z[:4]
        acc=np.linalg.solve([[M+m,m*l*math.cos(th)],[m*l*math.cos(th),m*l*l]],
                            [H*math.cos(nu*t)-k*x+m*l*om*om*math.sin(th),
                             -m*g*l*math.sin(th)-gamma*l*l*om])
        return np.array([v,acc[0],om,acc[1],H*math.cos(nu*t)*v,gamma*l*l*om*om])
    init=[.1,.12,.18,-.07,0,0];last=rk4(flow,init,5.)
    check('Q1 有限摆角能量功热平衡',en(last)-en(init),last[4]-last[5],rtol=1e-8,method='非线性ODE的RK4与独立功/热积分')

    # Q2: 3D angular velocity and planar translation integrated from Coulomb law.
    def slide(v,om,R,mu,g,kappa=.4,fraction=.8):
        v=np.array([*v,0.]);om=np.array(om);rc=np.array([0.,0.,-R]);u=v+np.cross(om,rc)
        T=kappa*np.linalg.norm(u)/((1+kappa)*mu*g)
        def f(t,z):
            vel=z[3:6];spin=z[6:9];uu=vel+np.cross(spin,rc);U=np.linalg.norm(uu)
            a=-mu*g*uu/U if U>1e-12 else np.zeros(3)
            return np.r_[vel,a,np.cross(rc,a)/(kappa*R*R)]
        state=rk4(f,np.r_[np.zeros(3),v,om],fraction*T,steps=2500)
        return state,T,u
    R,mu,gg=.12,.2,10.;v=np.array([.43,.25]);om=np.array([-8.,1.2,.7])
    state,T,u=slide(v,om,R,mu,gg)
    a=-mu*gg*u/np.linalg.norm(u);tt=.8*T
    check('Q2 滑动阶段质心位置',state[:3],np.r_[v,0]*tt+.5*a*tt*tt,method='平动/三维转动耦合ODE')
    check('Q2 接触点滑动速度衰减',state[3:6]+np.cross(state[6:9],[0,0,-R]),.2*u)
    check('Q2 竖直自旋保持',state[8],om[2])
    E0=.5*np.dot(v,v)+.5*.4*R*R*np.dot(om,om)
    Ef=.5*np.dot(state[3:6],state[3:6])+.5*.4*R*R*np.dot(state[6:9],state[6:9])
    check('Q2 滑动能量损失',E0-Ef,(1-.2**2)*np.dot(u,u)/7,method='平动与转动能独立合计')
    vf=np.r_[v,0]+a*T;omf=om+np.cross([0,0,-R],a)/(.4*R*R)*T
    check('Q2 最终纯滚条件',vf+np.cross(omf,[0,0,-R]),[0,0,0])
    for kap in [.4,2/3]:
        state,T,u=slide([1.,0],[0,0,0],R,mu,gg,kappa=kap,fraction=.75)
        check(f'Q2 一般惯量 κ={kap}',state[3:6],[1-.75*kap/(1+kap),0,0])
    def theta(ph):
        v=np.array([math.sin(ph)*math.cos(ph),math.sin(ph)**2,0.])
        slip=v+np.cross([-1.,0,0],[0,0,-1.])
        out=v-2*slip/7
        return math.atan2(out[0],out[1])
    ph=golden(lambda p:-theta(p),0,math.pi/2)
    check('Q2 30度规则极大位置',ph,.5*math.acos(5/9),rtol=1e-7,method='最终向量速度的黄金分割极值搜索')
    table=[math.degrees(theta(.5*math.acos(5/9)+math.radians(d))) for d in [0,5,10,-5,-10]]
    check('Q2 30度规则角度表',table,[33.75,33.23,31.87,33.09,30.76],rtol=0,atol=.005)

    # Q3: minimize original two-variable empirical expression along the path.
    beta=.00728
    def sig(T):p=beta*T;return 60+.065*T-24*p+3.15*p*p
    Tf=golden(sig,250,400);tw=1.48*(Tf-273.15)-48
    check('Q3 原经验式温度极小',Tf,.10972/(6.30*beta*beta),rtol=1e-7,method='原始温压公式约束极小搜索')
    check('Q3 注水温度',tw,34.08272103859859,rtol=1e-6)
    check('Q3 热容量平衡',.48*(100-(Tf-273.15)),(Tf-273.15)-tw)
    # Periodic cubic lattice vs slab: enumerate unique bonds, both free faces.
    side=7;sites={(x,y,z) for x in range(side) for y in range(side) for z in range(side)}
    def bonds(periodic_z):
        out=set()
        for p in sites:
            for ax in range(3):
                q=list(p);q[ax]+=1
                if ax!=2 or periodic_z:q[ax]%=side
                q=tuple(q)
                if q in sites:out.add(tuple(sorted((p,q))))
        return out
    lost=len(bonds(True))-len(bonds(False))
    check('Q3 表面键双计数',lost/(2*side*side),.5,method='三维晶格唯一键集合与双表面形成能')

    # Q4 numeric conventions: relativistic energy, independent inverse E-p relation.
    h,e,eps,c,me=6.63e-34,1.6e-19,8.85e-12,3e8,9.11e-31
    dx=.85e-15/100;p=h/(2*math.pi)/(2*dx);pc=p*c;rest=me*c*c
    K=math.hypot(pc,rest)-rest
    check('Q4 相对论层析能量 GeV',K/(e*1e9),11.63769278737632)
    inverse=math.sqrt(K*(K+2*rest))/c
    check('Q4 能量逆算动量',inverse/p,1.,method='相对论能量逆关系')
    check('Q4 极端相对论误差百分数',100*(pc-K)/K,.004403159869308666)
    vstar=e*e/(eps*h)
    check('Q4 散射局部估算速度',vstar,4362979.437755111)
    check('Q4 电磁耦合尺度',2*(e*e/(4*math.pi*eps*(h/(2*math.pi))*c))*c,vstar)
    q=2*1.01/(1.01**2-1)
    check('Q4 1%误差边界', (q-(math.sqrt(1+q*q)-1))/(math.sqrt(1+q*q)-1),.01)

    # Q5 finite wire sum and its numerical Jacobian.
    a,b,I,mu0=2.4,1.7,1.8,1.3;coef=16*mu0*a*b*I/(math.pi*(a*a+b*b)**2)
    def field(x,y):
        B=np.zeros(2)
        for s in [-1,1]:
            for t in [-1,1]:
                d=np.array([x-s*a/2,y-t*b/2]);B+=mu0*I/(2*math.pi)*(-s*t)*np.array([-d[1],d[0]])/np.dot(d,d)
        return B
    check('Q5 四导线中心场',field(0,0),[0,0])
    step=1e-5;jac=np.column_stack(((field(step,0)-field(-step,0))/(2*step),(field(0,step)-field(0,-step))/(2*step)))
    check('Q5 近轴雅可比',jac,[[-coef,0],[0,coef]],method='四根原始Biot—Savart场有限差分')
    rr=1e-4;pts=[np.linalg.norm(field(rr*math.cos(t),rr*math.sin(t))) for t in np.linspace(0,2*math.pi,13)]
    check('Q5 近轴径向场强',pts,[coef*rr]*13,rtol=1e-7)
    grid=(np.arange(100000)+.5)/100000
    check('Q5 均匀圆盘平均势能',np.sum(2*grid*grid)/len(grid),2/3,method='圆环微元数值积分')
    check('Q5 均匀圆盘势能方差',np.mean(2*grid**3)-(np.mean(2*grid**2))**2,1/18)
    check('Q5 收缩后粒子数总能平均能',[(.2)**2,(.2)**3,.2],[1/25,1/125,1/5])

    # Q6 integrate Cartesian Kepler equations from a finite remote point.
    b,v,GM=2.,1.4,.08;X=120.
    # Position (-X,b), energy at infinity 1/2 v^2; speed adjusted for potential.
    r=math.hypot(X,b);speed=math.sqrt(v*v+2*GM/r)
    def orbit(t,z):
        rad=np.linalg.norm(z[:2]);return np.r_[z[2:],-GM*z[:2]/rad**3]
    state=rk4(orbit,[-X,b,speed,0],2*X/v,steps=40000)
    Ei=.5*speed*speed-GM/r;Ef=.5*np.dot(state[2:],state[2:])-GM/np.linalg.norm(state[:2])
    check('Q6 笛卡尔引力轨道能量守恒',Ef,Ei,rtol=1e-8,method='笛卡尔RK4引力轨道积分')
    Li=-b*speed;Lf=state[0]*state[3]-state[1]*state[2]
    check('Q6 笛卡尔引力轨道角动量',Lf,Li,rtol=1e-8)
    deflection=abs(math.atan2(state[3],state[2]))
    check('Q6 双曲散射角',deflection,2*math.atan(GM/(b*v*v)),rtol=.001,atol=1e-5,method='有限远处数值轨道与无穷远解比较；保留边界误差')
    # Direct light-ray integration: dx as parameter, angle derivative from n gradient.
    q,b=.002,1.;X=80.
    def ray(x,z):
        y,ang=z;r=math.hypot(x,y);n=1+q/r
        nx=-q*x/r**3;ny=-q*y/r**3
        return np.array([math.tan(ang),(-nx*math.sin(ang)+ny*math.cos(ang))/(n*math.cos(ang))])
    state=rk4(lambda t,z:ray(t-X,z),[b,0],2*X,steps=50000)
    exact=2*math.acos(-q/b)/math.sqrt(1-q*q/(b*b))-math.pi
    check('Q6 光学笛卡尔射线偏折',abs(state[1]),exact,rtol=.0002,atol=1e-7,method='折射率梯度射线ODE与完整光学模型解')

    # Q7 enumerate every one-particle integer level, choose N smallest.
    def enum(N,f):
        n=np.arange(-100,101);ener=(n+f)**2;idx=np.argsort(ener)[:N]
        return float(np.sum(ener[idx])),sorted(n[idx].tolist())
    def formula(N,f):
        red=(f+.5)%1-.5
        return N*((N*N-1)/12+(red**2 if N%2 else (abs(red)-.5)**2))
    for N in [1,2,3,4,9,10]:
        fs=[-.5,-.31,0,.19,.5,2.3]
        check(f'Q7 {N}粒子整数能级穷举',[enum(N,f)[0] for f in fs],
              [formula(N,f) for f in fs],method='单电子能级排序和占据穷举')
    check('Q7 磁通周期穷举',[enum(9,.31)[0],enum(10,-.23)[0]],
          [enum(9,1.31)[0],enum(10,.77)[0]])
    for N in [5,6]:
        for parity,f in [(1,0),(0,.5)]:
            cases=[(enum(j,f)[0]+enum(2*N-j,f)[0],j,2*N-j)
                   for j in range(1,2*N) if j%2==parity]
            best=min(cases)
            expect=0 if N%2==parity else 2
            check(f'Q7 双环总数{2*N} 奇偶{parity}最优分配',abs(best[1]-best[2]),expect,method='全部允许分配的能量穷举')
    for M in [1,9,10]:
        A=(enum(2*M+1,0)[0]*2)/(4*M+2)
        B=(enum(2*M+2,.5)[0]+enum(2*M,.5)[0])/(4*M+2)
        check(f'Q7 双环a/b比 M={M}',A/B,4*M*(M+1)/(4*M*(M+1)+3))
    check('Q7 非中心磁通整数集合',enum(5,2.3)[1],[-4,-3,-2,-1,0])
    payload={'all_passed':True,'checks':ROWS,'check_count':len(ROWS),
             'scope':'选定参数下独立方程、数值积分与整数态穷举；不是所有参数和全部28变式的普遍证明。Q4按明示局域化与局部变化估算约定。',
             'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/'drafts').glob('*.md'))},
             'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'核验/physics-results.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2))
    print(json.dumps({'all_passed':True,'check_count':len(ROWS),'table':table,'Tf':Tf,'tw':tw},ensure_ascii=False))
if __name__=='__main__':main()
