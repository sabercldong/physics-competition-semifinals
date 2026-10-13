#!/usr/bin/env python3
"""Editable equation-based TikZ figures for the 2021 paper."""
from pathlib import Path
import math
ROOT=Path(__file__).resolve().parents[1]
FIGS={
"q1-lens":r"""
\begin{tikzpicture}[scale=.9]
\draw[arr] (-2,0)--(5,0) node[right] {主轴};
\draw[fill=blue!6] (-1.2,-1.5)--(-1.2,1.5)--(-.489,1.5)
--plot[domain=1.5:-1.5,samples=81] ({4-(2.4+sqrt(2.56+\x*\x/1.25))},\x)--cycle;
\foreach \h in {-1.3,0,1.3}{
\pgfmathsetmacro{\sx}{4-(2.4+sqrt(2.56+\h*\h/1.25))}
\draw[arr,blue] (-2,\h)--(\sx,\h);
\draw[arr,blue] (\sx,\h)--(4,0);}
\fill (4,0) circle(1.5pt) node[below] {$F$};
\fill (0,0) circle(1.5pt) node[below] {$O$};
\draw[<->] (0,-2)--(4,-2) node[midway,below] {$r_0$};
\node at (-.85,.55) {$n$};
\node at (1.8,2.2) {平行光到同一焦点的等光程};
\end{tikzpicture}
""",
"q1-pair":r"""
\begin{tikzpicture}[scale=.95]
\draw[arr] (-2,0)--(5.5,0) node[right] {主轴};
\draw[thick,blue,domain=-1.4:1.4,samples=81] plot({4-(2.4+sqrt(2.56+\x*\x/1.25))},\x);
\draw[thick,red,domain=-.6:.6,samples=81] plot({4-(.964286+sqrt(.287+ \x*\x/2.24))},\x);
\draw[thick,red] (3.5,-.6)--(3.5,.6);
\foreach \h in {-1.3,0,1.3}{
\pgfmathsetmacro{\xx}{4-(2.4+sqrt(2.56+\h*\h/1.25))}
\pgfmathsetmacro{\rad}{sqrt((4-\xx)^2+\h*\h)}
\pgfmathsetmacro{\cs}{(4-\xx)/\rad}
\pgfmathsetmacro{\rp}{1.2/(1.8*\cs-1)}
\pgfmathsetmacro{\xp}{4-\rp*\cs}
\pgfmathsetmacro{\yp}{\rp*\h/\rad}
\draw[arr] (-2,\h)--(\xx,\h)--(\xp,\yp)--(5.25,\yp);
\draw[dashed] (\xp,\yp)--(4,0);}
\fill (4,0) circle(1.5pt) node[below] {$F$};
\node[below] at (0,0) {$O$};\node[below] at (2.5,-.7) {$O'$};
\node at (-.6,1.9) {凸面$n$};\node at (3,1.3) {凹面$n'$};
\node at (1.8,-2.1) {同一入射光线：$y=r\sin\theta,\quad y'=r'\sin\theta$};
\end{tikzpicture}
""",
"q1-branch":r"""
\begin{tikzpicture}[scale=.85]
\draw[arr] (0,0)--(6,0) node[right] {$x$};
\draw[arr] (0,-2.2)--(0,2.2) node[above] {$y$};
\draw[dashed] (2.4,-2.2)--(2.4,2.2);
\draw[dashed] (.5,-2.125)--(4.3,2.125);
\draw[dashed] (.5,2.125)--(4.3,-2.125);
\draw[very thick,blue,domain=-1.9:1.9,samples=90] plot({2.4+sqrt(2.56+\x*\x/1.25)},\x);
\draw[thin,gray,domain=-1.9:1.9,samples=90] plot({2.4-sqrt(2.56+\x*\x/1.25)},\x);
\fill (4,0) circle(2pt) node[below right] {$O:r_0$};
\node[below left] at (0,0) {$F$};\node at (3.5,2.6) {蓝色右支满足未平方方程};
\end{tikzpicture}
""",
"q2-tube":r"""
\begin{tikzpicture}[scale=.9]
\foreach \xx/\hg/\hh/\lab in {0/1.5/1.5/初态,3/3/1.5/A末,6/4.5/0/B末}{
\begin{scope}[shift={(\xx,0)}]
\draw[thick] (0,4.5)--(0,0)--(1.4,0)--(1.4,4.5);
\fill[blue!6] (.02,.02) rectangle(1.38,\hg);
\ifdim\hh pt>0pt\fill[gray!35] (.02,\hg) rectangle(1.38,{\hg+\hh});\fi
\draw[very thick] (0,\hg)--(1.4,\hg);
\node at (.7,.6) {气体};\node at (.7,-.55) {\lab};
\end{scope}}
\node at (3.7,5.1) {全过程管口外压力为$p_0$};
\end{tikzpicture}
""",
"q2-pv":r"""
\begin{tikzpicture}[xscale=2,yscale=.8]
\draw[arr] (.6,0)--(3.5,0) node[right] {$V/(Sh)$};
\draw[arr] (.7,0)--(.7,5) node[above] {$p/(\rho gh)$};
\draw[very thick,blue,arr] (1,4)--(2,4);
\draw[very thick,red,arr] (2,4)--(3,3);
\foreach \x/\y/\lab in {1/4/初态,2/4/A末,3/3/B末}{
\fill (\x,\y) circle(1.7pt);\node[above] at (\x,\y) {\lab};
\draw[dashed] (\x,0)--(\x,\y);\node[below] at (\x,0) {$\x$};}
\node at (2.1,-.9) {曲线下的面积是气体边界功};
\end{tikzpicture}
""",
"q2-temperature":r"""
\begin{tikzpicture}[xscale=3.2,yscale=3.5]
\draw[arr] (1.9,1.95)--(3.15,1.95) node[right] {$y/h$};
\draw[arr] (1.9,1.95)--(1.9,2.36) node[above] {$T/T_0$};
\draw[thick,blue,domain=2:3,samples=70] plot(\x,{(6-\x)*\x/4});
\draw[dashed] (2,1.95)--(2,2); \draw[dashed] (3,1.95)--(3,2.25)--(1.9,2.25);
\node[below] at (2,1.95) {$2$};\node[below] at (3,1.95) {$3$};
\node[left] at (1.9,2.25) {$9/4$};
\node at (2.5,1.73) {$y=l-x$；管口排尽处温度斜率趋零};
\end{tikzpicture}
""",
"q3-bounces":r"""
\begin{tikzpicture}[scale=1.2]
\draw[very thick] (-.8,-.15)--(4,-.15);\draw[very thick] (-.8,2.15)--(4,2.15);
\draw[arr,blue] (0,1.6)--(1.5,0);
\draw[arr,blue] (1.5,0)--(2.509,2);
\draw[arr,blue] (2.509,2)--(1.5,0);
\draw[arr,red,dashed] (1.5,0)--(0,1.6);
\draw[thick] (0,1.6) circle(.15);
\node[above] at (2.65,2.1) {碰撞2};
\node[below] at (1.5,-.1) {碰撞1、3};
\draw[arr] (4.5,1.6)--(5.4,1.6) node[right] {$x$};
\draw[arr] (4.5,1.6)--(4.5,.65) node[below] {$y$};
\node at (1.7,2.8) {示意取$r\omega_0/v_0=5/26$，三碰后反向};
\end{tikzpicture}
""",
"q3-contact":r"""
\begin{tikzpicture}[scale=.9]
\foreach \xx/\up/\lab in {0/0/下板,5/1/上板}{
\begin{scope}[shift={(\xx,0)}]
\draw[thick] (0,0) circle(.8);
\ifnum\up=0
\draw[thick] (-1.7,-.8)--(1.7,-.8);
\draw[arr] (0,-.8)--(-1.4,-.8);\node at (0,-1.5) {$u_-=v-r\omega$};
\else
\draw[thick] (-1.7,.8)--(1.7,.8);
\draw[arr] (0,.8)--(-1.4,.8);\node at (0,-1.5) {$u_+=v+r\omega$};
\fi
\draw[arr] (.2,0)--(1.4,0) node[right] {$v$};
\node at (0,1.7) {\lab};
\end{scope}}
\node at (2.5,-2.2) {同样的切向冲量，上、下接触的角冲量符号相反};
\end{tikzpicture}
""",
"q4-dipoles":r"""
\begin{tikzpicture}[scale=1]
\draw[arr] (0,3.5)--(0,-1);
\node[right] at (.2,-1) {$z$向下};
\draw[arr] (0,3)--(2.2,3) node[right] {$x$};
\draw[arr,very thick,blue] (0,3)--(1.45,3) node[above] {$\boldsymbol\mu_A$};
\fill (0,.3) circle(2pt);
\draw[arr,very thick,red] (0,.3)--(-1.45,.3) node[left] {$\boldsymbol\mu_B$};
\draw[arr] (.6,.3)--(.6,1.5) node[right] {$F_{\rm mag}$};
\draw[arr] (.1,.3)--(.1,-.7) node[right] {$mg$};
\node at (3.3,.3) {$\theta=\pi$};
\node at (1.2,-1.8) {稳定指向与$\boldsymbol\mu_A$反平行};
\end{tikzpicture}
""",
"q4-angle":r"""
\begin{tikzpicture}[xscale=1,yscale=1.3]
\draw[arr] (0,0)--(6.8,0) node[right] {$\theta$};
\draw[arr] (0,-1.4)--(0,1.5) node[above] {$U_{\rm mag}/(C/z^3)$};
\draw[thick,blue,domain=0:6.283,samples=100] plot(\x,{cos(\x r)});
\node[below] at (3.1416,-1) {$\pi$稳定};
\node[above] at (1.4,1.2) {$0$不稳定};
\end{tikzpicture}
""",
"q4-height":r"""
\begin{tikzpicture}[xscale=2.4,yscale=1.4]
\draw[arr] (.55,-2.2)--(2.7,-2.2) node[right] {$z/z_e$};
\draw[arr] (.55,-2.2)--(.55,-1) node[above] {$U/(mgz_e)$};
\draw[thick,blue,domain=.65:2.2,samples=90] plot(\x,{-1/(3*\x*\x*\x)-\x});
\draw[dashed] (1,-2.2)--(1,-1.333);
\node[above] at (1,-1.3) {极大值};\node[below] at (1,-2.2) {$1$};
\node at (1.5,-2.75) {向上偏离会被吸上，向下偏离会下落};
\end{tikzpicture}
""",
"q5-slower":r"""
\begin{tikzpicture}[scale=.9]
\draw[fill=gray!10] (0,-.8) rectangle(6,.8);
\draw[arr,blue,thick] (-1,0)--(6.5,0) node[right] {原子$v$};
\draw[arr,red,thick] (7,.4)--(.3,.4) node[left] {激光};
\draw[arr] (0,-1.5)--(6.7,-1.5) node[right] {$z$};
\node[below] at (0,-1.5) {$0$};\node[below] at (6,-1.5) {$s$};
\node at (3,1.4) {$f_0(B)=f_0(0)+\beta B,\ \beta<0$};
\node at (3,-2.4) {速度下降，磁场增加，跃迁频率下降};
\end{tikzpicture}
""",
"q5-profiles":r"""
\begin{tikzpicture}[xscale=5,yscale=3]
\draw[arr] (0,0)--(1.15,0) node[right] {$z/s$};
\draw[arr] (0,0)--(0,1.2);
\draw[thick,blue,domain=0:1,samples=100] plot(\x,{sqrt(1-\x)});
\draw[thick,red,domain=0:1,samples=100] plot(\x,{1-sqrt(1-\x)});
\node[blue] at (.36,1.02) {$v/v_0$};\node[red] at (.65,.82) {$B/B_f$};
\node at (.5,-.42) {理想末端场梯度趋大，实际截断于非零小速度};
\end{tikzpicture}
""",
"q6-cylinders":r"""
\begin{tikzpicture}[scale=.9]
\draw[thick] (0,0) ellipse(2 and .6);\draw[thick] (0,4) ellipse(2 and .6);
\draw[thick] (-2,0)--(-2,4);\draw[thick] (2,0)--(2,4);
\draw[dashed] (0,0) ellipse(1 and .3);\draw[thick] (0,4) ellipse(1 and .3);
\draw[dashed] (-1,0)--(-1,4);\draw[dashed] (1,0)--(1,4);
\draw[dashed] (0,-.8)--(0,5);
\node at (0,2.8) {$+q,\ m$};\node at (1.6,2) {$-q,\ m$};
\draw[arr] (0,4)--(1,4) node[midway,above] {$r_1$};
\draw[arr] (0,4.8)--(2,4.8) node[midway,above] {$r_2$};
\node at (0,-1.4) {质量和电荷均按单位轴长计};
\end{tikzpicture}
""",
"q6-fields":r"""
\begin{tikzpicture}[xscale=2.4,yscale=1.4]
\draw[arr] (0,0)--(3.4,0) node[right] {$r/r_1$};
\draw[arr] (0,-1.5)--(0,1.4);
\draw[thick,blue] (0,0)--(1,0);
\draw[thick,blue,domain=1:2,samples=60] plot(\x,{1/\x});
\draw[thick,blue] (2,0)--(3.1,0);
\draw[thick,red] (0,0)--(1,0)--(1,-1)--(2,-1)--(2,0)--(3.1,0);
\node[blue] at (1.65,1.2) {$E_r$归一化};\node[red] at (1.6,-1.5) {$B_z$归一化};
\node[above] at (1,.08) {$1$};\node[above] at (2,.08) {$2$};
\node at (1.6,-2.05) {示例$r_2=2r_1$；红线沿$-z$};
\end{tikzpicture}
""",
"q6-radial":r"""
\begin{tikzpicture}[xscale=4,yscale=3]
\draw[arr] (.95,0)--(2.45,0) node[right] {$u=r/r_1$};
\draw[arr] (1,-.35)--(1,.65) node[above] {$K_r/K_*$};
\begin{scope}\clip (1,-.35) rectangle(2.35,.65);
\foreach \eta/\col in {.1/blue,.308065/black,.5/red}{
\draw[thick,\col,domain=1:2.35,samples=100] plot(\x,{ln(\x)-\eta*(\x*\x-1)^2/(\x*\x)});}
\end{scope}
\draw[dashed] (2,-.35)--(2,.6);\node[below] at (2,-.35) {$r_2/r_1=2$};
\node[blue] at (2.2,.55) {可达};\node[red] at (1.3,-.28) {提前转向};
\node at (1.7,-.85) {径向动能非负的连通区决定可达性};
\end{tikzpicture}
""",
"q6-induction":r"""
\begin{tikzpicture}[scale=1]
\draw[thick] (0,0) circle(1.3);\draw[thick] (0,0) circle(2.2);
\draw[arr] (1.55,1.55) arc(45:125:2.2);
\draw[arr] (.92,.92) arc(45:125:1.3);
\node at (2.8,1.2) {$\Omega$外筒};
\node at (0,.4) {$\omega$内筒};
\node at (0,-2.9) {磁通变化产生感应力矩，两筒同向转动};
\end{tikzpicture}
""",
"q7-car":r"""
\begin{tikzpicture}[scale=.8,rotate=15]
\draw[thick] (-1,0)--(8,0);
\draw[thick] (1,.7) circle(.7);\draw[thick] (6,.7) circle(.7);
\draw[thick,fill=gray!8] (.3,1.4) rectangle(6.7,2.5);
\fill (3.5,1.85) circle(2pt) node[above] {$M$};
\draw[dashed] (1,.7)--(6,.7);
\draw[<->] (1,3)--(6,3) node[midway,above] {$L$};
\draw[<->] (3.5,.7)--(3.5,1.85) node[midway,right] {$h$};
\node at (1,.7) {$m$};\node at (6,.7) {$m$};
\draw[arr] (7,1.7)--(8.4,1.7) node[right] {$a$};
\end{tikzpicture}
""",
"q7-forces":r"""
\begin{tikzpicture}[scale=.85]
\draw[thick] (0,1.4) rectangle(6,2.1);
\fill (3,1.75) circle(1.5pt); \node[above] at (3,2.2) {车身质心};
\draw[arr] (3,1.75)--(3,.1) node[below] {$Mg$};
\draw[arr] (.7,.3)--(.7,1.4) node[above] {$F_{y,\text{后}}$};
\draw[arr] (5.3,.3)--(5.3,1.4) node[above] {$F_{y,\text{前}}$};
\draw[arr] (.7,1.4)--(2,1.4); \node[below] at (1.4,1.2) {$F_x$};
\draw[arr,red] (5.5,2.75) arc(45:145:.65);
\node[red] at (4.7,3.5) {驱动反作用$+\tau_{\text{轮}}$};
\node at (3,-.7) {参考约定省略红色力矩；完整车身受力保留它};
\end{tikzpicture}
""",
"q8-motor":r"""
\begin{tikzpicture}[scale=1]
\draw[thick] (0,0) rectangle(6,2);
\draw[fill=white] (.7,-.3) rectangle(1.9,.3);\node at (1.3,0) {$R_\Sigma$};
\draw[fill=white] (3,-.3) circle(.5);\node at (3,0) {$\mathcal E$};
\draw[fill=white] (4.5,-.3) rectangle(5.5,.3);\node at (5,0) {$V$};
\draw[arr] (1,2)--(2.5,2) node[midway,above] {$I$};
\node at (3,1.2) {$\mathcal E=K\omega,\quad\tau=KI$};
\node at (3,-1.1) {反电动势抵消部分电源电压};
\end{tikzpicture}
""",
"q8-curves":r"""
\begin{tikzpicture}[xscale=5,yscale=3]
\draw[arr] (0,0)--(1.2,0) node[right] {$\omega/\omega_{\max}$};
\draw[arr] (0,0)--(0,1.2);
\draw[thick,blue] (0,1)--(1,0);
\draw[thick,red,domain=0:1,samples=90] plot(\x,{4*\x*(1-\x)});
\node[blue] at (.28,1.14) {$\tau/\tau_{\max}$};
\node[red] at (.85,1.14) {$P/P_{\max}$};
\draw[dashed] (.5,0)--(.5,1);\node[below] at (.5,0) {$1/2$};
\end{tikzpicture}
""",
"q8-speed":r"""
\begin{tikzpicture}[xscale=1.6,yscale=3]
\draw[arr] (0,0)--(4.4,0) node[right] {$t/(v_{\max}/a_{\max})$};
\draw[arr] (0,0)--(0,1.25) node[above] {$v/v_{\max}$};
\draw[thick,blue,domain=0:4,samples=90] plot(\x,{1-exp(-\x)});
\draw[dashed] (0,1)--(4.1,1);
\node at (2,1.2) {$v=v_{\max}(1-e^{-t/t_c})$};
\node at (2,-.42) {达到极限车速需要无限长时间};
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
