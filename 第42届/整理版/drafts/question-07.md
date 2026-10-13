# 第 7 题　自聚焦光纤中的三维光线与椭圆投影

圆柱形自聚焦光纤的对称轴为 $z$ 轴，采用柱坐标
$(\rho,\theta,z)$。折射率随离轴距离增大而减小：
$$
n(\rho)=n_0\sqrt{1-\alpha^2\rho^2},
$$
其中 $\alpha,n_0>0$，$\rho$ 足够小。光线为三维空间曲线，参数形式
$\rho=\rho(z),\theta=\theta(z)$。光纤截面半径足够大，轨迹始终不到圆柱侧面。

（1）导出 $\rho(z),\theta(z)$ 满足的微分方程。

（2）在 $z=0$ 处有
$$
\rho(0)=\rho_0,\quad \rho'(0)=k_1>0,\quad
\theta(0)=0,\quad\theta'(0)=k_2>0.
$$
撇号表示对 $z$ 求导。求以后传播的最大离轴距离
$\rho_{\max}$。

（3）在相同初始条件下，求直角坐标轨迹 $x(z),y(z)$。本题45分。

![图7-1　渐变折射率使光线持续弯曲，三维轨迹无需依靠侧面反射。](../figures/q7-fiber.png)

## 一、题型定位

折射率连续变化，光线方向也沿传播路径连续改变。沿 $z$ 平移和绕轴旋转的对称性给出两个不变量，能将径向问题化为一维转折点方程。

给定折射率的平方恰好是 $\rho^2$ 的线性函数，因此直角坐标中的光线方程最终成为同频谐振方程。求最大半径既可以从径向首次积分选根，也可以从横截面椭圆的长半轴计算。

## 二、知识点

- 光线切矢量、弧长与柱坐标几何。
- 费马原理、欧拉方程及循环坐标。
- 平移、旋转对称性对应的不变量。
- 径向转折点、二次方程的根筛选。
- 直角坐标谐振解、初始位置与斜率匹配。
- 横截面椭圆、轴心不可达与角度连续性。
- 精确给定模型与近轴近似的区别。

## 三、物理图像

折射率在轴心最大，向外降低，光线偏折趋势指向折射率较高的轴心。同时光线可以具有绕轴的切向传播分量，因此未必穿过轴线，而可能在两个非零半径之间往复。

初始 $\rho'>0$ 表示起初向外，初始 $\theta'>0$ 表示绕轴方向已确定。横截面投影不是一般意义上的圆：径向斜率与绕轴斜率不同，会产生椭圆；轴向传播使这一椭圆投影变为空间曲线。

## 四、解题入口

定义沿 $z$ 参数化的弧长因子
$$
w=\frac{ds}{dz}=\sqrt{1+\rho'^2+\rho^2\theta'^2}.
$$
光程泛函为 $\int n(\rho)w\,dz$。从费马原理先得到
$n/w=\beta$ 与 $\rho^2\theta'=\ell$ 两个常数，其中
$$
\beta=n_0\sqrt{\frac{1-\alpha^2\rho_0^2}
{1+k_1^2+\rho_0^2k_2^2}},\qquad
\ell=\rho_0^2k_2.
$$
最大半径满足 $\rho'=0$。直角坐标路线则直接用同一常量
$\beta$，避免在转折点除以 $\rho'$ 造成不必要的歧义。

## 五、解析

（1）弧长及费马原理的拉氏函数。

光线位置矢量为
$$
\mathbf r(z)=\rho\cos\theta\,\mathbf e_x+
\rho\sin\theta\,\mathbf e_y+z\,\mathbf e_z.
$$
求导：
$$
\mathbf r'=(\rho'\cos\theta-\rho\theta'\sin\theta)\mathbf e_x
+(\rho'\sin\theta+\rho\theta'\cos\theta)\mathbf e_y+\mathbf e_z.
$$
平方后交叉项抵消，得到
$$
|\mathbf r'|^2=1+\rho'^2+\rho^2\theta'^2.
$$
因此光程的拉氏函数是
$$
L=n(\rho)\sqrt{1+\rho'^2+\rho^2\theta'^2}=nw.
$$
不需要先假设 $\rho',\rho\theta'$ 很小；以下计算对题给
$n(\rho)$ 的几何光学模型保留完整弧长。

（2）从旋转对称性求角向不变量。

$L$ 不显含 $\theta$，欧拉方程给
$$
\frac{d}{dz}\frac{\partial L}{\partial\theta'}=0,
\qquad
\frac{\partial L}{\partial\theta'}
=\frac{n\rho^2\theta'}w.
$$
所以
$$
\frac{n\rho^2\theta'}w=J_{\rm opt}=\text{常数}.\tag{7.1}
$$
这里的常量是光线变分问题中的广义动量，不是物体的机械角动量，但对应同样的旋转对称性。

（3）从轴向平移对称性求另一不变量。

$L$ 不显含 $z$，故
$$
\rho'\frac{\partial L}{\partial\rho'}
+\theta'\frac{\partial L}{\partial\theta'}-L
=\text{常数}.
$$
左边为
$$
\frac{n(\rho'^2+\rho^2\theta'^2)}w-nw
=-\frac nw.
$$
于是可以取正常数
$$
\boxed{\frac{n(\rho)}{\sqrt{1+\rho'^2+\rho^2\theta'^2}}
=\beta>0.}\tag{7.2}
$$
把式（7.1）除以 $\beta$：
$$
\boxed{\rho^2\theta'=\ell=\text{常数}.}\tag{7.3}
$$
这也等价于
$$
\rho\theta''+2\rho'\theta'=0
$$
（$\rho>0$）。它说明半径较小时角向斜率较大，但并不代表光速改变为该角向斜率。

（4）写出径向完整微分方程。

径向欧拉方程
$$
\frac{d}{dz}\left(\frac{n\rho'}w\right)
=n_\rho w+\frac{n\rho\theta'^2}{w}.
$$
用 $n/w=\beta$ 为常数，得
$$
\beta\rho''=n_\rho w+\beta\rho\theta'^2.
$$
又
$$
\frac{n_\rho}{n}
=-\frac{\alpha^2\rho}{1-\alpha^2\rho^2},
$$
所以第（1）问可写为两条局部方程：
$$
\boxed{
\begin{aligned}
\rho''-\rho\theta'^2
&=-\frac{\alpha^2\rho}{1-\alpha^2\rho^2}
(1+\rho'^2+\rho^2\theta'^2),\\
\rho\theta''+2\rho'\theta'&=0.
\end{aligned}}\tag{7.4}
$$
也可用角向方程与式（7.2）的常量关系作为等价的首次积分形式。第一式右端径向力总指向轴心，左端保留柱坐标中的几何项。

（5）由初始条件确定所有常量。

记
$$
D_0=1+k_1^2+\rho_0^2k_2^2,\qquad
q_0=1-\alpha^2\rho_0^2.
$$
为使给定折射率为实且非零，初始点需 $q_0>0$。初始条件直接给
$$
\boxed{\beta=n_0\sqrt{\frac{q_0}{D_0}},
\qquad \ell=\rho_0^2k_2.}\tag{7.5}
$$
定义
$$
\kappa=\frac{n_0\alpha}{\beta}
=\alpha\sqrt{\frac{D_0}{q_0}},
\qquad
A=\frac{n_0^2}{\beta^2}-1.
$$
$\kappa$ 的单位为长度的倒数，$A$ 无量纲，$\ell$ 的单位为长度。注意原题 $k_1=\rho'$ 无量纲，而 $k_2=\theta'$ 的单位为长度的倒数；二者不能直接相加。

（6）径向首次积分与转折半径。

式（7.2）平方后代入 $n^2=n_0^2(1-\alpha^2\rho^2)$：
$$
1+\rho'^2+\rho^2\theta'^2
=\frac{n_0^2}{\beta^2}(1-\alpha^2\rho^2).
$$
使用 $\theta'=\ell/\rho^2$，得到
$$
\boxed{\rho'^2=A-\kappa^2\rho^2-\frac{\ell^2}{\rho^2}.}\tag{7.6}
$$
在径向转折点 $\rho'=0$，令 $u=\rho^2$：
$$
\kappa^2u^2-Au+\ell^2=0.
$$
两根
$$
u_\pm=\frac{A\pm\sqrt{A^2-4\kappa^2\ell^2}}{2\kappa^2}.
$$
由于初始 $k_1>0$，初始半径位于两转折点之间、首先向外到达较大根。因此
$$
\boxed{\rho_{\max}=
\sqrt{\frac{A+\sqrt{A^2-4\kappa^2\ell^2}}
{2\kappa^2}}.}\tag{7.7}
$$
相应最小半径为 $\rho_{\min}=\sqrt{u_-}$。对于通常的
$\rho_0>0,k_2>0$，$\ell>0$，故 $u_->0$，光线不穿过轴心。

若不引入 $A,\kappa$，结果也可写为
$$
\rho_{\max}^2=
\frac{n_0^2-\beta^2+
\sqrt{(n_0^2-\beta^2)^2-4n_0^2\alpha^2\beta^2\ell^2}}
{2n_0^2\alpha^2}.
$$
保留平方根外的再开方很重要，二次方程求得的是半径平方。

（7）转折点实数性与折射率范围。

由初始式（7.6）
$$
A=k_1^2+\kappa^2\rho_0^2+\frac{\ell^2}{\rho_0^2}
>2\kappa\ell
$$
（$\rho_0>0$）。最后一步使用正量的算术—几何平均不等式，而 $k_1^2>0$ 保证严格不等。因此判别式严格为正，两转折半径不同。

同时式（7.2）要求
$n^2=\beta^2(1+\rho'^2+\ell^2/\rho^2)\ge\beta^2>0$，所以
$$
\alpha^2\rho^2\le1-\frac{\beta^2}{n_0^2}<1.
$$
轨迹始终位于给定实折射率区域。题设光纤侧面不可达，还需实际截面半径大于 $\rho_{\max}$；“转折点存在”与“没有碰到侧面”是两项不同的几何条件。

（8）直角坐标中直接推导谐振方程。

换成 $x,y$，
$$
L=n(x,y)\sqrt{1+x'^2+y'^2},
\qquad n^2=n_0^2[1-\alpha^2(x^2+y^2)].
$$
仍有 $n/\sqrt{1+x'^2+y'^2}=\beta$。欧拉方程为
$$
\frac{d}{dz}(\beta x')=n_x\sqrt{1+x'^2+y'^2}.
$$
因为
$$
n_x=-\frac{n_0^2\alpha^2x}{n},\qquad
\sqrt{1+x'^2+y'^2}=\frac n\beta,
$$
所以
$$
\beta x''=-\frac{n_0^2\alpha^2}{\beta}x.
$$
同理对 $y$，得到
$$
\boxed{x''+\kappa^2x=0,\qquad
y''+\kappa^2y=0.}\tag{7.8}
$$
此推导没有除以 $\rho'$ 或 $x$，因此在径向转折点、坐标过零时都可连续使用。它也说明谐振不是将 $n$ 草率当作常数的结果，而来自题给 $n^2$ 的特殊二次形式。

（9）匹配初始位置和斜率。

由 $\theta(0)=0$：
$$
x(0)=\rho_0,\qquad y(0)=0.
$$
柱坐标求导给
$$
x'=\rho'\cos\theta-\rho\theta'\sin\theta,\qquad
y'=\rho'\sin\theta+\rho\theta'\cos\theta.
$$
初始斜率为
$$
x'(0)=k_1,\qquad y'(0)=\rho_0k_2.
$$
分别匹配谐振解的余弦、正弦系数：
$$
\boxed{x(z)=\rho_0\cos(\kappa z)
+\frac{k_1}{\kappa}\sin(\kappa z),}\tag{7.9}
$$
$$
\boxed{y(z)=\frac{\rho_0k_2}{\kappa}\sin(\kappa z),\qquad
\kappa=\alpha\sqrt{\frac{1+k_1^2+\rho_0^2k_2^2}
{1-\alpha^2\rho_0^2}}.}\tag{7.10}
$$
位置及两条初始斜率全部满足。$n_0$ 消去，说明在同样初始几何条件下，将整个折射率曲线乘一个常数不改变光线空间轨迹，只会改变传播时间。

（10）用横截面椭圆复求最大半径。

设 $B=k_1/\kappa$，$C=\rho_0k_2/\kappa$，$u=\kappa z$。轨迹可写成
$$
\begin{pmatrix}x\\y\end{pmatrix}
=
\begin{pmatrix}\rho_0&B\\0&C\end{pmatrix}
\begin{pmatrix}\cos u\\\sin u\end{pmatrix}.
$$
当 $u$ 变化时，单位圆在线性变换下成为中心在轴心的椭圆。半径平方为
$$
\rho^2=\rho_0^2\cos^2u+2\rho_0B\sin u\cos u
+(B^2+C^2)\sin^2u.
$$
最大、最小值是对称矩阵
$$
G=
\begin{pmatrix}
\rho_0^2&\rho_0B\\
\rho_0B&B^2+C^2
\end{pmatrix}
$$
的两个特征值。因而
$$
\boxed{\rho_{\max}^2=
\frac{\rho_0^2+B^2+C^2+
\sqrt{(\rho_0^2-B^2-C^2)^2+4\rho_0^2B^2}}2.}\tag{7.11}
$$
$\operatorname{tr}G=A/\kappa^2$，
$\det G=\ell^2/\kappa^2$，代回特征值公式，正好恢复式（7.7）。两种路线一个从径向守恒量出发，一个从完整轨迹的椭圆几何出发。

![图7-2　横截面投影为椭圆，最大和最小离轴距离等于长、短半轴。](../figures/q7-ellipse.png)

（11）角度连续性、周期与螺旋特征。

若需要恢复柱坐标角，
$$
\theta(z)=\operatorname{atan2}(y(z),x(z))
$$
并沿轨迹连续展开角度。不能只用 $\arctan(y/x)$，否则在跨象限时丢失 $\pi$ 的变化。因为
$$
xy'-yx'=\rho_0C\kappa=\rho_0^2k_2=\ell>0,
$$
角度始终正向增加。径向距离则在 $\rho_{\min},\rho_{\max}$ 之间变化。

$x,y$ 的完整重复周期为 $2\pi/\kappa$；半径平方周期为
$\pi/\kappa$，因为横截面半周后坐标整体变号而半径相同。一般空间轨迹不是等半径的圆螺旋，只有特殊初始斜率才产生圆形横截面投影。

若 $\rho_0=0$，柱坐标角在轴心没有通常的唯一意义，应从式（7.9）、（7.10）的直角坐标极限处理。此时 $y=0$，光线可穿越轴线，不能继续使用 $\ell>0$ 的不穿轴论证。

（12）近轴极限与均匀介质极限。

当 $\alpha\rho_0\ll1$ 且
$k_1^2+\rho_0^2k_2^2\ll1$，
$$
\kappa\simeq\alpha.
$$
于是近轴轨迹周期近似为 $2\pi/\alpha$，对初始斜率的依赖仅在更高阶。这是额外近轴近似的结果，不能在一般初始条件下把精确的 $\kappa$ 无条件替换为 $\alpha$。

若 $\alpha\to0$，折射率趋于均匀，利用
$\sin(\kappa z)/\kappa\to z$：
$$
x\to\rho_0+k_1z,\qquad y\to\rho_0k_2z.
$$
恢复直线传播。此时有初始横向斜率的光线没有有限的径向回转尺度，不能把式（7.7）在 $\kappa=0$ 处直接代入并宣称仍有有限最大半径。

（13）从同一轨迹求轴向周期的传播时间。

光在局部介质的速度为 $c/n$，故
$$
\frac{dt}{dz}=\frac nc\frac{ds}{dz}
=\frac{n^2}{\beta c}
=\frac{n_0^2}{\beta c}(1-\alpha^2\rho^2).
$$
一个轴向轨迹周期 $Z_{\rm per}=2\pi/\kappa$ 内，
$$
\langle\rho^2\rangle_z=
\frac12(\rho_0^2+B^2+C^2)=\frac{A}{2\kappa^2}.
$$
于是平均时间梯度为
$$
\boxed{\frac{\Delta t}{Z_{\rm per}}
=\frac{n_0^2+\beta^2}{2\beta c}.}\tag{7.12}
$$
这是给定几何光学模型下的补充结果。它说明空间轨迹的 $n_0$ 消去，不代表传播时间也与 $n_0$ 无关。对轨迹重复周期求平均时，积分变量是轴向坐标 $z$，不能误把它当实际弧长。

（14）将一组初始条件同时代入两种最大半径算法。

为便于核对，选任意长度单位 $L$，取
$$
\alpha=0.6/L,\quad \rho_0=0.35L,\quad
k_1=0.18,\quad k_2=0.7/L.
$$
径向斜率 $k_1=d\rho/dz$ 无量纲，角斜率 $k_2=d\theta/dz$ 的单位是长度的倒数。混淆它们的单位，会在 $\rho_0^2k_2^2$ 处立即出现量纲错误。

初始条件给
$$
q_0=1-\alpha^2\rho_0^2=0.9559,
\qquad D_0=1+k_1^2+\rho_0^2k_2^2=1.092425.
$$
于是
$$
\kappa=\alpha\sqrt{D_0/q_0}=0.641418/L,
\qquad B=0.280628L,\quad C=0.381966L.
$$
轨迹为
$$
\begin{aligned}
x/L&=0.35\cos(0.641418z/L)
+0.280628\sin(0.641418z/L),\\
y/L&=0.381966\sin(0.641418z/L).
\end{aligned}
$$
在 $z=0$ 直接求值和求导，恢复 $x=0.35L$、$y=0$、$x'=0.18$、$y'=0.245$。由 $\theta'=(xy'-yx')/\rho^2$ 再恢复 $k_2=0.7/L$，这同时检查了从柱坐标到直角坐标的初始条件转换。

第一种算法，把 $A=D_0/q_0-1$、$\ell=\rho_0^2k_2$ 代入径向转折点二次方程。第二种算法，对
$$
G=\begin{pmatrix}
\rho_0^2&\rho_0B\\
\rho_0B&B^2+C^2
\end{pmatrix}
$$
求两个特征值。两种算法均给
$$
\rho_{\min}=0.250737L,\qquad
\boxed{\rho_{\max}=0.533181L.}
$$
这两个数分别是椭圆的短、长半轴，不能把 $\max\{|x|,|y|\}$ 当作最大离轴距离。长轴一般不沿 $x$ 或 $y$ 轴，因为矩阵存在非零的混合项 $\rho_0B$。

模型有效范围也能直接检查：
$$
\alpha\rho_{\max}\approx0.319908<1.
$$
因此整个轨迹的折射率为实数。若实际光纤半径小于 $\rho_{\max}$，轨迹会遇到侧面，题设的无侧面作用模型便不能描述完整传播；这里的最大半径公式自身没有包含边界反射。

轴向坐标的完整轨迹周期为 $9.79578L$，径向周期为其一半。这个例子的 $n_0$ 尚未指定，但空间轨迹已经完全确定；给出 $n_0$ 后才可进一步计算传播时间。保留精确 $\kappa$ 得到的周期比近轴估计 $2\pi/\alpha$ 小，反映了有限初始斜率与离轴位置的修正。

## 六、关键洞察

旋转和平移对称性给出了角向与轴向不变量；这两项常量足以预测径向转折。特别的折射率平方形式进一步使横向直角坐标各自满足谐振方程。

把柱坐标守恒量与直角坐标椭圆对照，既能筛选最大半径的根，也能解释为什么一般光线不穿轴、半径周期比横向轨迹周期短一半。

## 七、易错点

- 弧长漏掉 $\rho^2\theta'^2$。
- 将折射率梯度视为突变界面，反复使用固定侧面反射。
- 未说明近轴条件就令 $ds/dz=1$。
- 把二次方程的 $\rho^2$ 根当成 $\rho$。
- 最大半径误取较小根。
- 以 $k_2$ 而非 $\rho_0k_2$ 作为初始 $y'$。
- 在转折点除以 $\rho'$，再把单点零值误判为整条轨迹分支。
- 使用单值 $\arctan(y/x)$ 导致跨象限角度不连续。
- 将一般椭圆投影当作等半径圆螺旋。

## 八、课堂讲解建议

先由弧长建立费马泛函，再从“没有显含 $\theta,z$”读出两个守恒量。径向方程要画出两个转折半径并解释根的选择。随后用直角坐标重新推导，不依靠对径向式作可能奇异的除法。

让学生逐项核对四个初始条件，并将 $\rho^2$ 写成二次型；长、短半轴与转折半径的等价可作为完整复核。最后讨论均匀介质极限，检查谐振轨迹如何连续变成直线。

## 九、变式训练

### 变式1　没有初始绕轴斜率

令 $k_2=0$，保持 $\rho_0>0,k_1>0$，求轨迹和最大半径。

**解答。** $\ell=0$，$\kappa=\alpha\sqrt{(1+k_1^2)/(1-\alpha^2\rho_0^2)}$。
初始 $y=y'=0$，故 $y$ 恒为零，
$$
x=\rho_0\cos\kappa z+\frac{k_1}{\kappa}\sin\kappa z.
$$
所以
$$
\boxed{\rho_{\max}=\sqrt{\rho_0^2+(k_1/\kappa)^2}.}
$$
光线可以穿过轴心，径向柱坐标为 $|x|$，过轴时角度需改变。原题 $\ell>0$ 的离心屏障在此消失。

### 变式2　寻找等半径圆螺旋

放宽原题 $k_1>0$，令 $k_1=0$，要求 $\rho(z)=\rho_0$ 恒定。求 $k_2$。

**解答。** 圆形投影要求 $x=\rho_0\cos\kappa z$、
$y=\rho_0\sin\kappa z$，即 $k_2=\kappa$。代入
$$
\kappa^2=\alpha^2\frac{1+\rho_0^2k_2^2}
{1-\alpha^2\rho_0^2},
$$
得到
$$
\boxed{k_2^2=\frac{\alpha^2}{1-2\alpha^2\rho_0^2}.}
$$
需 $\alpha\rho_0<1/\sqrt2$。这比折射率仅为实数的
$\alpha\rho_0<1$ 更严格，说明并非每个允许半径都能支持该等半径轨迹。

### 变式3　改变整体折射率标度

保持 $\alpha,\rho_0,k_1,k_2$ 不变，将 $n_0$ 加倍。问轨迹、最大半径、同一轴向段传播时间如何变化。

**解答。** $\beta$ 随 $n_0$ 加倍，故
$\kappa=n_0\alpha/\beta$ 不变。$\ell$ 不变，
$A=n_0^2/\beta^2-1$ 不变，因此 $x,y,\rho_{\max}$ 均不变。

但 $dt/dz=n^2/(\beta c)$ 中 $n^2$ 增为4倍、$\beta$ 增为2倍，所以传播时间加倍。几何轨迹由相对梯度决定，传播速度仍取决于绝对折射率。

### 变式4　用已知横向轨迹验证两个不变量

给出 $x=A_1\cos\kappa z+B_1\sin\kappa z$、
$y=A_2\cos\kappa z+B_2\sin\kappa z$。证明
$xy'-yx'$ 为常数，并求其值。

**解答。** 分别求导并代入，$\sin^2+\cos^2=1$，交叉项抵消：
$$
\boxed{xy'-yx'=\kappa(A_1B_2-A_2B_1).}
$$
它是横截面线性变换的行列式乘 $\kappa$，也是
$\rho^2\theta'$。若行列式非零，投影椭圆不退化且方向固定；若为零，轨迹投影退化为过轴直线。第二个不变量还需检验
$n^2=\beta^2(1+x'^2+y'^2)$，不能只凭常数面积率就断言任何谐振轨迹适合任意折射率。

