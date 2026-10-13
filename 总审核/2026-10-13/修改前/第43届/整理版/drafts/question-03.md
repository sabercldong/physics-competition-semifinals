# 第 3 题　磁偶极子在平面介质上方的镜像与稳定取向

一大小可忽略的磁偶极子固定在 $(0,0,h)$，$h>0$，其磁矩限制在 $xz$ 平面内：

$$
\boldsymbol m=m(\sin\theta\,\hat{\boldsymbol x}+\cos\theta\,\hat{\boldsymbol z}),
\qquad m>0.
$$

磁矩大小恒定，$\theta$ 为磁矩方向与 $z$ 轴正方向的夹角。$z>0$ 为真空，$z<0$ 为超导体或介质。真空区域的磁场可等效为该磁偶极子与一个镜像磁偶极子的场的叠加。已知真空中磁偶极子的场为

$$
\boldsymbol B(\boldsymbol r)=\frac{\mu_0}{4\pi r^3}
\left[3(\boldsymbol m\cdot\hat{\boldsymbol r})\hat{\boldsymbol r}
-\boldsymbol m\right],
$$

其中 $\boldsymbol r$ 从偶极子指向场点，$\mu_0$ 为真空磁导率。

（1.1）下半空间为理想超导体，其内部磁感应强度为零，求镜像磁矩 $\boldsymbol m_{\rm S}$。

（1.2）下半空间为磁导率 $\mu\to\infty$ 的理想软磁体，求镜像磁矩 $\boldsymbol m_{\rm I}$。

（2）求两种情况下真实偶极子受到的力矩 $\boldsymbol\tau_{\rm S}$、$\boldsymbol\tau_{\rm I}$。

（3）若真实偶极子可在 $xz$ 平面内转动，并受微弱阻尼，分别求最终可能的稳定取向。本题45分。

![图3-1　真实偶极子与平面边界，磁矩分解为切向分量和法向分量。](../figures/q3-model.png)

## 一、题型定位

镜像法把介质的磁响应转化为一个等效场源。真正决定镜像方向的是界面的场边界条件：超导体要求真空侧法向 $B$ 为零；理想软磁体要求真空侧切向 $H$ 为零。

镜像偶极子是求真空场的辅助对象，并非另一个可以独立转动的真实磁体。力矩可直接用镜像场计算；若进一步用能量讨论稳定性，则必须考虑镜像随真实磁矩改变而改变。

## 二、知识点

- 磁感应强度的法向分量在界面连续。
- 无自由面电流时，磁场强度的切向分量连续；在真空中 $\boldsymbol H=\boldsymbol B/\mu_0$。
- 理想软磁体在 $\mu\to\infty$ 的有限磁场极限下，内部切向 $H$ 趋于零。
- 磁偶极子的外场力矩为 $\boldsymbol\tau=\boldsymbol m\times\boldsymbol B_{\text{外}}$。
- 绕 $+y$ 轴转动使磁矩从 $+z$ 转向 $+x$，故本题 $\theta$ 的正变化对应 $+y$ 力矩。
- 平衡角需满足力矩为零；稳定性还要检查角度受到小扰动后的恢复方向。

## 三、物理图像

写 $m_x=m\sin\theta$、$m_z=m\cos\theta$。镜像位置是 $(0,0,-h)$。两个场源到界面同一场点的距离相等，而它们的法向位移符号相反。因此，平行和垂直于界面的磁矩分量通常要采用不同的镜像符号。

![图3-2　两种镜像：超导体保留切向磁矩、反转法向磁矩；软磁体反之。](../figures/q3-images.png)

在真实偶极子的位置，镜像到它的矢量沿 $+z$，距离为 $2h$。因此该点的镜像场有一个较简单的形式：切向磁矩贡献为其负值，法向磁矩贡献为其两倍。先确定镜像，再使用这一轴线上的场，可以减少向量代数。

## 四、解题入口

在界面任意点 $(x,y,0)$ 写出真实场和镜像场，分别令总 $B_z=0$ 或总 $B_x=B_y=0$。不能只在原点检验，因为原点会使含 $x,y$ 的条件自动消失。

确定镜像后，计算其在 $(0,0,h)$ 的场，再作叉乘。最后在线性扰动下检查 $\tau_y(\theta)$ 的导数，区分稳定与不稳定的零力矩方向。

## 五、解析

（1）在整个平面上建立边界条件。

设镜像磁矩为 $(m_x',0,m_z')$。对界面点 $(x,y,0)$，定义

$$
R=\sqrt{x^2+y^2+h^2},\quad
\boldsymbol R=(x,y,-h),\quad
\boldsymbol R'=(x,y,h).
$$

真实偶极子的法向场为

$$
B_z=\frac{\mu_0}{4\pi R^5}
\left[-3hx m_x+(3h^2-R^2)m_z\right],
$$

镜像的法向场为

$$
B_z'=\frac{\mu_0}{4\pi R^5}
\left[3hx m_x'+(3h^2-R^2)m_z'\right].
$$

理想超导体内部 $B_z=0$；由法向连续性，界面真空侧也要满足 $B_z+B_z'=0$。把同类项合并：

$$
3hx(m_x'-m_x)+(3h^2-R^2)(m_z+m_z')=0.
$$

该等式须对所有 $x,y$ 成立。因此

$$
m_x'=m_x,\qquad m_z'=-m_z,
$$

得到

$$
\boxed{\boldsymbol m_{\rm S}
=m(\sin\theta\,\hat{\boldsymbol x}-\cos\theta\,\hat{\boldsymbol z}).}
\tag{3.1}
$$

超导表面允许出现维持磁通排斥的屏蔽面电流，所以不能在这里额外强加“切向 $H$ 连续且为零”的软磁体条件。

（2）理想软磁体的镜像。

软磁体界面无外加自由面电流，在理想极限下，真空侧切向场为零。真实与镜像的 $x$ 分量相加后为

$$
B_x+B_x'=\frac{\mu_0}{4\pi R^5}
\left[(3x^2-R^2)(m_x+m_x')+3hx(m_z'-m_z)\right].
$$

要求对所有场点为零，给出

$$
m_x'=-m_x,\qquad m_z'=m_z.
$$

还须检查另一切向分量：

$$
B_y+B_y'=\frac{3\mu_0y}{4\pi R^5}
\left[x(m_x+m_x')+h(m_z'-m_z)\right]=0.
$$

同一组镜像满足两个切向条件，故

$$
\boxed{\boldsymbol m_{\rm I}
=m(-\sin\theta\,\hat{\boldsymbol x}+\cos\theta\,\hat{\boldsymbol z}).}
\tag{3.2}
$$

（3）求真实位置的镜像场。

真实偶极子自身的场不作为外场代入力矩。取

$$
C=\frac{\mu_0}{4\pi(2h)^3}=\frac{\mu_0}{32\pi h^3}.
$$

在镜像的 $z$ 轴线上，任意镜像磁矩给出

$$
\boldsymbol B'=C(-m_x'\hat{\boldsymbol x}+2m_z'\hat{\boldsymbol z}).
$$

所以

$$
\boldsymbol B_{\rm S}'=-C(m_x\hat{\boldsymbol x}+2m_z\hat{\boldsymbol z}),
\qquad
\boldsymbol B_{\rm I}'=C(m_x\hat{\boldsymbol x}+2m_z\hat{\boldsymbol z}).
$$

（4）逐项计算力矩。

对 $\boldsymbol m=m_x\hat{\boldsymbol x}+m_z\hat{\boldsymbol z}$、
$\boldsymbol B'=B_x'\hat{\boldsymbol x}+B_z'\hat{\boldsymbol z}$，

$$
\boldsymbol m\times\boldsymbol B'
=(m_zB_x'-m_xB_z')\hat{\boldsymbol y},
$$

因为 $\hat{\boldsymbol z}\times\hat{\boldsymbol x}=\hat{\boldsymbol y}$、
$\hat{\boldsymbol x}\times\hat{\boldsymbol z}=-\hat{\boldsymbol y}$。代入两种场：

$$
\boxed{\boldsymbol\tau_{\rm S}
=Cm_xm_z\hat{\boldsymbol y}
=\frac{\mu_0m^2}{64\pi h^3}\sin2\theta\,\hat{\boldsymbol y},}
\tag{3.3}
$$

$$
\boxed{\boldsymbol\tau_{\rm I}
=-Cm_xm_z\hat{\boldsymbol y}
=-\frac{\mu_0m^2}{64\pi h^3}\sin2\theta\,\hat{\boldsymbol y}.}
\tag{3.4}
$$

两者只差一个符号，但这个符号决定稳定方向是否互换。

（5）由小扰动判断稳定性。

定义 $A=Cm^2>0$。对于超导体，$\tau_y=A\sin\theta\cos\theta$。零力矩方向为 $\theta=0,\pi/2,\pi,3\pi/2$。

在 $\theta=0+\epsilon$ 附近，$\tau_y\simeq A\epsilon$，推动 $\epsilon$ 继续增大，因而不稳定。在 $\theta=\pi/2+\epsilon$ 附近，$\tau_y\simeq-A\epsilon$，产生恢复力矩，因而稳定。同理，$\theta=\pi$ 不稳定、$\theta=3\pi/2$ 稳定。

软磁体力矩反号，所以其稳定方向为 $\theta=0,\pi$，不稳定方向为 $\theta=\pi/2,3\pi/2$。因此

$$
\boxed{\text{超导体：磁矩平行于界面，沿 }\pm\hat{\boldsymbol x};}
$$

$$
\boxed{\text{软磁体：磁矩垂直于界面，沿 }\pm\hat{\boldsymbol z}.}
$$

微弱阻尼使一般初始状态的摆动能量逐渐减少，最终趋向某个稳定方向。若理想模型中恰好从不稳定平衡静止释放，而且完全没有扰动，它仍可停在那里；这不使该方向成为稳定取向。

（6）用能量检查力矩。

对线性诱导响应，体系的取向能量为

$$
U=-\frac12\boldsymbol m\cdot\boldsymbol B'.
$$

因 $\boldsymbol m\cdot\boldsymbol B_{\rm S}'=-C(m_x^2+2m_z^2)$，

$$
U_{\rm S}=\frac A2(1+\cos^2\theta),\qquad
U_{\rm I}=-\frac A2(1+\cos^2\theta).
$$

分别计算 $-\partial U/\partial\theta$，得到 $\pm A\sin\theta\cos\theta$，与叉乘完全一致。超导体的能量最小处为 $\cos\theta=0$；软磁体的能量最小处为 $|\cos\theta|=1$。

这里的因子 $1/2$ 来自场源的诱导性质。若把镜像误当作固定的独立永久磁体，在随 $\theta$ 同时变化的镜像场中直接使用 $-\boldsymbol m\cdot\boldsymbol B'$ 求导，就会把力矩算大一倍。

（7）用法向投影重写镜像和力矩。

设界面指向真空的单位法向为 $\boldsymbol n=\hat{\boldsymbol z}$。任意磁矩可以分解为

$$
\boldsymbol m_\perp=(\boldsymbol m\cdot\boldsymbol n)\boldsymbol n,\qquad
\boldsymbol m_\parallel=\boldsymbol m-\boldsymbol m_\perp.
$$

两种镜像分别为

$$
\boldsymbol m_{\rm S}=\boldsymbol m_\parallel-\boldsymbol m_\perp,\qquad
\boldsymbol m_{\rm I}=-\boldsymbol m_\parallel+\boldsymbol m_\perp.
$$

镜像到真实源的方向沿 $\boldsymbol n$，故该处镜像场的一般式为

$$
\boldsymbol B'=C\big[
3(\boldsymbol m'\cdot\boldsymbol n)\boldsymbol n-\boldsymbol m'\big].
$$

超导体情形化为

$$
\boldsymbol B'_{\rm S}
=-C\big[\boldsymbol m+(\boldsymbol m\cdot\boldsymbol n)\boldsymbol n\big],
$$

软磁体场反号。因为 $\boldsymbol m\times\boldsymbol m=0$，只有法向投影项产生力矩：

$$
\boldsymbol\tau_{\rm S}
=-C(\boldsymbol m\cdot\boldsymbol n)(\boldsymbol m\times\boldsymbol n),
\qquad
\boldsymbol\tau_{\rm I}=-\boldsymbol\tau_{\rm S}.
$$

代回本题磁矩，$\boldsymbol m\times\boldsymbol n=-m_x\hat{\boldsymbol y}$，得到超导体力矩 $+Cm_xm_z\hat{\boldsymbol y}$。这同时检查叉乘方向，并说明规则适用于面内任意方位。

（8）边界条件为何必须在整个平面成立。

在 $(x,y)=(0,0)$，超导体法向边界条件只含 $m_z+m_z'$，切向磁矩的信息完全消失。仅用这个点求镜像，会留下一个没有确定的分量。

再取 $(x,0,0)$，$x\ne0$，并比较 $(-x,0,0)$：含切向磁矩的项反号，法向磁矩的项不变。两点条件相减、相加，分别得到

$$
6hx(m_x'-m_x)=0,
$$

$$
2(2h^2-x^2)(m_z+m_z')=0.
$$

选择 $x^2\ne2h^2$，即可分别确定两个分量。一般场点法一次保留这些独立空间函数，避免被特殊点的零值掩盖。

软磁体若只在 $y=0$ 的直线上检查，$B_y$ 自动为零，仍未检验整个切向边界。将求得的镜像代回任意场点，两种界面真空侧的总场为

$$
\begin{aligned}
B_{{\rm S},x}
&=\frac{\mu_0}{4\pi R^5}
\big[2(3x^2-R^2)m_x-6hx m_z\big],\\
B_{{\rm S},y}
&=\frac{6\mu_0y}{4\pi R^5}(xm_x-hm_z),\\
B_{{\rm S},z}&=0,
\end{aligned}
$$

以及

$$
B_{{\rm I},x}=B_{{\rm I},y}=0,\qquad
B_{{\rm I},z}=\frac{\mu_0}{4\pi R^5}
\big[-6hx m_x+2(3h^2-R^2)m_z\big].
$$

超导表面总场沿界面，理想软磁表面总场垂直界面。它们均不要求真空侧总场处处为零，场的方向是各自边界条件的几何表现。

（9）逐步建立磁矩，理解能量的二分之一。

暂时把磁矩从零缓慢增到给定值，位置和方向不变，令中间磁矩为 $\boldsymbol m(s)=s\boldsymbol m$，$0\le s\le1$。本题线性诱导响应使诱导场同步变为 $s\boldsymbol B'$。每一步用已经建立的诱导场计算磁矩增量所对应的能量：

$$
U=-\int_0^1(s\boldsymbol B')\cdot(\boldsymbol m\,ds)
=-\frac12\boldsymbol m\cdot\boldsymbol B'.
$$

积分依赖线性响应。若介质响应具有滞后或非线性，就不能直接沿用。对于固定外场 $\boldsymbol B_0$，场不随 $s$ 改变，积分给出 $-\boldsymbol m\cdot\boldsymbol B_0$，没有二分之一。

超导体能量求导的全过程是

$$
\frac{dU_{\rm S}}{d\theta}
=\frac A2\,2\cos\theta(-\sin\theta)
=-A\sin\theta\cos\theta.
$$

于是 $\tau_y=-dU/d\theta$ 与叉乘一致。真实磁矩与诱导场的角度依赖共同参与求导，不能一边把镜像当作独立固定场源，一边又在能量中让它随磁矩变化。

（10）阻尼选择取向的能量依据。

设转动惯量 $J>0$，阻尼力矩为 $-b\dot\theta$，$b>0$。有

$$
J\ddot\theta=-\frac{dU}{d\theta}-b\dot\theta,\qquad
\mathcal E_{\rm rot}=\frac J2\dot\theta^2+U(\theta).
$$

方程乘以 $\dot\theta$，得到

$$
\frac{d\mathcal E_{\rm rot}}{dt}=-b\dot\theta^2\le0.
$$

一般运动的转动能逐渐下降，最终落入能量谷底。超导体的垂直与平行取向能量差为 $A/2$；软磁体高低次序互换，差值仍为 $A/2$。介质决定能量谷底的位置，阻尼负责耗散运动能量。

若解除磁矩在 $xz$ 平面内的限制，超导体的所有面内方向具有相同最小能量：离开界面的扰动有恢复力矩，改变面内方位没有恢复力矩。软磁体的两个法向方向仍为离散的稳定取向。本题二维限制才将超导体的连续面内方向缩为 $\pm\hat{\boldsymbol x}$。


## 六、关键洞察

“镜像反向”必须分清分量。法向磁矩和切向磁矩对边界场的作用不同，不应把整个向量统一乘以 $-1$。超导体与软磁体的镜像彼此相反，但它们各自都不是普遍与真实磁矩同向或反向。

力矩只依赖真实位置的诱导外场；能量则同时计入产生诱导响应的过程。这解释了直接力矩公式没有 $1/2$，而诱导能量有 $1/2$，两者并不矛盾。

## 七、易错点

- 仅在 $(0,0,0)$ 检验边界，无法充分限制切向磁矩。
- 用超导体的 $B_n=0$ 条件解软磁体，或认为超导体也要求所有切向场为零。
- 计算轴线上磁场时漏掉法向分量的系数2。
- 把 $\theta$ 的正方向与 $y$ 力矩方向对应反了。
- 只列出四个零力矩方向，没有检验恢复力矩。
- 对随真实磁矩改变的镜像使用固定外场的能量表达式。

## 八、课堂讲解建议

先把磁矩拆成两个分量，分别画出镜像，再组合回任意角度。推导边界时使用一般场点，避免从一张特殊轴线图猜答案。

力矩部分可先让学生在 $\theta=45^\circ$ 时用右手定则判断方向，再写叉乘。稳定性部分用 $\theta=\theta_*+\epsilon$ 展开，最后用能量曲线复核。把诱导能量的因子 $1/2$ 留到直接力矩完成后讨论，有利于理解其来源。

## 九、变式训练

### 变式1　有限磁导率介质

下半空间为线性磁性介质，磁导率为有限正数 $\mu$，无自由面电流。求镜像及稳定取向。

**解答。** 定义 $\eta=(\mu-\mu_0)/(\mu+\mu_0)$。可由标量势边界条件求其符号：真空侧磁势写成真实源加镜像源，下半空间写成透射源。将切向 $H$ 连续转化为界面磁势连续，法向 $B$ 连续给出其法向导数乘以各自磁导率相等。

分别对切向偶极分量应用两个条件，若透射系数为 $t_x$，得到

$$
1+\alpha_x=t_x,\qquad \mu_0(1-\alpha_x)=\mu t_x,
$$

所以 $\alpha_x=(\mu_0-\mu)/(\mu_0+\mu)=-\eta$。对法向分量，镜像的界面磁势符号反向，条件为

$$
1-\alpha_z=t_z,\qquad \mu_0(1+\alpha_z)=\mu t_z,
$$

故 $\alpha_z=\eta$。因此

$$
\boldsymbol m'=\eta(-m_x\hat{\boldsymbol x}+m_z\hat{\boldsymbol z}),
\qquad \tau_y=-\eta A\sin\theta\cos\theta.
$$

若 $\eta>0$，稳定取向垂直界面；若 $\eta<0$，稳定取向平行界面；若 $\mu=\mu_0$，$\eta=0$，平面不产生镜像响应，也没有取向选择。$\mu\to\infty$ 与形式极限 $\mu\to0$ 分别恢复本题两种镜像；超导体的磁通排斥仍应按本题理想边界理解。

### 变式2　竖直作用力

保持磁矩取向固定，求超导体与理想软磁体对真实偶极子的竖直力。

**解答。** 能量中 $A=\mu_0m^2/(32\pi h^3)$，因此

$$
F_{{\rm S},z}=-\frac{\partial U_{\rm S}}{\partial h}
=\frac{3\mu_0m^2}{64\pi h^4}(1+\cos^2\theta),
\qquad F_{{\rm I},z}=-F_{{\rm S},z}.
$$

超导体为排斥力，软磁体为吸引力。法向取向的力是切向取向的两倍。这个导数包含镜像位置随 $h$ 改变的效应，必须同时使用诱导能量的 $1/2$。

也可固定镜像的位置和磁矩，对真实偶极子所在场点计算 $\partial_z(\boldsymbol m\cdot\boldsymbol B')$；距离 $2h$ 的场按距离三次方下降，得到同一结果。这条外场求力路线不再额外乘 $1/2$。

### 变式3　稳定方向附近的小振动

设偶极子绕 $y$ 轴的转动惯量为 $J$，阻尼力矩为 $-b\dot\theta$。求两种理想介质情况下的小振动频率。

**解答。** 在各自稳定方向写 $\theta=\theta_*+\epsilon$，两种情况均有 $\tau_y=-A\epsilon+O(\epsilon^3)$。于是

$$
J\ddot\epsilon+b\dot\epsilon+A\epsilon=0.
$$

无阻尼角频率为 $\omega_{\rm lib}=\sqrt{A/J}$。若 $b^2<4JA$，解为振幅按 $e^{-bt/(2J)}$ 衰减的振动，其角频率为

$$
\omega_{\rm d}=\sqrt{\frac AJ-\frac{b^2}{4J^2}}.
$$

有限磁导率时，将 $A$ 换为 $|\eta|A$。随着 $\mu\to\mu_0$，恢复力和振动频率均趋于零，符合界面失去磁响应的极限。

### 变式4　超导平面上方再加均匀磁场

在超导体情形，假设外加背景场在真实偶极子位置为 $B_0\hat{\boldsymbol z}$，且该局部背景场不随偶极子取向变化。$B_0>0$。求稳定角。

**解答。** 总取向能量为

$$
U=\frac A2(1+\cos^2\theta)-mB_0\cos\theta.
$$

把 $q=\cos\theta$ 作为变量，$-1\le q\le1$。配方：

$$
U=\frac A2\left(q-\frac{mB_0}{A}\right)^2
+\frac A2-\frac{m^2B_0^2}{2A}.
$$

若 $0<mB_0<A$，最小值在 $q=mB_0/A$，即磁矩从平行方向逐渐偏向 $+z$，两侧倾斜方向均可。若 $mB_0\ge A$，受约束的最小值在 $q=1$，稳定方向为 $+z$。

从力矩看，$\tau_y=\sin\theta(A\cos\theta-mB_0)$，给出同样结果。临界场 $B_{\rm c}=A/m=\mu_0m/(32\pi h^3)$。这里的 $B_0$ 是指定的局部背景场；若需要从边界外的实际线圈场求它，还须另行计算超导体对背景场的响应。
