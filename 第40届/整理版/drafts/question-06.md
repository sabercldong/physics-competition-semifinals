# 第 6 题　涡电流的悬浮与热效应（40分）

交变磁场在导体内部产生涡电流，可用于加热、制动和悬浮。半径为 $b$ 的水平圆线圈固定于桌面，电流为 $I(t)=I_0\cos\omega t$。重力大小为 $G$、半径为 $a$、电导率为 $\sigma$ 的导体球位于线圈中心正上方，高度为 $h$。已知 $a\ll b$，趋肤深度

$$\delta=\sqrt{\frac2{\omega\mu_0\sigma}}\ll a,$$

其中 $\mu_0$ 为真空磁导率，忽略电磁辐射。

![水平圆线圈与轴线上导体球](../figures/q6-levitation.png)

（1）将原来内部无磁场、半径为 $a$ 的理想导体球（$\sigma\to\infty$）放在均匀稳恒外场 $\boldsymbol B_e=B_e\hat{\boldsymbol z}$ 中。已知球外附加场等效于球心磁偶极矩 $\boldsymbol m$ 的场

$$\boldsymbol B'=\frac{\mu_0}{4\pi r^3}
[3(\boldsymbol m\cdot\hat{\boldsymbol r})\hat{\boldsymbol r}-\boldsymbol m].$$

求 $\boldsymbol m$ 和球面电流密度分布。

（2）求圆线圈在球心处的磁感应强度 $\boldsymbol B(t)$。

（3）求悬浮在给定高度 $h$ 所需的电流幅值 $I_0$。假设频率足够高，球在悬浮位置附近的振动幅度可忽略。提示：磁偶极矩与外场均沿 $z$ 轴时，安培力为 $\boldsymbol F=m(dB_e/dz)\hat{\boldsymbol z}$。

（4）把趋肤层内沿径向的涡电流近似为均匀分布，其余球内电流为零。求一个周期的平均热功率，最终式不含 $\delta$。

## 一、题型定位

磁场边界条件、感应磁矩、空间非均匀磁场中的力和趋肤层焦耳热。理想导体部分提供有限电导率、高频极限下的领先阶面电流；再用趋肤层厚度把面电流转为体电流，估算耗散。

求磁矩用磁场法向连续；求电流用切向磁场跃变。两种边界关系分别回答不同问题，不能相互代替。

## 二、知识点

磁场满足无磁单极子的高斯定理；球面面电流 $\boldsymbol K$ 满足 $\mu_0\boldsymbol K=\hat{\boldsymbol r}\times(\boldsymbol B_{\rm out}-\boldsymbol B_{\rm in})$。圆线圈轴上场由毕奥—萨伐尔定律求出。导体热功率密度为 $J^2/\sigma$，交变正弦的平方在一个周期内平均为 $1/2$。

题中球内磁场始终为零依赖“初始无磁场”的条件。理想导体保持初始磁通的行为，不应省略初始条件后推广成任意静磁场都自动被排斥。

## 三、物理图像

感应环流的磁矩反向于外场，使球内磁场抵消。在线圈上方，外场幅值随高度降低，反向磁矩受到向上的力。每半个周期外场与感应磁矩同时反号，力仍向上，因此平均力可平衡重力。

电流集中于厚度 $\delta$ 的薄层。面电流一定时，层越薄，体电流密度越大；焦耳热并不只由球体体积决定。

## 四、解题入口

令球外总場为外场加偶极子场，先在 $r=a$ 令法向分量为零，求磁矩。再代回切向场求 $\boldsymbol K$。线圈轴上场写成 $B_0(z)\cos\omega t$，对 $z$ 求导，再平均磁力。热量从体积分出发，先做球面角积分，最后消去趋肤深度。

## 五、解析

### 1　球面的法向磁场条件

由对称性，感应磁矩沿 $z$ 轴，设其有向分量为 $m$。球外总場的径向分量为

$$B_r=B_e\cos\theta+\frac{\mu_0}{4\pi r^3},2m\cos\theta.$$

球内磁场为零，法向分量连续，所以 $r=a$ 处

$$B_e\cos\theta+\frac{\mu_0m}{2\pi a^3}\cos\theta=0.$$

这个关系须对所有 $\theta$ 成立，故

$$\boxed{\boldsymbol m=-\frac{2\pi a^3}{\mu_0}\boldsymbol B_e.}$$

负号表示反向感应；磁矩正比于球体积尺度 $a^3$。只在赤道取法向条件会得到恒等式0=0，不能据此求磁矩。

### 2　切向磁场与面电流方向

外场的球坐标角向分量为 $-B_e\sin\theta$。偶极子場的角向分量为 $\mu_0m\sin\theta/(4\pi a^3)$，代入磁矩得

$$B_{\theta,\rm out}=-B_e\sin\theta-\frac12B_e\sin\theta
=-\frac32B_e\sin\theta.$$

球内切向场仍为零。由面电流边界条件和 $\hat{\boldsymbol r}\times\hat{\boldsymbol\theta}=\hat{\boldsymbol\phi}$，

$$\boxed{\boldsymbol K(\theta)
=-\frac{3B_e}{2\mu_0}\sin\theta\,\hat{\boldsymbol\phi}.}$$

电流在两极为零、赤道最大。外场沿正 $z$ 时电流沿负方位方向，按右手定则产生负 $z$ 磁矩，符合反向感应的物理图像。

![球面电流与赤道处的最大电流密度](../figures/q6-current.png)

### 3　积分复核磁矩

面电流分布的磁矩可由

$$\boldsymbol m=\frac12\int\boldsymbol r\times\boldsymbol K\,dS$$

求得。设 $K_\phi=K_0\sin\theta$，$dS=a^2\sin\theta\,d\theta\,d\phi$。$z$ 分量为

$$m_z=\frac12a^3K_0\int_0^{2\pi}d\phi
\int_0^\pi\sin^3\theta\,d\theta.$$

利用 $\int_0^\pi\sin^3\theta\,d\theta=4/3$，

$$m_z=\frac{4\pi a^3}{3}K_0
=-\frac{2\pi a^3}{\mu_0}B_e.$$

因此面电流边界条件所得分布与法向条件所得磁矩一致。这项积分同时检查了 $3/2$ 系数与电流方向。

### 4　圆线圈轴上场的积分

轴上点高度为 $z$，到任意线元距离为 $\sqrt{b^2+z^2}$。各线元的水平场分量相互抵消，竖直分量相加。毕奥—萨伐尔定律给出

$$B_z=\frac{\mu_0I}{4\pi}
\frac b{(b^2+z^2)^{3/2}}\int_0^{2\pi}b\,d\phi,$$

所以

$$\boxed{\boldsymbol B(z,t)=
\frac{\mu_0I_0b^2}{2(b^2+z^2)^{3/2}}
\cos\omega t\,\hat{\boldsymbol z}.}$$

球心处 $z=h$，定义幅值

$$B_0=\frac{\mu_0I_0b^2}{2(b^2+h^2)^{3/2}}.$$

当 $z=0$，它回到线圈中心场 $\mu_0I/(2b)$；远轴上 $z\gg b$ 时衰减为 $z^{-3}$，与磁偶极子场一致。

### 5　感应磁矩的瞬时力

由于 $a\ll b$，球附近的外场近似均匀；又因 $\delta\ll a$，感应磁矩取理想导体的领先阶：

$$m(z,t)\simeq-\frac{2\pi a^3}{\mu_0}B(z,t).$$

按题目给出的力公式，先对外场作空间导数：

$$F_z=m\frac{\partial B}{\partial z}
=-\frac{2\pi a^3}{\mu_0}B\frac{\partial B}{\partial z}
=-\frac{\pi a^3}{\mu_0}\frac{\partial B^2}{\partial z}.$$

这里空间导数作用于外场，并非把 $mB$ 当固定磁矩势能随意求导。因磁矩由场感应，直接求 $-mB$ 的全导数会多一个因子2。

对线圈场平方求导：

$$\frac{\partial B^2}{\partial z}
=-\frac{3\mu_0^2I_0^2b^4z}{2(b^2+z^2)^4}
\cos^2\omega t.$$

所以

$$\boxed{F_z(z,t)=
\frac{3\pi\mu_0a^3b^4zI_0^2}{2(b^2+z^2)^4}
\cos^2\omega t.}$$

对 $z>0$，力始终向上。反转线圈电流不会反转该力，因为感应磁矩同时反转。

### 6　平均力与悬浮电流

在球的位移一个电流周期内可忽略时，固定 $z=h$ 再取时间平均，得

$$\boxed{\langle F_z\rangle=
\frac{3\pi\mu_0a^3b^4hI_0^2}{4(b^2+h^2)^4}.}$$

令平均力等于重力 $G$，

$$\boxed{I_0=\sqrt{
\frac{4G(b^2+h^2)^4}{3\pi\mu_0a^3b^4h}}.}$$

该式求的是峰值电流，若问有效值，则应除以 $\sqrt2$。用有效值平均后再乘 $1/2$，会重复平均而少一个因子2。

### 7　趋肤层体电流与焦耳热微元

把面电流 $\boldsymbol K$ 均匀分摊到厚度 $\delta$ 中，题设近似给出

$$\boldsymbol J=\frac{\boldsymbol K}{\delta}
=-\frac{3B(t)}{2\mu_0\delta}\sin\theta\,
\hat{\boldsymbol\phi}.$$

体功率密度为

$$p_J=\frac{J^2}{\sigma}
=\frac{9B(t)^2}{4\mu_0^2\sigma\delta^2}\sin^2\theta.$$

球壳体积微元为 $r^2\sin\theta\,dr\,d\theta\,d\phi$，电流只在 $a-\delta<r<a$ 中存在，故

$$P(t)=\frac{9B(t)^2}{4\mu_0^2\sigma\delta^2}
\int_{a-\delta}^a r^2dr
\int_0^\pi\sin^3\theta d\theta
\int_0^{2\pi}d\phi.$$

径向积分为

$$\frac{a^3-(a-\delta)^3}{3}
=a^2\delta-a\delta^2+\frac{\delta^3}{3}
\simeq a^2\delta.$$

保留薄层领先阶，并用角积分 $4/3$，得到

$$\boxed{P(t)\simeq
\frac{6\pi a^2}{\mu_0^2\sigma\delta}B(t)^2.}$$

若在题设均匀电流模型中保留有限厚度修正，还要乘 $1-\delta/a+\delta^2/(3a^2)$；本题只要求 $\delta\ll a$ 的近似。

### 8　平均功率并消去趋肤深度

$B(t)=B_0\cos\omega t$，因此

$$\langle P\rangle=
\frac{3\pi a^2B_0^2}{\mu_0^2\sigma\delta}
=\frac{3\pi a^2b^4I_0^2}
{4(b^2+h^2)^3\sigma\delta}.$$

利用

$$\frac1{\sigma\delta}=\sqrt{\frac{\omega\mu_0}{2\sigma}},$$

最终为

$$\boxed{\langle P\rangle\simeq
\frac{3\pi a^2b^4I_0^2}{8(b^2+h^2)^3}
\sqrt{\frac{2\omega\mu_0}{\sigma}}.}$$

功率始终非负。在场幅值一定时，电导率增大使热损失下降；频率增大使趋肤层变薄，功率按 $\sqrt\omega$ 增长。该比例限于题设高电导、薄趋肤层且忽略辐射的模型。

### 9　悬浮条件下的热功率

把平均力平衡求出的 $I_0^2$ 代入功率，可消去线圈电流：

$$\boxed{\langle P\rangle_{\rm lev}
=\frac{G(b^2+h^2)}{a h}
\sqrt{\frac{\omega}{2\mu_0\sigma}}.}$$

也可利用 $1/(\mu_0\sigma\delta)=\omega\delta/2$ 写为

$$\langle P\rangle_{\rm lev}
=\frac{G(b^2+h^2)}{2ah}\omega\delta.$$

这个式子显示，在给定几何和重力下，悬浮的平均力可在理想极限保持有限，而热损失随着 $\sigma\to\infty$ 趋于零。没有必要用耗散产生热来解释平均磁力的存在，两者的物理来源不同。

### 10　平均平衡与竖直稳定性的区别

平均力随高度为 $F_{\rm av}(z)=Cz/(b^2+z^2)^4$，其中 $C>0$。其导数为

$$F'_{\rm av}(z)=C\frac{b^2-7z^2}{(b^2+z^2)^5}.$$

在固定电流下，向上偏移后平均支持力减小才具有竖直恢复性，所以稳定侧要求 $h>b/\sqrt7$。对球质量 $M_s=G/g$，竖直慢振动频率满足

$$\Omega_z^2=-\frac{F'_{\rm av}(h)}{M_s}
=\frac{g(7h^2-b^2)}{h(b^2+h^2)}.$$

这只是竖直稳定性分析，未判断横向稳定性。原题第三问只要求给定位置的平均力平衡；补充此条件能避免把任意代数平衡点都当成稳定悬浮。

### 11　高频近似的位移尺度

平衡高度处 $F_z(t)=G[1+\cos2\omega t]$。减去重力后，快速加速度近似为 $g\cos2\omega t$，其受迫位移幅值为

$$\Delta z_{\rm fast}\simeq\frac g{4\omega^2}.$$

因此需同时满足位移远小于场幅值变化尺度，并使 $\omega$ 远大于慢振动频率；另外仍须满足 $\delta\ll a$。单纯说“频率高”不能替代这两类不同的尺度检查。

## 六、关键洞察

球面磁场边界条件决定感应磁矩和面电流；空间梯度决定平均力；有限电导率和趋肤层决定热损失。使用同一磁矩近似连接三者，但每一步都有独立的物理条件。

## 七、易错点

忽略理想导体球初始无磁场的条件；球面场只写外场、漏附加场；用体电流代替面电流；忘记时间平均的 $1/2$；把感应磁矩当常量求势能导数；热量积分漏 $\sin\theta$ 体积因子；把 $G$ 当质量；把平均平衡直接等同于完整稳定性。

## 八、课堂讲解建议

把四问分成“边界条件—外场—力—热量”四行，每行注明已知条件和待求量。先用电流方向和远场极限检查磁矩，再独立积分磁矩。热量推导保留三重积分至最后，避免把结果简写成“球壳体积乘最大功率密度”。

## 九、变式训练

### 变式1　电流频率增至四倍

几何、电导率和电流幅值不变，频率增至原来的4倍，仍满足题设近似。求趋肤深度、平均力和平均热功率的变化。

解：$\delta\propto\omega^{-1/2}$，因此深度减半。领先阶理想导体磁矩和平均力不含频率，平均力不变。功率正比 $\sqrt\omega$，所以加倍。快速振动位移幅值正比 $\omega^{-2}$，减少到原来的 $1/16$。

### 变式2　寻找电流需求最小的高度

线圈半径 $b$ 固定，球和重力固定。求平均力平衡所需 $I_0$ 最小的高度，并判断竖直稳定性。

解：$I_0^2$ 正比 $(b^2+h^2)^4/h$。对数求导：

$$\frac{d}{dh}\ln I_0^2=
\frac{8h}{b^2+h^2}-\frac1h.$$

令其为零，得 $7h^2=b^2$，即 $h=b/\sqrt7$。这个高度也是平均力对高度的最大点，线性竖直恢复系数为零。实际选择需在稳定的高侧留出余量；最小电流的数学点不能自动提供线性稳定悬浮。


还可比较固定电流略高于最小值时的两个平衡高度。平均支持力从地面附近的零值先增大，达到 $z=b/\sqrt7$ 的最大值后下降。因此最大支持力大于 $G$ 时，一般有低、高两个正平衡根。低根处 $F'_{\rm av}>0$，向上偏移会获得更大的上推力，竖直不稳定；高根处 $F'_{\rm av}<0$，具有竖直恢复性。

代入高根 $h$，慢振动频率为

$$\Omega_z=\sqrt{\frac{g(7h^2-b^2)}{h(b^2+h^2)}}.$$

当 $h\to b/\sqrt7$，这个频率趋于零，因而接近最小电流点时恢复作用很弱。上述判断针对平均动力学，另需高频微振动幅值 $g/(4\omega^2)$ 足够小，才可把快速运动和慢速恢复运动分开。


### 变式3　给定高度选择线圈半径

$h$ 固定，求使所需电流幅值最小的 $b$，并写出此时功率。

解：$I_0^2\propto(b^2+h^2)^4/b^4$。求对数导数 $8b/(b^2+h^2)-4/b=0$，得到 $b=h$。此时平均平衡下

$$\langle P\rangle=\frac{2Gh}{a}
\sqrt{\frac{\omega}{2\mu_0\sigma}}.$$

由于 $h>b/\sqrt7$，这个几何选择位于竖直稳定侧，但依然没有分析横向稳定与工程损耗。

### 变式4　有限球壳厚度的积分修正

仍按题设把体电流沿径向均匀分布，但不把壳体体积近似为面积乘厚度。求功率相对薄壳领先阶的修正因子。

解：径向精确积分为 $a^2\delta-a\delta^2+\delta^3/3$，其他角积分不变。因此

$$\frac{P_{\rm shell}}{P_{\rm leading}}
=1-\frac\delta a+\frac{\delta^2}{3a^2}.$$

当 $\delta/a=0.05$ 时因子约0.951，领先阶高估约5%。此结果只修正壳体几何体积，未修正真实电流沿径向的指数衰减和感应磁矩的相位偏差，不能把它称为完整有限电导率解。
