# 第 3 题　恒流电磁轨道炮的磁力、电压与能量（40 分）

电磁轨道炮的两圆柱形固定导轨平行，轴线所在平面与水平面夹角为$\theta$。两轨长均为$L$、半径均为$b$，每单位长度电阻均为$\lambda$，两轨最近距离为$d$，且$d$很小。质量为$m$的金属弹丸可视为薄片，直径为$d$、电阻为$R$，置于两轨之间并保持良好接触。两轨下端横截面共面，通过与导轨同轴且较长的硬导线接电流为$I$的理想恒流源，忽略源内部能量损耗。忽略空气阻力和摩擦，真空磁导率为$\mu_0$，重力加速度为$g$。弹丸从导轨下端静止出发，被磁场加速直至射出。

![图3a　斜置双导轨、电流闭合路径及弹丸位置](../figures/q3-rails.png)

（1）求弹丸加速过程中受到的磁场作用力。

（2）求弹丸的出射速度。

（3）求加速过程中任意时刻以及出射时刻恒流源两端的电压。

（4）求整个加速过程中恒流源做的功。

（5）当$\theta=0^\circ$且导轨和弹丸电阻均可忽略时，求出射动能与恒流源做功之比。

## 一、题型定位

这是一道磁场积分、动力学、变化回路感应与能量守恒的综合题。电流由理想恒流源维持，故电流不随弹丸运动而下降；但回路长度、导轨电阻、回路磁通与恒流源电压都随弹丸位置改变。

磁力计算最容易出现二倍错误。弹丸位于载流导轨的末端，每段导轨在弹丸处按半无限长直导线处理；回路内部的磁通主要由两侧长直导线场决定。这两处场的系数不同。最终可用磁力与电感梯度、源功与磁场储能之间的关系检验这个差别。

本题采用小轨隙下的长导线近似，忽略端部、引线固定部分和弹丸内部电流分布的细节。固定部分磁场能量不随弹丸位置变化，所以只需计算随轨道有效长度增加的那部分能量。

## 二、知识点

### 1. 导线端点的磁场

直导线的一般磁场可以从毕奥—萨伐尔积分得到。在垂直距离$q$处，若导线从端点向负方向无限延伸，

$$
B_{\rm end}
=\frac{\mu_0I}{4\pi}
\int_0^\infty\frac{q\,dz}{(q^2+z^2)^{3/2}}
=\frac{\mu_0I}{4\pi q}.
$$

积分原函数为$z/[q\sqrt{q^2+z^2}]$，两端相减给$1/q$。无限长导线把两侧半线贡献相加，得到

$$
B_{\rm long}=\frac{\mu_0I}{2\pi q}.
$$

不能因为导轨整体很长，就把弹丸所在端点也当成一条两侧都无限延伸的载流导线。

### 2. 分布场中的安培力

弹丸沿轨隙横向载流，取微小长度$dq$。微段磁力大小为

$$
dF=I B(q)\,dq.
$$

磁场强度随$q$变化，必须积分，不能取轨隙中点磁场再乘$d$。当$d/b$足够小，中点近似才给出同一结果的低阶展开。

### 3. 变化回路的电压

恒流源要克服两部分电压：回路电阻压降及回路磁通增加引起的反电动势。定义反电动势的正大小为$\mathcal E_b=d\Phi/dt>0$，有

$$
U=I R_{\rm loop}+\mathcal E_b.
$$

若把感应电动势作为沿电流方向的有符号量，则$\mathcal E_{\rm ind}=-d\Phi/dt$，相同方程写成$U+\mathcal E_{\rm ind}=IR_{\rm loop}$。两种写法一致，不可在中途把符号约定混用。

## 三、物理图像

图3b取导轨轴间距为$s=2b+d$。从左轨轴测量弹丸横向位置$q$，弹丸占据$b\le q\le b+d$。两条导轨电流方向相反，在轨隙内的磁场方向相同；弹丸微段的安培力都指向沿轨道的前方。

![图3b　横向积分区间、两个导线端点场与安培力](../figures/q3-field.png)

在回路内部，以长直导线场积分磁通。弹丸前进一小段$dx$，有效回路新增一个宽为$dx$、跨越轨隙的条带。这个新增条带使电感增加，因此恒流源除了提供弹丸运动所需机械功，还必须增加磁场能量。

![图3c　恒流源功的三个去向：焦耳热、机械能及磁能](../figures/q3-energy.png)

图中的机械能包含弹丸动能和重力势能。弹丸向上射出时，磁力做功不全变成动能；而恒流源做功又不全等于磁力做功。

## 四、解题入口

先定义只由几何决定的电感梯度

$$
\kappa_L=\frac{\mu_0}{\pi}\ln\frac{b+d}{b}.
$$

其单位为$\mathrm{H/m}$。磁力应为$F_B=\kappa_LI^2/2$，新增回路磁通应为$\Phi=\kappa_LIx$。这两条结果来自不同场的积分，可以相互做能量检验。

再令沿导轨向上为正，定义净加速度

$$
a_B=\frac{\kappa_LI^2}{2m}-g\sin\theta.
$$

如果$a_B\le0$，从下端静止出发的弹丸不能按题设向前射出，后面的出射时间与速度公式没有适用的运动分支。下文均取$a_B>0$。

## 五、解析

### （1）弹丸磁力的积分

在弹丸横向位置$q$，距右轨轴的距离为$s-q$。两个端点场相加，

$$
B_{\rm end}(q)=\frac{\mu_0I}{4\pi}
\left(\frac1q+\frac1{s-q}\right).
$$

弹丸的安培力为

$$
F_B=\frac{\mu_0I^2}{4\pi}
\int_b^{b+d}
\left(\frac1q+\frac1{s-q}\right)dq.
$$

分别积分：

$$
\int_b^{b+d}\frac{dq}{q}
=\ln\frac{b+d}{b},
$$

$$
\int_b^{b+d}\frac{dq}{s-q}
=-\ln(s-q)\bigg|_b^{b+d}
=\ln\frac{b+d}{b}.
$$

第二项中$s-(b+d)=b$、$s-b=b+d$，两项对称相等。所以

$$
\boxed{
F_B=\frac{\mu_0I^2}{2\pi}
\ln\left(1+\frac db\right)
=\frac12\kappa_LI^2}.
$$

方向沿导轨向上。对于固定电流及固定横向几何，这个磁力不依赖弹丸在轨道上的纵向位置。

小间隙展开为

$$
F_B=\frac{\mu_0I^2}{2\pi}
\left[\frac db-\frac12\left(\frac db\right)^2
+O\left((d/b)^3\right)\right].
$$

当$d\to0$，弹丸的横向载流长度趋于零，力也趋于零。这一极限同时检验积分上下限，没有把轴间距$2b+d$误当成弹丸长度。

### （2）加速度、速度与出射条件

弹丸沿轨道方向的重力分量为$-mg\sin\theta$。动力学方程为

$$
ma_B=F_B-mg\sin\theta.
$$

因此

$$
\boxed{
a_B=\frac{\mu_0I^2}{2\pi m}
\ln\left(1+\frac db\right)-g\sin\theta}.
$$

这是一恒定加速度。以开始运动为$t=0$，有

$$
x(t)=\frac12a_Bt^2,\qquad v(t)=a_Bt.
$$

出射位置$x=L$，对应

$$
\boxed{
T=\sqrt{\frac{2L}{a_B}},
\qquad
v_e=\sqrt{2a_BL}}.
$$

展开速度结果即

$$
\boxed{
v_e=\sqrt{2L\left[
\frac{\mu_0I^2}{2\pi m}\ln\left(1+\frac db\right)
-g\sin\theta\right]}}.
$$

当$0<\theta<\pi/2$时，电流必须超过

$$
I_{\rm crit}=
\sqrt{\frac{2mg\sin\theta}{\kappa_L}}.
$$

等于临界值时净力为零，静止弹丸不会自行走完整段；低于临界值时题设向上出射过程不能成立。

### 由机械能再核对出射速度

磁力做功为$F_BL$，弹丸上升高度$L\sin\theta$，于是

$$
\frac12mv_e^2+mgL\sin\theta=F_BL.
$$

代入$F_B=\kappa_LI^2/2$，得到

$$
\frac12mv_e^2
=\frac12\kappa_LI^2L-mgL\sin\theta.
$$

它与匀加速运动所得速度平方相同。电阻不会改变此处磁力和速度，是恒流源保持$I$不变的结果；电阻改变的是所需源电压和源功。

### （3）随位置变化的磁通

回路内部长直导线场为

$$
B_{\rm long}(q)=\frac{\mu_0I}{2\pi}
\left(\frac1q+\frac1{s-q}\right).
$$

在小轨隙、长回路近似下，长度$x$的轨道回路新增磁通是

$$
\begin{aligned}
\Phi(x)
&=x\int_b^{b+d} B_{\rm long}(q)\,dq\\
&=\frac{\mu_0Ix}{\pi}\ln\frac{b+d}{b}\\
&=\boxed{\kappa_LIx}.
\end{aligned}
$$

不变的引线磁通可以加上一个常量，它的时间导数为零，不影响本问。有效电感写成$\mathcal L(x)=\mathcal L_0+\kappa_Lx$，本题$I$恒定，故

$$
\boxed{\mathcal E_b=\frac{d\Phi}{dt}
=\kappa_LI\,v}.
$$

如果直接只算弹丸微段的动生电动势，末端场给出的那部分功率恰好对应磁力的机械功率；完整源电压还包含整个可变磁场的感应贡献。回路磁通法把这一贡献统一保留。

### 任意时刻的源电压

电流通过左右两轨各长$x$的部分，回路电阻为

$$
R_{\rm loop}(x)=R+2\lambda x.
$$

恒流源电压为

$$
\boxed{U(x,v)=I(R+2\lambda x)+\kappa_LIv}.
$$

代入$x=a_Bt^2/2$、$v=a_Bt$，

$$
\boxed{U(t)=IR+\lambda Ia_Bt^2+\kappa_LIa_Bt},
\qquad 0\le t\le T.
$$

起始电压为$IR$；随着回路长度和速度增长，导轨电阻压降与反电动势都增加。当$\lambda\ge0$时，

$$
\frac{dU}{dt}=2\lambda Ia_Bt+\kappa_LIa_B>0,
$$

所以最高电压出现在出射时：

$$
\boxed{
U_e=I(R+2\lambda L)+\kappa_LI\sqrt{2a_BL}}.
$$

理想恒流源不限制电压，才可以维持这种电流。若实际电源有电压上限，便应检查$U_e$，不能仅检查启动电压。

### （4）恒流源的总功

源功是

$$
W_s=\int_0^T U(t)I\,dt.
$$

分别积分三个功率项：

$$
W_R=I^2RT,
$$

$$
W_{\rm rail}=
\int_0^T\lambda I^2a_Bt^2\,dt
=\frac{\lambda I^2a_BT^3}{3},
$$

$$
W_{\rm flux}=
\int_0^T\kappa_LI^2a_Bt\,dt
=\frac12\kappa_LI^2a_BT^2.
$$

由$a_BT^2=2L$，

$$
W_{\rm flux}=\kappa_LI^2L,
\qquad
W_{\rm rail}=\frac23\lambda I^2LT.
$$

于是一个不含高次时间的结果为

$$
\boxed{
W_s=I^2T\left(R+\frac23\lambda L\right)
+\kappa_LI^2L}.
$$

其中$T=\sqrt{2L/a_B}$。轨道焦耳热之所以含$2\lambda L/3$，是因为两轨有效电阻随$x\propto t^2$增加，时间平均长度为$L/3$，而不是$L/2$。

### 源功为什么是磁力机械功的二倍再加焦耳热

固定电流下，有效回路磁场能量增加

$$
\Delta U_B=\frac12I^2[\mathcal L(L)-\mathcal L(0)]
=\frac12\kappa_LI^2L.
$$

磁力机械功为

$$
W_B=F_BL=\frac12\kappa_LI^2L.
$$

因此两个去向相等。总能量平衡为

$$
\boxed{
W_s=Q_J+\Delta U_B+\Delta K+\Delta U_g},
$$

其中

$$
Q_J=I^2T\left(R+\frac23\lambda L\right),
\qquad
\Delta K+\Delta U_g=F_BL.
$$

逐时刻也能核对：

$$
\begin{aligned}
UI
&=I^2(R+2\lambda x)+\kappa_LI^2v\\
&=P_J+\frac12\kappa_LI^2v+\frac12\kappa_LI^2v.
\end{aligned}
$$

后一对分别是$dU_B/dt$和$F_Bv$。若磁力也用了长直导线场，机械功率会多出二倍，无法同时满足这个平衡。

### （5）无电阻水平发射时的能量比例

当$\theta=0$、$R=\lambda=0$时，

$$
K_e=F_BL=\frac12\kappa_LI^2L,
$$

而源做功是

$$
W_s=\kappa_LI^2L.
$$

故

$$
\boxed{\frac{K_e}{W_s}=\frac12=50\%}.
$$

剩下的一半为有效回路增加的磁场能量，而非隐藏的电阻损耗。在弹丸出射前这一瞬间比较能量即可；出射以后回路怎样断开、磁能怎样回收或消耗，不在题给模型中。

无电阻也不意味着源电压为零。只要$v>0$，$U=\kappa_LIv>0$，源仍须对抗磁通增加产生的反电动势。

## 六、关键洞察

固定电流的可变电感系统满足$F=I^2(d\mathcal L/dx)/2$。源的非焦耳功率$I^2(d\mathcal L/dx)v$被机械功与磁能增量平分，二分之一来自磁场能量的$I^2\mathcal L/2$，不是某个经验“效率损失”。

恒流条件下，电阻不改变磁力和机械运动，却会改变电源所做的功。换成恒压驱动后，情况不同。恒压时电流随位置和速度改变，磁力不再是常量。

## 七、易错点

把$b$误当作轨道直径，会改变积分下限和对数。把$d$误当成轴间距，会改变整个磁场几何。两个端点场在轨隙中同向，应相加。

磁力位置的半无限场与回路内部的长导线场不能混用。源电压公式必须统一感应电动势符号。源功积分上限是运动时间$T$，不是轨道长度$L$；改用位置积分时要保留$dt=dx/v(x)$。

出射动能应先扣除重力势能。无电阻时源功仍大于机械功，不能把二者直接设成相等。

## 八、课堂讲解建议

先画横截面，把$b,q,s-q$与积分边界标明。推导完磁力暂不做电压，用动力学建立$a_B,T,v_e$，检查启动条件。

再从磁通条带转到源电压。最后画能量流程图，将焦耳热、机械能与磁场能量逐项列出。让学生用逐时刻功率闭合判别二倍系数，这比单纯记住“端点要除二”更有说服力。

## 九、变式训练

### 变式1　倾角与临界电流

给定$I$，求能够从静止向上发射的最大倾角；若要求出射速度至少为$v_{\min}$，条件怎样改变？

**解答：** 净加速度为$F_B/m-g\sin\theta$。从静止走完整段必须有

$$
\sin\theta<\frac{\kappa_LI^2}{2mg}.
$$

右侧小于1时，倾角严格小于其反正弦；右侧大于1时，所有$0\le\theta<\pi/2$均有正净加速度。等号不可称为能够从静止出射。

若要求$v_e^2\ge v_{\min}^2$，由能量或运动学，

$$
\boxed{
\sin\theta\le
\frac{\kappa_LI^2}{2mg}-\frac{v_{\min}^2}{2gL}}.
$$

右侧若为负，连水平发射也达不到规定速度；若$v_{\min}>0$，等号对应恰达到规定速度，此时净加速度仍为正。

### 变式2　电阻存在时的水平效率

取$\theta=0$，保留$R,\lambda$，求动能效率并分析电流增大时的趋势。

**解答：** 此时$a_B=\kappa_LI^2/(2m)$，故

$$
T=\frac{2\sqrt{mL/\kappa_L}}{I}.
$$

动能$K_e=\kappa_LI^2L/2$，源功等于$\kappa_LI^2L+I^2T(R+2\lambda L/3)$。所以

$$
\boxed{
\eta=\frac1{2\left[
1+\dfrac{T(R+2\lambda L/3)}{\kappa_LL}\right]}}.
$$

对于固定几何、电阻和质量，$T\propto I^{-1}$，效率随$I$增加而增加，极限为$1/2$。这是理想恒流模型的结论；真实材料温升与电源限制可能使模型失效，不能据此无限提高电流。

### 变式3　给定轨道参数的完整能量闭合

取$b=5.00\,\mathrm{mm}$、$d=2.00\,\mathrm{mm}$、$L=1.00\,\mathrm m$、$m=0.0100\,\mathrm{kg}$、$I=10.0\,\mathrm{kA}$、$R=1.00\,\mathrm m\Omega$、$\lambda=0.500\,\mathrm m\Omega/\mathrm m$、$\theta=0$。取$\mu_0=4\pi\times10^{-7}\,\mathrm{H/m}$。求速度、最高电压及源功。

**解答：** 电感梯度

$$
\kappa_L=4\times10^{-7}\ln1.4
\simeq1.34589\times10^{-7}\,\mathrm{H/m}.
$$

于是$F_B\simeq6.7294\,\mathrm N$、$a_B\simeq672.94\,\mathrm{m/s^2}$，

$$
v_e=\sqrt{2a_BL}\simeq36.686\,\mathrm{m/s},
\qquad T\simeq0.054516\,\mathrm s.
$$

出射电压为

$$
U_e=10^4(0.001+0.001)
+\kappa_L10^4v_e
\simeq20.0494\,\mathrm V.
$$

焦耳热约$I^2T(0.001+0.001/3)=7268.8\,\mathrm J$；机械动能与新增磁能各为$6.7294\,\mathrm J$。源功约$7282.3\,\mathrm J$，其中焦耳热占主导。保持电流并不能保证高效率。

### 变式4　电流可变时的电压与力

把驱动电流改为已知的$I(t)$，回路电感为$\mathcal L(x)=\mathcal L_0+\kappa_Lx$。推导源电压与磁力，并核对功率。

**解答：** 完整磁链为$\mathcal L(x)I(t)$，所以

$$
\boxed{
U=I(R+2\lambda x)+\mathcal L(x)\dot I
+\kappa_LI\dot x}.
$$

磁力仍由当前位置电流给出$F_B=\kappa_LI^2/2$。磁场能量变化为

$$
\frac{d}{dt}\left(\frac12\mathcal L I^2\right)
=\mathcal L I\dot I+\frac12\kappa_LI^2\dot x.
$$

于是$UI-P_J-dU_B/dt=\kappa_LI^2\dot x/2=F_B\dot x$，能量闭合。只有$\dot I=0$时，非焦耳源功才在磁能与机械能间按原题的固定比例分配；电流建立和关断阶段不能忽略$\mathcal L I\dot I$。
