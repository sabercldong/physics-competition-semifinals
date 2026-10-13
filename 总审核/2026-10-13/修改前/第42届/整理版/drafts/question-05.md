# 第 5 题　约瑟夫森结的时间相位、磁通干涉与小振动

理想约瑟夫森结由“超导体—薄绝缘层—超导体”组成。以结中心为原点，绝缘层厚度为 $d\ll Y,Z$，其 $y$-$z$ 截面的边长为 $Y,Z$；电流沿 $x$ 方向。两超导体波函数相位分别为 $\varphi_1,\varphi_2$，相位差
$\delta=\varphi_2-\varphi_1$。结电流密度和相位满足
$$
j=j_0\sin\delta,\qquad
\frac{\partial\delta}{\partial t}=\frac{2e}{\hbar}U.
$$
$j_0>0$，$\hbar$ 为约化普朗克常量，$e>0$。以上关系在外磁场为零和非零时均成立；无外磁场时相位差与空间无关。

（1）结两端加恒定直流电压 $U_0$，初相位为 $\delta(0)$。求电流密度 $j(t)$ 及周期。

（2）令 $U=0$，沿 $z$ 方向加静磁场。由于超导体屏蔽，磁场只存在于绝缘层及两侧各厚度为 $\lambda$ 的等效区域。绝缘层内
$\mathbf B=B_z(y)\mathbf e_z$，相位满足
$$
\frac{d\delta}{dy}=\frac{2e(d+2\lambda)}{\hbar}B_z(y).
$$
（2.1）忽略电流自生磁场，$B_z=B_0$ 为常数。求
$\delta(y)$、总电流 $I_J(B_0)$，以及 $I_J=0$ 对应的 $B_0$。已知 $\delta(0)=\delta_0\ne k\pi$。
（2.2）考虑电流自生磁场，证明
$$
\frac{d^2\delta}{dy^2}=\frac1{\lambda_J^2}\sin\delta,
$$
并求约瑟夫森穿透深度 $\lambda_J$。绝缘层磁导率为 $\mu_0$。

（3）外磁场为零，宏观模型为理想约瑟夫森结 $J$ 与电阻 $R$、电容 $C$ 并联，外加恒定偏置电流 $I$，记 $I_0=j_0YZ$。
（3.1）用 $\delta(t)$ 及其导数表示三个支路电流，导出相位方程。
以下认为 $R$ 足够大，可忽略电阻支路。
（3.2）将方程类比为单位质量粒子在势 $V(\delta)$ 中运动。求势、存在势阱的电流范围、阱底相位及小振动角频率 $\omega$。
（3.3）$\omega$ 的最大值为 $\omega_J$，已知结中电磁波速度
$\tilde c=\omega_J\lambda_J$。绝缘层相对介电常数
$\epsilon_r=9.0$，$d=3.0\,\mathrm{nm}$，$\lambda=53\,\mathrm{nm}$，求 $\tilde c/c$，保留两位有效数字。本题45分。

![图5-1　绝缘层与两侧磁场穿透区域形成有效磁厚度 $d+2\lambda$。](../figures/q5-junction.png)

![图5-2　电阻、电容与理想约瑟夫森结并联，三个支路具有相同电压。](../figures/q5-rcsj.png)

## 一、题型定位

同一相位变量在时间方向和空间方向分别受电压、磁场控制。时间相位线性增长产生交流电流；空间相位线性变化使不同位置的电流相互抵消。考虑自生磁场后，空间相位满足非线性微分方程。

电容使相位获得类似惯性的二阶时间项，偏置电流使周期势倾斜，平衡与小振动频率由势的导数决定。结中波速最后由时间响应尺度与空间穿透尺度的乘积给出。

## 二、知识点

- 相位积分、正弦电流与交流周期。
- 有限宽结的空间积分及干涉零点。
- 安培定律、非线性空间方程。
- 并联电路的电流守恒与电容电流。
- 势能曲率、稳定与不稳定平衡。
- 临界偏置、小振动与势垒。
- 平行板电容、有效磁厚度与波速。

## 三、物理图像

电压不为零时，相位不断推进，因此即使电压恒定，约瑟夫森电流仍随时间振荡。静磁场在结宽度方向造成相位梯度，局部电流可以正负不同，总电流需对整个截面积分。

在偏置电流模型中，相位像一个在波浪形斜坡上运动的坐标。偏置较小时仍有局部谷底；偏置接近临界电流时谷底与峰顶合并，小振动变慢；超过临界后没有静止阱底。

## 四、解题入口

先定义有效磁厚度与磁通量子
$$
d_{\rm eff}=d+2\lambda,\qquad
\Phi_0=\frac{\pi\hbar}{e}.
$$
静磁场问题使用
$\beta=2ed_{\rm eff}B_0/\hbar$，相位为
$\delta_0+\beta y$，总电流在 $-Y/2$ 至 $Y/2$ 积分。

并联电路先写共同电压
$U=(\hbar/2e)\dot\delta$，再逐个写支路电流。类比单位质量时应先将相位方程除以
$\hbar C/(2e)$；否则势与频率的系数会错。

## 五、解析

（1）直流电压下的交流约瑟夫森电流。

$U=U_0$ 恒定，积分相位方程：
$$
\delta(t)=\delta(0)+\frac{2eU_0}{\hbar}t.
$$
于是
$$
\boxed{j(t)=j_0\sin\!\left(\delta(0)+\frac{2eU_0}{\hbar}t\right).}\tag{5.1}
$$
非零 $U_0$ 时角频率大小及周期为
$$
\boxed{\omega_{\rm ac}=\frac{2e|U_0|}{\hbar},\qquad
T_{\rm ac}=\frac{\pi\hbar}{e|U_0|}.}\tag{5.2}
$$
电压若为负，相位推进方向相反，但周期仍为正。$U_0=0$ 时相位恒定、电流为直流，不存在有限的上述振荡周期。

（2）均匀静磁场造成线性空间相位。

由题给空间相位方程，
$$
\frac{d\delta}{dy}=\beta,\qquad
\beta=\frac{2ed_{\rm eff}B_0}{\hbar}.
$$
用中心相位 $\delta(0)=\delta_0$：
$$
\boxed{\delta(y)=\delta_0+\beta y.}\tag{5.3}
$$
局部电流密度为 $j_0\sin(\delta_0+\beta y)$。总电流是
$$
I_J=j_0Z\int_{-Y/2}^{Y/2}\sin(\delta_0+\beta y)\,dy.
$$
展开正弦：
$$
\sin(\delta_0+\beta y)
=\sin\delta_0\cos\beta y+\cos\delta_0\sin\beta y.
$$
第二项为奇函数，关于中心对称积分为零，第一项积分给出
$$
I_J=\frac{2j_0Z}{\beta}\sin\delta_0\sin\frac{\beta Y}{2}.
$$
定义 $\chi=\beta Y/2$，得到
$$
\boxed{I_J=I_0\sin\delta_0\,\frac{\sin\chi}{\chi},
\quad \chi=\frac{ed_{\rm eff}B_0Y}{\hbar}
=\frac{\pi\Phi}{\Phi_0},}\tag{5.4}
$$
其中 $\Phi=B_0d_{\rm eff}Y$ 是穿过有效磁截面的磁通。

（3）电流零点与零磁场极限。

题设 $\delta_0\ne k\pi$，所以 $\sin\delta_0\ne0$。非零磁场零点来自 $\sin\chi=0$：
$$
\chi=n\pi,\qquad n=\pm1,\pm2,\ldots.
$$
因此
$$
\boxed{B_{0,n}=\frac{n\pi\hbar}{ed_{\rm eff}Y}
=\frac{n\Phi_0}{d_{\rm eff}Y},\qquad n\ne0.}\tag{5.5}
$$
不能把 $n=0$ 也作为零点。因为
$\lim_{\chi\to0}\sin\chi/\chi=1$，零磁场时
$I_J=I_0\sin\delta_0\ne0$。

若允许调节中心相位，对 $\delta_0$ 最大化电流的绝对值，得到临界包络
$$
I_{\max}(B_0)=I_0\left|\frac{\sin\chi}{\chi}\right|.
$$
固定 $\delta_0$ 的有符号电流与包络的绝对值是两种不同量，不能在式（5.4）中随意删除符号。

![图5-3　允许调节中心相位时的最大电流包络，整数非零磁通处相互抵消。](../figures/q5-fringe.png)

（4）考虑自生磁场，得到空间非线性方程。

在当前坐标约定下，安培定律的 $x$ 分量为
$$
(\nabla\times\mathbf B)_x=\frac{dB_z}{dy}
=\mu_0j_x=\mu_0j_0\sin\delta.
$$
将空间相位关系再对 $y$ 求导：
$$
\delta''=\frac{2ed_{\rm eff}}{\hbar}B_z'
=\frac{2e\mu_0j_0d_{\rm eff}}{\hbar}\sin\delta.
$$
与要求的形式对照：
$$
\boxed{\lambda_J=
\sqrt{\frac{\hbar}{2e\mu_0j_0d_{\rm eff}}}.}\tag{5.6}
$$
有效磁厚度必须使用 $d+2\lambda$；电流密度的面积为 $YZ$，两者来自不同几何方向。

对 $\delta=2n\pi+\xi$ 的小空间偏离，$\sin\delta\simeq\xi$，方程
$\xi''=\xi/\lambda_J^2$ 的解为指数型。它描述静态空间相位的穿透尺度，并不是时间谐振动方程，因此此处的正号不表示动态不稳定。

（5）空间方程的首次积分与局域磁通解。

将 $\delta''=\sin\delta/\lambda_J^2$ 乘 $\delta'$，积分：
$$
\frac12(\delta')^2=-\frac{\cos\delta}{\lambda_J^2}+C_{\rm s}.
$$
若在一侧相位趋于0且梯度趋于0，$C_{\rm s}=1/\lambda_J^2$，从而
$$
(\delta')^2=\frac{2}{\lambda_J^2}(1-\cos\delta)
=\frac4{\lambda_J^2}\sin^2\frac\delta2.
$$
对于从0单调增加至 $2\pi$ 的解，选正分支：
$$
\delta'=\frac2{\lambda_J}\sin\frac\delta2.
$$
分离变量，利用
$\int d\delta/[2\sin(\delta/2)]=\ln\tan(\delta/4)$，
得到
$$
\delta(y)=4\arctan e^{(y-y_0)/\lambda_J}.
$$
对应磁场
$$
B_z=\frac{\hbar}{2ed_{\rm eff}}\delta'
=\frac{\hbar}{ed_{\rm eff}\lambda_J}
\operatorname{sech}\frac{y-y_0}{\lambda_J}.
$$
积分有效截面的磁通：
$$
d_{\rm eff}\int_{-\infty}^{\infty}B_z\,dy
=\frac{\hbar}{2e}[\delta(+\infty)-\delta(-\infty)]
=\Phi_0.
$$
这是原空间方程的一个补充边界值解，帮助理解 $\lambda_J$ 与磁通尺度。有限宽结的实际边界条件还需由外磁场决定，不能将这个无限区间解强加到所有有限结。

（6）三个并联支路电流与相位方程。

三个支路共同电压为
$$
U=\frac{\hbar}{2e}\dot\delta.
$$
理想约瑟夫森支路：
$$
I_J=I_0\sin\delta.
$$
电阻支路：
$$
I_R=\frac UR=\frac{\hbar}{2eR}\dot\delta.
$$
电容支路：
$$
I_C=C\dot U=\frac{\hbar C}{2e}\ddot\delta.
$$
外加恒定电流等于三者之和：
$$
\boxed{
\frac{\hbar C}{2e}\ddot\delta
+\frac{\hbar}{2eR}\dot\delta
+I_0\sin\delta=I.}\tag{5.7}
$$
有限 $R$ 产生类似黏性阻尼的一阶导数项，电容产生二阶导数的惯性项。忽略电阻电流意味着取近似 $1/(RC)\to0$，不是将整个电阻支路的相位关系改成另一种电压。

（7）单位质量类比的势。

在题设大 $R$ 条件下，将式（5.7）除以 $\hbar C/(2e)$：
$$
\ddot\delta+\frac{2eI_0}{\hbar C}\sin\delta
-\frac{2eI}{\hbar C}=0.
$$
要写成 $\ddot\delta=-V'(\delta)$，取
$$
\boxed{V(\delta)=
-\frac{2e}{\hbar C}(I\delta+I_0\cos\delta)+\text{常数}.}\tag{5.8}
$$
乘以 $\dot\delta$ 可积分为
$$
\frac12\dot\delta^2+V(\delta)=E_{\rm unit}.
$$
这里采用单位“质量”类比，$V$ 的量纲是 $\mathrm{s^{-2}}$。它不是直接以焦耳计的物理电路能量。

若希望使用真正能量，定义
$$
M_\delta=C\left(\frac{\hbar}{2e}\right)^2,\qquad
E_J=\frac{\hbar I_0}{2e}.
$$
则电容储能为 $M_\delta\dot\delta^2/2$，物理势为
$$
U_\delta=-E_J\cos\delta-\frac{\hbar I}{2e}\delta.
$$
且 $U_\delta=M_\delta V$。两种写法求出的频率一致；混用它们会错掉相位惯性系数。

![图5-4　非零偏置使余弦势倾斜，局部势阱存在于临界电流以下。](../figures/q5-potential.png)

（8）求平衡相位与稳定性。

令 $i=I/I_0$，平衡条件
$$
V'(\delta)=\frac{2eI_0}{\hbar C}(\sin\delta-i)=0
$$
给 $\sin\delta=i$。当 $|i|<1$ 时有两类：
$$
\delta_{\rm s}=\arcsin i+2n\pi,
\qquad
\delta_{\rm u}=\pi-\arcsin i+2n\pi.
$$
二阶导数为
$$
V''(\delta)=\frac{2eI_0}{\hbar C}\cos\delta.
$$
第一类 $\cos\delta_{\rm s}=+\sqrt{1-i^2}>0$ 为阱底；第二类二阶导数为负，是势垒顶。因此
$$
\boxed{|I|<I_0,\qquad
\delta_{\rm bottom}=\arcsin(I/I_0)+2n\pi.}\tag{5.9}
$$
$|I|=I_0$ 时两个分支合并、曲率为零，只是退化静止点，没有有限深的势阱。$|I|>I_0$ 时无静止点。

（9）阱底小振动频率及临界趋势。

令 $\delta=\delta_{\rm s}+\xi$，$|\xi|\ll1$。展开
$$
\sin(\delta_{\rm s}+\xi)
=\sin\delta_{\rm s}+\cos\delta_{\rm s}\,\xi+O(\xi^2).
$$
偏置常项抵消，方程成为
$$
\ddot\xi+\frac{2eI_0}{\hbar C}\cos\delta_{\rm s}\,\xi=0.
$$
所以
$$
\boxed{\omega=
\sqrt{\frac{2eI_0}{\hbar C}}\,(1-i^2)^{1/4}.}\tag{5.10}
$$
最大值在 $I=0$：
$$
\boxed{\omega_J=\sqrt{\frac{2eI_0}{\hbar C}}.}\tag{5.11}
$$
频率对偏置是四次方根，不是平方根。因为相位曲率已经含一个 $\sqrt{1-i^2}$，从曲率再取平方根又开一次根号。

若 $i=1-\zeta$、$\zeta\ll1$，
$$
\omega\simeq\omega_J(2\zeta)^{1/4}.
$$
接近临界时小振动明显变慢，同时允许的小振幅也变小；不能在频率趋零时仍使用任意固定幅度的线性振荡。

（10）势垒高度及小振动适用幅度。

考虑 $0\le i<1$，向下倾斜方向的相邻势垒顶为
$\delta_{\rm u}=\pi-\arcsin i$。势阱底与顶的距离是
$2\arccos i$。物理势差
$$
\Delta U_\delta
=U_\delta(\delta_{\rm u})-U_\delta(\delta_{\rm s}).
$$
使用 $\cos\delta_{\rm s}=\sqrt{1-i^2}$、
$\cos\delta_{\rm u}=-\sqrt{1-i^2}$，得到
$$
\boxed{\Delta U_\delta=
2E_J\left[\sqrt{1-i^2}-i\arccos i\right].}\tag{5.12}
$$
$i=0$ 时势垒为 $2E_J$，$i\to1^-$ 时趋零。接近临界
$\Delta U_\delta\simeq(4\sqrt2/3)E_J(1-i)^{3/2}$。
这说明频率虽只按四次方根变小，势阱深度却更快消失。小振动的相位幅度应远小于相邻顶、底间距，而不只是笼统写 $|\xi|\ll1$。

（11）求结中波速并检查面积消去。

理想平行板电容
$$
C=\frac{\epsilon_r\epsilon_0YZ}{d},\qquad I_0=j_0YZ.
$$
所以
$$
\omega_J^2=\frac{2ej_0d}{\hbar\epsilon_r\epsilon_0}.
$$
与式（5.6）的 $\lambda_J^2$ 相乘：
$$
\tilde c^2=\omega_J^2\lambda_J^2
=\frac{d}{\mu_0\epsilon_0\epsilon_r(d+2\lambda)}.
$$
由于 $c^2=1/(\mu_0\epsilon_0)$，
$$
\boxed{\frac{\tilde c}{c}
=\sqrt{\frac{d}{\epsilon_r(d+2\lambda)}}.}\tag{5.13}
$$
代入纳米长度即可，因为只出现长度比：
$$
\frac{\tilde c}{c}
=\sqrt{\frac{3.0}{9.0(3.0+106)}}\approx0.0553.
$$
两位有效数字为
$$
\boxed{\tilde c/c=0.055.}
$$
$j_0,Y,Z$ 全部消去：它们分别影响时间和空间响应尺度，但在乘积中抵消。若忽略超导体内的磁穿透厚度，会误得到 $1/\sqrt{\epsilon_r}$，明显高估波速。

## 六、关键洞察

同一相位的时间梯度对应电压，空间梯度对应磁场。均匀磁场下的总电流不是每处电流的简单同号相加，而是相位在整个结宽度上积分的结果。

电流偏置下相位“势能”有归一化类比和物理能量两种口径。把相位惯性系数写明，就能统一两种表达式，也能避免频率中少一个平方根。

## 七、易错点

- 直流电压误判为直流约瑟夫森电流。
- 时间周期漏绝对值，或把零电压代入后称有限周期。
- 磁通面积用 $YZ$，而不是 $Y(d+2\lambda)$。
- 将零磁场也算作电流零点。
- 把固定中心相位的电流和临界包络混同。
- 电容电流错写成一阶导数。
- 将 $|I|=I_0$ 的退化点当作仍有势阱。
- 频率中的 $(1-i^2)^{1/4}$ 写成 $(1-i^2)^{1/2}$。
- 将单位质量类比势直接标为焦耳。

## 八、课堂讲解建议

先比较“电压导致时间相位梯度”和“磁场导致空间相位梯度”两条关系。空间积分可先将正弦拆成奇、偶项，便于看出中心相位如何留下。画出有符号总电流与绝对值包络的区别。

电路部分逐支路写电流后再合并。势图先看零偏置，再加入线性倾斜；用阱底曲率解释频率，用顶、底合并解释临界电流。数值部分先在符号层面消去 $j_0$ 与面积，再代入长度比。

## 九、变式训练

### 变式1　小磁通下的总电流修正

固定 $\delta_0$，$|\Phi|\ll\Phi_0$。求总电流的最低阶磁场修正。

**解答。** 令 $\chi=\pi\Phi/\Phi_0$，
$\sin\chi/\chi=1-\chi^2/6+O(\chi^4)$，故
$$
\boxed{I_J=I_0\sin\delta_0
\left[1-\frac{\pi^2}{6}\left(\frac{\Phi}{\Phi_0}\right)^2+\cdots\right].}
$$
一阶磁场项因结宽度关于中心对称而消失。若结电流密度不均匀且不对称，则这一结论需重新由积分判断。

### 变式2　给定频率比例反求偏置电流

测得小振动频率 $\omega=\omega_J/2$，求偏置电流大小。

**解答。** 原式为
$\omega/\omega_J=(1-i^2)^{1/4}$，四次方后
$1-i^2=1/16$，所以
$$
\boxed{|I|=\frac{\sqrt{15}}4I_0\approx0.968I_0.}
$$
这是接近临界的状态。势垒变小，实际振幅必须足够小才能用线性频率；由频率大小无法判断偏置的正负。

### 变式3　保留有限电阻的小振动

在 $|i|<1$ 的阱底附近保留电阻支路，求振动的衰减形式。

**解答。** 将式（5.7）线性化并除以 $\hbar C/(2e)$：
$$
\ddot\xi+\frac1{RC}\dot\xi+\omega^2\xi=0.
$$
设 $\Gamma=1/(2RC)$。欠阻尼 $\Gamma<\omega$ 时
$$
\xi=e^{-\Gamma t}
(A\cos\omega_dt+B\sin\omega_dt),\qquad
\omega_d=\sqrt{\omega^2-\Gamma^2}.
$$
临界阻尼为 $\Gamma=\omega$；更大阻尼时为两个非振荡指数解。电阻不仅改变幅度，也改变实际振荡频率。

### 变式4　有效磁厚度加倍但电容不变

把磁穿透厚度改变，使 $d_{\rm eff}$ 加倍，保持 $d,\epsilon_r,j_0,Y,Z$ 不变。求 $\lambda_J,\omega_J,\tilde c$ 和首个磁场零点的变化。

**解答。** $\lambda_J\propto d_{\rm eff}^{-1/2}$，故降为原来的 $1/\sqrt2$。$\omega_J$ 只依赖 $j_0d/(\epsilon_r\epsilon_0)$，保持不变。因此 $\tilde c$ 也降为 $1/\sqrt2$。

零点 $|B_{0,1}|=\Phi_0/(d_{\rm eff}Y)$ 降为原来的一半。这两种不同的比例说明空间穿透尺度与磁通周期虽都受有效厚度影响，依赖幂次并不相同。

