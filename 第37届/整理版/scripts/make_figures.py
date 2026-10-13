#!/usr/bin/env python3
"""Editable, equation-based teaching figures for the 2020 paper."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FIGS={
"q1-chambers":r"""
\begin{tikzpicture}[scale=.9]
\draw[thick,fill=gray!8] (-.3,3) rectangle(2.7,3.6);
\node at (1.2,3.3) {簧上负载};
\draw[thick] (0,2.7)--(0,.5)--(2.4,.5)--(2.4,2.7);
\draw[very thick] (-.1,2.7)--(2.5,2.7);
\node at (1.2,1.5) {主室$p_1,V_1$};
\draw[thick] (-4,.5) rectangle(-2.2,2.2);
\node at (-3.1,1.4) {附加室$V_2$};
\draw[thick] (-2.2,1)--(-1.5,1)--(-1.5,2.1)--(0,2.1);
\draw[thick] (-1.2,1.9)--(-.8,2.3); \draw[thick] (-1.2,2.3)--(-.8,1.9);
\node[above] at (-1,2.5) {阀门};
\draw[arr] (3,2.7)--(3,1.9) node[below] {$y>0$};
\draw[arr,red] (1.2,3.6)--(1.2,4.5) node[above] {$F=(p_1-p_0)A_e$};
\node at (-.7,-.25) {主室随位移改变；附加室容积固定};
\end{tikzpicture}
""",
"q1-force":r"""
\begin{tikzpicture}[xscale=3,yscale=3]
\draw[arr] (-1,1)--(1,1) node[right] {$y/y_*$};
\draw[arr] (0,.82)--(0,1.22) node[above] {$F/F_0$};
\draw[thick,blue,domain=-.85:.85,samples=80] plot(\x,{(3/(1-.06*\x)-1)*(1+.03*\x)/2});
\draw[thick,red,domain=-.85:.85,samples=80] plot(\x,{(3/(1-.06*\x)^1.4-1)*(1+.03*\x)/2});
\node[blue] at (-.65,1.08) {等温};
\node[red] at (.6,1.2) {绝热更陡};
\node at (0,.62) {$dF/dy=A_e\,dp/dy+\beta(p-p_0)>0$};
\end{tikzpicture}
""",
"q2-impact":r"""
\begin{tikzpicture}[scale=1.2]
\draw[thick] (-2,0)--(2.7,0);
\draw[thick] (0,1) circle(1);
\fill (0,1) circle(1.5pt) node[left] {$C$};
\draw[arr,blue,very thick] (-2,1.5)--(-.866,1.5) node[midway,above] {$P$};
\draw[dashed] (-1.3,1)--(1,1);
\draw[<->] (-1.3,1)--(-1.3,1.5) node[midway,left] {$R/2$};
\draw[arr] (.2,1)--(1.7,1) node[right] {$v_0$};
\draw[arr] (1.3,1.7) arc(45:-45:.7);
\node[right] at (1.7,1.7) {$\omega_0$};
\draw[arr,red] (0,0)--(-1.2,0);
\node[below] at (-.6,-.1) {$u_0=-P/(4m)$};
\end{tikzpicture}
""",
"q2-friction":r"""
\begin{tikzpicture}[scale=1.15]
\draw[thick] (-1.8,0)--(2,0); \draw[thick] (0,1) circle(1);
\draw[arr,red,very thick] (0,0)--(1.3,0) node[right] {$f=\mu mg$};
\draw[arr] (0,1)--(0,.65); \node[left] at (-.1,.82) {$mg$};
\draw[arr] (0,0)--(0,.4); \node[right] at (.1,.2) {$N$};
\draw[arr,blue] (0,1)--(1.4,1) node[right] {$v$增大};
\node at (0,2.6) {$\omega$减小，$v-R\omega$趋零};
\end{tikzpicture}
""",
"q2-cycloid":r"""
\begin{tikzpicture}[xscale=.9,yscale=.9]
\draw[arr] (-.4,0)--(7,0) node[right] {$x/R$};
\draw[arr] (0,0)--(0,2.7) node[above] {$y/R$};
\draw[dashed] (0,1)--(6.283,1);
\draw[thick,blue,domain=0:6.283,samples=140] plot({\x-sin(\x r)},{1-cos(\x r)});
\foreach \a in {0,3.1416,6.2832}{
\draw[gray] (\a,1) circle(1);
\fill[blue] ({\a-sin(\a r)},{1-cos(\a r)}) circle(2pt);}
\node[above] at (3.1416,2.1) {球顶：$v_B=2v_c$};
\node at (3.1,-.9) {$x_B/R=\theta-\sin\theta,\quad y_B/R=1-\cos\theta$};
\end{tikzpicture}
""",
"q3-circuit":r"""
\begin{tikzpicture}[scale=.95]
\draw[thick] (0,0)--(0,.6); \draw[thick] (-.2,.6) rectangle(.2,1.4);
\node[left] at (-.2,1) {$R$}; \draw[thick] (0,1.4)--(0,2)--(.5,2);
\draw[thick,decorate,decoration={coil,aspect=.3,segment length=4pt,amplitude=3pt}] (.5,2)--(1.4,2);
\node[above] at (.95,2.25) {$L$};\draw[thick] (1.4,2)--(1.9,2);
\draw[thick] (1.9,1.7)--(1.9,2.3); \draw[thick] (2.1,1.7)--(2.1,2.3);
\node[above] at (2,2.3) {$C$}; \draw[thick] (2.1,2)--(3,2);
\draw[thick] (3,2)--(3,1.4); \draw[thick,fill=gray!12] (2.65,.6) rectangle(3.35,1.4);
\node at (3,1) {$D$};\draw[thick] (3,.6)--(3,0)--(0,0);
\node[right] at (3.4,1) {$r_d=-R_0$};
\draw[thick] (3,2)--(4,2);
\draw[thick,decorate,decoration={coil,aspect=.3,segment length=4pt,amplitude=3pt}] (4,2)--(5,2);
\node[above] at (4.5,2.3) {RFC};
\draw[thick] (5,2)--(6,2)--(6,1.4); \draw[thick] (6,1) circle(.4);
\node at (6,1) {$V_0$};\draw[thick] (6,.6)--(6,0)--(3,0);
\draw[arr,blue] (.7,1.3)--(1.8,1.3) node[midway,below] {$i(t)$};
\draw[arr,red] (5.7,3.1)--(3.4,3.1) node[midway,above] {$I$};
\node at (3,-.7) {左侧交流回路；右侧直流偏置};
\end{tikzpicture}
""",
"q3-responses":r"""
\begin{tikzpicture}[xscale=.5,yscale=1]
\draw[arr] (0,0)--(13.5,0) node[right] {$\omega_0t$};
\draw[arr] (0,-2)--(0,2.2) node[above] {$i/(\beta/\omega_0)$};
\begin{scope}\clip (0,-2) rectangle(13,2);
\foreach \d/\col in {.06/blue,0/black,-.06/red}{
\draw[thick,\col,domain=0:13,samples=180] plot(\x,{exp(-\d*\x)*sin(sqrt(1-\d*\d)*\x r)/sqrt(1-\d*\d)});}
\end{scope}
\node[blue] at (2,-2.6) {衰减};
\node at (6.5,-2.6) {等幅};
\node[red] at (11,-2.6) {增长};
\end{tikzpicture}
""",
"q3-roots":r"""
\begin{tikzpicture}[xscale=2.8,yscale=1]
\draw[arr] (-1.6,0)--(1.7,0) node[right] {$\delta/\omega_0$};
\foreach \x in {-1,0,1}{\draw (\x,-.12)--(\x,.12); \node[below] at (\x,-.12) {$\x$};}
\draw[very thick,red] (-1,0)--(0,0);
\draw[very thick,blue] (0,0)--(1,0);
\node at (-1.3,1.1) {双实根增长};
\node[red] at (-.5,.6) {增长振荡};
\node[blue] at (.5,.6) {衰减振荡};
\node at (1.3,1.1) {双实根衰减};
\node at (0,-1) {$\delta=0$等幅；$\delta=\pm\omega_0$重根};
\end{tikzpicture}
""",
"q3-bias":r"""
\begin{tikzpicture}[xscale=1,yscale=2.4]
\draw[arr] (0,0)--(6.8,0) node[right] {$\omega t$};
\draw[arr] (0,0)--(0,1.25) node[above] {$V_D$};
\draw[dashed] (0,1)--(6.3,1) node[right] {$V_{\max}$};
\draw[dashed] (0,.5)--(6.3,.5) node[right] {中点};
\node[left] at (0,0) {$V_{\min}$};
\draw[thick,blue,domain=0:6.283,samples=100] plot(\x,{.5+.5*sin(\x r)});
\draw[thick,red,domain=0:6.283,samples=100] plot(\x,{.75+.25*sin(\x r)});
\node[blue] at (2,-.3) {中点：最大幅度};
\node[red] at (5,-.6) {偏置偏移：幅度减少};
\end{tikzpicture}
""",
"q4-orbit":r"""
\begin{tikzpicture}[scale=1]
\draw[thick] (0,0) circle(2);
\draw[arr] (2,0) arc(0:65:2);
\draw[arr] (0,2)--(-1.4,2) node[left] {$\mathbf p$};
\draw[arr,red] (0,2)--(0,.7) node[left] {$e\mathbf v\times\mathbf B$};
\draw[arr] (0,0)--(2,0) node[midway,below] {$R$};
\foreach \x/\y in {-1/-1,1/1,1/-1}{\node at (\x,\y) {$\otimes$};}
\node at (0,-2.8) {$p=eBR,\quad 2\pi R\leq L_{\max}$};
\node at (3.1,.7) {$\mathbf B$入纸面};
\end{tikzpicture}
""",
"q4-threshold":r"""
\begin{tikzpicture}[scale=1]
\node at (-.3,2.9) {固定靶初态};
\fill[blue] (0,1.8) circle(3pt); \draw[arr,blue] (0,1.8)--(1.5,1.8);
\node[above] at (.6,1.9) {$E_1,p_1$};
\fill (3,1.8) circle(3pt); \node[above] at (3,2) {靶静止};
\node at (-.3,.4) {阈值末态};
\foreach \x/\lab in {0/p,.8/p,1.6/p,2.4/\bar p}{
\fill[red] (\x,-.3) circle(3pt); \node[below] at (\x,-.4) {$\lab$};
\draw[arr,red] (\x,-.3)--(\x+.45,-.3);}
\node at (2,-1.3) {实验室同速；质心系各自静止};
\end{tikzpicture}
""",
"q5-ships":r"""
\begin{tikzpicture}[scale=1]
\draw[arr] (-.5,0)--(5,0) node[right] {$x$};
\draw[arr] (0,0)--(0,4.2) node[above] {$y$};
\node[left] at (0,3.4) {甲};\draw[arr,blue] (0,3.4)--(0,2.5);
\node[left] at (0,1.4) {乙};\draw[arr] (0,1.4)--(0,.6);
\draw[dashed] (3.7,0)--(3.7,4);
\node[right] at (3.7,1.4) {丙};\draw[arr,red] (3.7,1.4)--(3.7,2.4);
\draw[<->] (0,-.6)--(3.7,-.6) node[midway,below] {$d$};
\node at (1.8,5.2) {$v_\text{甲}=-2c/3,\ v_\text{乙}=-c/3,\ v_\text{丙}=2c/3$};
\end{tikzpicture}
""",
"q5-light":r"""
\begin{tikzpicture}[xscale=3.5,yscale=3.5]
\draw[arr] (-1.3,0)--(.3,0) node[right] {$y/(cT)$};
\draw[arr] (0,0)--(0,1.6) node[above] {$t/T$};
\draw[dashed,thick] (0,0)--(-.98,1.47);
\draw[dashed,thick] (-.74536,0)--(-1.23536,1.47);
\draw[arr,blue,thick] (0,0)--(-1.118034,1.118034);
\draw[arr,blue,thick] (-1.118034,1.118034)--(-.894427,1.341641);
\node[below right] at (0,0) {$A$};
\node[left] at (-1.118034,1.118034) {$B$反射};
\node[above right] at (-.894427,1.341641) {$C$返回};
\node at (-.65,-.25) {实线光信号，虚线甲与乙};
\end{tikzpicture}
""",
"q5-parcel":r"""
\begin{tikzpicture}[scale=1]
\draw[arr] (-.3,0)--(3.1,0) node[right] {$x$};
\draw[arr] (0,0)--(0,4.8) node[above] {$y$};
\draw[dashed] (2,0)--(2,4.6);
\draw[arr,blue,thick] (0,0)--(2,3.88057);
\fill (2,3.88057) circle(2pt) node[right] {丙接收};
\node[below left] at (0,0) {甲发射};
\draw[arr,red] (0,0)--(.6872,0) node[above] {$u_x$};
\draw[arr,red] (.6872,0)--(.6872,1.3333) node[right] {$u_y$};
\draw[<->] (0,-.7)--(2,-.7) node[midway,below] {$d$};
\node at (1.2,5.4) {$u_y=2c/3,\quad u_x=\sqrt{17}\,c/12$};
\end{tikzpicture}
""",
"q6-ring":r"""
\begin{tikzpicture}[scale=1]
\draw[thick] (0,0) circle(2);
\fill (0,2) circle(2pt) node[above] {$A$};
\draw[arr,blue,thick] (0,2) arc(90:155:2); \node[blue] at (-2.8,1.2) {CCW};
\draw[arr,red,thick] (0,2) arc(90:25:2); \node[red] at (2.8,1.2) {CW};
\draw[arr] (1,0) arc(0:90:1); \node at (.8,.8) {$\Omega$};
\draw[arr] (0,0)--(2,0) node[midway,below] {$R$};
\node at (0,-2.7) {光传播与移动分束器相遇};
\end{tikzpicture}
""",
"q6-guide":r"""
\begin{tikzpicture}[scale=1]
\draw[fill=gray!8] (0,-.85) rectangle(5,.85);
\draw[fill=blue!5] (0,-.55) rectangle(5,.55);
\draw[dashed] (-1.5,0)--(5.3,0);
\draw[arr,red] (-1.5,-.897)--(0,0)--(1.5,.55)--(4.5,-.55)--(5,-.3667);
\draw[dashed] (1.5,-.2)--(1.5,1.15);
\node at (-.8,-.2) {$i$};
\node at (.7,-.18) {$\theta$};
\node[right] at (1.55,.25) {$\psi$};
\node at (3,.15) {$n_1$}; \node at (3,.72) {$n_2$};
\node at (-.8,.65) {$n_0$};
\node at (2.1,-1.45) {$n_0\sin i=n_1\sin\theta,\quad\psi+\theta=\pi/2$};
\end{tikzpicture}
""",
"q6-cone":r"""
\begin{tikzpicture}[scale=1]
\draw[fill=blue!5] (0,-.6) rectangle(4,.6);
\draw[dashed] (-2.4,0)--(4.4,0);
\draw[blue,thick] (-2,-.9)--(0,0)--(-2,.9);
\draw[blue,dashed] (-2,-.9)--(-2,.9);
\draw[arr,red] (-2,-.45)--(0,0)--(2,.45);
\node at (-1.4,.45) {$i_{\max}$};
\node at (2,.95) {芯内导光};
\node at (1,-1.3) {$n_0|\sin i|\leq\sqrt{n_1^2-n_2^2}$};
\end{tikzpicture}
""",
"q6-resonance":r"""
\begin{tikzpicture}[xscale=1.6,yscale=3]
\draw[arr] (-2,0)--(2.3,0) node[right] {$f-f_0$};
\draw[arr] (-2,0)--(-2,1.2) node[above] {共振响应};
\draw[thick,blue,domain=-1.9:1.9,samples=160] plot(\x,{1/(1+16*(\x+.5)^2)});
\draw[thick,red,domain=-1.9:1.9,samples=160] plot(\x,{1/(1+16*(\x-.5)^2)});
\node[blue] at (-.65,1.15) {CCW};
\node[red] at (.65,1.15) {CW};
\draw[<->] (-.5,1.42)--(.5,1.42) node[midway,above] {$\Delta f$};
\node at (0,-.4) {同级次相位闭合使两共振反向移动};
\end{tikzpicture}
""",
"q7-binary":r"""
\begin{tikzpicture}[scale=1]
\draw[dashed] (0,0) circle(1); \draw[dashed] (0,0) circle(2);
\fill[blue] (-1,0) circle(5pt) node[left] {$M$};
\fill[red] (2,0) circle(3pt) node[right] {$m$};
\fill (0,0) circle(1.5pt) node[above] {$O$};
\draw[arr] (-1,-.1)--(-1,-.8); \draw[arr] (2,.1)--(2,.9);
\draw[<->] (-1,2.5)--(2,2.5) node[midway,above] {$L=r_M+r_m$};
\node at (0,-2.7) {$Mr_M=mr_m,\quad I=\mu L^2$};
\end{tikzpicture}
""",
"q7-evolution":r"""
\begin{tikzpicture}[xscale=6,yscale=1]
\draw[arr] (0,0)--(1.12,0) node[right] {$t/t_c$};
\draw[arr] (0,0)--(0,4.6);
\draw[thick,blue,domain=0:.98,samples=150] plot(\x,{(1-\x)^.25});
\draw[thick,red,domain=0:.98,samples=150] plot(\x,{(1-\x)^(-.375)});
\draw[dashed] (.9375,0)--(.9375,2.828);
\node[below] at (.9375,0) {$15/16$};
\node[blue] at (.35,.45) {$L/L_0$};
\node[red] at (.62,2.6) {$\omega/\omega_0$};
\node at (.5,-.9) {近端点时近圆牛顿模型失效};
\end{tikzpicture}
""",
"q8-optics":r"""
\begin{tikzpicture}[scale=.85]
\draw[arr,thick] (-1,0)--(9,0) node[right] {$x_3$光};
\draw[very thick] (0,-.8)--(0,.8);
\node[above] at (0,.85) {$P_1\parallel x_1$};
\draw[fill=blue!5,thick] (1,-.6) rectangle(5,.6);
\node at (3,.2) {电光晶体};
\node at (1,-.85) {$+$};\node at (5,-.85) {$-$};
\draw[<->] (1,1.3)--(5,1.3) node[midway,above] {$l$};
\draw[<->] (1,-1.3)--(5,-1.3) node[midway,below] {$V,\ E=V/l$};
\draw[very thick] (6,-.8)--(6,.8); \node[above] at (6,.85) {$1/4$波片};
\draw[very thick] (7.6,-.8)--(7.6,.8); \node[above] at (7.8,1.4) {$P_2\parallel x_2$};
\draw[arr] (3,-3.8)--(3,-2.8) node[above] {$x_1$};
\draw[arr] (3,-3.8)--(4,-3.8) node[right] {$x_2$};
\draw[arr,blue] (3,-3.8)--(2.3,-3.1) node[left] {$x'_1$};
\draw[arr,red] (3,-3.8)--(3.7,-3.1) node[right] {$x'_2$};
\end{tikzpicture}
""",
"q8-circuit":r"""
\begin{tikzpicture}[scale=.9]
\draw[thick] (0,0)--(0,.6); \draw[thick] (0,1) circle(.4); \node at (0,1) {$V$};
\draw[thick] (0,1.4)--(0,2)--(.8,2);
\draw[thick] (.8,1.8) rectangle(1.8,2.2); \node[above] at (1.3,2.3) {$R_m$};
\draw[thick] (1.8,2)--(5.1,2);
\draw[thick] (3,2)--(3,1.4); \draw[thick] (2.8,.6) rectangle(3.2,1.4);
\node[left] at (2.8,1) {$R$};\draw[thick] (3,.6)--(3,0);
\draw[thick] (4.4,2)--(4.4,1.15); \draw[thick] (4.1,1.15)--(4.7,1.15);
\draw[thick] (4.1,.95)--(4.7,.95); \draw[thick] (4.4,.95)--(4.4,0);
\node[right] at (4.65,1) {$C$};
\draw (5.1,2) circle(1.5pt); \draw (5.8,2) circle(1.5pt);
\draw[thick] (5.1,2)--(5.7,2.35); \node at (5.4,2.7) {$S$};
\draw[thick] (5.8,2)--(7.7,2);
\draw[thick] (6.2,2)--(6.2,1.6);
\draw[thick,decorate,decoration={coil,aspect=.3,segment length=4pt,amplitude=3pt}] (6.2,1.6)--(6.2,.5);
\draw[thick] (6.2,.5)--(6.2,0); \node[right] at (6.5,1) {$L$};
\draw[thick] (7.7,2)--(7.7,1.4); \draw[thick] (7.5,.6) rectangle(7.9,1.4);
\node[right] at (7.9,1) {$R_L$}; \draw[thick] (7.7,.6)--(7.7,0)--(0,0);
\node at (4,-.8) {闭合$S$接入并联$L,R_L$};
\end{tikzpicture}
""",
"q8-transfer":r"""
\begin{tikzpicture}[xscale=5,yscale=3]
\draw[arr] (-.72,0)--(.82,0) node[right] {$V/V_\pi$};
\draw[arr] (0,0)--(0,1.2) node[above] {$\mathcal T$};
\draw[thick,blue,domain=-.7:.7,samples=120] plot(\x,{sin(90*\x)^2});
\draw[thick,red,domain=-.7:.7,samples=120] plot(\x,{(1+sin(180*\x))/2});
\draw[dashed,domain=-.25:.25] plot(\x,{.5+pi*\x/2});
\node[blue] at (-.42,1.3) {无波片};
\node[red] at (.42,1.3) {加$1/4$波片};
\node at (0,-.42) {固定$\pi/2$偏置使零电压处斜率非零};
\end{tikzpicture}
""",
"q8-response":r"""
\begin{tikzpicture}[xscale=3,yscale=3]
\draw[arr] (.15,0)--(2.2,0) node[right] {$\omega/\omega_0$};
\draw[arr] (.15,0)--(.15,1.15) node[above] {$|V_c/V|$};
\draw[thick,blue,domain=.2:2,samples=150] plot(\x,{1/sqrt(1+25*\x*\x)});
\draw[thick,red,domain=.2:2,samples=250] plot(\x,{1/sqrt(1.01^2+25*(\x-1/\x)^2)});
\draw[dashed] (1,0)--(1,1); \node[below] at (1,0) {$1$};
\node[blue] at (.62,1.25) {无补偿};
\node[red] at (1.5,1.25) {谐振补偿};
\node at (1.2,-.42) {峰值受损耗限制，恢复只在调谐频带内};
\end{tikzpicture}
""",
}
TEMPLATE=r"""\documentclass[border=9pt]{standalone}
\usepackage[fontset=fandol]{ctex}
\usepackage{amsmath,amssymb,tikz}
\usetikzlibrary{arrows.meta,calc,decorations.pathmorphing}
\tikzset{arr/.style={-{Stealth[length=2mm]},semithick}}
\begin{document}
%BODY%
\end{document}
"""
def main():
    out=ROOT/"figures";out.mkdir(exist_ok=True)
    for name,body in FIGS.items():
        (out/(name+".tikz")).write_text(body.strip()+"\n")
        (out/(name+".tex")).write_text(TEMPLATE.replace("%BODY%",body))
    print(f"{len(FIGS)} editable figures")
if __name__=="__main__":main()
