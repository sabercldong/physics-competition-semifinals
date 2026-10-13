# 第 7 题　双黑洞旋近的辐射与轨道演化（40分）

双黑洞并合分为旋近、并合、衰荡三个阶段。旋近阶段，两黑洞绕系统质心在同一平面内作近似圆周运动，机械能损失转为引力波辐射能，间距$L$逐渐减小。

在旋近阶段忽略黑洞自转与大小，将它们视为质量$M,m$的质点。系统除引力波辐射外没有能量耗散；不考虑辐射反作用的详细形式，轨道关系用牛顿引力近似。

![图7a　双质点绕共同质心旋近](../figures/q7-binary.png)

（1）辐射功率与$G$正比，可与$M,m,L$、绕质心的转动惯量$I$、角速度$\omega$、辐射传播速度$c$有关。取描述转动体系的三个物理量，与$G$一起用量纲分析求功率形式，无量纲比例系数记为$\alpha$。

（2）已知$t=0$时两黑洞间距$L_0$，$\alpha$为已知常量。求两黑洞从$t=0$开始绕系统质心旋转360°所需时间。

（3）求当间距缩为$L_0/2$时，自初始时刻起旋转的度数。

## 一、题型定位

本题用量纲分析建立辐射功率，再用近似圆轨道关系和能量守恒把辐射转成轨道参数演化。系统失去机械能，轨道能量变得更负，间距减小、角速度升高。

第二问不能以初始角速度固定不变算$2\pi/\omega_0$，因为旋转过程中轨道在缩小。应求角速度随时间的变化并积分角位移。

牛顿准圆旋近模型有适用区间。形式上间距可降到零，但真实黑洞会进入并合；若代数式要求越过这一模型端点，不能给出没有物理分支的“一整圈时间”。

## 二、知识点

### 1. 量纲选择

描述转动体系选择$I,\omega,c$。设

$$
P=\alpha G I^a\omega^bc^d.
$$

已知

$$
[G]=\mathrm{L^3M^{-1}T^{-2}},
\quad [I]=\mathrm{ML^2},
\quad[\omega]=\mathrm{T^{-1}},
\quad[c]=\mathrm{LT^{-1}}.
$$

功率量纲为$\mathrm{ML^2T^{-3}}$。这里$\alpha$承载量纲分析不能决定的纯数信息；题目后续假设它是给定常量。

### 2. 质心与约化质量

令总质量$S=M+m$，约化质量

$$
\mu=\frac{Mm}{M+m}.
$$

两质点到质心的距离$r_M,r_m$满足

$$
Mr_M=mr_m,\qquad r_M+r_m=L,
$$

故

$$
r_M=\frac mS L,\qquad r_m=\frac MS L.
$$

绕质心的总惯量

$$
I=Mr_M^2+mr_m^2=\mu L^2.
$$

### 3. 圆轨道关系

两质点分别受同样大小的引力$GMm/L^2$。对较小质量$m$写

$$
\frac{GMm}{L^2}=m\omega^2r_m.
$$

代$r_m=ML/S$，得到

$$
\boxed{\omega^2=\frac{GS}{L^3}}.
$$

轨道总动能

$$
K=\frac12I\omega^2=\frac{GMm}{2L},
$$

引力势能$U=-GMm/L$，故总机械能

$$
\boxed{E=-\frac{GMm}{2L}}.
$$

### 4. 辐射能量平衡

辐射功率$P>0$使系统机械能变化为

$$
\frac{dE}{dt}=-P.
$$

因为$E(L)$随$L$增大而增大，$dE/dL=GMm/(2L^2)>0$，所以失能必有$\dot L<0$。

## 三、物理图像

两质点相对质心有相同角速度，但转动半径不同。较重质点靠近质心，较轻质点离质心较远，所有轨道关系可以由约化质量集中表示。

辐射使$E$降低，即变得更负。由$\omega\propto L^{-3/2}$，旋转越来越快；引力波频率随之升高，形成“啁啾”的频率增长。

![图7b　间距与角速度的归一化演化](../figures/q7-evolution.png)

图中的横坐标使用形式上的演化时间尺度，越接近端点，间距下降越快、频率增长越快。靠近端点时慢变化近圆轨道与牛顿近似都会失效，应在实际适用范围内解释。

## 四、解题入口

先量纲求$P$，再代$I=\mu L^2$和$\omega^2=GS/L^3$，将功率化成单一$L$函数。对$E(L)$求导得到一阶$\dot L$方程。

从$L(t)$求$\omega(t)$，积分

$$
\Delta\theta(t)=\int_0^t\omega(s)\,ds.
$$

第二问令$\Delta\theta=2\pi$并筛选$t$；第三问先求$L/L_0=1/2$对应的参数，再算角位移，最后换成度。

## 五、解析

### （1）辐射功率的量纲

代入量纲，

$$
[G I^a\omega^bc^d]
=\mathrm{M^{a-1}L^{3+2a+d}T^{-2-b-d}}.
$$

与$\mathrm{ML^2T^{-3}}$比较，得到

$$
a-1=1,\qquad 3+2a+d=2,\qquad -2-b-d=-3.
$$

依次解出

$$
a=2,\qquad d=-5,\qquad b=6.
$$

因此

$$
\boxed{P=\frac{\alpha G I^2\omega^6}{c^5}}.
$$

量纲正确：

$$
\frac{(\mathrm{L^3M^{-1}T^{-2}})
(\mathrm{M^2L^4})(\mathrm{T^{-6}})}
{\mathrm{L^5T^{-5}}}
=\mathrm{ML^2T^{-3}}.
$$

这个分析不能单独确定$\alpha$的数值，也不能证明所有辐射体系都只有这三个参数；它依据题目指定的近圆双质点模型和选取的转动变量。

### 将辐射功率写成间距函数

利用$I=\mu L^2$、$\omega^6=G^3S^3/L^9$，

$$
\begin{aligned}
P
&=\frac{\alpha G}{c^5}
\mu^2L^4\frac{G^3S^3}{L^9}\\
&=\frac{\alpha G^4\mu^2S^3}{c^5L^5}\\
&=\boxed{\frac{\alpha G^4M^2m^2S}{c^5L^5}}.
\end{aligned}
$$

功率随间距的五次倒数增长。虽然惯量随$L^2$降低，角速度六次方增长更强，使整体辐射增强。

### （2）间距的微分方程

机械能$E=-GMm/(2L)$，所以

$$
\frac{dE}{dt}
=\frac{GMm}{2L^2}\dot L.
$$

令其等于$-P$，

$$
\frac{GMm}{2L^2}\dot L
=-\frac{\alpha G^4M^2m^2S}{c^5L^5}.
$$

定义正量

$$
\boxed{\mathcal A=\frac{2\alpha G^3MmS}{c^5}},
$$

量纲为$\mathrm{L^4/T}$。得到

$$
\boxed{\dot L=-\frac{\mathcal A}{L^3}}.
$$

对两边乘$4L^3$，

$$
\frac{d(L^4)}{dt}=-4\mathcal A.
$$

积分并用$L(0)=L_0$，

$$
\boxed{L(t)=[L_0^4-4\mathcal A t]^{1/4}}.
$$

选择正根，因为间距为正。形式解的时间范围$0\leq t<t_c$，其中

$$
\boxed{
t_c=\frac{L_0^4}{4\mathcal A}
=\frac{c^5L_0^4}{8\alpha G^3MmS}}.
$$

该$t_c$是本模型的形式端点，不是对真实黑洞并合时刻的完整预测。

### 角速度随时间增加

初始角速度

$$
\omega_0=\sqrt{\frac{GS}{L_0^3}}.
$$

由圆轨道关系，

$$
\boxed{
\omega(t)=\omega_0
\left(1-\frac t{t_c}\right)^{-3/8}}.
$$

初始角速度随辐射而增大，指数$-3/8$来自$L\propto(1-t/t_c)^{1/4}$与$\omega\propto L^{-3/2}$的组合。

### 角位移的积分

积分

$$
\Delta\theta(t)
=\omega_0\int_0^t
\left(1-\frac s{t_c}\right)^{-3/8}ds.
$$

令$z=1-s/t_c$，$ds=-t_cdz$，上下限从1到$1-t/t_c$。因此

$$
\begin{aligned}
\Delta\theta(t)
&=\omega_0t_c
\int_{1-t/t_c}^1z^{-3/8}dz\\
&=\frac85\omega_0t_c
\left[1-\left(1-\frac t{t_c}\right)^{5/8}\right].
\end{aligned}
$$

定义

$$
\boxed{
\Theta_c=\frac85\omega_0t_c
=\frac{c^5L_0^{5/2}}
{5\alpha G^{5/2}Mm\sqrt S}}.
$$

于是

$$
\boxed{
\Delta\theta(t)=\Theta_c
\left[1-\left(1-\frac t{t_c}\right)^{5/8}\right]}.
$$

$\Theta_c$是形式上从$L_0$到零间距的累计角位移。角速度虽然在端点发散，积分仍有限，因为指数$3/8<1$。

### 一整圈时间的分支条件

令$\Delta\theta=2\pi$，定义

$$
\chi=\frac{2\pi}{\Theta_c}
=\frac{10\pi\alpha G^{5/2}Mm\sqrt S}
{c^5L_0^{5/2}}.
$$

方程为

$$
\left(1-\frac{t_1}{t_c}\right)^{5/8}=1-\chi.
$$

左侧在物理分支非负。若希望整圈在正间距处完成，需

$$
\boxed{0<\chi<1}.
$$

此时

$$
\boxed{
t_1=t_c\left[1-(1-\chi)^{8/5}\right]}.
$$

用原参数展开，

$$
\boxed{
\begin{aligned}
t_1={}&\frac{c^5L_0^4}{8\alpha G^3Mm(M+m)}\\
&\times\left\{
1-\left[
1-\frac{10\pi\alpha G^{5/2}Mm\sqrt{M+m}}
{c^5L_0^{5/2}}
\right]^{8/5}
\right\}.
\end{aligned}}
$$

若$\chi=1$，形式整圈恰好在零间距端点完成，而端点不属于慢旋近有效区；若$\chi>1$，这个模型在端点前累计转角不足一圈。不能将负的$1-\chi$取分数幂并将其解释成另一条真实时间解。

### 缓慢耗散的周期检查

当$\chi\ll1$，二项展开

$$
1-(1-\chi)^{8/5}
=\frac85\chi-\frac{12}{25}\chi^2+O(\chi^3).
$$

利用$t_c(8/5)\chi=2\pi/\omega_0$，

$$
\boxed{
t_1=\frac{2\pi}{\omega_0}
\left[1-\frac3{10}\chi+O(\chi^2)\right]}.
$$

无耗散极限$\alpha\to0$时，$\chi\to0$、$t_c\to\infty$，乘积保持有限，恢复初始轨道周期。实际$t_1$略短于该周期，因为角速度在一圈内逐渐增大。

### （3）间距缩小一半的时间

令$L=L_0/2$，则

$$
\left(\frac L{L_0}\right)^4
=1-\frac t{t_c}=\frac1{16}.
$$

因此

$$
\boxed{
t_{1/2}=\frac{15}{16}t_c
=\frac{15c^5L_0^4}
{128\alpha G^3MmS}}.
$$

求得这段时间后，还需积分角速度并换算为度；时间结果也可用于核对中间计算。

### 半间距对应的累计角位移

代$1-t/t_c=1/16$，

$$
\left(1-\frac{t_{1/2}}{t_c}\right)^{5/8}
=16^{-5/8}=2^{-5/2}=\frac{\sqrt2}{8}.
$$

所以弧度为

$$
\boxed{
\Delta\theta_{1/2}
=\Theta_c\left(1-\frac{\sqrt2}{8}\right)}.
$$

换成度数，

$$
\boxed{
\begin{aligned}
\Delta\theta_{1/2}^{(\deg)}
={}&\left(1-\frac{\sqrt2}{8}\right)
\frac{c^5L_0^{5/2}}
{5\alpha G^{5/2}Mm\sqrt{M+m}}\\
&\times\frac{180^\circ}{\pi}.
\end{aligned}}
$$

角位移不是将初始$\omega_0$乘$t_{1/2}$。这一段经历很大的频率变化：半间距时$\omega/\omega_0=2^{3/2}=2\sqrt2$。

### 直接对间距积分的独立路线

由$\dot L=-\mathcal A/L^3$，

$$
dt=-\frac{L^3}{\mathcal A}\,dL.
$$

角位移微元

$$
d\theta=\omega\,dt
=-\frac{\sqrt{GS}}{\mathcal A}L^{3/2}\,dL.
$$

从$L_0$积分到$L$，

$$
\boxed{
\Delta\theta(L)
=\frac{2\sqrt{GS}}{5\mathcal A}
(L_0^{5/2}-L^{5/2})}.
$$

代$L=L_0(1-t/t_c)^{1/4}$恢复先前时间式，代$L=L_0/2$恢复半间距结果。这个积分将微分方程与角运动关系直接相接，提供不同消元路径。

### 用角速度方程再检查

由$\omega=\sqrt{GS}L^{-3/2}$，

$$
\dot\omega=-\frac32\sqrt{GS}L^{-5/2}\dot L
=\frac32\mathcal A\sqrt{GS}L^{-11/2}.
$$

消去$L$，

$$
\boxed{
\dot\omega
=\frac{3\alpha G^{5/3}Mm}
{c^5S^{1/3}}\omega^{11/3}}.
$$

分离变量，

$$
\omega^{-11/3}d\omega
=\frac{3\alpha G^{5/3}Mm}{c^5S^{1/3}}dt,
$$

积分得

$$
\omega^{-8/3}
=\omega_0^{-8/3}
-\frac{8\alpha G^{5/3}Mm}{c^5S^{1/3}}t.
$$

它与$\omega(t)=\omega_0(1-t/t_c)^{-3/8}$一致，独立核对了幂次和系数。

### 近圆与牛顿近似的适用条件

径向变化相对一圈运动必须缓慢：

$$
\epsilon_{\rm ad}
=\frac{|\dot L|}{L\omega}
=\frac{\mathcal A}{\sqrt{GS}\,L^{5/2}}\ll1.
$$

牛顿轨道速度尺度$\omega L=\sqrt{GS/L}$也应明显小于$c$，即$GS/(Lc^2)\ll1$。随着$L$减小，两个条件都会变差。

因此形式解在$t_c$附近的发散主要提示模型失效。题目关注旋近阶段，不能把这条近似曲线当作真实并合或衰荡的完整解。

## 六、关键洞察

轨道失能使负能量更负、半径更小、频率更大；“能量降低所以运动变慢”的日常直觉在束缚引力系统不适用。

量纲分析先确定功率结构，再由牛顿轨道消去$I,\omega$。得到的$L^{-5}$辐射律和$L^{-3}$缩距律有不同幂次，因为能量对$L$的导数参与了转换。

角速度端点发散并不意味着总转角无穷。必须检查积分，第二问整圈是否在有效模型内存在，还需要根的范围条件。

## 七、易错点

把$L$当成某一个黑洞的转动半径，会漏掉质心分配。惯量应$MmL^2/(M+m)$，不是$(M+m)L^2$。

能量平衡应$dE/dt=-P$。符号错会使轨道因辐射而增大。计算一圈时间不能固定$\omega=\omega_0$。

分数幂必须筛选底数与时间范围；半间距应代$L^4/L_0^4=1/16$，不是1/2。弧度转换为度还需$180^\circ/\pi$。

## 八、课堂讲解建议

先在质心图中标两半径，再引入约化质量。用量纲方程求三个指数，随后将功率和机械能都化成$L$。

画$L(t)$与$\omega(t)$，让学生先定性判断一圈时间比初始周期短还是长。积分后用$\alpha\to0$验证。

最后将“数学端点”“近似模型有效区”和“真实并合”分开。利用$\epsilon_{\rm ad}$说明为什么不能无限外推。

## 九、变式训练

### 变式1　固定总质量的质量比

总质量$S=M+m$、初始间距$L_0$及$\alpha$固定时，哪种质量分配使半间距所需时间最短？

**解答：**$t_{1/2}\propto1/(Mm)$。在固定和$S$下，$Mm=M(S-M)\leq S^2/4$，等号在$M=m=S/2$。因此等质量双体辐射缩距最快，时间最短。极端质量比$m\to0$时功率$\propto m^2$、缩距速度$\propto m$趋零，时间增大。

### 变式2　任意缩距比例

求间距降为$\lambda L_0$（$0<\lambda<1$）时的时间、角速度与累计转角。

**解答：**

$$
t_\lambda=t_c(1-\lambda^4),\qquad
\omega_\lambda=\omega_0\lambda^{-3/2},
$$

$$
\Delta\theta_\lambda=\Theta_c(1-\lambda^{5/2}).
$$

三式分别来自间距方程、圆轨道关系和角位移积分。它们在$\lambda=1$给零时间和零转角，在$\lambda=1/2$恢复原题结果。

### 变式3　啁啾质量与频率增长

若辐射主频$f=\omega/\pi$，定义啁啾质量$\mathcal M=\mu^{3/5}S^{2/5}$。求$\dot f$的形式。

**解答：**$\mathcal M^{5/3}=\mu S^{2/3}=Mm/S^{1/3}$。由角速度方程，

$$
\dot f
=\frac{3\alpha\pi^{8/3}(G\mathcal M)^{5/3}}
{c^5}f^{11/3}.
$$

频率及其增长率可以组合约束$\mathcal M$，但仅靠这一个组合不能分别确定$M,m$。本变式明确指定辐射谐波关系，原题量纲分析本身不能决定它。

### 变式4　一圈中缩距很小的近似

在$\chi\ll1$时，求完成第一圈后$L_1/L_0$的一阶近似，并核对时间修正方向。

**解答：**由一圈角位移条件，$L_1^{5/2}/L_0^{5/2}=1-\chi$，所以

$$
\frac{L_1}{L_0}=(1-\chi)^{2/5}
=1-\frac25\chi+O(\chi^2).
$$

初始频率到末频率增加$\omega_1/\omega_0=(1-\chi)^{-3/5}\simeq1+3\chi/5$，平均频率一阶增加约$3\chi/10$，周期时间相应缩短$t_1\simeq(2\pi/\omega_0)(1-3\chi/10)$。它与精确积分展开一致。
