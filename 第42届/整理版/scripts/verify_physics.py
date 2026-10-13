#!/usr/bin/env python3
"""Independent quadrature, port-network solves and ODE checks for edition 42.
Checks are numerical evidence over specified parameters, not proofs for all inputs.
"""
from pathlib import Path
import json, math, hashlib
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
CHECKS=[]
def check(name,computed,expected,tol=1e-8,details=None):
    x=np.array(computed,dtype=float);y=np.array(expected,dtype=float)
    err=float(np.max(np.abs(x-y)))
    record={"name":name,"computed":x.tolist(),"expected":y.tolist(),"max_abs_error":err,"tolerance":tol,"passed":err<=tol}
    if details:record["details"]=details
    CHECKS.append(record)
    assert record["passed"],record

def quad(f,a,b,n=240):
    x,w=np.polynomial.legendre.leggauss(n)
    return float(np.dot(w,np.array([f(t) for t in (a+b)/2+(b-a)*x/2]))*(b-a)/2)
def golden(f,a,b,maximum=False):
    ratio=(math.sqrt(5)-1)/2
    g=(lambda t:-f(t)) if maximum else f
    c=b-ratio*(b-a);d=a+ratio*(b-a)
    for _ in range(130):
        if g(c)<g(d):b,d=d,c;c=b-ratio*(b-a)
        else:a,c=c,d;d=a+ratio*(b-a)
    return (a+b)/2

def rk4(fun,y0,end,steps=14000):
    y=np.array(y0,dtype=float);h=end/steps;t=0.
    data=[y.copy()]
    for i in range(steps):
        k1=fun(t,y);k2=fun(t+h/2,y+h*k1/2);k3=fun(t+h/2,y+h*k2/2);k4=fun(t+h,y+h*k3)
        y+=h*(k1+2*k2+2*k3+k4)/6;t+=h;data.append(y.copy())
    return np.linspace(0,end,steps+1),np.array(data)

# Q1: integrate the original joint Gaussian at the detection plane.
s=.7;omega=2.3;g=1.1;h=1.4;t=1.3;a=s/omega
H=h-g*t*t/2;A=1+omega**2*t*t
n=math.exp(-omega**2*H*H/(2*s*s*A))*omega/(math.sqrt(2*math.pi)*s*math.sqrt(A))
u=g*t+omega**2*H*t/A;q=s/math.sqrt(A)
phi=lambda x:math.exp(-x*x/2)/math.sqrt(2*math.pi)
Phi=lambda x:(1+math.erf(x/math.sqrt(2)))/2
joint=lambda v:math.exp(-((H-v*t)/a)**2/2-(v/s)**2/2)/(2*math.pi*a*s)
check("Q1 Gaussian density from initial position/velocity quadrature",quad(joint,-9*s,9*s),n,2e-12)
check("Q1 downward-only flux from velocity-domain quadrature",quad(lambda v:(v+g*t)*joint(v),-g*t,9*s),n*(u*Phi(u/q)+q*phi(u/q)),2e-12)
check("Q1 signed net flux from complete velocity-domain quadrature",quad(lambda v:(v+g*t)*joint(v),-9*s,9*s),n*u,2e-12)
g=1.;h=1.;s=.2;t0=math.sqrt(2*h/g);eta=s*s/(g*h)
density=lambda t:math.exp(-(h/t-g*t/2)**2/(2*s*s))/t
flux=lambda t:(h/t**2+g/2)*math.exp(-(h/t-g*t/2)**2/(2*s*s))/(math.sqrt(2*math.pi)*s)
tn=math.sqrt(2*(math.sqrt(s**4+g*g*h*h)-s*s)/g**2)
roots=np.roots([1,1,4*eta-1,-1]);x=float([v.real for v in roots if abs(v.imag)<1e-9 and v.real>0][0]);ti=t0*math.sqrt(x)
check("Q1 density and flux peak direct optimization",[golden(density,.7*t0,1.3*t0,True),golden(flux,.7*t0,1.3*t0,True)],[tn,ti],4e-8)
check("Q1 strong-trap integrated arrival flux equals total particle number",quad(flux,.2,4.,420),1.,3e-12)

# Q2: analyzer trajectory, focusing and nonuniform slit response.
D=1.;A=4.;theta=math.pi/6
X=lambda v:A*math.sin(2*v)+D/math.tan(v)
fstep=.0001
first=(X(theta+fstep)-X(theta-fstep))/(2*fstep)
second=(X(theta+fstep)-2*X(theta)+X(theta-fstep))/fstep**2
check("Q2 second-order focus first and second derivatives",[first,second],[0,0],1.5e-6)
check("Q2 residual displacement leading cubic",(X(theta+.001)-X(theta-.001))/2, -16*D*.001**3,2e-13)
# Actual line intersection after electric-field flight, no use of detector-map formula.
K=2.;qion=1.;Va=1.;d=.5;Y1=.25;Y2=.75;XD=3*math.sqrt(3)
tha=.22;thb=.34;l=.013;ti0=theta
v=math.sqrt(2*K);acc=qion*Va/d
# Upward y; positive l moves the source right and down according to the original.
r0=np.array([l*math.cos(tha),-Y1-l*math.sin(tha)])
vy=v*math.sin(ti0);vx=v*math.cos(ti0)
entertime=-r0[1]/vy;xentry=r0[0]+vx*entertime
xexit=xentry+vx*(2*vy/acc)
# Detector point=(XD-s*cos thb,-Y2-s*sin thb); outgoing slope=-tan ti0.
s_direct=(math.tan(ti0)*(XD-xexit)-Y2)/(math.sin(thb)+math.tan(ti0)*math.cos(thb))
ca=math.cos(tha)*math.tan(ti0)+math.sin(tha);cb=math.cos(thb)*math.tan(ti0)+math.sin(thb)
Q=XD*math.tan(ti0)-D-4*K*d/(qion*Va)*math.sin(ti0)**2
check("Q2 independent ballistic intersection with inclined detector",s_direct,(Q-ca*l)/cb,2e-12)
bias=.3;uu=.24
upper=quad(lambda z:1+bias*z,uu,1);lower=quad(lambda z:1+bias*z,-1,uu)
asym=(upper-lower)/(upper+lower)
check("Q2 nonuniform slit asymmetry integral and inversion",[asym,(-1+math.sqrt(1-2*bias*asym+bias*bias))/bias],[-uu+bias*(1-uu*uu)/2,uu],2e-12)

# Q3: solve all 8 port equations/device, external-node KCL and one voltage gauge.
def port_network(rc,connections,inj,r=1.):
    rc=np.array(rc);dev,nport=rc.shape
    assert nport==8
    groups=[[8*j+i] for j in range(dev) for i in range(8)]
    for connection in connections:
        items=[8*j+(i-1) for j,i in connection]
        related=[group for group in groups if any(k in group for k in items)]
        groups=[group for group in groups if group not in related]+[sum(related,[])]
    group_index={p:gi for gi,group in enumerate(groups) for p in group}
    currents=dev*8;variables=currents+len(groups);rows=[];rhs=[]
    for j in range(dev):
        for i in range(8):
            p=j*8+i;prev=j*8+(i-1)%8
            row=np.zeros(variables)
            row[currents+group_index[p]]+=1;row[currents+group_index[prev]]-=1
            row[p]-=rc[j,i]+2*r;row[prev]+=rc[j,(i-1)%8]
            rows.append(row);rhs.append(0.)
    injected={group_index[8*j+i-1]:value for (j,i),value in inj.items()}
    for gi,group in enumerate(groups):
        row=np.zeros(variables)
        for p in group:row[p]=1
        rows.append(row);rhs.append(injected.get(gi,0.))
    gauge=np.zeros(variables);gauge[-1]=1;rows.append(gauge);rhs.append(0.)
    matrix=np.array(rows);out=np.linalg.lstsq(matrix,np.array(rhs),rcond=None)[0]
    assert np.linalg.matrix_rank(matrix)==variables
    assert np.max(np.abs(matrix@out-rhs))<3e-13
    I=out[:currents].reshape(dev,8)
    T=np.array([out[currents+group_index[p]] for p in range(currents)]).reshape(dev,8)
    return I,T
rc=np.array([[.011,.012,.013,.014,.015,.016,.017,.018]])
I,T=port_network(rc,[],{(0,1):1.,(0,5):-1.})
check("Q3 single-device four-terminal result with all contacts nonzero",T[0,2]-T[0,6],2.,2e-12)
rc=np.array([[.0011,.0012,.0013,.0014,.0015,.0016,.0017,.0018],
             [.0021,.0022,.0023,.0024,.0025,.0026,.0027,.0028]])
aa=rc[0,4]+rc[1,0];bb=rc[0,6]+rc[1,2]
I,T=port_network(rc,[[(0,5),(1,1)]],{(0,1):1.,(1,5):-1.})
check("Q3 open series complete port-network solve",T[0,2]-T[1,6],4+aa,3e-12)
I,T=port_network(rc,[[(0,5),(1,1)],[(0,7),(1,3)]],{(0,1):1.,(1,5):-1.})
check("Q3 compensated series complete port-network solve",[T[0,2]-T[1,6],I[1,2]],[4+aa*bb/(4+aa+bb),aa/(4+aa+bb)],3e-12)
rc=np.array([[.11,.12,.13,.14,0,0,0,.18],[.21,.22,.23,.24,0,0,0,.28]])
connect=[[(0,i),(1,i)] for i in [1,2,3,5,6,7]]
I,T=port_network(rc,connect,{(0,1):1.,(0,5):-1.})
S=rc.sum(axis=0);Diff=rc[0]-rc[1]
i2=2*Diff[0]/((4+S[0])*(4+S[1]));i3=S[1]*i2/(4+S[2]);rr=1+Diff[0]*S[1]*Diff[2]/((4+S[0])*(4+S[1])*(4+S[2]))
check("Q3 triple parallel complete port-network currents and voltage",[I[0,1],I[0,2],T[0,2]-T[0,6]],[i2,i3,rr],3e-12)

# Q4: integrate Lorentz force in lab time, optimize injection direction, integrate radiation ODE.
a=1.3
def lorentz(t,y):
    ux,uz,xx,zz=y;gam=math.sqrt(1+ux*ux+uz*uz);co=math.cos(t-zz)
    return np.array([-a*(1-uz/gam)*co,-a*ux/gam*co,ux/gam,uz/gam])
ts,ys=rk4(lorentz,[0,0,0,0],12.,18000)
phase=ts-ys[:,3];analytic=np.column_stack((-a*np.sin(phase),a*a*np.sin(phase)**2/2,a*(np.cos(phase)-1),a*a*(phase-np.sin(2*phase)/2)/4))
check("Q4 lab-time Lorentz ODE vs parametric momentum and trajectory",float(np.max(np.abs(ys-analytic))),0.,3e-9)
check("Q4 light-front invariant over entire integrated orbit",float(np.max(np.abs(np.sqrt(1+ys[:,0]**2+ys[:,1]**2)-ys[:,1]-1))),0.,3e-10)
gamma0=2.2;P=math.sqrt(gamma0**2-1)
peak=lambda th:gamma0+(a*a+2*a*P*math.sin(th))/(2*(gamma0-P*math.cos(th)))
thopt=math.atan(2/(a*gamma0+P*math.sqrt(a*a+4)))
check("Q4 direct injection-angle optimization",[golden(peak,0,math.pi,True),peak(thopt)],[thopt,((a*a+2)*gamma0+a*P*math.sqrt(a*a+4))/2],4e-8)
e=1.602e-19;mu=4*math.pi*1e-7;m=9.101e-31;c=2.998e8;intensity=1e26;wavelength=800e-9
rad=e**4*mu**2*intensity/(2*math.pi*m**4*c**4);energy0=1000*m*c*c;tau=wavelength/c;radchi=rad*energy0*tau
_,y=rk4(lambda t,y:np.array([-radchi*y[0]**2]),[1.],1.,3000)
check("Q4 nonlinear radiation loss over one optical period",y[-1,0],1/(1+radchi),2e-12,{"chi":radchi,"fractional_loss":-radchi/(1+radchi)})

# Q5: integrate current density, check soliton field and local well curvature.
chi=.82;delta0=.65
check("Q5 Josephson integrated current over width",quad(lambda yy:math.sin(delta0+2*chi*yy),-.5,.5),math.sin(delta0)*math.sin(chi)/chi,2e-12)
z=np.linspace(-4,4,91);delta=lambda z:4*math.atan(math.exp(z));step=.0001
sg=[(delta(v+step)-2*delta(v)+delta(v-step))/step**2-math.sin(delta(v)) for v in z]
check("Q5 sine-Gordon fluxon via finite-difference second derivative",max(abs(v) for v in sg),0.,3e-7)
i=.37;stable=math.asin(i);saddle=math.pi-stable;U=lambda de:-math.cos(de)-i*de
check("Q5 tilted-well barrier from stationary-point energies",U(saddle)-U(stable),2*(math.sqrt(1-i*i)-i*math.acos(i)),2e-12)
_,y=rk4(lambda t,y:np.array([y[1],i-math.sin(y[0])]),[stable,1e-5],30.,22000)
# positive zero crossings of displacement, interpolate instead of selecting a timestep.
disp=y[:,0]-stable;cross=[];tgrid=np.linspace(0,30.,22001)
for j in range(len(disp)-1):
    if disp[j]<=0 and disp[j+1]>0:cross.append(tgrid[j]-disp[j]*(tgrid[j+1]-tgrid[j])/(disp[j+1]-disp[j]))
measured=float(np.mean(np.diff(cross)))
check("Q5 RCSJ small-oscillation period from independent nonlinear ODE",measured,2*math.pi/(1-i*i)**.25,2e-7)
check("Q5 junction propagation speed ratio",math.sqrt(3/(9*(3+2*53))),.0553,2e-5)

# Q6: freely rotating rotor, numerical curvatures and nonzero-shaft-inertia limit.
k=1.;J=1.4;theta0=.7;omega0=math.sqrt(k*theta0/(J*math.sin(theta0)*math.cos(theta0)));Pz=J*math.sin(theta0)**2*omega0
freq=math.sqrt(k/J+omega0**2*(1+2*math.cos(theta0)**2))
V=lambda th:Pz**2/(2*J*math.sin(th)**2)+k*th*th/2
step=2e-4
check("Q6 fixed-angular-momentum effective-potential curvature",(V(theta0+step)-2*V(theta0)+V(theta0-step))/step**2/J,freq**2,6e-7)
tgrid,y=rk4(lambda t,y:np.array([y[1],-k*y[0]/J+Pz**2*math.cos(y[0])/(J*J*math.sin(y[0])**3)]),[theta0,1e-5],20.,16000)
disp=y[:,0]-theta0;cross=[]
for j in range(len(disp)-1):
    if disp[j]<=0 and disp[j+1]>0:cross.append(tgrid[j]-disp[j]*(tgrid[j+1]-tgrid[j])/(disp[j+1]-disp[j]))
check("Q6 free-rotor tilt period from nonlinear ODE",float(np.mean(np.diff(cross))),2*math.pi/freq,3e-7)
energies=.5*J*y[:,1]**2+np.array([V(v) for v in y[:,0]])
check("Q6 post-impact conservation of effective energy",np.ptp(energies),0.,2e-12)
Js=.8;Pzs=(Js+J*math.sin(theta0)**2)*omega0
Vs=lambda th:Pzs**2/(2*(Js+J*math.sin(th)**2))+k*th*th/2
expected=k/J-omega0**2*math.cos(2*theta0)+4*J*omega0**2*math.sin(theta0)**2*math.cos(theta0)**2/(Js+J*math.sin(theta0)**2)
check("Q6 added shaft-inertia variant via numerical curvature",(Vs(theta0+step)-2*Vs(theta0)+Vs(theta0-step))/step**2/J,expected,4e-7)

# Q7: integrate unreduced Fermat ray equations in Cartesian coordinates.
alpha=.6;rho0=.35;k1=.18;k2=.7;n0=1.5
D0=1+k1*k1+rho0*rho0*k2*k2;q0=1-alpha*alpha*rho0*rho0
beta=n0*math.sqrt(q0/D0);kap=n0*alpha/beta;ell=rho0*rho0*k2
end=2*math.pi/kap
ray=lambda z,y:np.array([y[2],y[3],-alpha**2*y[0]*(1+y[2]**2+y[3]**2)/(1-alpha**2*(y[0]**2+y[1]**2)),-alpha**2*y[1]*(1+y[2]**2+y[3]**2)/(1-alpha**2*(y[0]**2+y[1]**2))])
zs,y=rk4(ray,[rho0,0,k1,rho0*k2],end,18000)
x=rho0*np.cos(kap*zs)+k1/kap*np.sin(kap*zs);yy=rho0*k2/kap*np.sin(kap*zs)
check("Q7 full Fermat ray ODE vs analytic Cartesian solution",float(np.max(np.abs(y[:,:2]-np.column_stack((x,yy))))),0.,4e-10)
rhosq=y[:,0]**2+y[:,1]**2
betas=n0*np.sqrt(1-alpha*alpha*rhosq)/np.sqrt(1+y[:,2]**2+y[:,3]**2)
ells=y[:,0]*y[:,3]-y[:,1]*y[:,2]
check("Q7 both Fermat invariants along numerical ray",[np.max(np.abs(betas-beta)),np.max(np.abs(ells-ell))],[0,0],3e-11)
B=k1/kap;C=rho0*k2/kap;matrix=np.array([[rho0,B],[0,C]])
eigenvalues=np.linalg.eigvalsh(matrix.T@matrix);AA=n0*n0/(beta*beta)-1
roots=np.array([(AA-math.sqrt(AA*AA-4*kap*kap*ell*ell))/(2*kap*kap),(AA+math.sqrt(AA*AA-4*kap*kap*ell*ell))/(2*kap*kap)])
check("Q7 first-integral radial extrema vs ellipse matrix eigenvalues",eigenvalues,roots,2e-12)
timegradient=quad(lambda z:n0*n0*(1-alpha*alpha*((rho0*math.cos(kap*z)+B*math.sin(kap*z))**2+(C*math.sin(kap*z))**2))/(beta*c),0,end)/end
check("Q7 period-averaged travel time independent quadrature",timegradient,(n0*n0+beta*beta)/(2*beta*c),2e-20)
result={"all_passed":all(r["passed"] for r in CHECKS),"checks":CHECKS,"script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),"scope":"Specified numerical parameters; source contains analytic derivations. Numerical agreement is not a universal proof."}
(ROOT/"核验/physics-results.json").write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps({"all_passed":result["all_passed"],"checks":len(CHECKS),"Q4_chi":radchi,"Q4_loss":-radchi/(1+radchi)},ensure_ascii=False,indent=2))
