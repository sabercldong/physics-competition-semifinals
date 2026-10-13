# 第 4 题　随圆环转动的铰接细杆（60分）

匀质刚性细杆长$2a$、质量$m$，一端小孔嵌套在半径$R$的水平圆环的固定点$P$。$P$随圆环绕中心竖直轴以恒定角速度$\omega$转动；杆同时可绕$P$无摩擦转动，且杆与矢径$OP$始终在同一竖直平面内。杆与竖直向上方向的夹角为$\theta$，由竖直向上转向径向外侧的方向为正，重力加速度$g$。

![图4a　几何、角度和质心位置](../figures/q4-rod.png)

（1）将所有保守力的功与势能变化联系，分别在实验室系$L$和随$OP$转动的系$S$写出杆的机械能，可含$\theta$。

（2）在$S$中导出平衡位形满足的条件。

（3）用图解法分析各象限可能的平衡数目及$a,R,\omega$的条件。四象限依次为$[0,\pi/2)$、$[\pi/2,\pi)$、$[\pi,3\pi/2)$、$[3\pi/2,2\pi)$。

（4）在$S$中分象限画出对$P$点力矩有贡献的受力图，分布力可用力矩等效力示意，检验（3）。

（5）讨论各平衡位形的稳定性。

## 一、题型定位

本题研究受几何约束的转动体系。杆在实验室中既绕竖直轴转，又在径向竖直平面内摆动；在随圆环转动的参考系中，只剩一个角坐标$\theta$。选择转动系能把平衡和稳定性统一为一个有效势能问题。

全题的主线是：几何质量积分、有效势能、平衡条件、图解计数、受力检验、势能曲率。前一环节的符号一旦错误，会传递到后面全部象限判断，因此应从质元位置出发，而不是把整根杆当作质点。

第三象限最复杂。杆向轴内侧、向下倾斜，部分质元可能越过中心轴，离心力的方向也随质元所在侧改变。杆足够长、转速足够大时，第三象限可新增一对平衡；两者在临界参数处合并。

## 二、知识点

### 1. 质元位置和转动惯量

以从$P$沿杆的距离$s$标记质元，$0\leq s\leq2a$，质量元$dm=m\,ds/(2a)$。令$\varrho$为相对于中心轴的有向径向坐标，则

$$
\varrho(s)=R+s\sin\theta,\qquad z(s)=s\cos\theta.
$$

$\varrho<0$表示质元越到轴的另一侧；到轴的距离应为$|\varrho|$。动能和离心势能均用$\varrho^2$，因此可统一使用有向坐标。

杆对$P$的摆动转动惯量

$$
I_P=\int s^2dm=\frac43ma^2.
$$

对中心竖直轴的转动惯量

$$
I_z(\theta)=\int(R+s\sin\theta)^2dm
=m\left(R^2+2Ra\sin\theta+\frac43a^2\sin^2\theta\right).
$$

这两个惯量对应不同运动，不能用同一个$I$代替。

### 2. 恒定转动系的惯性力

离心力元为$\omega^2\varrho\,dm$，方向沿有向径向。其势能可取

$$
U_c=-\frac12\omega^2 I_z.
$$

科里奥利力与相对速度垂直，不做功。杆的相对运动在径向竖直平面内，科里奥利力沿方位方向，由维持平面约束的反力平衡，它不进入$\theta$的广义力。

圆环角速度恒定，欧拉惯性力为零。因此$S$系中的有效势能不显含时间，相关机械能可守恒。实验室中则存在驱动圆环维持$\omega$的外部做功，写出机械能表达式不等于证明它守恒。

### 3. 一维平衡与稳定判据

运动方程为

$$
I_P\ddot\theta=-U'(\theta).
$$

平衡$\theta_E$满足$U'(\theta_E)=0$。若$U''(\theta_E)>0$，小扰动产生恢复力矩；若小于零，扰动增长。二阶导数为零时需考察三阶或四阶项。

## 三、物理图像

竖直向上为$\theta=0$，径向向外水平为$\pi/2$，竖直向下为$\pi$，径向向内水平为$3\pi/2$。这一约定与通常从竖直向下量摆角的单摆不同，所以重力势能是$+mga\cos\theta$。

第一象限中，重力和离心力对$P$的力矩都使$\theta$增大，不可能抵消。第二象限杆向外且向下，重力倾向回到竖直向下，离心力倾向向外水平，两者可以形成稳定平衡。

第四象限杆向内且向上，存在一个力矩抵消点，但两侧力矩都把杆推离它，因此不稳定。第三象限中，需要足够强的向内离心力矩才能与重力抵消；短杆没有这种能力，长杆可能有两个平衡。

有效势能包含$\sin\theta$的一次项和二次项。前者来自铰点偏离中心轴的距离$R$，打破了径向内外对称；后者来自整根杆的质量分布。第三象限的新增平衡由二次项与重力、偏置项的竞争决定。

## 四、解题入口

先写$I_z(\theta)$，随后把两个参考系的能量并列：

$$
E_L=\frac12I_P\dot\theta^2+\frac12I_z\omega^2+mga\cos\theta,
$$

$$
E_S=\frac12I_P\dot\theta^2-\frac12I_z\omega^2+mga\cos\theta.
$$

它们最明显的区别是竖直轴转动能在$L$中为正动能，在$S$中进入负的离心势能。其余几何项完全相同。

平衡方程先保留无分母形式，之后才改写成正切或余切：

$$
g\sin\theta+R\omega^2\cos\theta
+\frac43a\omega^2\sin\theta\cos\theta=0.
$$

使用$\tan\theta$前先检查$\cos\theta=0$的轴线位置，使用$\cot\theta$前先检查$\sin\theta=0$。本题$R>0,g>0,\omega>0$时，四条象限边界均不是平衡，不会丢掉边界解。

## 五、解析

### （1）实验室系中的动能与机械能

质元的速度有三个正交分量：径向$s\dot\theta\cos\theta$、竖直$-s\dot\theta\sin\theta$、方位$\omega(R+s\sin\theta)$。所以

$$
v^2=s^2\dot\theta^2+\omega^2(R+s\sin\theta)^2.
$$

积分即得

$$
K_L=\frac12I_P\dot\theta^2+\frac12I_z\omega^2.
$$

以圆环平面为重力势能零面，质心高$a\cos\theta$，重力势能为$mga\cos\theta$。因此

$$
\boxed{
\begin{aligned}
E_L={}&\frac23ma^2\dot\theta^2+mga\cos\theta\\
&+\frac12m\omega^2
\left(R^2+2Ra\sin\theta+\frac43a^2\sin^2\theta\right).
\end{aligned}}
$$

用质心平动加绕质心转动也能检验：质心动能为$m[a^2\dot\theta^2+\omega^2(R+a\sin\theta)^2]/2$；绕质心动能为$ma^2(\dot\theta^2+\omega^2\sin^2\theta)/6$。相加得到同样的系数。

### 转动系中的有效机械能

在$S$中只剩绕$P$的相对摆动，动能

$$
K_S=\frac12I_P\dot\theta^2=\frac23ma^2\dot\theta^2.
$$

重力和离心势能之和

$$
U(\theta)=mga\cos\theta-\frac12\omega^2I_z(\theta).
$$

所以

$$
\boxed{
\begin{aligned}
E_S={}&\frac23ma^2\dot\theta^2+mga\cos\theta\\
&-\frac12m\omega^2
\left(R^2+2Ra\sin\theta+\frac43a^2\sin^2\theta\right).
\end{aligned}}
$$

$-mR^2\omega^2/2$是常数，改变势能零点时可略去；求机械能表达式时保留便于与$E_L$比较。常数不能影响平衡、曲率和稳定性。

两系能量关系为$E_L-E_S=\omega^2I_z(\theta)$。$E_S$守恒时

$$
\frac{dE_L}{dt}=\omega^2\frac{dI_z}{dt}.
$$

实验室角动量的竖直分量为$L_z=\omega I_z$，维持转速的外力矩功率$\omega\,dL_z/dt$正好等于上式。这说明实验室机械能变化来自驱动装置。

### （2）平衡位形方程

对$U$求导：

$$
U'=-mga\sin\theta
-ma\omega^2\left(R+\frac43a\sin\theta\right)\cos\theta.
$$

平衡要求

$$
\boxed{
g\sin\theta+\omega^2
\left(R+\frac43a\sin\theta\right)\cos\theta=0}.
$$

对四条边界分别代入，广义力除以$ma$依次为$R\omega^2,g,-R\omega^2,-g$，均非零。故可在各开象限使用三角函数形式：

$$
-\tan\theta=A\sin\theta+B,\quad
A=\frac{4a\omega^2}{3g},\quad B=\frac{R\omega^2}{g}.
$$

另一等价形式是

$$
-\cot\theta=A'\cos\theta+B',\quad
A'=\frac{4a}{3R},\quad B'=\frac{g}{R\omega^2}.
$$

两组系数均为正。图解时不要把$A,B$当成可以分别任意变号的参数。

### （3）图解计数：第一、第二和第四象限

![图4b　正切曲线与正弦曲线的交点](../figures/q4-intersections.png)

第一象限中$-\tan\theta<0$，而$A\sin\theta+B>0$，没有交点。无分母式也显示三项均非负且至少一项正。

第二象限可用余切形式证明唯一性：$-\cot\theta$由0严格增至正无穷，$A'\cos\theta+B'$严格减小且有界。在$\pi/2$处前者低于后者，在$\pi$前则高于后者，所以恰有一个交点。

第四象限用正切形式最简单：$-\tan\theta$从正无穷严格降至0，$A\sin\theta+B$严格增加，在右端为$B>0$。因此也恰有一个交点。右曲线在左端可能为负，并不妨碍其与左曲线只交一次。

这里图形显示数目，单调性证明排除了“可能还有其他交点”的疑问。不同象限选择不同等价式，是为了使唯一性更容易看清。

### 第三象限：最大值与相切条件

定义差函数

$$
f(\theta)=-\tan\theta-A\sin\theta-B,
\qquad \pi<\theta<3\pi/2.
$$

其左端值趋近$-B<0$，右端趋于负无穷。若它的内部最大值大于0，有两个交点；等于0，有一个重合交点；小于0，无交点。

求导：

$$
f'=-\frac1{\cos^2\theta}-A\cos\theta.
$$

当$A\leq1$时，$f'$在第三象限为负，没有内部峰值，故无平衡。$A>1$时有唯一峰值角$\theta_0$：

$$
\cos^3\theta_0=-\frac1A,
\qquad \pi<\theta_0<3\pi/2.
$$

在峰顶相切时还须$f(\theta_0)=0$。代入$\cos^3\theta_0=-1/A$，可得

$$
B=\tan^3\theta_0=-A\sin^3\theta_0.
$$

利用$\sin^2\theta_0+\cos^2\theta_0=1$，

$$
\boxed{A^{2/3}=1+B^{2/3}}.
$$

这个等式自动要求$A>1$，无需额外附加一条重复条件。

### 用原始参数表述全部条件

令

$$
D=\left(\frac{4a}{3}\right)^{2/3}
-R^{2/3}-\left(\frac g{\omega^2}\right)^{2/3}.
$$

则

$$
\boxed{\begin{array}{c|c}
\text{象限}&\text{平衡位形数}\\ \hline
\mathrm I&0\\
\mathrm {II}&1\\
\mathrm {III}&0\ (D<0),\quad1\ (D=0),\quad2\ (D>0)\\
\mathrm {IV}&1
\end{array}}
$$

等价无量纲形式是

$$
\left(\frac{3R}{4a}\right)^{2/3}
+\left(\frac{3g}{4a\omega^2}\right)^{2/3}
\begin{cases}>1,&\mathrm{III}\text{无解},\\
=1,&\mathrm{III}\text{一个重合解},\\
<1,&\mathrm{III}\text{两个解}.
\end{cases}
$$

![图4c　第三象限平衡出现的参数边界](../figures/q4-boundary.png)

图中两坐标都是非负。要使第三象限出现两解，至少要有$4a/3>R$，并且转速足够大。若$4a/3\leq R$，无论多快旋转，第三象限均不出现平衡。若$4a/3>R$，临界转速满足

$$
\omega_c^2=
\frac{g}{[(4a/3)^{2/3}-R^{2/3}]^{3/2}}.
$$

总平衡数因此为2、3或4，其中临界总数3包含一个不稳定的退化平衡。

### （4）分布离心力的力矩与示意图

质元离心力为$dF_c=\omega^2(R+s\sin\theta)dm$，对$P$的广义力矩

$$
Q_c=\int_0^{2a}s\cos\theta\,dF_c
=ma\omega^2\left(R+\frac43a\sin\theta\right)\cos\theta.
$$

重力广义力矩$Q_g=mga\sin\theta$。铰接反力作用于$P$，不贡献关于$P$的力矩。

为了在图上准确代表$Q_c$，可在质心处画一个水平的“力矩等效力”

$$
F_\tau=m\omega^2\left(R+\frac43a\sin\theta\right),
$$

其力臂为$a\cos\theta$。这不是离心力的真实合力；真实合力为$m\omega^2(R+a\sin\theta)$，作用线位置一般不在质心。题目只要求力矩示意，明确两者差别可避免误用。

![图4d　各象限的重力与离心力矩等效示意](../figures/q4-forces.png)

第一象限中$\sin,\cos$均正，$Q_g,Q_c$均正，不能平衡。第二象限$\sin>0,\cos<0$，且$F_\tau>0$，两力矩相反，可以平衡。

第三象限$\sin<0,\cos<0$。短杆使$R+(4a/3)\sin\theta>0$，$Q_c<0$，与重力同向，不能平衡。足够长时该括号可为负，向内的力矩等效力产生$Q_c>0$，可能与重力抵消。是否恰好抵消仍由$D$决定，单凭等效力向内不能证明一定有平衡。

第四象限中$Q_g<0,\cos>0$，平衡点要求$F_\tau>0$，离心力矩为正。图中选取了这一可能平衡的方向；其他第四象限姿态若$F_\tau<0$，则两力矩同向，当然不处于平衡。

### （5）稳定性：先求统一曲率

二阶导数为

$$
U''=ma\left[-g\cos\theta+R\omega^2\sin\theta
-\frac43a\omega^2\cos2\theta\right].
$$

在平衡点，用$B=-\tan\theta_E-A\sin\theta_E$消去$B$，可化成

$$
\boxed{
U''(\theta_E)
=-\frac{mga}{\cos\theta_E}
(1+A\cos^3\theta_E)}.
$$

另一等价形式

$$
U''(\theta_E)
=\frac{mga\cos^2\theta_E}{\sin\theta_E}
(B-\tan^3\theta_E).
$$

第二式适合直接判断第二、第四象限；第一式适合第三象限与临界角的比较。

### 第二、第四象限

第二象限$\sin>0,\tan<0$，所以$B-\tan^3\theta_E>0$，曲率为正：

$$
\boxed{\mathrm{II}\text{的唯一平衡稳定}}.
$$

第四象限$\sin<0,\tan<0$，同一括号为正，但前因子为负，故

$$
\boxed{\mathrm{IV}\text{的唯一平衡不稳定}}.
$$

第二象限稳定点附近的小振动频率若需要，可由$\Omega^2=U''/I_P$得到。它是相对于转动系的摆动频率，不是圆环本身的$\omega$。

### 第三象限两平衡

设两平衡角按大小记$\theta_-<\theta_+$，峰顶角$\theta_0$在两者之间，满足$\cos^3\theta_0=-1/A$。

第三象限内$\cos\theta$由$-1$增到0，因此：

$$
\theta_-<\theta_0
\ \Longrightarrow\ 1+A\cos^3\theta_-<0
\ \Longrightarrow\ U''(\theta_-)<0;
$$

$$
\theta_+>\theta_0
\ \Longrightarrow\ 1+A\cos^3\theta_+>0
\ \Longrightarrow\ U''(\theta_+)>0.
$$

故

$$
\boxed{\mathrm{III}\text{较小角平衡不稳定，较大角平衡稳定}}.
$$

两个稳定点分别位于第二、第三象限，二者之间存在势垒；若初始能量足够高，杆可以越过不稳定平衡，不能仅用局部稳定性断言永远留在某一象限。

### 临界重合平衡

$D=0$时$\theta_E=\theta_0$，曲率为零。三阶导数为

$$
U'''=mga[\sin\theta+B\cos\theta+4A\sin\theta\cos\theta].
$$

利用平衡条件，

$$
U'''(\theta_0)
=3Amga\sin\theta_0\cos\theta_0\neq0.
$$

第三象限$\sin\theta_0,\cos\theta_0$都负，乘积为正。因此该点是有水平切线的势能拐点，不是极小值：

$$
\boxed{\mathrm{III}\text{临界重合平衡不稳定}}.
$$

在它附近，力矩的最低阶项为$-\tfrac12U'''(\theta_0)(\delta\theta)^2$，两侧都指向同一角度方向，因而不能把小扰动推回。

### 数量级与退化极限检查

$\omega\to0$时，平衡趋向重力单摆的$\theta=\pi$稳定、$\theta=0$不稳定。由于本题$R>0,\omega>0$，它们分别向第二、第四象限偏移，所以象限计数与零转速极限连续。

若$a$很小，$A$小，第三象限无解，只有一稳一不稳两个平衡。若转速很大，是否出现第二个稳定点取决于$4a/3>R$，这正是杆的分布质量足以跨过轴并产生反向离心力矩的几何条件。

将细杆错误简化成距铰点$a$的质点，会把$4a/3$替换成$a$，进而改变临界杆长、转速和稳定频率。因此本题必须保留转动惯量积分。

## 六、关键洞察

实验室能量和转动系有效能量描述不同的能量账目。恒定$\omega$由驱动装置维持，实验室机械能通常不守恒；转动系里的离心势能则使单自由度运动有守恒积分。

图解法的价值不是避开所有计算，而是把根的出现、合并与消失直接显示出来。第三象限的相切条件同时给出参数临界边界和零曲率条件，是平衡数量与稳定性之间的桥梁。

分布力的合力与力矩等效力不能混用。特别在杆跨轴时，真实合力甚至可能很小，但对铰点的力矩仍大。明确“图上等效的是哪个量”是建立模型的必要步骤。

### 临界点附近的两种尺度

固定$A>1$，令$B_c=(A^{2/3}-1)^{3/2}$，从两平衡一侧接近相切，即$B=B_c-\varepsilon$，$0<\varepsilon\ll1$。峰顶角$\theta_0$由$A$决定，不随$B$移动。差函数在峰顶附近展开为

$$
f(\theta_0+\xi)
=\varepsilon+\frac32A\sin\theta_0\,\xi^2
+O(\xi^3).
$$

由于$\sin\theta_0<0$，两个根的偏角为

$$
\xi_\pm\simeq\pm
\sqrt{\frac{2\varepsilon}{3A|\sin\theta_0|}}.
$$

所以两个平衡角的间距按$\varepsilon^{1/2}$趋零。根越接近，不是“稳定性完全相同”，而是一稳一不稳的曲率分别趋向零。

在根上$U''=mga\cos\theta_E\,f'(\theta_E)$，用$f'\simeq3A\sin\theta_0\,\xi$可得稳定点的曲率正比$\varepsilon^{1/2}$。因此相对摆动频率

$$
\Omega=\sqrt{\frac{U''}{I_P}}\propto\varepsilon^{1/4}.
$$

这说明接近临界参数时摆动越来越慢，但临界点本身并不是稳定极小值。课堂上可以先用分支图展示两根靠拢，再用这个展开解释为什么数值求根在临界附近更敏感。

另一种检查是直接求真实离心合力为零的姿态：$R+a\sin\theta=0$。此时力矩仍可为$ma\omega^2(a\sin\theta/3)\cos\theta$，一般不为零。分布力在两侧相互抵消合力，却保留对铰点的力偶效应，这个例子最能说明为何不能把离心力简单作用在质心。

## 七、易错点

从竖直向下量角却仍使用$mga\cos\theta$，会整体颠倒重力势能。把杆绕竖直轴的惯量写成$I_P$，会把$\theta$依赖丢掉，无法得到正确离心力矩。

将$\tan$方程平方得到四次式后直接数根，容易包含象限符号错误的伪根。除以$\cos\theta$后也应补查边界。

第三象限两个根都稳定、或都不稳定的判断通常来自没有在平衡条件下简化$U''$。临界点二阶导数零时直接称“中性稳定”，会漏掉非零三次项。

## 八、课堂讲解建议

建议分两课时。第一课时处理质元几何、两系能量和力矩；第二课时处理图解计数及稳定性。每个阶段都让学生独立检查一个极限：$\omega=0$、$a\to0$、临界相切。

画图时先标四象限和两条渐近线，再画正弦基线$B$与幅度$A$。第三象限从“不相交—相切—两交点”三幅图建立参数变化的直觉，然后推导$A^{2/3}=1+B^{2/3}$。

受力图应在推导后用来核验符号。对于第三象限，要求学生把离心力矩因子$R+(4a/3)\sin\theta$写在图旁，避免只凭杆跨轴与否作过强结论。

## 九、变式训练

### 变式1　给定无量纲参数的全部平衡

取$A=3,B=0.6$，求四象限平衡数量，并用数值法给出平衡角和稳定性。

**解答：**$A^{2/3}\approx2.080$，$1+B^{2/3}\approx1.711$，第三象限两解，总共四解。求解$\sin\theta+B\cos\theta+A\sin\theta\cos\theta=0$，角度约为$106.0^\circ,197.9^\circ,244.7^\circ,351.4^\circ$。第二象限和第三象限较大角稳定；第三象限较小角和第四象限不稳定。数值只是图解法的校验，正式判据仍由参数和曲率给出。

### 变式2　给定杆长求临界转速

设$a=R$，求出现第三象限双平衡的临界$\omega$，以$\sqrt{g/R}$为单位。

**解答：**由于$4a/3>R$，存在有限临界转速。

$$
\frac{\omega_c}{\sqrt{g/R}}
=\left[(4/3)^{2/3}-1\right]^{-3/4}
\simeq3.21.
$$

$\omega>\omega_c$时第三象限两个平衡；等号时一个不稳定拐点；小于时无平衡。不能把“杆长$2a>R$”当作充分条件，转速还需达到临界值。

### 变式3　弱旋转下的角度偏移

当$R\omega^2/g\ll1$、$a\omega^2/g\ll1$时，求稳定平衡相对竖直向下的偏角。

**解答：**令$\theta=\pi-\varepsilon$，$\varepsilon>0$小。代入平衡方程并保留一阶角度项：

$$
g\varepsilon-R\omega^2-\frac43a\omega^2\varepsilon=0.
$$

所以$\varepsilon\simeq R\omega^2/[g-(4a/3)\omega^2]$。若只保留转速的最低非零阶，则$\varepsilon\simeq R\omega^2/g$。分母表达式是在小角线性化下得到的，接近分母零点时小角假设失效，不可把其发散当作真实角度发散。

### 变式4　铰点位于中心轴

改成$R=0$，仍保持杆在随转动的某个竖直平面中，讨论平衡与稳定性。

**解答：**平衡条件为

$$
\sin\theta\left[g+\frac43a\omega^2\cos\theta\right]=0.
$$

始终有$\theta=0,\pi$。上竖直不稳定；下竖直曲率$mga[1-A]$，$A=4a\omega^2/(3g)$，在$A<1$时稳定、$A>1$时不稳定。$A>1$还存在$\cos\theta=-1/A$的两解，分别在第二、第三象限，曲率$mga(A-1/A)>0$，均稳定。

在$A=1$时，下竖直的二阶项为零，但展开得$U(\pi+\varepsilon)-U(\pi)=mga\,\varepsilon^4/8+O(\varepsilon^6)$，仍是平坦的稳定极小值。它与原题$R>0$时非零三次项的临界拐点不同。这个变式强调二阶导数为零必须继续展开，结论不能照搬。
