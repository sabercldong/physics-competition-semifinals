# 第 1 题　高层建筑的摆式减振器（45分）

高层建筑在风的作用下会发生晃动。在特定条件下，晃动幅度会变得较大。

（1）为减小晃动，在建筑物上安装摆式减振器。摆的悬点固定在大楼上，摆锤质量为 $m$，刚性摆臂长为 $l$，摆臂质量可忽略。大楼视为质量为 $M$ 的刚体，其水平回复力等效为劲度系数为 $k$ 的弹簧；整个系统总质量为 $M+m$。风的水平强迫力向左为正，随时间变化为

$$F(t)=H\cos\omega t,$$

其中 $H$、$\omega$ 为常量，重力加速度为 $g$。本问只考虑摆和振子的微小振动。

![建筑物与摆式减振器；位移和摆角向左为正](../figures/q1-building.png)

（1.1）求大楼在强迫力作用下产生的稳定振动的振幅。

（1.2）指出没有减振器时，什么风频率使大楼受迫振幅最大；针对此频率，减振器满足什么条件才能最大限度减小大楼的受迫振动？

（2）风频率为第（1.2）问所得频率的 $\sqrt{0.99}$ 倍。求没有减振器时大楼的受迫振幅。若摆长 $l$ 满足第（1.2）问的条件，要使振幅降到无减振器时的 $1\%$，求 $m/M$。

（3）实际装置将摆锤浸没在固定于大楼的油池中。油的质量可忽略，或已包含在 $M$ 中。油相对大楼静止，摆锤相对油的速度为 $\boldsymbol v'$ 时受到阻力 $\boldsymbol f=-\gamma\boldsymbol v'$，$\gamma$ 为常量。写出含阻尼力的系统运动方程组，列式时不作小振幅近似，无需求解。定性说明阻尼力为何不可缺少。

## 一、题型定位

两个自由度的受迫振动与动力吸振。大楼的位移和摆的相对位移相互耦合；摆的存在改变了整套系统的固有频率，并可在某个驱动频率产生反共振。第（3）问进一步要求在有限摆角下正确处理相对速度、阻力反作用和能量耗散。

“稳定振动”在无阻尼部分按题意理解为与外力同频的特解。没有阻尼时，自由振动一般不会自行消失；在真正的共振频率上也不存在有限振幅的同频特解。求出的带符号响应系数需要取绝对值，才是实际振幅。

## 二、知识点

悬点平动的单摆运动；小量阶数与线性化；牛顿定律和系统动量方程；同频特解与相位；反共振和共振的区别；粘性阻尼的相对速度；能量损失率。

对 $\theta$ 作小量展开时，$\sin\theta\simeq\theta$、$\cos\theta\simeq1$，而 $\dot\theta^2$、$\ddot x\theta$ 等为二阶量。不能一面使用小振动方程，一面保留同阶的某个乘积却忽略另一个。

## 三、物理图像

若大楼向左加速，悬点系中摆锤受到向右的惯性力。摆锤的相对振动又通过摆臂给建筑物一个水平反作用。精确调谐时，大楼可以近乎静止，外力主要由摆的反作用抵消。

无阻尼摆没有把能量变成热，它是储能并交换能量的附加振子。安装后原来单一的共振峰分裂为两个峰，中间出现大楼响应为零的频率。阻尼使峰值有限，并使风停止后振动衰减。

![耦合系统的两个固有频率与反共振频率](../figures/q1-response.png)

## 四、解题入口

取大楼位移 $x$ 向左为正，摆相对铅垂向下方向的偏角 $\theta$ 向左为正，记 $y=l\theta$。先写摆锤的绝对位置，分别列摆锤和大楼方程，再取线性近似。令 $x=X\cos\omega t$、$y=Y\cos\omega t$，解两个代数方程。

第（2）问最好把频率和质量无量纲化，避免把“振幅减小到 $1\%$”误读成“减小 $1\%$”。第（3）问回到未线性化的坐标，阻尼只能依赖 $\boldsymbol v'$，不能使用摆锤对地速度。

## 五、解析

### 1　绝对坐标与摆锤受力

竖直坐标 $z$ 向下为正。悬点高度不变，把悬点的竖直坐标取为零，则摆锤位置为

$$x_m=x+l\sin\theta,\qquad z_m=l\cos\theta.$$

一次和二次微分分别给出

$$\dot x_m=\dot x+l\dot\theta\cos\theta,
\qquad \dot z_m=-l\dot\theta\sin\theta,$$

$$\ddot x_m=\ddot x+l\ddot\theta\cos\theta-l\dot\theta^2\sin\theta,$$

$$\ddot z_m=-l\ddot\theta\sin\theta-l\dot\theta^2\cos\theta.$$

设摆臂沿朝向悬点的力大小为 $T$。没有油阻力时，牛顿方程为

$$m(\ddot x+l\ddot\theta\cos\theta-l\dot\theta^2\sin\theta)
=-T\sin\theta,$$

$$m(-l\ddot\theta\sin\theta-l\dot\theta^2\cos\theta)
=mg-T\cos\theta.$$

在小振动的一阶精度内，竖直方程的惯性项均是二阶量，因此

$$T=mg+O(\theta^2).$$

代入水平式、除以 $m$，得到

$$\boxed{\ddot x+l\ddot\theta+g\theta=0.}$$

用相对水平位移 $y=l\theta$ 和 $\omega_0^2=g/l$ 表示，即

$$\boxed{\ddot x+\ddot y+\omega_0^2y=0.}$$

注意 $\ddot x$ 是悬点加速度。若把这一项遗漏，就把本题错误地变成了悬点不动的单摆。

### 2　大楼方程与系统方程的相互检查

摆锤通过摆臂拉大楼向左，水平反作用为 $T\sin\theta$。大楼方程为

$$M\ddot x=-kx+T\sin\theta+H\cos\omega t.$$

线性化并用 $y=l\theta$，有

$$\boxed{M\ddot x+kx-m\omega_0^2y=H\cos\omega t.}$$

也可把摆锤和大楼看成整体。它们的总水平动量在线性精度内为

$$P_x=(M+m)\dot x+m\dot y.$$

摆臂内力相消，故

$$\boxed{(M+m)\ddot x+m\ddot y+kx=H\cos\omega t.}$$

利用摆方程 $\ddot y=-\ddot x-\omega_0^2y$，这一式立即还原为大楼方程。整体方程里出现 $M+m$，单独大楼方程里出现 $M$，两者没有矛盾；相对运动项不能随意删去。

### 3　求同频响应

令带符号响应系数为 $X,Y$：

$$x=X\cos\omega t,\qquad y=Y\cos\omega t.$$

将它们代入两个线性方程，得到

$$-\omega^2X+(\omega_0^2-\omega^2)Y=0,$$

$$ (k-M\omega^2)X-m\omega_0^2Y=H.$$

当 $\omega\ne\omega_0$ 时，从第一式有

$$Y=\frac{\omega^2}{\omega_0^2-\omega^2}X.$$

代入第二式并通分，定义

$$D(\omega)=(\omega_0^2-\omega^2)(k-M\omega^2)
-m\omega_0^2\omega^2,$$

便有

$$\boxed{X=\frac{(\omega_0^2-\omega^2)H}{D(\omega)},
\qquad Y=\frac{\omega^2H}{D(\omega)}.}$$

实际振幅为

$$\boxed{A=|X|
=\frac{H|\omega_0^2-\omega^2|}{|D(\omega)|}.}$$

这里取 $H>0$；若外力系数也带符号，分子应使用 $|H|$。$X>0$ 表示大楼与外力同相，$X<0$ 表示反相。不能将负值报告成负振幅。

在 $\omega=\omega_0$ 处，先前的中间消元除数为零，但原代数方程仍有解：

$$X=0,\qquad Y=-\frac{H}{m\omega_0^2},\qquad m>0.$$

因此最终表达式可连续使用。这是反共振：大楼不动，摆保持有限的反相振动。摆角振幅为

$$\Theta=\frac{|Y|}{l}=\frac{H}{mg}.$$

要让小角近似自洽，必须另有 $H/(mg)\ll1$。仅仅得到 $X=0$，不能保证摆锤小幅运动。

### 4　无减振器的共振与摆长调谐

没有摆时取 $m=0$，大楼方程单独给出

$$X_{\rm bare}=\frac{H}{k-M\omega^2}.$$

其固有频率为

$$\boxed{\Omega=\sqrt{\frac{k}{M}}.}$$

当 $\omega\to\Omega$ 时，无阻尼同频响应的振幅趋于无穷。在恰好共振时，运动含随时间增长的项，而不是具有有限最大值的稳定正弦振动。

现在使风频率固定为 $\Omega$，安装摆后代入 $k-M\Omega^2=0$，有

$$X(\Omega)
=\frac{(\Omega^2-\omega_0^2)H}{m\omega_0^2\Omega^2}
=\frac{H(kl-Mg)}{mgk}.$$

其大小最小的调谐条件是

$$\boxed{\omega_0=\Omega,
\qquad l=\frac{Mg}{k}.}$$

若摆长不能精确调谐，增大 $m$ 也会减小上述响应，但不能对任意风频率都保证无限制改善。精确调谐所得零振幅针对指定频率，离开这个频率后仍须使用完整的 $D(\omega)$。

### 5　频率偏离调谐值时的质量要求

题给 $\omega^2=0.99k/M=0.99\Omega^2$。无摆时

$$\boxed{A_{\rm bare}=\frac{H}{k-0.99k}=\frac{100H}{k}.}$$

调谐摆满足 $\omega_0^2=\Omega^2$。令

$$s=\frac{\omega^2}{\Omega^2}=0.99,
\qquad \eta=\frac mM.$$

将分母提取因子 $k\Omega^2$，得到

$$D=k\Omega^2[(1-s)^2-\eta s].$$

于是

$$X=\frac Hk\frac{1-s}{(1-s)^2-\eta s},$$

$$\frac{A}{A_{\rm bare}}
=\frac{(1-s)^2}{|(1-s)^2-\eta s|}.$$

要求 $A/A_{\rm bare}=0.01$，故

$$|0.0001-0.99\eta|=0.01.$$

有两个代数分支。若 $0.0001-0.99\eta=0.01$，则 $\eta<0$，不是可用的摆锤质量；另一分支给出

$$0.0001-0.99\eta=-0.01,$$

$$\boxed{\frac mM=\frac{0.0101}{0.99}
=\frac{101}{9900}\simeq0.01020.}$$

这一质量约为大楼质量的 $1.02\%$。代回有 $X=-H/k$，实际振幅 $H/k$，正是 $100H/k$ 的百分之一；负号表明响应已经进入反相分支。

如果只要求“不超过百分之一”，则同样在正质量支上得到 $m/M\ge101/9900$，但仍须满足摆幅和装置尺寸等模型条件。

### 6　安装摆后为何仍可能共振

取外力为零，同频运动的非零解要求 $D=0$。在调谐情形写成

$$s^2-(2+\eta)s+1=0.$$

两个固有频率平方对应

$$\boxed{s_\pm=
\frac{2+\eta\pm\sqrt{\eta^2+4\eta}}2,
\qquad \omega_\pm=\Omega\sqrt{s_\pm}.}$$

因 $s_-s_+=1$，且 $s_-<1<s_+$，反共振频率 $\Omega$ 位于两个共振频率之间。摆的作用是重塑频率响应，并没有消灭无阻尼系统的全部共振。

对 $\eta=101/9900$，计算得 $\omega_-/\Omega\simeq0.9508$、$\omega_+/\Omega\simeq1.0518$。题给风频率约为 $0.9950\Omega$，处在两个共振峰之间。

### 7　有限摆角下的油阻力

油随大楼平动，因而摆锤相对油的速度为

$$\boldsymbol v'
=l\dot\theta\cos\theta\,\boldsymbol e_x
-l\dot\theta\sin\theta\,\boldsymbol e_z.$$

相应阻力分量为

$$f_x=-\gamma l\dot\theta\cos\theta,
\qquad f_z=\gamma l\dot\theta\sin\theta.$$

使用第1节的精确加速度，摆锤两方向方程为

$$m(\ddot x+l\ddot\theta\cos\theta-l\dot\theta^2\sin\theta)
=-T\sin\theta-\gamma l\dot\theta\cos\theta,$$

$$m(-l\ddot\theta\sin\theta-l\dot\theta^2\cos\theta)
=mg-T\cos\theta+\gamma l\dot\theta\sin\theta.$$

摆锤对油的反作用最终传给大楼，不能遗漏它。大楼精确方程为

$$\boxed{M\ddot x=-kx+T\sin\theta
+\gamma l\dot\theta\cos\theta+H\cos\omega t.}$$

上面三个方程配合未知量 $x,\theta,T$，就是一组完整答案。也可消去 $T$，写成更紧凑的两自由度方程：

$$\boxed{ml^2\ddot\theta+ml\ddot x\cos\theta
+mgl\sin\theta+\gamma l^2\dot\theta=0,}$$

$$\boxed{(M+m)\ddot x
+ml(\ddot\theta\cos\theta-\dot\theta^2\sin\theta)
+kx=H\cos\omega t.}$$

第二式是全系统的水平动量方程，因此摆臂力和油阻力均作为内力相消。两种形式应给出一致运动。

### 8　用能量说明阻尼的必要性

以最低摆位为重力势能零点，总机械能为

$$\begin{aligned}
E={}&\frac12(M+m)\dot x^2
+ml\dot x\dot\theta\cos\theta
+\frac12ml^2\dot\theta^2\\
&+\frac12kx^2+mgl(1-\cos\theta).
\end{aligned}$$

阻力作用于摆锤和大楼的总功率是

$$\boldsymbol f\cdot\boldsymbol v_m
-\boldsymbol f\cdot\boldsymbol v_{\rm oil}
=\boldsymbol f\cdot\boldsymbol v'
=-\gamma l^2\dot\theta^2.$$

因此

$$\boxed{\frac{dE}{dt}
=H\cos\omega t\,\dot x-\gamma l^2\dot\theta^2.}$$

风停后 $H=0$，有 $dE/dt\le0$。油阻力把相对摆动的机械能转为热，使自由振动逐步衰减。受迫运动时，它也限制两个耦合共振峰，并缓和精确调谐对频率漂移的敏感性。

### 9　量纲、静态极限与结果汇总

$D$ 的量纲为质量乘以时间的负四次方，$H(\omega_0^2-\omega^2)/D$ 的量纲为长度，符合位移。$\omega\to0$ 时 $X\to H/k$、$Y\to0$，对应大楼准静态形变和竖直单摆。取 $m\to0$ 且避开可约分的奇点，恢复单自由度响应。

本题主要结果是大楼振幅 $|X|$，调谐摆长 $Mg/k$，第（2）问质量比 $101/9900$，以及第（3）问有限摆角运动方程。零响应和有限摆幅必须同时检查，只有质量为正的代数支可用。

## 六、关键洞察

反共振是某个观测坐标的响应为零，不是所有运动都消失。把总动量方程与摆角方程并列，能直接看清附加质量的惯性反馈。无阻尼所谓“稳定振动”只是选取特解；物理上自由振动衰减需要阻尼。

## 七、易错点

把 $M$ 改为 $M+m$ 后删掉相对加速度；把负响应系数当负振幅；在 $\omega=\omega_0$ 处直接除以零；质量比解出后不筛选正质量；只给摆加阻力而不给大楼加反作用；用对地速度代替相对油速度。

## 八、课堂讲解建议

先让学生写摆锤的绝对位置，用全系统动量检查两套方程。随后在同一条频率轴上标出 $\omega_-$、$\omega_0$、$\omega_+$，区分两峰与中间零点。讲第（2）问时保留绝对值到分支筛选之后。最后通过阻力总功率推导耗散率，把几何、动力学与能量联系起来。

## 九、变式训练

### 变式1　摆长轻微失谐

仍用 $\omega=\Omega$，摆长变成 $l=l_0(1+\delta)$，其中 $l_0=Mg/k$。求大楼振幅，并判断一阶误差。

解：在 $\omega=\Omega$ 处使用未取绝对值的完整响应，有

$$X=\frac{H(kl-Mg)}{mgk}
=\frac{HM\delta}{mk},\qquad
A=\frac Hk\frac{|\delta|}{\eta}.$$

这里结果对 $\delta$ 是精确线性的，但模型仍要求小振动。若 $\eta=0.01$、$|\delta|=0.001$，则 $A=0.1H/k$。在零响应附近不能定义相对于零的百分比误差，应报告绝对振幅。

### 变式2　给定允许摆角求最小摆锤质量

精确调谐且驱动频率为 $\Omega$，要求摆角不超过 $\Theta_{\max}$，求 $m$ 的下限。

解：反共振时 $X=0$，摆的相对位移 $Y=-H/(m\Omega^2)$。因 $l=g/\Omega^2$，有

$$\Theta=\frac{|Y|}{l}=\frac H{mg}.
\qquad \boxed{m\ge\frac H{g\Theta_{\max}}.}$$

例如 $H=2.0\times10^5\,\mathrm N$、$g=10\,\mathrm{m/s^2}$、$\Theta_{\max}=0.02$，需 $m\ge10^6\,\mathrm{kg}$。由摆角约束决定的质量可能比单独用大楼振幅要求所得质量更大。

### 变式3　线性油阻尼下的响应

用小振动近似，求频率为 $\omega$ 的复振幅表达式。

解：令 $y=l\theta$，线性方程为

$$\ddot x+\ddot y+\frac\gamma m\dot y+\omega_0^2y=0,
\quad (M+m)\ddot x+m\ddot y+kx=H\cos\omega t.$$

设 $x=\Re(\widetilde X e^{i\omega t})$、$y=\Re(\widetilde Y e^{i\omega t})$，定义 $q=\omega_0^2-\omega^2+i\gamma\omega/m$。第一式给 $\widetilde Y=\omega^2\widetilde X/q$，第二式于是给出

$$\boxed{\widetilde X=
\frac{Hq}{[k-(M+m)\omega^2]q-m\omega^4}.}$$

实际幅度为 $|\widetilde X|$、相位为其辐角。取 $\gamma\to0$ 可还原正文结果；$\gamma>0$ 时 $q$ 不再在反共振频率为零，所以理想的零响应变为有限的低谷。

### 变式4　风停止后的机械能下降

已知某一段内摆角近似为 $\theta=\Theta\cos\nu t$，振幅变化很慢，求油阻力一周期平均耗散功率。

解：由精确耗散率 $P_{\rm loss}=\gamma l^2\dot\theta^2$，代入 $\dot\theta=-\nu\Theta\sin\nu t$，得

$$\boxed{\langle P_{\rm loss}\rangle
=\frac12\gamma l^2\nu^2\Theta^2.}$$

一个周期内损失的能量约为 $\pi\gamma l^2\nu\Theta^2$。该近似要求一周期内能量变化相对较小；若阻尼很强，应直接解耦合运动方程并积分耗散率。

若这段运动是一个弱阻尼正常模态，还可求其振幅衰减率。设 $x=X\cos\nu t$、$y=Y\cos\nu t$，$Y=l\Theta$。等效质量二次型为

$$\mathcal M=(M+m)X^2+2mXY+mY^2.$$

对无阻尼正常模态，平均动能与平均势能相等，周期内的总能量为 $E=\nu^2\mathcal M/2$。平均耗散率为 $\gamma\nu^2Y^2/2$，于是

$$\frac{\langle P_{\rm loss}\rangle}{E}
=\frac{\gamma Y^2}{\mathcal M}.$$

当形状比 $Y/X$ 近似不变时，模态振幅按

$$\boxed{a(t)\simeq a(0)\exp\left(-\frac{\gamma Y^2}{2\mathcal M}t\right)}$$

衰减。比值中的 $X,Y$ 可取任意同一归一化下的模态形状，因为共同倍数会相消。此式把阻尼效果与摆的相对运动参与程度联系起来：摆相对位移越小，同样油阻力对该模态耗散越弱。
