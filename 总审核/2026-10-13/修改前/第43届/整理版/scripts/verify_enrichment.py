#!/usr/bin/env python3
"""Independent checks for the added derivations; numpy only."""
from pathlib import Path
import hashlib,json,math
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def record(name,values,ok):
    assert ok,(name,values)
    checks.append({"check":name,"passed":True,"values":values})
def gauss(f,a,b,n=160):
    x,w=np.polynomial.legendre.leggauss(n)
    return float((b-a)/2*np.dot(w,f((a+b)/2+(b-a)*x/2)))
edges=[(0,1,1/9),(0,2,16),(0,3,1),(2,1,1),(3,1,16),(2,3,8)]
def network(port):
    V=np.array([port,0.,.6*port,.4*port])
    for _ in range(80):
        res=np.zeros(2);jac=np.zeros((2,2))
        for i,j,c in edges:
            dv=V[i]-V[j]
            for node,sign in [(i,1),(j,-1)]:
                if node>=2:
                    res[node-2]+=sign*c*dv**3
                    if i>=2:jac[node-2,i-2]+=sign*3*c*dv**2
                    if j>=2:jac[node-2,j-2]-=sign*3*c*dv**2
        if np.linalg.norm(res)<1e-14:break
        V[2:]-=np.linalg.solve(jac,res)
    I=sum(c*(V[i]-V[j])**3 for i,j,c in edges if i==0)
    return V,I,jac
v,cur,jac=network(1.)
eps=1e-5
vp,ip,_=network(1+eps);vm,im,_=network(1-eps)
increment=(vp[2:]-vm[2:])/(2*eps);conduct=(ip-im)/(2*eps)
def functional(x):
    q=np.array([1.,0.,*x])
    return sum(c*(q[i]-q[j])**4/4 for i,j,c in edges)
grad=[]
for j in range(2):
    d=np.eye(2)[j]*eps
    grad.append((functional(v[2:]+d)-functional(v[2:]-d))/(2*eps))
record("Added Q1: nonlinear network perturbation and variational stationary point",
       {"internal_derivative":increment.tolist(),"port_derivative":conduct,
        "functional_gradient":grad,"Hessian_eigenvalues":np.linalg.eigvalsh(jac).tolist()},
       np.max(abs(increment-[2/3,1/3]))<1e-8 and abs(conduct-3)<1e-8
       and max(abs(x) for x in grad)<1e-8 and min(np.linalg.eigvalsh(jac))>0)

# Integrate the effective energy orbit, without the solved time function.
a=6.2;O=40.;u=.4;l0=1.
d=(math.sqrt(a*a+O*O*u*u)-a)/(O*O)
def orbit_integrand(psi):
    delta=-d+d*np.sin(psi)**2
    speed=np.sqrt(u*u+2*a*delta-O*O*delta*delta)
    return 2*d*np.sin(psi)*np.cos(psi)/speed
half=gauss(orbit_integrand,0,math.pi/2)
avg=-gauss(lambda p:(-d+d*np.sin(p)**2)*orbit_integrand(p),0,math.pi/2)/half
expected=2/O*math.atan(O*u/a)
avg_expected=(2*u-a*expected)/(O*O*expected)
record("Added Q2: energy-orbit quadrature for return time and mean compression",
       {"quadrature_time":2*half,"time_formula":expected,
        "mean_compression":avg,"maximum_compression":d},
       abs(2*half/expected-1)<1e-8 and abs(avg-avg_expected)<1e-9 and 0<avg<d)

# Direct dipole fields vs explicit complete surface expressions.
def dip(m,r):
    R=np.linalg.norm(r)
    return (3*np.dot(m,r)*r/R**2-m)/R**3
h=1.3;mx=.6;mz=.8
rng=np.random.default_rng(430311);error=0.
for x,y in rng.uniform(-3,3,(100,2)):
    R2=x*x+y*y+h*h;R5=R2**2.5
    base=dip(np.array([mx,0,mz]),np.array([x,y,-h]))
    actualS=base+dip(np.array([mx,0,-mz]),np.array([x,y,h]))
    actualI=base+dip(np.array([-mx,0,mz]),np.array([x,y,h]))
    explicitS=np.array([2*(3*x*x-R2)*mx-6*h*x*mz,6*y*(x*mx-h*mz),0])/R5
    explicitI=np.array([0,0,-6*h*x*mx+2*(3*h*h-R2)*mz])/R5
    error=max(error,float(np.max(abs(actualS-explicitS))),float(np.max(abs(actualI-explicitI))))
record("Added Q3: complete surface component formulas vs full dipole fields",
       {"maximum_component_error":error},error<1e-12)

# Potential of the exact endpoint positions; compare its angular derivative.
r0=1000.;L=1.;m1=9.;m2=1.;mu=1e9;Om2=mu/r0**3
l1=m2*L/(m1+m2);l2=m1*L/(m1+m2);J=m1*l1*l1+m2*l2*l2
def gravU(theta):
    n=np.array([math.cos(theta),math.sin(theta)])
    c=np.array([r0,0.])
    return -mu*(m1/np.linalg.norm(c+l1*n)+m2/np.linalg.norm(c-l2*n))
theta=.4;step=1e-3
exact_torque=-(gravU(theta+step)-gravU(theta-step))/(2*step)
tidal=-3*J*Om2*math.sin(theta)*math.cos(theta)
M=m1+m2
def energy(r):return -mu*M/(2*r)
def angular_momentum(r):return M*math.sqrt(mu*r)
dr=.1
slope=(energy(r0+dr)-energy(r0-dr))/(angular_momentum(r0+dr)-angular_momentum(r0-dr))
record("Added Q4: exact gravitational potential derivative and circular energy-angular momentum relation",
       {"exact_potential_torque":exact_torque,"first_order_tidal_torque":tidal,
        "dE_dH_numerical":slope,"orbital_Omega":math.sqrt(Om2)},
       abs(exact_torque/tidal-1)<.002 and abs(slope/math.sqrt(Om2)-1)<1e-8)

# Shoelace centroid for the actual submerged polygon, not strip formulas.
def polygon_centroid(v):
    w=np.roll(v,-1,axis=0)
    cross=v[:,0]*w[:,1]-w[:,0]*v[:,1]
    area=cross.sum()/2
    return np.array([np.sum((v[:,0]+w[:,0])*cross),
                     np.sum((v[:,1]+w[:,1])*cross)])/(6*area)
a5=1.4;b5=1.;h5=1.1;A=a5*a5/(3*h5);GM=-b5+h5/2+A
def hydroU(theta):
    return GM*(1-math.cos(theta))+A/2*(1/math.cos(theta)+math.cos(theta)-2)
errors=[]
for theta in [.08,.16,-.11]:
    t=math.tan(theta)
    poly=np.array([[-a5,-b5],[a5,-b5],[a5,h5-b5+a5*t],[-a5,h5-b5-a5*t]])
    x,y=polygon_centroid(poly)
    arm=x*math.cos(theta)+y*math.sin(theta)
    step=1e-5
    energy_arm=(hydroU(theta+step)-hydroU(theta-step))/(2*step)
    errors.append(abs(arm-energy_arm))
record("Added Q5: polygon centroid lever arm vs hydrostatic potential derivative",
       {"maximum_lever_arm_error":max(errors),"GM":GM},
       max(errors)<1e-9)

# Finite-radius induced charge integrated directly vs flux from potential.
errors=[]
for r in [.2,1.,5.]:
    induced=gauss(lambda s:-s*np.exp(-s),0,r)
    step=1e-5
    phi=lambda s:math.exp(-s)/s
    radial_field=-(phi(r+step)-phi(r-step))/(2*step)
    flux=r*r*radial_field
    errors.append(abs((1+induced)-flux))
record("Added Q6: finite-ball screening charge integral vs potential-derived flux",
       {"maximum_charge_flux_error":max(errors)},max(errors)<1e-8)

# Solve all interface E,E' conditions simultaneously, independently of layer matrices.
def matching(ns,ds,k,n0):
    count=len(ns);unknowns=2*count+2
    A=np.zeros((unknowns,unknowns),complex);rhs=np.zeros(unknowns,complex)
    indices={(0,"B"):0,(count+1,"A"):2*count+1}
    for j in range(1,count+1):
        indices[(j,"A")]=2*j-1;indices[(j,"B")]=2*j
    alln=[n0,*ns,n0]
    for j in range(count+1):
        delta=0. if j==0 else ns[j-1]*ds[j-1]*k
        for reg,factor,phase in [(j,1.,delta),(j+1,-1.,0.)]:
            n=alln[reg]
            for direction,sgn in [("A",1),("B",-1)]:
                f=factor*np.exp(1j*sgn*phase)
                terms=[f,f*n*sgn]
                col=indices.get((reg,direction))
                for q,term in enumerate(terms):
                    if col is not None:A[2*j+q,col]+=term
                    elif (reg,direction)==(0,"A"):rhs[2*j+q]-=term
    result=np.linalg.solve(A,rhs)
    return result[0],result[-1]
def layer(n,d,k):
    x=n*d*k
    return np.array([[math.cos(x),1j*math.sin(x)/n],
                     [1j*n*math.sin(x),math.cos(x)]])
def matrix_rt(ns,ds,k,n0):
    P=np.eye(2,dtype=complex)
    for n,d in zip(ns,ds):P=layer(n,d,k)@P
    aa=P[0,0]+n0*P[0,1];bb=P[0,0]-n0*P[0,1]
    cc=P[1,0]+n0*P[1,1];dd=P[1,0]-n0*P[1,1]
    r=(cc-n0*aa)/(n0*bb-dd)
    return r,aa+bb*r
opt_error=0.;energy_error=0.
for n0,n2,d1,d2,N,k in [(1.5,1.3,.7,.4,4,2.1),(1.4,1.8,.3,.5,6,3.),
                       (1.5,1.5001,.7,.4,7,2.1),(1.5,1.2,3/1.5,2/1.2,3,math.pi)]:
    ns=[n2,n0]*N;ds=[d2,d1]*N
    r,t=matching(ns,ds,k,n0);rm,tm=matrix_rt(ns,ds,k,n0)
    opt_error=max(opt_error,abs(r-rm),abs(t-tm))
    energy_error=max(energy_error,abs(abs(r)**2+abs(t)**2-1))
missing_r=abs(r)
record("Added Q7: global interface equations vs full layer matrix, energy and exact missing order",
       {"maximum_complex_amplitude_error":opt_error,"maximum_energy_error":energy_error,
        "missing_order_abs_r":missing_r},
       opt_error<1e-11 and energy_error<1e-11 and missing_r<1e-11)

# Locate finite-N peaks by direct complex path summation.
def golden_max(f,left,right):
    ratio=(math.sqrt(5)-1)/2
    x=right-ratio*(right-left);y=left+ratio*(right-left)
    fx=f(x);fy=f(y)
    for _ in range(100):
        if fx>fy:
            right=y;y=x;fy=fx;x=right-ratio*(right-left);fx=f(x)
        else:
            left=x;x=y;fx=fy;y=left+ratio*(right-left);fy=f(y)
    return (left+right)/2
q=.31;m=1;comparisons=[]
for N in [40,80,120]:
    def paths(y):
        phase=m*math.pi+y
        return abs((1-np.exp(2j*q*phase))*np.exp(2j*np.arange(N)*phase).sum())
    peak=golden_max(paths,-.5/N,.5/N)
    a=m*math.pi*q
    prediction=q/math.tan(a)/(q*q/math.sin(a)**2+(N*N-1)/3)
    comparisons.append({"N":N,"numerical_peak_shift":peak,"local_formula":prediction})
record("Added Q7: finite-N peak optimization vs derived center shift",
       {"cases":comparisons},
       all(abs(x["numerical_peak_shift"]/x["local_formula"]-1)<.004 for x in comparisons))
out={"all_passed":True,"checks":checks,
     "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/"核验/enrichment-results.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(out,ensure_ascii=False,indent=2))

