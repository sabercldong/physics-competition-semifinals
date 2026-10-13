"""One-time additions preserving solved variants and teaching detail."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def insert(n,marker,extra):
    p=ROOT/'drafts'/f'question-{n:02d}.md';t=p.read_text()
    if extra.strip() not in t:
        if marker:t=t.replace(marker,extra+'\n\n'+marker,1)
        else:t=t.rstrip()+'\n\n'+extra+'\n'
        p.write_text(t)
insert(1,None,r"""
若改为固定像素数的绝对标准误差 $\sigma_{l_1}=\sigma_{l_2}=\sigma_l$，须先把绝对误差转换到各自的相对误差，得到

$$\left(\frac{\sigma_F}{F}\right)^2
=\left[\frac{l_2}{l_1(l_1-l_2)}\right]^2\sigma_l^2
+\left[\frac{l_1}{l_2(l_1-l_2)}\right]^2\sigma_l^2.$$

此时较小的 $l_2$ 会使第二项增大，不能一味把第二个像缩得极小。实验设计需同时避开 $l_1\simeq l_2$ 的差分不稳定和 $l_2\simeq0$ 的像素分辨率不足。

如果像长共用同一个比例校准误差，两项并非独立。应在上式中加入协方差项

$$2\frac{\partial\ln F}{\partial l_1}
\frac{\partial\ln F}{\partial l_2}\,
\operatorname{Cov}(l_1,l_2).$$

两个偏导异号，所以正相关的共同校准误差部分抵消；若物长 $l$ 也共用该校准，还会进一步抵消。先识别误差来源，再写方差关系，比机械地把所有误差绝对值相加更合适。
""")
insert(2,None,r"""
还可用势垒顶附近的动力学检查等号的含义。在中央附近，线性不稳定方程为

$$\ddot\theta=\lambda^2\theta,\qquad
\lambda=\sqrt{\frac{g\delta}{r}}.$$

临界能量轨道向中央靠近时 $\dot\theta\simeq-\lambda\theta$，所以

$$\theta(t)\simeq C e^{-\lambda t}.$$

它需要无限长时间才能到达严格的 $\theta=0$。相同结论可从时间积分 $dt\simeq-d\theta/(\lambda\theta)$ 的对数发散看出。初速度恰等于阈值时，活塞不在有限时间跨到另一势阱；略大于阈值才有真正的跨越轨道。

若给的是切向速度 $v$ 而非角速度，必须先用 $v=r\Omega$ 转换，阈值切向速度为 $v_{\rm th}=\delta\sqrt{gr/(2c)}$。速度和角速度的量纲不能在代入动能时混用。
""")
insert(3,None,r"""
物理上 $k\ge0$，因此纯滚动数据应满足

$$0<A\le
\frac{g\sin\theta}{1-m\cos^2\theta/(M+m)}.$$

上界是没有转动能量需求的 $k=0$ 极限。若测量值超过上界，不能只把反求出的负 $k$ 舍为零；应回查加速度的参考系、斜面角度和是否确实纯滚动。

加速度小误差 $\delta A$ 对惯量参数的影响为

$$\delta k\simeq-\frac{g\sin\theta}{A^2}\delta A.$$

当 $A$ 很小时，固定绝对测量误差会严重放大。以 $M=m$、$\theta=45^\circ$ 为例，实心球 $k=2/5$ 时 $A/g=5\sqrt2/11.5\simeq0.615$；反代可恢复 $k=0.400$。在代入前，仍须用该组参数计算 $\mu_0$ 并确认接触处不滑动。
""")
insert(4,None,r"""
为检查载荷怎样影响接触，定义

$$D_m=\frac b{\cos\theta}+2Rt-a,\qquad
\alpha=\frac{b}{2\cos\theta D_m}.$$

则 $N_1(W)=N_1(0)+\alpha W$。所以杆间控制接触的摩擦比为

$$\mu_{\rm req}(W)
=t\left(1+\frac{mg}{N_1(0)+\alpha W}\right).$$

在 $\alpha>0$、接触仍保持压紧时，该比值随中央载荷增大而减小，趋近 $t$。这是一个有具体条件的结果：中央载荷增强了压紧，所需摩擦力虽增大，法向力相对增长更多。

地面所需摩擦的有向量可整理为

$$f_5(W)=(\tan\theta-t)N_1(W)-tmg
-\frac12[(M+m)g+W]\tan\theta.$$

故地面条件是 $|f_5(W)|\le\mu'[3(M+m)g/2+W/2]$。这项比值未必与杆间阈值同方向变化；应逐项代入检查。计算还要保留 $N_4(W)\ge0$，否则上面的接触状态解已不适用。
""")
insert(5,"## 六、关键洞察",r"""
### 11　向内分支的有限时间尺度

若 $\cos\theta_0<0$，从完整二阶径向方程及初值积分得到

$$r^2(t)=r_0^2-
\frac{2\kappa|\cos\theta_0|}{mr_0^2}t^2.$$

理想奇点模型到达原点的时间为

$$t_c=r_0^2\sqrt{\frac{m}{2\kappa|\cos\theta_0|}}.$$

这不要求轨道是一条径向直线；除轴上释放外，角运动同时存在，但组合不变量使半径仍满足这个关系。$\theta_0\to\pi/2^+$ 时 $t_c$ 增大，边界处转为恒定半径轨道。公式只描述到奇点前的运动，不规定碰撞后如何继续。
""")
insert(5,None,r"""
在定半径条件下，令 $\eta=\psi-\pi$，角运动方程为

$$\ddot\eta+\frac{\kappa}{mr_0^4}\sin\eta=0.$$

看起来像单摆，但其能量由 $C=0$ 限定，对应转向角 $\eta=\pm\pi/2$，并非任意小振幅。因此不能直接把小角单摆周期作为这个轨道的周期。

用第一积分计算完整往返周期：

$$\mathcal T=
4r_0^2\sqrt{\frac m\kappa}\,
K(1/\sqrt2),$$

其中 $K(k)=\int_0^{\pi/2}(1-k^2\sin^2u)^{-1/2}du$。由于 $K(1/\sqrt2)\simeq1.854$，$\mathcal T\simeq7.42r_0^2\sqrt{m/\kappa}$。不同满足定半径条件的初始位置与速度只改变这条往返轨道上的初相，不改变其振幅和周期。
""")
insert(6,"### 变式3",r"""
还可比较固定电流略高于最小值时的两个平衡高度。平均支持力从地面附近的零值先增大，达到 $z=b/\sqrt7$ 的最大值后下降。因此最大支持力大于 $G$ 时，一般有低、高两个正平衡根。低根处 $F'_{\rm av}>0$，向上偏移会获得更大的上推力，竖直不稳定；高根处 $F'_{\rm av}<0$，具有竖直恢复性。

代入高根 $h$，慢振动频率为

$$\Omega_z=\sqrt{\frac{g(7h^2-b^2)}{h(b^2+h^2)}}.$$

当 $h\to b/\sqrt7$，这个频率趋于零，因而接近最小电流点时恢复作用很弱。上述判断针对平均动力学，另需高频微振动幅值 $g/(4\omega^2)$ 足够小，才可把快速运动和慢速恢复运动分开。
""")
insert(7,None,r"""
还可以由球面中心角给出精确的地表距离上界。两端到切点的中心角分别为

$$\varphi_a=\arccos\frac{R_e}{R_e+h_a},\qquad
\varphi_b=\arccos\frac{R_e}{R_e+h_b}.$$

地表弧长上界为 $D_{\rm arc}=R_e(\varphi_a+\varphi_b)$，无遮挡直线长度上界则为两个切线段长度之和。低高度时 $\varphi\simeq\sqrt{2h/R_e}$，两者都回到 $\sqrt{2R_eh_a}+\sqrt{2R_eh_b}$ 的领先阶。

这种比较可检查估算采用的距离类型。几百公里视距与几千公里导波之间相差明显，即使保留球面精确修正，四种组合的分类也不改变。
""")
insert(8,"### 变式3",r"""
若还要求电子反冲方向，取入射光子沿 $x$ 轴，出射光子偏转角为 $\theta$。反冲电子与正 $x$ 轴的夹角大小 $\varphi$ 满足

$$\tan\varphi=\frac{p_1\sin\theta}{p_0-p_1\cos\theta}.$$

利用 $p_1/p_0=[1+x(1-\cos\theta)]^{-1}$，化简为

$$\tan\varphi=
\frac{\sin\theta}{(1+x)(1-\cos\theta)}
=\frac{\cot(\theta/2)}{1+x}.$$

反向光子散射 $\theta=\pi$ 时，反冲电子沿入射光方向，$\varphi=0$。若要计算其速率，令 $K$ 为已求动能，用相对论能量动量关系：

$$\frac vc=\frac{\sqrt{K(K+2mc^2)}}{K+mc^2}.$$

它在 $K\ll mc^2$ 时回到 $\sqrt{2K/m}/c$，并在高能极限始终小于1。这样可同时核对反冲动能、动量方向和速率，避免只由能量给出一个超光速的非相对论估计。
""")
if __name__=='__main__': print("Teaching detail synchronized.")
