#!/usr/bin/env python3
"""Independent numerical checks; numpy only, no symbolic-answer substitution."""
from pathlib import Path
import hashlib, json, math
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
REPORT=[]
def record(name,values,condition):
    assert condition, f"FAILED: {name}: {values}"
    REPORT.append({"check":name,"passed":True,"values":values})
def gauss(f,a,b,n=120):
    x,w=np.polynomial.legendre.leggauss(n)
    xx=(a+b)/2+(b-a)*x/2
    return float((b-a)/2*np.dot(w,f(xx)))

# Q1: solve full two-node KCL by Newton, from several initial states.
edges=[(0,1,1/9),(0,2,16),(0,3,1),(2,1,1),(3,1,16),(2,3,8)]
solutions=[]
for initial in ([.1,.9],[.9,.1],[.5,.5],[1.5,-.4]):
    V=np.array([1.,0.,*initial])
    for it in range(100):
        res=np.zeros(2); J=np.zeros((2,2))
        for i,j,c in edges:
            d=V[i]-V[j]; cur=c*d**3; g=3*c*d*d
            for node,sign in ((i,1),(j,-1)):
                if node>=2:
                    res[node-2]+=sign*cur
                    if i>=2:J[node-2,i-2]+=sign*g
                    if j>=2:J[node-2,j-2]-=sign*g
        if np.linalg.norm(res)<1e-13:break
        V[2:]-=np.linalg.solve(J,res)
    solutions.append(V[2:].tolist())
curr=sum(c*(V[i]-V[j])**3 for i,j,c in edges if i==0)
power=sum(c*(V[i]-V[j])**4 for i,j,c in edges)
record("Q1 full KCL Newton + branch power",{"solutions":solutions,"input_current":curr,"branch_power":power},
       max(abs(x[0]-2/3)+abs(x[1]-1/3) for x in solutions)<1e-11 and abs(curr-power)<1e-12)

# Q2: integrate the unexpanded radial equation and angular velocity.
l0=1.;g=9.8;om=4.;k=2e5;u=.02
a=om*om*l0-g;O=math.sqrt(k+3*om*om);tp=2/O*math.atan(O*u/a)
predang=om*((1-2*a/(l0*O*O))*tp+4*u/(l0*O*O))
def rhs(state):
    r,v,angle=state
    return np.array([v,l0**4*om**2/r**3-k*(r-l0)-g,om*l0**2/r**2])
dt=tp/15000;state=np.array([l0,-u,0.]);previous=state.copy();t=0.; dmax=0
for i in range(20000):
    previous=state.copy();tprev=t
    f1=rhs(state);f2=rhs(state+.5*dt*f1);f3=rhs(state+.5*dt*f2);f4=rhs(state+dt*f3)
    state+=dt/6*(f1+2*f2+2*f3+f4);t+=dt;dmax=max(dmax,l0-state[0])
    if i>2 and previous[0]<l0<=state[0]:
        frac=(l0-previous[0])/(state[0]-previous[0])
        t=tprev+frac*dt;state=previous+frac*(state-previous);break
record("Q2 unexpanded ODE vs first-order stance",{"predicted_time":tp,"ODE_time":t,
       "predicted_angle":predang,"ODE_angle":float(state[2]),"max_relative_compression":dmax/l0},
       abs(t/tp-1)<1e-6 and abs(state[2]/predang-1)<1e-6)
# Independent integral of the first-order solution.
integ=gauss(lambda t:a/O**2*(1-np.cos(O*t))-u/O*np.sin(O*t),0,tp)
record("Q2 angular quadrature",{"integral":integ,"angle":om*(tp-2*integ/l0)},
       abs(om*(tp-2*integ/l0)-predang)<1e-13)

# Q3: evaluate full dipole fields on arbitrary boundary points.
def dip(m,r):
    r=np.array(r,dtype=float);d=np.linalg.norm(r)
    return (3*np.dot(m,r)*r/d**2-m)/d**3 # omit common mu0/(4pi)
h=1.3;m=np.array([.6,0.,.8]);rng=np.random.default_rng(4303)
eS=eI=eFinite=0.
for xy in rng.uniform(-3,3,(100,2)):
    ra=np.array([*xy,-h]);rb=np.array([*xy,h])
    base=dip(m,ra)
    bs=base+dip(m*np.array([1,1,-1]),rb)
    bi=base+dip(m*np.array([-1,1,1]),rb)
    eS=max(eS,abs(bs[2]));eI=max(eI,float(np.linalg.norm(bi[:2])))
    mu=7.3;eta=(mu-1)/(mu+1);mt=2/(mu+1)*m
    above=base+dip(eta*m*np.array([-1,1,1]),rb)
    belowH=dip(mt,ra);belowB=mu*belowH
    eFinite=max(eFinite,abs(above[2]-belowB[2]),float(np.linalg.norm(above[:2]-belowH[:2])))
record("Q3 boundary fields, ideal and finite permeability",
       {"SC_normal_max":eS,"iron_tangent_max":eI,"finite_mu_boundary_max":eFinite},
       max(eS,eI,eFinite)<1e-13)
theta=.72;mm=np.array([math.sin(theta),0.,math.cos(theta)])
tau=np.cross(mm,dip(mm*np.array([1,1,-1]),[0,0,2*h]))[1]
step=1e-6
energy=lambda th:(1+math.cos(th)**2)/(2*(2*h)**3)
minus_deriv=-(energy(theta+step)-energy(theta-step))/(2*step)
record("Q3 direct torque vs induced energy derivative",
       {"torque":float(tau),"energy_derivative":minus_deriv},abs(tau-minus_deriv)<1e-10)

# Q4: numerical data, uniform force torque quadrature, exact tidal force.
G=6.67e-11;ME=5.97e24;r0=6.77e6;m1=450.;m2=50.;M=m1+m2;L=5000.;B=3e-5;Rt=200.
v=math.sqrt(G*ME/r0);orbO=v/r0;P=B*B*L*L*v*v/Rt
hdot=-2*P*r0*r0/(G*ME*M);dh=hdot*2*math.pi/orbO
l1=m2*L/M;l2=m1*L/M;J=m1*l1*l1+m2*l2*l2
chi=v*B*B*L*(m1-m2)/(2*Rt*m1*m2)
te=math.asin(chi/(3*orbO**2));I=B*L*v*math.cos(te)/Rt
torque_quad=gauss(lambda s:-s*I*B,-l2,l1)
expected=J*chi*math.cos(te)
n=np.array([math.cos(te),math.sin(te)])
forces=[]
for mass,s in [(m1,l1),(m2,-l2)]:
    rr=np.array([r0,0.])+s*n
    exact=mass*(-G*ME*rr/np.linalg.norm(rr)**3+np.array([G*ME/r0**2,0.]))
    approx=mass*orbO**2*s*np.array([2*n[0],-n[1]])
    forces.append((exact,approx))
tidal_tau=sum((s*n[0]*f[0][1]-s*n[1]*f[0][0]) for s,f in [(l1,forces[0]),(-l2,forces[1])])
pred_tidal=-3*J*orbO**2*math.sin(te)*math.cos(te)
record("Q4 numerical data + line-force torque + exact gravitational gradient",
       {"v0":v,"Omega0":orbO,"P0":P,"hdot":hdot,"one_orbit_dh":dh,
        "theta_eq_degrees":math.degrees(te),"omega2":math.sqrt(3)*orbO*math.cos(te),
        "line_torque":torque_quad,"tidal_torque_exact":tidal_tau,"tidal_torque_first_order":pred_tidal},
       abs(torque_quad/expected-1)<1e-12 and abs(tidal_tau/pred_tidal-1)<.002)

# Q5: independent 2D quadrature over the immersed trapezoid.
a5=2.;b5=1.5;beta=.55;hh=2*b5*beta;th=.08
H=lambda x:hh+x*np.tan(th)
area=gauss(H,-a5,a5)
xb=gauss(lambda x:x*H(x),-a5,a5)/area
yb=gauss(lambda x:-b5*H(x)+H(x)**2/2,-a5,a5)/area
ym=yb+xb/math.tan(th)
exactxb=a5*a5/(3*hh)*math.tan(th)
exactyb=-b5+hh/2+a5*a5/(6*hh)*math.tan(th)**2
record("Q5 submerged-area centroid quadrature",{"area":area,"x_B":xb,"y_B":yb,"M_theta":ym},
       max(abs(area-2*a5*hh),abs(xb-exactxb),abs(yb-exactyb))<1e-12)
linearM=a5*a5/(3*hh)-b5+hh/2
ratio=3*hh*linearM/(a5*a5+b5*b5)
record("Q5 stability and frequency ratio",{"y_M":linearM,"frequency_squared_ratio":ratio},0<ratio<1)

# Q6: independently integrate screened charge and finite-difference radial ODE.
qind=-gauss(lambda x:x*np.exp(-x),0,40,180)
r=np.linspace(.4,4,40);dr=1e-4
psi=lambda r:np.exp(-r)
res=(psi(r+dr)-2*psi(r)+psi(r-dr))/dr**2-psi(r)
record("Q6 screened charge integral and radial differential equation",
       {"induced_charge_over_Q":qind,"ODE_residual_max":float(np.max(np.abs(res)))},
       abs(qind+1)<1e-12 and np.max(np.abs(res))<1e-7)
wp=math.sqrt(1e7*(1e-19)**2/(1e-30*1e-11))
record("Q6 cutoff and high-frequency response",{"omega_p":wp,"f_p":wp/(2*math.pi),
       "visible_epsilon_deviation":(wp/(2*math.pi*1e14))**2},abs(wp-1e5)<1e-8)

# Q7: exact layer matrices, independent from single-path summation.
def layer(n,d,k):
    z=n*d*k;c=math.cos(z);s=math.sin(z)
    return np.array([[c,1j*s/n],[1j*n*s,c]],complex)
def exact_reflect(n1,n2,d1,d2,N,k):
    mat=np.linalg.matrix_power(layer(n1,d1,k)@layer(n2,d2,k),N)
    A=mat[1,0]-n1*mat[0,0];BB=n1*mat[1,1]-n1*n1*mat[0,1]
    rr=(A+BB)/(BB-A)
    tt=mat[0,0]*(1+rr)+mat[0,1]*n1*(1-rr)
    return rr,tt
def path_sum(n1,n2,d1,d2,N,k):
    S=n1*d1+n2*d2;rr=(n1-n2)/(n1+n2)
    return rr*sum(np.exp(2j*p*k*S)-np.exp(2j*k*(p*S+n2*d2)) for p in range(N))
n1=1.5;n2=1.50001;d1=1.;d2=.7;N=20;k=math.pi/(n1*d1+n2*d2)
rr,tt=exact_reflect(n1,n2,d1,d2,N,k);rp=path_sum(n1,n2,d1,d2,N,k)
record("Q7 exact transfer matrix vs weak single-path reflection",
       {"exact_abs_r":abs(rr),"first_order_abs_r":abs(rp),
        "complex_difference":abs(rr-rp),"energy_sum":abs(rr)**2+abs(tt)**2},
       abs(rr-rp)<2e-10 and abs(abs(rr)**2+abs(tt)**2-1)<1e-12)
# Missing-order expansion: keep S, test both signs of detuning.
n2=1.5001;d2=1/n2;d1=1/n1;S=2.;N=30;km=2*math.pi/S
eps=1e-7;rr0=(n1-n2)/(n1+n2)
near=[abs(path_sum(n1,n2,d1,d2,N,km+x)) for x in (-eps,eps)]
linear=2*N*abs(rr0)*n2*d2*eps
record("Q7 missing-order absolute detuning",{"two_sides":near,"linear_prediction":linear},
       max(abs(y/linear-1) for y in near)<1e-7)
# Exact single-slab geometric-series formula vs boundary matrix.
n2=2.1;k=.93;d2=.8
rs,ts=exact_reflect(n1,n2,0,d2,1,k);r12=(n1-n2)/(n1+n2);phase=np.exp(2j*n2*k*d2)
slab=r12*(1-phase)/(1-r12*r12*phase)
record("Q7 exact slab alternative calculation",{"complex_difference":abs(rs-slab),
       "energy_sum":abs(rs)**2+abs(ts)**2},
       abs(rs-slab)<1e-13 and abs(abs(rs)**2+abs(ts)**2-1)<1e-12)

# Variant families: altered network topology and exponent.
def network_solve(edge_list,p=3):
    VV=np.array([1.,0.,.6,.4])
    for _ in range(100):
        res=np.zeros(2);jac=np.zeros((2,2))
        for i,j,c in edge_list:
            z=VV[i]-VV[j];cur=c*z**p;gg=p*c*z**(p-1)
            for node,sign in ((i,1),(j,-1)):
                if node>=2:
                    res[node-2]+=sign*cur
                    if i>=2:jac[node-2,i-2]+=sign*gg
                    if j>=2:jac[node-2,j-2]-=sign*gg
        if np.linalg.norm(res)<1e-13:break
        VV[2:]-=np.linalg.solve(jac,res)
    current=sum(c*(VV[i]-VV[j])**p for i,j,c in edge_list if i==0)
    return VV,current
vo,io=network_solve(edges[:-1]);s=16**(1/3)
e5=[(0,1,1/9),(0,2,64),(0,3,1),(2,1,1),(3,1,64),(2,3,32)]
v5,i5=network_solve(e5,p=5)
record("Variants Q1: open topology and fifth-power network",
       {"open_voltage":vo[2:].tolist(),"open_current":io,"p5_voltage":v5[2:].tolist(),"p5_current":i5},
       abs(io-(1/9+32/(1+s)**3))<1e-12 and abs(i5-41/81)<1e-12)
# Fixed-image field gradient for force; direct torque slope for libration.
mm=np.array([math.sin(theta),0.,math.cos(theta)])
ms=mm*np.array([1,1,-1])
zz=2*h
df=(np.dot(mm,dip(ms,[0,0,zz+step]))-np.dot(mm,dip(ms,[0,0,zz-step])))/(2*step)
predforce=3*(1+math.cos(theta)**2)/(16*h**4)
record("Variants Q3: fixed-image gradient gives vertical force",
       {"direct_gradient":df,"energy_force":predforce},abs(df-predforce)<1e-9)
# Nonlinear hydrostatic restoring moment at the critical aspect ratio.
be=.5;bcrit=1.;hcrit=1.;acrit=math.sqrt(1.5);ang=.002
height=lambda x:hcrit+x*np.tan(ang)
ar=gauss(height,-acrit,acrit)
xc=gauss(lambda x:x*height(x),-acrit,acrit)/ar
yc=gauss(lambda x:-bcrit*height(x)+height(x)**2/2,-acrit,acrit)/ar
clockwise_torque=-(xc*math.cos(ang)+yc*math.sin(ang))
cubic=-(acrit**2/(6*hcrit))*ang**3
record("Variants Q5: critical restoring torque from centroid integration",
       {"torque_over_mg":clockwise_torque,"cubic_prediction":cubic},
       abs(clockwise_torque/cubic-1)<1e-5)
# Two Boltzmann species finite response, independently differentiated.
Te=3.;Ti=2.;potential=1e-6
charge=lambda phi:math.exp(-phi/Ti)-math.exp(phi/Te)
der=(charge(potential)-charge(-potential))/(2*potential)
record("Variants Q6: two mobile species charge susceptibility",
       {"numerical_derivative":der,"linear_prediction":-(1/Te+1/Ti)},
       abs(der+1/Te+1/Ti)<1e-9)
# Main-lobe zeros evaluated as a finite complex path sum.
n1=1.5;n2=1.50001;d1=1.;d2=.7;NN=40;S=n1*d1+n2*d2;kc=math.pi/S
zeros=[abs(path_sum(n1,n2,d1,d2,NN,kc+sign*math.pi/(NN*S))) for sign in (-1,1)]
record("Variants Q7: nearest interference zeros",{"finite_path_sum_abs":zeros},
       max(zeros)<1e-15)

out=ROOT/"核验/physics-results.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps({"checks":REPORT,"all_passed":True,
 "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
 ensure_ascii=False,indent=2),encoding="utf-8")
print(f"{len(REPORT)} independent checks passed")
for r in REPORT:print(r["check"])
