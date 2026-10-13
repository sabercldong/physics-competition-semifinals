# 第 2 题　弹簧腿机器人的一次支撑过程

机器人在刚性水平地面上跑步，可简化为质量为 $m$ 的质点与一根劲度系数为 $k$ 的轻质直弹簧腿相连。整个运动始终在同一竖直平面内，每次着地时腿与地面的夹角均为 $\alpha_0$，它小于但接近 $90^\circ$。从着地到离地，腿与地面的接触点不动，腿可伸缩但不弯曲，长度变化量远小于自由长度 $l_0$。腿同时绕接触点转动，与地面的夹角始终接近 $90^\circ$。

某次刚着地时，腿长为 $l_0$，绕接触点顺时针转动的角速度大小为 $\omega$。以地面为重力势能零点，系统机械能为 $E$，并以刚着地时为 $t=0$。求：

（1）支撑过程中腿长随时间的变化关系，以及刚离地的时刻 $t'$；

（2）腿转过的角度 $\Delta\varphi$，须保留到非零结果。

已知重力加速度为 $g$，$\omega^2>g/l_0$。接触点无摩擦力矩，忽略空气阻力。腿与地面夹角的正弦可近似取1，但角度的时间变化率不可忽略；计算只保留弹簧腿相对形变量的一阶小量。本题45分。

![图2-1　触地后的极坐标、径向速度与顺时针转动方向。](../figures/q2-model.png)

## 一、题型定位

这是一道带有小形变近似的平面极坐标动力学题。腿的伸缩与转动耦合：径向加速度包含离心项，角速度又随长度变化。处理时应先保留这个耦合，再在 $r-l_0$ 上作一阶展开。

问题的关键不是普通竖直弹簧振子，而是离心项对有效振动频率的贡献。另一个关键是从周期运动中选出第一次恢复自然长度的时刻；这个时刻对应弹簧推力刚降为零。

## 二、知识点

- 极坐标径向加速度为 $\ddot r-r\dot\varphi^2$，切向加速度为 $r\ddot\varphi+2\dot r\dot\varphi$。
- 轻质弹簧的作用力沿腿方向，不对接触点产生力矩。
- 腿近似竖直时，重力径向分量约为 $-mg$，重力矩在本题角度近似下忽略。
- 机械能决定着地瞬间速度的大小；还要用“开始压缩”选择径向速度的负根。
- 首次离地条件是长度从小于 $l_0$ 的一侧回到 $l_0$，不能选择初始根或更晚的根。
- 角位移由瞬时角速度积分得到，即使角度接近 $90^\circ$，也不能把其变化率置零。

## 三、物理图像

取固定接触点为极坐标原点 $O$，$r$ 为腿长，$\varphi$ 为从水平向右方向逆时针计量的角度。于是初始角速度为 $\dot\varphi(0)=-\omega$，而顺时针转过的角度大小为

$$
\Delta\varphi=-\int_0^{t'}\dot\varphi\,dt.
$$

用 $\delta=r-l_0$ 表示伸长量。支撑期内 $\delta<0$，弹簧处于压缩状态。地面不能把腿向下拉住，因此不能把恢复长度后的数学解继续当作支撑运动。

![图2-2　一次支撑中的长度变化：初始压缩、最短长度、首次恢复自然长度。](../figures/q2-compression.png)

在径向上，弹簧力为 $-k\delta$，重力为 $-mg$。转动给出向外的运动学项 $r\dot\varphi^2$。题给 $\omega^2l_0>g$，意味着在自然长度处径向加速度向外；压缩之所以发生，是因为着地瞬间具有足够的向内径向速度。

## 四、解题入口

先由初始机械能求向内速度大小 $u$，然后用接触点角动量近似守恒得到 $\dot\varphi=-\omega l_0^2/r^2$。把它代入径向方程，展开 $r^{-3}$，解带常量驱动的简谐方程。离地时间用半角公式处理；最后积分角速度，保留长度变化造成的一阶修正。

为缩短代数，定义

$$
u=\sqrt{\frac{2E}{m}-l_0^2\omega^2-2gl_0},\qquad
a=\omega^2l_0-g,\qquad
\Omega^2=\frac{k}{m}+3\omega^2.
$$

其中 $u$ 的单位是速度，$a$ 的单位是加速度，$\Omega$ 的单位是角频率。本题有效的非零支撑过程要求 $u>0$。

## 五、解析

（1）由能量确定初始径向速度。

刚着地时，弹簧没有弹性势能，质点高度为 $l_0\sin\alpha_0\simeq l_0$。速度分成互相垂直的径向与切向两部分，切向速率为 $l_0\omega$，因此

$$
E=\frac{m}{2}\left[\dot r(0)^2+l_0^2\omega^2\right]+mgl_0.
$$

解出

$$
\dot r(0)^2=\frac{2E}{m}-l_0^2\omega^2-2gl_0=u^2.
$$

刚着地随后压缩，故选择 $\dot r(0)=-u$。若根号内为负，题给初始状态不能实现；若 $u=0$，因 $a>0$，腿在自然长度处立即趋向伸长，不能形成题设的有限压缩阶段。

（2）把转动方程化成角动量关系。

接触点固定，腿力不产生力矩。重力矩为

$$
\tau_O=-mgr\cos\varphi.
$$

在题给的近竖直角度近似下，取 $\cos\varphi\simeq0$，因此

$$
\frac{d}{dt}(mr^2\dot\varphi)\simeq0.
$$

由初始条件确定常数：

$$
mr^2\dot\varphi=-ml_0^2\omega,
\qquad
\dot\varphi=-\frac{l_0^2\omega}{r^2}.
\tag{2.1}
$$

这里的近似角动量守恒只用于本题规定的近竖直过程。若腿摆过很大角度，重力矩不能忽略，便不能沿用式（2.1）。

（3）建立并线性化径向方程。

沿向外的径向取正，有

$$
m(\ddot r-r\dot\varphi^2)=-k(r-l_0)-mg.
$$

代入式（2.1），得到

$$
\ddot r=\frac{l_0^4\omega^2}{r^3}-\frac{k}{m}(r-l_0)-g.
$$

令 $r=l_0+\delta$，并用

$$
\frac{1}{r^3}
=\frac{1}{l_0^3}\left(1+\frac{\delta}{l_0}\right)^{-3}
\simeq\frac{1}{l_0^3}\left(1-\frac{3\delta}{l_0}\right).
$$

于是

$$
\ddot\delta=\omega^2l_0-3\omega^2\delta-\frac{k}{m}\delta-g,
$$

即

$$
\ddot\delta+\Omega^2\delta=a.
\tag{2.2}
$$

$3\omega^2$ 来自角动量守恒下的离心项展开。如果先把 $\dot\varphi$ 固定为 $-\omega$，会得到不同的线性系数；那样舍弃了与本题所保留形变同阶的角速度变化。

（4）解初值问题。

式（2.2）的常数特解为 $a/\Omega^2$，通解写成

$$
\delta=\frac{a}{\Omega^2}+A\cos\Omega t+B\sin\Omega t.
$$

由 $\delta(0)=0$ 和 $\dot\delta(0)=-u$，有 $A=-a/\Omega^2$、$B=-u/\Omega$。故

$$
\boxed{r(t)=l_0+\frac{a}{\Omega^2}(1-\cos\Omega t)
-\frac{u}{\Omega}\sin\Omega t,\quad 0\le t\le t'.}
\tag{2.3}
$$

初始导数为 $-u$，初始二阶导数为 $a$，均与先前动力学一致。对很小的正时间，$\delta=-ut+at^2/2+\cdots<0$，确实先压缩。

（5）选择第一次离地的根。

离地时 $\delta(t')=0$。令 $q=\Omega t'$，则

$$
a(1-\cos q)=\Omega u\sin q.
$$

使用 $1-\cos q=2\sin^2(q/2)$ 与 $\sin q=2\sin(q/2)\cos(q/2)$，除去初始根 $\sin(q/2)=0$，得

$$
\tan\frac q2=\frac{\Omega u}{a}.
$$

因 $a,u>0$，首次非零根位于 $0<q<\pi$，因此

$$
\boxed{t'=\frac{2}{\Omega}\arctan\frac{\Omega u}{a}.}
\tag{2.4}
$$

不存在把反正切加上 $\pi$ 的自由：那会选到已经离地后的数学延拓。代回速度表达式

$$
\dot\delta=\frac a\Omega\sin\Omega t-u\cos\Omega t,
$$

使用半角关系可得 $\dot\delta(t')=u>0$，说明长度在向外恢复。

（6）积分求顺时针角位移。

由式（2.1），在形变一阶精度内

$$
-\dot\varphi=\omega\left(1+\frac{\delta}{l_0}\right)^{-2}
\simeq\omega\left(1-\frac{2\delta}{l_0}\right).
$$

因此

$$
\Delta\varphi=\omega t'-\frac{2\omega}{l_0}\int_0^{t'}\delta(t)\,dt.
\tag{2.5}
$$

将式（2.3）逐项积分：

$$
\int_0^{t'}\delta\,dt
=\frac{a}{\Omega^2}\left(t'-\frac{\sin q}{\Omega}\right)
+\frac{u}{\Omega^2}(\cos q-1).
$$

令 $z=\Omega u/a$，则 $\sin q=2z/(1+z^2)$、$\cos q-1=-2z^2/(1+z^2)$。积分中的两个三角项合并为

$$
-\frac{a\sin q}{\Omega}+u(\cos q-1)
=-\frac{2u}{1+z^2}-\frac{2uz^2}{1+z^2}=-2u.
$$

故

$$
\int_0^{t'}\delta\,dt=\frac{at'-2u}{\Omega^2}.
$$

代入式（2.5），得到

$$
\boxed{\Delta\varphi
=\omega\left[\left(1-\frac{2a}{l_0\Omega^2}\right)t'
+\frac{4u}{l_0\Omega^2}\right].}
\tag{2.6}
$$

消去 $t'$ 后，也可写成

$$
\boxed{\Delta\varphi=\frac{2\omega}{\Omega}
\left[\left(1-\frac{2a}{l_0\Omega^2}\right)
\arctan\frac{\Omega u}{a}+\frac{2u}{l_0\Omega}\right].}
$$

这里 $\Delta\varphi$ 是顺时针转角的正值；以逆时针为正的有向角变化为 $-\Delta\varphi$。

（7）检查近似和物理趋势。

支撑期内 $\delta<0$，因此角速度大小大于 $\omega$，式（2.5）给出 $\Delta\varphi>\omega t'$。这一不等式可在积分前判断，有助于检查一阶修正的符号。

最小长度对应 $\dot\delta=0$，首次发生在

$$
\Omega t_{\min}=\arctan\frac{\Omega u}{a}=\frac{\Omega t'}2.
$$

代入式（2.3），最大压缩量为

$$
d_{\max}=-\delta_{\min}
=\frac{\sqrt{a^2+\Omega^2u^2}-a}{\Omega^2}.
\tag{2.7}
$$

计算结果须满足 $d_{\max}/l_0\ll1$；同时 $\Delta\varphi$ 及初始偏离竖直的角度均须足够小，才符合近竖直假设。这是两个不同的近似条件，不能只检查弹簧压缩量。

还可以用式（2.2）的积分验证回程速度：乘以 $\dot\delta$，得到

$$
\frac12\dot\delta^2+\frac12\Omega^2\delta^2-a\delta=\frac12u^2.
$$

在首次返回 $\delta=0$ 时，速度大小恢复为 $u$；经过压缩后的回程应取正根，与离地状态一致。

（8）由有效势独立推导径向方程。

在近竖直模型中，角动量大小 $\ell=ml_0^2\omega$ 固定。消去切向速度后，能量写成

$$
\frac m2\dot r^2+U_{\rm eff}(r)=E,
\qquad
U_{\rm eff}=\frac{k}{2}(r-l_0)^2+mgr+\frac{\ell^2}{2mr^2}.
$$

最后一项已经包含切向动能，不能再额外加上 $mr^2\omega^2/2$。重力势 $mgr$ 使用 $\sin\varphi\simeq1$，与之前忽略重力矩的角度近似配套。

令 $r=l_0+\delta$，转动能展开为

$$
\frac{\ell^2}{2mr^2}
=\frac{ml_0^2\omega^2}{2}
\left[1-\frac{2\delta}{l_0}
+\frac{3\delta^2}{l_0^2}
+O\left(\frac{\delta^3}{l_0^3}\right)\right].
$$

合并各项，

$$
U_{\rm eff}
=U_{\rm eff}(l_0)-ma\delta+\frac m2\Omega^2\delta^2
+O\left(\frac{m\omega^2|\delta|^3}{l_0}\right).
$$

从 $m\ddot\delta=-\partial U_{\rm eff}/\partial\delta$ 再次得到 $\ddot\delta+\Omega^2\delta=a$。方程保留形变一阶，势能却须保留到二阶，因为求导降一阶；只展开势能的一次项会丢失恢复系数。

（9）用能量积分确定支撑过程。

定义偏移中心和振幅

$$
\delta_c=\frac a{\Omega^2},\qquad
D=\sqrt{a^2+\Omega^2u^2},\qquad
A_r=\frac D{\Omega^2}.
$$

能量积分配方后成为

$$
\dot\delta^2+\Omega^2(\delta-\delta_c)^2=\Omega^2A_r^2.
$$

这是一条相平面椭圆。初始点为 $(0,-u)$，最短长度对应 $\delta_{\min}=\delta_c-A_r<0$。另一个数学转折点 $\delta_c+A_r>0$ 在自然长度之外，支撑早已结束，不属于本次接触运动。

压缩阶段取速度负根，回程取正根，两段时间相等：

$$
t'=2\int_{\delta_{\min}}^0
\frac{d\delta}{\sqrt{u^2+2a\delta-\Omega^2\delta^2}}.
$$

令 $\delta-\delta_c=-A_r\cos\psi$。从最短长度回到自然长度，$\psi$ 从0增到 $\psi_0$，其中

$$
\cos\psi_0=\frac aD,\qquad
\sin\psi_0=\frac{\Omega u}{D}.
$$

分母变为 $\Omega A_r\sin\psi$，分子为 $A_r\sin\psi\,d\psi$，故

$$
t'=\frac2\Omega\int_0^{\psi_0}d\psi
=\frac2\Omega\arctan\frac{\Omega u}{a}.
$$

这条推导独立于先前的时间函数求根。它解释了最短长度为什么出现在 $t'/2$，也说明支撑时间一般不等于半个简谐周期。

（10）用平均压缩量检查角位移。

定义支撑过程的平均压缩量

$$
\overline d=-\frac1{t'}\int_0^{t'}\delta\,dt
=\frac{2u-at'}{\Omega^2t'}.
$$

角位移可写成

$$
\Delta\varphi=\omega t'\left(1+\frac{2\overline d}{l_0}\right).
$$

支撑期 $-d_{\max}\le\delta\le0$，且除个别时刻外为严格不等式，所以

$$
0<\overline d<d_{\max},\qquad
1<\frac{\Delta\varphi}{\omega t'}
<1+\frac{2d_{\max}}{l_0}.
$$

这是无需重复积分的检验区间。若计算结果落在区间之外，应检查角速度展开的符号、离地根和积分端点。

也可直接证明平均压缩为正。令 $z=\Omega u/a>0$，利用

$$
\arctan z=\int_0^z\frac{ds}{1+s^2}<z,
$$

有 $at'=2a\arctan z/\Omega<2u$，因此 $2u-at'>0$。这里不是把一个负的形变量直接当作负的压缩量，二者定义正好相反。

（11）分别估计形变和角度近似。

用 $\eta=d_{\max}/l_0$ 衡量形变，用 $\zeta=\omega t'$ 衡量基本转角。$\eta\ll1$ 控制 $r^{-3},r^{-2}$ 展开的误差；$\zeta$ 加上初始偏离竖直的角度，控制重力分解和重力矩近似。两个条件不能互相替代。

径向方程舍弃的离心项首项为 $6\omega^2\delta^2/l_0$。与保留的恢复项 $\Omega^2|\delta|$ 比较，

$$
\frac{6\omega^2\delta^2/l_0}{\Omega^2|\delta|}
=\frac{6\omega^2}{\Omega^2}\frac{|\delta|}{l_0}
\le2\eta.
$$

角速度展开的下一项为 $3\omega\delta^2/l_0^2$，在支撑期的积分绝对值不超过 $3\omega t'\eta^2$。这给出一阶角位移所舍弃项的量级。

若 $\varphi=\pi/2+\gamma$，径向重力为 $-mg\cos\gamma=-mg[1+O(\gamma^2)]$，重力矩却为 $mgr\sin\gamma$，从角度一阶开始影响角动量。因此“正弦接近1”本身不能精确证明角动量守恒；守恒是本题近竖直、短支撑模型采用的领先阶近似，所得转角须反过来接受这一条件检验。

更高精度的运动须同时保留

$$
\begin{aligned}
m(\ddot r-r\dot\varphi^2)&=-k(r-l_0)-mg\sin\varphi,\\
\frac d{dt}(mr^2\dot\varphi)&=-mgr\cos\varphi,
\end{aligned}
$$

并在恢复自然长度后切换为飞行阶段。只提高一处展开阶数、仍忽略另一处同量级效应，不能保证整体精度提高。


## 六、关键洞察

弹簧的自由长度是离地界面，数学振动中心却在 $\delta=a/\Omega^2>0$。两者不重合，所以支撑期一般不是半个简谐周期。$t'$ 的半角公式描述的恰好是围绕偏移平衡点运动的第一次回归。

有效势中的二次项包含转动效应。角动量固定时，转动能为 $m l_0^4\omega^2/(2r^2)$；它对 $r$ 的二阶导数在 $l_0$ 处为 $3m\omega^2$，从能量法也能得到 $\Omega^2=k/m+3\omega^2$。

## 七、易错点

- 把题给机械能 $E$ 当成动能，会丢掉 $mgl_0$。
- 由平方关系取 $\dot r(0)=+u$，会得到从触地即伸长的错误过程。
- 一边用角动量守恒，一边在径向方程把角速度当作常量，精度不一致。
- 除去半角因子时忘记解释被舍弃的 $t=0$ 根。
- 把 $\sin\varphi\simeq1$ 理解为 $\dot\varphi=0$，从而错误地得到零转角。
- 角位移修正符号写成负值；压缩使转动加快，修正必须为正。

## 八、课堂讲解建议

先只画着地瞬间的径向和切向速度，让学生从能量求出 $u$ 并选择符号。随后写极坐标方程，保留原始非线性离心项，再展开到一阶。这样可以说明系数3的来源。

推导离地时间时，在图2-2上标出初始点、最小长度和首次回到自然长度的位置。把 $t'=t_{\min}\times2$ 作为求根后的检查，而不是预设“半周期”。角度部分先判断修正为正，再做积分和半角化简。

最后用最大压缩量和转角检查参数是否落在题设近似范围内。这一步可区分“方程解得出来”与“该解适用于所给机器人”。

## 九、变式训练

### 变式1　离心项刚好抵消重力

把题给条件改为 $\omega^2l_0=g$，保持 $u>0$ 和其余近似。求支撑时间和转角。

**解答。** 此时 $a=0$，但 $\Omega^2=k/m+3\omega^2$ 不为零。式（2.2）变成齐次振子：

$$
\delta=-\frac{u}{\Omega}\sin\Omega t.
$$

它在 $0<t<\pi/\Omega$ 内为负，首次回零为 $t'=\pi/\Omega$。积分为

$$
\int_0^{t'}\delta\,dt=-\frac{u}{\Omega^2}
\int_0^\pi\sin q\,dq=-\frac{2u}{\Omega^2}.
$$

因此

$$
\Delta\varphi=\omega\left(\frac{\pi}{\Omega}
+\frac{4u}{l_0\Omega^2}\right).
$$

这也等于原式在 $a\to0^+$、$u$ 固定时的极限，不能在原式中直接把 $\Omega u/a$ 当成普通有限数。

### 变式2　求最大地面支持力

原条件下，求最大压缩量、出现时刻以及弹簧传给接触点的最大力。

**解答。** 令 $\dot\delta=0$，首次根满足 $\tan(\Omega t_{\min})=\Omega u/a$，故 $t_{\min}=t'/2$。令 $D=\sqrt{a^2+\Omega^2u^2}$，该时刻 $\cos\Omega t_{\min}=a/D$、$\sin\Omega t_{\min}=\Omega u/D$。于是

$$
\delta_{\min}=\frac a{\Omega^2}
-\frac{a^2+\Omega^2u^2}{\Omega^2D}
=\frac{a-D}{\Omega^2}.
$$

轻质腿传递的轴向压缩力为 $k(-\delta)$，所以最大轴向力为

$$
F_{\max}=\frac{k}{\Omega^2}(D-a).
$$

近竖直条件下，其竖直分量约等于这个值；并不需要额外再加 $mg$。重力已通过质点运动方程影响 $\delta$，地面力等于腿传递的弹簧力。

### 变式3　由允许压缩量反求初始能量

给定允许的最大压缩量 $d\ll l_0$，求恰好压到该值时的向内初速和机械能。

**解答。** 在 $\delta=-d$、$\dot\delta=0$ 处使用有效能量积分：

$$
\frac12\Omega^2d^2+ad=\frac12u^2.
$$

所以

$$
u=\sqrt{\Omega^2d^2+2ad},\qquad
E=mgl_0+\frac m2
\left(l_0^2\omega^2+\Omega^2d^2+2ad\right).
$$

若已知 $u$ 而设计 $k$，可解出

$$
k=m\left(\frac{u^2-2ad}{d^2}-3\omega^2\right).
$$

右侧必须为正，还须检查转角是否足够小。一个正的机械能并不自动保证给出的压缩指标与正劲度弹簧相容。

### 变式4　增加弹簧劲度会怎样

固定 $m,l_0,\omega,u$，证明支撑时间随 $k$ 增大而减小，并求很硬弹簧的首项。

**解答。** 令 $x=\Omega u/a>0$，把 $t'=2\arctan x/\Omega$ 对 $\Omega$ 求导：

$$
\frac{dt'}{d\Omega}
=\frac{2}{\Omega^2}
\left[\frac{x}{1+x^2}-\arctan x\right].
$$

定义 $f(x)=\arctan x-x/(1+x^2)$，则 $f(0)=0$，且

$$
f'(x)=\frac{2x^2}{(1+x^2)^2}>0.
$$

所以括号内为负，$dt'/d\Omega<0$。又 $d\Omega/dk=1/(2m\Omega)>0$，故 $dt'/dk<0$。

当 $\Omega\to\infty$，

$$
\arctan\frac{\Omega u}{a}
=\frac{\pi}{2}-\frac{a}{\Omega u}+O(\Omega^{-3}),
$$

从而

$$
t'=\frac{\pi}{\Omega}-\frac{2a}{\Omega^2u}+O(\Omega^{-4}),
\quad d_{\max}=\frac{u}{\Omega}-\frac a{\Omega^2}+O(\Omega^{-3}).
$$

转角的首项为 $\Delta\varphi\simeq\pi\omega/\Omega$。较硬的弹簧同时缩短支撑时间与压缩量，但最大力的首项 $ku/\Omega\simeq u\sqrt{km}$ 会增大；降低压缩并不意味着降低冲击力。
