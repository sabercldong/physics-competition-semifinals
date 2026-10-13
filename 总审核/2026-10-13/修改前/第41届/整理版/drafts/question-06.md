# 第 6 题　引力散射与星光偏折（45分）

广义相对论预言星光经过太阳附近会发生偏折，1919年的日全食观测曾检验这一效应。本题先在牛顿理论下计算，再用弱场有效折射率模型计算。

（1）在牛顿动力学和万有引力框架下，质量为 $m$ 的质点在原点处质量 $M\gg m$ 的引力场中运动。平面极坐标轨道为

$$r(\theta)=\frac p{1+e\cos\theta},\qquad-\pi<\theta\le\pi,$$

其中半通径 $p>0$、偏心率 $e\ge0$。若 $e>1$，存在 $\theta_{\max}$ 使 $-\theta_{\max}<\theta<\theta_{\max}$。求 $\theta_{\max}$ 及其取值范围。

（2）由质点的机械能 $E$ 和相对于原点的轨道角动量大小 $L$，导出 $p(E,L)$、$e(E,L)$。

（3）一个物体以速度 $v_0$ 从外太空飞入太阳系，瞄准距离为 $b$，即初始速度所在直线到太阳中心的距离。设 $v_0^2b/(GM_\odot)\gg1$。求飞出方向相对原入射方向的偏折角 $\Delta\varphi$：

（i）入射物是陨石；

（ii）入射物是一束星光，恰好掠过太阳表面进入观测站，此时可近似取 $b=R_\odot$。

![远处入射方向、瞄准距离和出射偏折角](../figures/q6-scatter.png)

（4）弱场广义相对论效应可用等效相对折射率

$$n_{\rm eff}(r)=1-\frac{2\varphi(r)}{c^2}$$

表示，其中 $\varphi(r)$ 是牛顿引力势。光线满足费马原理 $\delta\int_A^B n_{\rm eff}(r)dl=0$。若 $n_{\rm eff}$ 与 $\theta$ 无关，以 $\theta=\theta(r)$ 写轨迹，有

$$\frac d{dr}\left(
\frac{r^2\theta'}{\sqrt{1+r^2\theta'^2}}n_{\rm eff}(r)
\right)=0,\qquad\theta'=\frac{d\theta}{dr}.$$

用这一关系重新计算掠过太阳表面的星光偏折角。已知太阳质量 $M_\odot$、太阳半径 $R_\odot$、引力常量 $G$ 和光速 $c$。

## 一、题型定位

中心力圆锥轨道、双曲散射的角度几何与分层近似。先由守恒量决定轨道，再由渐近方向得到散射角；光学部分由旋转对称产生的第一积分得到另一条轨道。

牛顿框架把光束形式上按高速粒子计算，只给出完整弱场光偏折的一半。题中有效折射率包含弱场广义相对论效应，最终恢复系数四。

## 二、知识点

中心引力势能 $-GMm/r$；能量和角动量守恒；有效势能；半通径与偏心率；无穷远条件；渐近径向位置与实际运动速度方向的区别；弱散射展开；费马原理；循环坐标与守恒光学角动量；倒数半径变量。

在双曲轨道中，$E>0$、$e>1$。瞄准距离 $b$ 是无穷远处入射直线的几何量，最近距离一般比 $b$ 小；弱场极限下二者才可在领头阶近似等同。

## 三、物理图像

吸引引力使入射轨迹弯向太阳。在无穷远，入射速度方向与指向入射位置的径向方向相反，出射速度方向与出射径向方向相同，所以散射角不是简单的 $2\theta_{\max}$，而是 $2\theta_{\max}-\pi$。

有效折射率靠近太阳时增大，光线向折射率更大的区域弯曲。旋转对称性使 $nr\sin\alpha$ 保持不变，远处此常数就是瞄准距离。

![圆锥轨道的两支渐近方向与最近点](../figures/q6-orbit.png)

## 四、解题入口

从 $r>0$ 推出 $1+e\cos\theta>0$。用 $L=mr^2\dot\theta$ 消去 $\dot\theta$，再把 $u=1/r=(1+e\cos\theta)/p$ 代入能量，比较常数项和 $u$ 项。

对光线，把给定微分式积分一次，确定常数为 $b$。倒数半径将含根式的一阶关系化为多项式形式，便于同圆锥轨道或线性轨道微分方程比较。

## 五、解析

### 1　双曲线允许的角度范围

因 $p>0$ 且物理半径 $r>0$，分母必须为正：

$$1+e\cos\theta>0.$$

当 $e>1$，这给出

$$\cos\theta>-\frac1e,$$

$$\boxed{\theta_{\max}=\arccos\left(-\frac1e\right).}$$

因为 $-1<-1/e<0$，有

$$\boxed{\frac\pi2<\theta_{\max}<\pi.}$$

当 $\theta\to\pm\theta_{\max}$，分母趋零、$r\to\infty$，两端就是双曲轨道的渐近方向。边界角不包含在有限位置的轨道中。

$e\to1^+$ 时 $\theta_{\max}\to\pi$，双曲轨道趋近抛物线；$e\to\infty$ 时 $\theta_{\max}\to\pi/2$，散射越来越弱。

### 2　机械能与角动量

记中心引力参数 $\Gamma=GM$。质点机械能为

$$E=\frac m2(\dot r^2+r^2\dot\theta^2)-\frac{\Gamma m}{r},$$

角动量大小为

$$L=mr^2\dot\theta,$$

这里按 $\dot\theta>0$ 选轨道方向；若原方向相反，可用角动量大小并交换角度正向。消去角速度，得

$$\boxed{E=\frac m2\dot r^2
+\frac{L^2}{2mr^2}-\frac{\Gamma m}{r}.}$$

后两项组成径向有效势能

$$U_{\rm eff}(r)=\frac{L^2}{2mr^2}-\frac{\Gamma m}{r}.$$

第一项为角动量屏障，第二项为吸引势能。对 $L>0$，很小的半径处角动量屏障会占优势；纯径向 $L=0$ 为退化情形，不能直接使用非零半通径的表达式。

### 3　由给定轨道比较守恒量

令 $u=1/r$。因

$$\dot r=\frac{dr}{d\theta}\dot\theta
=-\frac1{u^2}\frac{du}{d\theta}\frac Lm u^2
=-\frac Lm u',$$

能量化为

$$E=\frac{L^2}{2m}(u'^2+u^2)-\Gamma m u.$$

题给轨道和导数为

$$u=\frac{1+e\cos\theta}{p},
\qquad u'=-\frac e p\sin\theta.$$

于是

$$u'^2+u^2
=\frac{1+e^2+2e\cos\theta}{p^2}
=\frac{e^2-1}{p^2}+\frac{2u}{p}.$$

代入能量，

$$E=\frac{L^2(e^2-1)}{2mp^2}
+\left(\frac{L^2}{mp}-\Gamma m\right)u.$$

能量与沿轨道改变的 $u$ 无关，所以一次项系数必须为零：

$$\frac{L^2}{mp}=\Gamma m,$$

$$\boxed{p=\frac{L^2}{GMm^2}.}$$

常数项则给

$$E=\frac{G^2M^2m^3}{2L^2}(e^2-1),$$

$$\boxed{e=\sqrt{1+\frac{2EL^2}{G^2M^2m^3}}.}$$

该路线没有除以 $dr/d\theta$，因此在最近点 $\theta=0$、$dr/d\theta=0$ 处也无中间奇点。

### 4　用轨道方程作第二次检查

牛顿径向方程为

$$\ddot r-r\dot\theta^2=-\frac\Gamma{r^2}.$$

结合角动量守恒并换成 $u$，可导出Binet方程

$$u''+u=\frac{\Gamma m^2}{L^2}.$$

给定圆锥轨道满足 $u''+u=1/p$，与上节的 $p$ 完全一致。能量符号亦给出圆锥类别：$E<0$ 对应 $e<1$ 的椭圆，$E=0$ 对应 $e=1$ 的抛物线，$E>0$ 对应双曲线。

### 5　无穷远入射条件

现在换成太阳引力参数 $\Gamma_\odot=GM_\odot$。无穷远处势能为零，故

$$\boxed{E=\frac12mv_0^2.}$$

速度直线到太阳中心的距离为 $b$，角动量大小为

$$\boxed{L=mv_0b.}$$

代入轨道参数，

$$\boxed{p=\frac{v_0^2b^2}{\Gamma_\odot},
\qquad e=\sqrt{1+\frac{v_0^4b^2}{\Gamma_\odot^2}}.}$$

粒子质量消去，反映经典引力散射的轨道与试探粒子质量无关。定义小参数

$$\lambda_N=\frac{\Gamma_\odot}{bv_0^2}\ll1,$$

则 $e=\sqrt{1+\lambda_N^{-2}}$。

### 6　渐近角和牛顿偏折角

轨道关于最近点轴对称。入射位置的渐近方向是 $-\theta_{\max}$，但入射速度指向太阳，须反转 $\pi$；出射速度沿 $+\theta_{\max}$。因此偏折角的大小为

$$\boxed{\Delta\varphi_N=2\theta_{\max}-\pi.}$$

用 $\theta_{\max}=\pi/2+\arcsin(1/e)$，可写成

$$\Delta\varphi_N=2\arcsin\frac1e.$$

因 $1/e=\lambda_N/\sqrt{1+\lambda_N^2}$，使用直角三角关系得精确散射结果

$$\boxed{\Delta\varphi_N=2\arctan\lambda_N
=2\arctan\frac{GM_\odot}{bv_0^2}.}$$

弱散射条件下展开：

$$\boxed{\Delta\varphi_N
\simeq\frac{2GM_\odot}{bv_0^2}.}$$

误差的首项为 $-2\lambda_N^3/3$，所以领头阶相对误差约 $\lambda_N^2/3$。角度必须按弧度使用这个展开。

### 7　沿近似直线积分的核验

弱偏折时，可将原入射轨迹近似为 $x=v_0t$、横向距离为 $b$。指向太阳的横向加速度大小为

$$a_\perp(t)=\frac{\Gamma_\odot b}{(b^2+v_0^2t^2)^{3/2}}.$$

积分全程，令 $\xi=v_0t/b$：

$$\Delta v_\perp
=\frac{\Gamma_\odot}{bv_0}
\int_{-\infty}^{\infty}\frac{d\xi}{(1+\xi^2)^{3/2}}.$$

由原函数 $\xi/\sqrt{1+\xi^2}$，定积分等于2，故

$$\Delta\varphi\simeq\frac{\Delta v_\perp}{v_0}
=\frac{2\Gamma_\odot}{bv_0^2}.$$

这条路线与双曲轨道的领头阶一致，但它已使用小偏折近似，不能替代任意 $b$ 条件下的精确双曲散射。

### 8　牛顿框架中的星光结果

按第（3）（ii）问的形式计算，令 $v_0=c$、$b\simeq R_\odot$，有

$$\boxed{\Delta\varphi_{\rm light,N}
\simeq\frac{2GM_\odot}{c^2R_\odot}.}$$

此处沿用牛顿粒子轨道模型，不能解释为光具有普通非相对论质量和动能。它提供的是牛顿框架的对照值，随后由题给弱场光学模型修正。

### 9　光学第一积分及常数的几何意义

对太阳外部，引力势为

$$\varphi(r)=-\frac{GM_\odot}{r}.$$

题给有效折射率于是为

$$\boxed{n(r)=1+\frac qr,
\qquad q=\frac{2GM_\odot}{c^2}.}$$

对给定微分式积分一次：

$$\frac{n(r)r^2\theta'}{\sqrt{1+r^2\theta'^2}}=C.$$

设轨道切线与径向方向夹角为 $\alpha$，则在一个 $r$ 单调的分支上有

$$\sin\alpha=\frac{r\theta'}{\sqrt{1+r^2\theta'^2}},$$

所以光学角动量不变量为

$$\boxed{C=nr\sin\alpha.}$$

无穷远处 $n\to1$，入射直线离太阳中心的距离为 $b=r\sin\alpha$，故守恒量的大小是

$$\boxed{|C|=b.}$$

入射和出射分支的 $d\theta/dr$ 符号可能不同。推导中使用正的大小，再利用轨道对称性合并两支，不能假定半径全程单调。

### 10　从第一积分导出轨道

将第一积分平方并解出 $\theta'^2$：

$$\theta'^2=\frac{b^2}{r^2[n(r)^2r^2-b^2]}.$$

令 $u=1/r$，使用 $dr/d\theta=-u'/u^2$，得到

$$\boxed{u'^2=\frac{(1+qu)^2}{b^2}-u^2.}$$

取弱场小参数 $q/b\ll1$。保留领头阶，

$$u'^2=\frac1{b^2}+\frac{2q}{b^2}u-u^2
+\text{二阶修正}.$$

微分或直接代入解形式，可得到领头阶轨道方程

$$u''+u=\frac q{b^2}.$$

其圆锥形式为

$$u=\frac{1+e_g\cos\theta}{p_g},$$

$$\boxed{p_g=\frac{b^2}{q},
\qquad e_g=\sqrt{1+\frac{b^2}{q^2}}.}$$

上述参数用于领头阶弱场计算。式中出现的 $q^2$ 只用于方便表达圆锥关系，不意味着我们已经控制了真实广义相对论的全部二阶项。

### 11　完整弱场星光偏折

同样用两渐近角关系，

$$\Delta\varphi_g=2\arcsin\frac1{e_g}
\simeq\frac{2q}{b}.$$

代入 $q=2GM_\odot/c^2$，

$$\boxed{\Delta\varphi_g
\simeq\frac{4GM_\odot}{c^2b}.}$$

对掠日光线 $b\simeq R_\odot$，有

$$\boxed{\Delta\varphi_{\rm grazing}
\simeq\frac{4GM_\odot}{c^2R_\odot}.}$$

它是第（3）（ii）问牛顿对照结果的两倍。该因子二来自题给有效折射率模型的引力效应，不是把同一条光线路径重复计算两次。

### 12　用横向折射率梯度独立检查

弱偏折、$n\simeq1$ 时，光线横向方向变化率领头阶为 $\partial n/\partial y$。以未偏折的直线 $y=b$ 计算，

$$\left|\frac{\partial n}{\partial y}\right|
=\frac{qb}{(x^2+b^2)^{3/2}}.$$

因此

$$\Delta\varphi_g\simeq
\int_{-\infty}^{\infty}\frac{qb\,dx}{(x^2+b^2)^{3/2}}
=\frac{2q}{b}.$$

这与轨道第一积分路线一致。此检查使用的是折射率梯度而不是牛顿质量粒子的加速度，故也能看清两个模型系数不同的来源。

### 13　最近距离和瞄准距离

在光线最近点，切线垂直径向方向，故 $\sin\alpha=1$。第一积分给

$$b=n(r_{\min})r_{\min}=r_{\min}+q.$$

在这个一阶有效折射率模型内，

$$r_{\min}=b-q.$$

若光线真正擦过太阳表面，则更准确应取 $b=R_\odot+q$。由于 $q/R_\odot\ll1$，把它换成 $b=R_\odot$ 只会改变偏折角的二阶小量，不影响本题领头阶答案。

牛顿陨石轨道的最近距离为

$$r_{\min,N}=\frac{p}{1+e}
=b\big(\sqrt{1+\lambda_N^2}-\lambda_N\big),$$

也不严格等于 $b$。近似从一开始就应写明在哪个阶数上用 $b$ 代替最近距离。

### 14　量纲、极限与答案整理

$GM$ 的量纲是长度的三次方每时间平方，故 $GM/(bv^2)$ 和 $GM/(c^2R)$ 无量纲，适合表示弧度角。$b\to\infty$、$M\to0$ 时偏折趋零；更小的瞄准距离或更慢的陨石速度使牛顿偏折增大，但进入强散射后必须回到精确反正切式。

本题结果依次为 $\theta_{\max}=\arccos(-1/e)$、轨道守恒量关系、陨石弱偏折 $2GM_\odot/(bv_0^2)$、牛顿光束对照 $2GM_\odot/(c^2R_\odot)$，以及弱场光学结果 $4GM_\odot/(c^2R_\odot)$。

## 六、关键洞察

角度关系的核心是入射速度与入射位置径向方向相反。守恒量在粒子轨道和光学轨道中各有不同含义：前者是机械角动量，后者是 $nr\sin\alpha$。领头阶比较可以统一形式，却不能把不同模型的高阶项混用。

## 七、易错点

用 $2\theta_{\max}$ 作为散射角；漏掉平方根中的质量幂；把 $b$ 当精确最近距离；对全过程假设 $r$ 单调；忘记折射率无穷远趋于一以确定常数；将牛顿光束结果当完整广义相对论结果；保留部分二阶项却宣称二阶精确。

## 八、课堂讲解建议

先画两条渐近线，分别标位置矢量和速度，现场推出减去 $\pi$ 的角度关系。再用倒数半径统一能量推导与轨道方程。光学部分从 $nr\sin\alpha=b$ 入手，让学生自行确定常数，然后用直线梯度积分检查偏折系数。

## 九、变式训练

### 变式1　从偏折角反求瞄准距离

牛顿陨石散射给定速度 $v_0$、精确偏折角 $\delta$，求 $b$。

解：由 $\delta=2\arctan[GM/(bv_0^2)]$，有

$$\boxed{b=\frac{GM}{v_0^2}\cot\frac\delta2.}$$

当 $\delta\ll1$，恢复 $b\simeq2GM/(v_0^2\delta)$。若 $\delta=60^\circ$，则 $b=\sqrt3GM/v_0^2$，这时弱偏折假设不成立，应使用精确关系。

### 变式2　给定最近距离求偏折

质点在质量 $M$ 周围散射，远处速度为 $v_0$，最近距离为 $r_p$。求瞄准距离和偏折角。

解：最近点径向速度为零，能量与角动量给

$$\frac12mv_0^2=\frac{m v_0^2b^2}{2r_p^2}-\frac{GMm}{r_p}.$$

故

$$\boxed{b^2=r_p^2+\frac{2GM r_p}{v_0^2},
\quad\delta=2\arctan\frac{GM}{v_0^2b}.}$$

吸引作用使 $b>r_p$。当 $GM/(r_pv_0^2)\ll1$，两者差约 $GM/v_0^2$；更强聚焦时不得忽略。

### 变式3　一般弱场折射率系数

假设有效折射率为 $n=1-\chi\varphi/c^2$，$\chi>0$。求弱偏折。

解：中心引力势使 $n=1+q_\chi/r$，$q_\chi=\chi GM/c^2$。按正文横向梯度积分，

$$\boxed{\delta\simeq\frac{2q_\chi}{b}
=\frac{2\chi GM}{c^2b}.}$$

题给 $\chi=2$ 得系数四。这个结果只使用指定光学模型，不能仅由改变 $\chi$ 就宣称得到另一套完整相对论理论。

### 变式4　有效折射率模型的完整轨道

将 $n=1+q/r$ 当作一个给定的光学模型，不再丢弃其中 $q^2$ 项，且 $b>q$。求该模型的散射角。

解：倒数半径满足

$$u'^2=\frac1{b^2}+\frac{2q}{b^2}u
-\left(1-\frac{q^2}{b^2}\right)u^2.$$

令 $\eta=\sqrt{1-q^2/b^2}$，以最近点为 $\theta=0$，解为

$$u=\frac{q+b\cos(\eta\theta)}{b^2-q^2}.$$

无穷远时 $\cos(\eta\theta_{\max})=-q/b$，故

$$\boxed{\delta=\frac{2\arccos(-q/b)}{\sqrt{1-q^2/b^2}}-\pi.}$$

展开首项为 $2q/b$，与正文一致。它是在指定折射率函数内的完整解；由于真实弱场折射率本身只给到一阶，其更高阶系数不能直接视为广义相对论的精确预言。
