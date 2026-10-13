# 第 2 题　半圆管活塞的临界稳定性（40分）

将粗细均匀、两端封闭的细玻璃管弯成半径为 $r$ 的半圆环，竖直固定于水平地面，两端与地面接触。管的横截面尺寸远小于 $r$。管内有质量为 $m$ 的薄活塞，与管壁密接，摩擦忽略；活塞相对竖直方向的角位置为 $\theta$。两侧各有 $n$ 摩尔理想气体，其温度始终与外界温度 $T$ 相同，所有气体状态变化均可视为准静态。重力加速度为 $g$，普适气体常量为 $R$。

![半圆管、活塞与两侧气体长度](../figures/q2-piston.png)

（1）当 $T$ 高于某临界温度 $T_c$ 时，$\theta=0$ 为稳定平衡位置。求 $T_c$ 及活塞在该位置附近微振动的圆频率。

（2）$T=T_c$ 时，判断中央平衡位置的稳定性。

以下可视 $T_c$ 为已知量，不必代入第（1）问结果。

（3）$T<T_c$ 时，求稳定平衡角 $\theta_0$ 满足的方程，并求 $T$ 略低于 $T_c$ 时 $\theta_0$ 的最低非零阶近似。

（4）求 $T<T_c$ 时稳定位置附近的微振动圆频率 $\omega_0(\theta_0)$，表达式可含 $\theta_0$，不可含 $T$；并给出 $T$ 略高于及略低于 $T_c$ 时圆频率随温度的变化。

（5）$T<T_c$ 时，初始速度近似为零，求从正中央运动到可到达的角位置 $\theta$ 时角速度的大小。

## 一、题型定位

气体压力与重力共同作用下的平衡、稳定性和非线性运动。活塞在圆环最高点时，重力使它偏离中央；两侧气体的压强差则把它推回中央。改变温度会改变气体恢复力，从而改变稳定平衡位置的数目。

临界温度处线性项为零，必须保留更高阶项。线性微振动频率为零只表示线性近似失效，不足以判定“中性平衡”。

## 二、知识点

等温理想气体 $pV=nRT$；圆弧切向动力学；小角展开；力的导数与稳定性；势能的局部极小；非线性方程的第一积分。用角坐标时，实际切向加速度为 $r\ddot\theta$，动能为 $mr^2\dot\theta^2/2$。

外界保持气体等温，气体与热库交换热量；不能把活塞动能与重力势能单独相加并声称守恒。可以把压强力对位置的作用积分成一个等效势能，这个势能含气体自由能的变化。

## 三、物理图像

取 $\theta>0$ 为向右偏转。右侧气柱变短，左侧气柱变长，右侧压强更大，气体合力沿切线向左。重力的切向分量向右，为 $mg\sin\theta$。中央处两侧压强相等，重力切向分量也为零，所以任何温度下中央都是一个平衡位置。

高温时气体恢复力较强，只有中央稳定；低温时中央不稳定，左右各出现一个稳定位置。对称性要求两个位置以 $\pm\theta_0$ 成对出现。

## 四、解题入口

引入管截面积 $S$，写出两侧体积，求压力后乘以 $S$。截面积会消掉。把切向动力学方程写成 $\ddot\theta=A(\theta)$，先展开 $A'(0)$ 求临界温度，再展开三次项。非中央平衡先用完整方程求出，再把它用于消去频率式中的 $T$。

## 五、解析

### 1　完整切向运动方程

记 $a=\pi/2$。两侧气柱的弧长分别为 $r(a+\theta)$、$r(a-\theta)$，所以

$$V_L=Sr(a+\theta),\qquad V_R=Sr(a-\theta).$$

等温条件给出

$$p_L=\frac{nRT}{Sr(a+\theta)},\qquad
p_R=\frac{nRT}{Sr(a-\theta)}.$$

沿 $\theta$ 增大方向的合力为

$$F_t=mg\sin\theta+p_LS-p_RS.$$

故

$$mr\ddot\theta=mg\sin\theta
-\frac{nRT}{r(a-\theta)}+\frac{nRT}{r(a+\theta)}.$$

合并分式，并再除以 $mr$：

$$\boxed{\ddot\theta=\frac gr\sin\theta
-\frac{2nRT}{mr^2}\frac\theta{a^2-\theta^2}.}$$

物理区间为 $|\theta|<a$。活塞逼近端点时，某侧体积趋于零，压强发散；本模型内有限能量运动不能越过这个边界。

### 2　中央位置的线性稳定性

在 $|\theta|\ll1$ 时，$\sin\theta\simeq\theta$，$1/(a^2-\theta^2)\simeq1/a^2$，因此

$$\ddot\theta=\left(\frac gr-\frac{8nRT}{\pi^2mr^2}\right)\theta.$$

稳定的小振动要求括号为负。临界条件为

$$\frac gr=\frac{8nRT_c}{\pi^2mr^2},$$

于是

$$\boxed{T_c=\frac{\pi^2mgr}{8nR}.}$$

对 $T>T_c$，写成 $\ddot\theta+\omega^2\theta=0$，得

$$\boxed{\omega^2=\frac{8nRT}{\pi^2mr^2}-\frac gr
=\frac gr\left(\frac T{T_c}-1\right).}$$

该频率是无限小振幅的线性频率。离临界点足够近时，非线性项对任何固定振幅都可能重要，使用线性式须同时限制振幅。

### 3　无量纲化使临界条件更透明

记 $\tau=T/T_c$，利用临界温度把完整方程整理为

$$\boxed{\ddot\theta=\frac gr
\left[\sin\theta-\frac{\tau\theta}{1-4\theta^2/\pi^2}\right].}$$

再定义时间 $\xi=t\sqrt{g/r}$，方程中除 $\tau$ 外不再含参数：

$$\frac{d^2\theta}{d\xi^2}
=\sin\theta-\frac{\tau\theta}{1-4\theta^2/\pi^2}.$$

这说明不同质量、半径和气体量的装置，只要温度比 $\tau$ 相同，角运动在适当时间尺度下相同。质量和气体量通过 $T_c$ 影响稳定性，而 $\sqrt{r/g}$ 决定时间尺度。

### 4　临界温度必须保留三次项

分别展开

$$\sin\theta=\theta-\frac{\theta^3}{6}+O(\theta^5),$$

$$\frac{\theta}{1-4\theta^2/\pi^2}
=\theta+\frac4{\pi^2}\theta^3+O(\theta^5).$$

在 $\tau=1$ 时，线性项相消，得到

$$\ddot\theta=-\frac gr
\left(\frac16+\frac4{\pi^2}\right)\theta^3+O(\theta^5).$$

定义

$$c=\frac16+\frac4{\pi^2}=\frac{24+\pi^2}{6\pi^2}>0,$$

则领先阶为 $\ddot\theta=-(g/r)c\theta^3$。任何小的正偏移都对应负加速度，负偏移对应正加速度，因此

$$\boxed{T=T_c\text{ 时中央仍为稳定平衡位置，但不是线性简谐振子。}}$$

“稳定”表示足够小的初始扰动不会使轨道离开中央附近；无摩擦时并不表示活塞最终停回中央。

### 5　低温非中央平衡方程

设平衡角 $\theta_0\ne0$，把完整方程右侧设为零：

$$\sin\theta_0=\frac{\tau\theta_0}{1-4\theta_0^2/\pi^2}.$$

所以

$$\boxed{\frac T{T_c}
=\left(1-\frac{4\theta_0^2}{\pi^2}\right)
\frac{\sin\theta_0}{\theta_0}.}$$

对于 $0<\theta_0<\pi/2$，两个因子均为正且严格下降。$\sin x/x$ 的导数为 $(x\cos x-\sin x)/x^2<0$，因为 $\tan x>x$。右侧从1连续降到0。因此每个 $0<\tau<1$ 恰有一个正根，对称性再给一个负根。

当 $\tau>1$，右侧不可能达到 $\tau$，没有非中央平衡。中央的加速度斜率为 $(g/r)(1-\tau)$，所以它在低温时不稳定，高温时稳定。

### 6　近平衡分支的平方根规律

若 $T$ 略小于 $T_c$，$\theta_0$ 很小。展开平衡式：

$$\tau=\left(1-\frac{4\theta_0^2}{\pi^2}\right)
\left(1-\frac{\theta_0^2}{6}+O(\theta_0^4)\right)
=1-c\theta_0^2+O(\theta_0^4).$$

于是

$$\boxed{\theta_0\simeq\pm
\sqrt{\frac{6\pi^2}{24+\pi^2}\frac{T_c-T}{T_c}}.}$$

这是最低非零阶近似。不能把 $\theta_0$ 写成正比于 $T_c-T$：对称性使平衡式的首个角度修正为二次项，解出角度自然出现平方根。

例如 $\tau=0.99$，近似角度为 $\sqrt{0.01/c}\simeq0.132$ rad，约7.57°。将它代回完整平衡式可检查遗漏的四次项只造成更高阶偏差。

### 7　非中央稳定位置附近的频率

令 $\theta=\theta_0+\eta$，$|\eta|\ll1$，并记完整右侧为 $A(\theta)$。因为 $A(\theta_0)=0$，

$$\ddot\eta=A'(\theta_0)\eta+O(\eta^2),\qquad
\omega_0^2=-A'(\theta_0).$$

从未消温度的完整式求导：

$$A'(\theta)=\frac gr\cos\theta
-\frac{2nRT}{mr^2}\frac{a^2+\theta^2}{(a^2-\theta^2)^2}.$$

平衡条件给出

$$\frac{2nRT}{mr^2}
=\frac gr\frac{\sin\theta_0}{\theta_0}(a^2-\theta_0^2).$$

代入得到不含 $T$ 的形式：

$$\boxed{\omega_0^2=\frac gr
\left[\frac{\sin\theta_0}{\theta_0}
\frac{a^2+\theta_0^2}{a^2-\theta_0^2}-\cos\theta_0\right].}$$

等价地，写成参考解答的形式为

$$\omega_0^2=\frac{g\cos\theta_0}{r}
\left[\frac{\tan\theta_0}{\theta_0}
\frac{\pi^2/2+2\theta_0^2}{\pi^2/2-2\theta_0^2}-1\right].$$

对正根，$\sin\theta_0/\theta_0>\cos\theta_0$，且分式大于1，所以括号为正；负根给出相同结果。两个非中央根确实稳定，不只是力为零。

### 8　临界点两侧的频率比较

高温一侧的结果已知：

$$\boxed{\omega\simeq\sqrt{\frac gr\frac{T-T_c}{T_c}}.}$$

低温一侧，把频率式展开到 $\theta_0^2$：

$$\frac{\sin\theta_0}{\theta_0}\simeq1-\frac{\theta_0^2}{6},\qquad
\frac{a^2+\theta_0^2}{a^2-\theta_0^2}\simeq1+\frac{8\theta_0^2}{\pi^2},$$

$$\cos\theta_0\simeq1-\frac{\theta_0^2}{2}.$$

相减后系数为 $1/3+8/\pi^2=2c$，因此

$$\omega_0^2\simeq\frac gr,2c\theta_0^2
\simeq\frac{2g}{r}\frac{T_c-T}{T_c}.$$

即

$$\boxed{\omega_0\simeq\sqrt{\frac{2g}{r}\frac{T_c-T}{T_c}}.}$$

相同相对温差下，低温稳定分支的线性频率是高温中央分支的 $\sqrt2$ 倍。频率都随温差的平方根趋于零，这种趋零不能等同于失去非线性稳定性。

### 9　等效势能与完整稳定性图像

把广义力积分，选 $U(0)=0$：

$$\boxed{U(\theta)=mgr(\cos\theta-1)
-nRT\ln\left(1-\frac{4\theta^2}{\pi^2}\right).}$$

它满足 $mr^2\ddot\theta=-U'(\theta)$。气体项也可由两侧等温自由能 $-nRT\ln V_L-nRT\ln V_R$ 的变化求得。

中央附近展开为

$$\frac{U}{mgr}
=\frac{\tau-1}{2}\theta^2
+\left(\frac1{24}+\frac\tau{\pi^2}\right)\theta^4
+O(\theta^6).$$

临界点四次系数为 $c/4>0$；高温是单个势阱，低温为两个势阱。原方程中的左右对称在势能中表现为偶函数。

![高温单阱、临界四次阱与低温双阱](../figures/q2-potential.png)

### 10　从中央附近释放的角速度

对完整切向方程乘 $r\,d\theta$，或用等效势能的第一积分，得到

$$\frac12mr^2\dot\theta^2+U(\theta)=E.$$

取从中央出发、初始动能趋于零的极限，则 $E=U(0)=0$，所以

$$\frac12mr^2\dot\theta^2
=mgr(1-\cos\theta)
+nRT\ln\left(1-\frac{4\theta^2}{\pi^2}\right).$$

故在可达区间中

$$\boxed{|\dot\theta|=
\sqrt{\frac{2g}{r}(1-\cos\theta)
+\frac{2nRT}{mr^2}\ln\left(1-\frac{4\theta^2}{\pi^2}\right)}.}$$

根号中的气体项为负：活塞偏离中央时气体恢复力阻碍运动。若误写成正号，就会预测活塞能以无穷速度冲入压强发散的端点，违反本模型的受力方向。

### 11　可达角与“从正中央开始”的数学细节

只有根号内非负的位置可到达。非零转向角 $\theta_m$ 由 $U(\theta_m)=0$ 确定。近平衡临界区，用四次势近似：

$$\frac{U}{mgr}\simeq-\frac{1-\tau}{2}\theta^2+\frac c4\theta^4,$$

所以 $\theta_m^2\simeq2(1-\tau)/c=2\theta_0^2$。释放轨道会经过稳定位置，直到更远的转向点；它不会因为经过合力为零的位置就停止。

严格给定 $\theta(0)=0$ 且 $\dot\theta(0)=0$，光滑动力学方程的唯一解是永远停在中央，即使中央不稳定。题目“初始速度近似为零”应按极小扰动后离开中央、初始能量趋于 $U(0)$ 的极限理解。上式是位置与速度的能量关系，并不保证严格静止的活塞自行启动。

### 12　低温与临界点的其他极限

在 $\tau\to0^+$ 时，正平衡根接近端点。令 $\theta_0=\pi/2-\epsilon$，则

$$\tau\simeq\frac{8\epsilon}{\pi^2},\qquad
\epsilon\simeq\frac{\pi^2}{8}\tau.$$

每个非零温度都仍有有限的气柱体积；$T=0$ 本身不再适合照搬经典理想气体的等温模型。这个渐近式只说明完整平衡方程在小正温度比下的数学行为。

临界点的小振幅运动满足 $\ddot\theta+\alpha\theta^3=0$，$\alpha=gc/r$。振幅 $A$ 下的第一积分是

$$\dot\theta^2=\frac\alpha2(A^4-\theta^4).$$

周期因而为

$$\mathcal T=\frac{4\sqrt2}{A\sqrt\alpha}
\int_0^1\frac{dx}{\sqrt{1-x^4}}.$$

周期随 $A^{-1}$ 增大；角频率与振幅成正比。它解释了为何临界点稳定，却没有与振幅无关的非零线性频率。

## 六、关键洞察

临界温度由两种线性斜率相消决定，非线性项决定临界点的稳定性。低温的平衡位置和微振动频率来自同一个局部四次势能，二者的平方根规律及频率的 $\sqrt2$ 比例可以互相校验。

## 七、易错点

混淆管的截面与圆环半径；遗漏压力乘面积后面积消去；临界点只保留一次项；把 $\omega=0$ 判成中性平衡；在非中央平衡频率中漏用平衡条件消去 $T$；把等温气体内能当成活塞压强力的势能；忽略从严格静止的不稳定点不能自动出发。

## 八、课堂讲解建议

先画一条沿圆弧的受力图，用符号判断压力差与重力的方向，再逐层展开完整方程。将“平衡条件”“稳定性条件”“运动转向条件”并排比较：分别为 $U'=0$、$U''>0$（临界时看高阶）、$E=U$。让学生说明三者为何不能相互替代。

## 九、变式训练

### 变式1　临界四次振子的周期

$T=T_c$，活塞从小角度 $A>0$ 处静止释放。求最低阶的振动周期，并判断振幅减半后周期怎样变化。

解：临界方程为 $\ddot\theta=-\alpha\theta^3$，$\alpha=gc/r$。乘 $\dot\theta$ 积分得 $\dot\theta^2=\alpha(A^4-\theta^4)/2$。从中央到最大角度的四分之一周期为

$$\frac{\mathcal T}{4}=\sqrt{\frac2\alpha}\int_0^A
\frac{d\theta}{\sqrt{A^4-\theta^4}}
=\frac1A\sqrt{\frac2\alpha}\int_0^1\frac{dx}{\sqrt{1-x^4}}.$$

最后积分约为1.311，故 $\mathcal T\simeq7.42/(A\sqrt\alpha)$。振幅减半，周期约加倍。只在 $A\ll1$ 时可忽略五次及更高阶恢复力。

### 变式2　气体改为准静态绝热

两侧气体中央位置的温度为 $T_0$，随活塞运动满足 $pV^\gamma=$常量，$\gamma>1$。求中央线性稳定的临界温度和小振动频率。

解：中央压强 $p_0=nRT_0/(Sra)$。偏移后

$$p_L=p_0(1+\theta/a)^{-\gamma},\quad
p_R=p_0(1-\theta/a)^{-\gamma}.$$

展开得 $S(p_L-p_R)\simeq-2\gamma nRT_0\theta/(ra^2)$。故

$$\ddot\theta=\left(\frac gr-\frac{8\gamma nRT_0}{\pi^2mr^2}\right)\theta.$$

临界温度为 $T_{0c}=\pi^2mgr/(8\gamma nR)=T_c/\gamma$，稳定侧频率平方为 $8\gamma nRT_0/(\pi^2mr^2)-g/r$。绝热压强变化更陡，达到同样恢复斜率所需的中央温度更低。

### 变式3　两侧气体量略不相等

左侧为 $n(1+\varepsilon)$ 摩尔，右侧为 $n(1-\varepsilon)$ 摩尔，$|\varepsilon|\ll1$；温度高于 $T_c$，离临界点不太近。求中央附近的平衡角到 $\varepsilon$ 的一阶。

解：气体切向合力为

$$\frac{nRT}{r}\left[\frac{1+\varepsilon}{a+\theta}
-\frac{1-\varepsilon}{a-\theta}\right]
\simeq\frac{2nRT\varepsilon}{ra}-\frac{2nRT\theta}{ra^2}.$$

令合力为零并用临界温度消元：

$$\boxed{\theta_{\rm eq}\simeq
\frac{\pi}{2}\frac{T/T_c}{T/T_c-1}\varepsilon.}$$

左侧气体多时平衡向右偏移。近临界点分母很小，线性式会失效；使用它还须满足所得 $|\theta_{\rm eq}|\ll1$，并使三次恢复力小于线性恢复力。

### 变式4　低温势垒与初速度

温度比为 $\tau=1-\delta$，$0<\delta\ll1$。活塞在一个稳定位置获得朝中央的初始角速度。求刚能跨越中央势垒所需角速度的最低阶。

解：用 $U/(mgr)=-\delta\theta^2/2+c\theta^4/4$，稳定角为 $\theta_0^2=\delta/c$。稳定位置的势能为 $U(\theta_0)=-mgr\delta^2/(4c)$，中央势能为零。临界初始动能等于势垒高度，因此

$$\frac12mr^2\Omega^2=\frac{mgr\delta^2}{4c},\qquad
\boxed{\Omega=\delta\sqrt{\frac{g}{2cr}}.}$$

等号对应渐近接近中央的不稳定轨道；真正越过中央须略大于这个速度。这个阈值随温差成一次比例，和局部微振动频率的平方根比例不同。


还可用势垒顶附近的动力学检查等号的含义。在中央附近，线性不稳定方程为

$$\ddot\theta=\lambda^2\theta,\qquad
\lambda=\sqrt{\frac{g\delta}{r}}.$$

临界能量轨道向中央靠近时 $\dot\theta\simeq-\lambda\theta$，所以

$$\theta(t)\simeq C e^{-\lambda t}.$$

它需要无限长时间才能到达严格的 $\theta=0$。相同结论可从时间积分 $dt\simeq-d\theta/(\lambda\theta)$ 的对数发散看出。初速度恰等于阈值时，活塞不在有限时间跨到另一势阱；略大于阈值才有真正的跨越轨道。

若给的是切向速度 $v$ 而非角速度，必须先用 $v=r\Omega$ 转换，阈值切向速度为 $v_{\rm th}=\delta\sqrt{gr/(2c)}$。速度和角速度的量纲不能在代入动能时混用。

