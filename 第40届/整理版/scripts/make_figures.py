#!/usr/bin/env python3
"""Editable TikZ figures; plots are model schematics, not measured data."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FIGS={
"q1-principal":r"""
\begin{tikzpicture}[scale=.9]
\draw[arr] (-.6,0)--(7.8,0);
\draw[dashed] (2,-1)--(4.8,-1)--(4.8,1)--(2,1)--cycle;
\draw[densely dashed] (2.7,-.75)--(2.7,.75) node[above] {$H$};
\draw[densely dashed] (4.1,-.75)--(4.1,.75) node[above] {$H'$};
\fill (0,0) circle(2pt) node[above] {物};
\fill (7,0) circle(2pt) node[above] {像};
\draw[<->] (0,-.55)--(2.7,-.55) node[midway,below] {$u$};
\draw[<->] (4.1,-.55)--(7,-.55) node[midway,below] {$v$};
\node at (3.4,-1.45) {透镜组：距离分别从两主点起算};
\end{tikzpicture}
""",
"q1-two-lenses":r"""
\begin{tikzpicture}[scale=1.1]
\draw[arr] (-1.8,0)--(5.2,0) node[right] {光轴};
\draw[<->,thick] (0,-1.45)--(0,1.45);
\draw[<->,thick] (2,-1.45)--(2,1.45);
\draw[arr] (-1.7,1.2)--(0,1.2);
\draw[arr] (0,1.2)--(2,.72);
\draw[arr] (2,.72)--(4.3077,0);
\draw[dashed] (.769,-.6)--(.769,1.5);
\draw[dashed] (.4615,-1.2)--(.4615,.55);
\node[below] at (0,-1.5) {$O_1$};
\node[below] at (2,-1.5) {$O_2$};
\node[above] at (.769,1.5) {$H$};
\node[below] at (.4615,-1.2) {$H'$};
\fill (4.3077,0) circle(1.6pt) node[below] {$F'$};
\draw[<->] (0,-1.95)--(2,-1.95) node[midway,below] {$d$};
\node at (2.0,2.05) {平行入射光的折线与等效主平面};
\end{tikzpicture}
""",
"q2-piston":r"""
\begin{tikzpicture}[scale=1]
\draw[thick] (-3.4,0)--(3.4,0);
\draw[very thick] (3,0) arc(0:180:3);
\draw[dashed] (0,0)--(0,3);
\draw[dashed] (0,0)--(70:3);
\draw[thick] (70:2.82)--(70:3.18);
\draw[<->] (0,0)--(145:3) node[midway,above,fill=white,inner sep=1pt] {$r$};
\draw[arr] (0,1.0) arc(90:70:1);
\node at (.3,1.25) {$\theta$};
\node at (-1.45,2.1) {$n,\ T$};
\node at (1.8,1.25) {$n,\ T$};
\node[above right] at (70:3.2) {活塞 $m$};
\node at (-2.2,2.9) {$r(\pi/2+\theta)$};
\node at (3.3,2.3) {$r(\pi/2-\theta)$};
\end{tikzpicture}
""",
"q2-potential":r"""
\begin{tikzpicture}[xscale=4.2,yscale=8]
\draw[arr] (-.85,0)--(.9,0) node[right] {$\theta$};
\draw[arr] (0,-.05)--(0,.28) node[above] {$U/(mgr)$};
\draw[thick,blue,domain=-.8:.8,samples=81] plot(\x,{.08*\x*\x+.143*\x*\x*\x*\x});
\draw[thick,black,domain=-.8:.8,samples=81] plot(\x,{.143*\x*\x*\x*\x});
\draw[thick,red,domain=-.8:.8,samples=81] plot(\x,{-.07*\x*\x+.143*\x*\x*\x*\x});
\draw[blue,thick] (1.02,.24)--(1.15,.24);
\draw[black,thick] (1.02,.15)--(1.15,.15);
\draw[red,thick] (1.02,.06)--(1.15,.06);
\node[blue,right] at (1.17,.24) {高温};
\node[right] at (1.17,.15) {临界};
\node[red,right] at (1.17,.06) {低温};
\node at (.1,-.12) {中央附近的四次势能模型};
\end{tikzpicture}
""",
"q3-wedge":r"""
\begin{tikzpicture}[scale=1]
\draw[thick] (-.5,0)--(6.4,0);
\draw[thick,fill=gray!10] (0,0)--(5,0)--(5,2.6)--cycle;
\draw[thick] (3.58,2.4) circle(.48);
\fill (3.58,2.4) circle(1.5pt);
\node[above] at (3.58,2.95) {$m,\ r$};
\node at (3.8,.7) {$M$};
\draw (1,0) arc(0:27.47:1);
\node at (1.15,.28) {$\theta$};
\draw[arr] (2.4,1.6)--(1.2,.976) node[left] {$v_c$};
\draw[arr] (4.2,.45)--(5.6,.45) node[right] {$v_0$};
\node at (2.8,-.55) {球向左下运动，楔块向右};
\end{tikzpicture}
""",
"q3-forces":r"""
\begin{tikzpicture}[scale=1.15]
\draw[thick] (-2,-1)--(2,1);
\draw[thick] (-.2907,.5814) circle(.65);
\coordinate (C) at (-.2907,.5814);
\draw[arr] (C)--++(0,-1.6) node[right] {$mg$};
\draw[arr] (C)--++(-1.7,0) node[left] {$ma_0$};
\draw[arr] (C)--++(-.65,1.3) node[above] {$N_1$};
\draw[arr] (0,0)--++(1.1,.55) node[above right] {$f$};
\node at (.4,2.6) {楔块系的球受力};
\node at (.3,-1.6) {惯性力水平向左；摩擦沿斜面向上};
\end{tikzpicture}
""",
"q4-bridge":r"""
\begin{tikzpicture}[scale=.75]
\draw[thick] (-.8,0)--(9.5,0);
\begin{scope}[rotate=45]
\draw[thick,fill=gray!12] (0,0)--(7.5,0)--(7.5,.414214)--(0,.414214)--cycle;
\end{scope}
\begin{scope}[shift={(8.778175,0)},rotate=135]
\draw[thick,fill=gray!12] (0,-.414214)--(7.5,-.414214)--(7.5,0)--(0,0)--cycle;
\end{scope}
\draw[thick,fill=white] (.639088,3.474874)--(8.139088,3.474874)--(8.139088,3.889088)--(.639088,3.889088)--cycle;
\draw[thick,fill=white] (2.389088,3.267767) circle(.207107);
\draw[thick,fill=white] (6.389088,3.267767) circle(.207107);
\draw[thick,fill=white] (4.389088,4.096194) circle(.207107);
\node[font=\scriptsize] at (2.389088,3.267767) {$A$};
\node[font=\scriptsize] at (6.389088,3.267767) {$A'$};
\node[font=\scriptsize] at (4.389088,4.096194) {$B$};
\node[left] at (.639088,3.681981) {$C$};
\node[left] at (.35,.65) {$D$};
\node[right] at (8.4,.65) {$D'$};
\draw (1,0) arc(0:45:1); \node at (1.12,.35) {$\theta$};
\draw[<->,dashed] (-.6,.6)--(2.228427,3.428427) node[midway,left] {$a$};
\draw[<->,dashed] (-1,1)--(3.242641,5.242641) node[midway,left] {$b$};
\node at (4.4,-.7) {侧视投影：相交长杆不发生接触};
\end{tikzpicture}
""",
"q4-forces":r"""
\begin{tikzpicture}[scale=.88]
\draw[thick] (0,0) rectangle(5,.35);
\node at (2.5,.65) {$C$};
\draw[arr] (.55,-.5)--(.55,.1) node[above] {$N_1$};
\draw[arr] (4.45,-.5)--(4.45,.1) node[above] {$N_1$};
\draw[arr] (2.3,.35)--(2.3,-1.2) node[below] {$N_3$};
\draw[arr] (2.8,.1)--(2.8,-.8) node[right] {$Mg$};
\draw[arr] (.55,0)--(-.6,0) node[left] {$f_1$};
\draw[arr] (4.45,0)--(5.7,0) node[right] {$f_1$};
\begin{scope}[shift={(7,-1.0)}]
\draw[thick] (0,0)--(3.3,3.3)--(3.55,3.05)--(.25,-.25)--cycle;
\node at (3.8,2.2) {$D$};
\draw[arr] (.15,-.2)--(.15,1.0) node[above left] {$N_5$};
\draw[arr] (.15,-.2)--(1.3,-.2);
\node[below] at (.8,-.35) {$f_5$};
\draw[arr] (1.3,1.1)--(2.4,0) node[below right] {$N_2$};
\draw[arr] (1.1,1.3)--(.3,.5);
\node[left] at (0,.45) {$f_2$};
\draw[arr] (2.7,2.7)--(1.9,3.5) node[above] {$N_4$};
\draw[arr] (1.75,1.6)--(1.75,.1);
\node[below] at (1.8,-.12) {$Mg$};
\end{scope}
\end{tikzpicture}
""",
"q5-dipole":r"""
\begin{tikzpicture}[scale=1]
\draw[arr] (0,-1.2)--(0,3.4) node[above] {$z$};
\draw[arr,very thick] (0,-.6)--(0,.6) node[left] {$\boldsymbol p$};
\fill (0,0) circle(1.6pt) node[below right] {$O$};
\draw[arr] (0,0)--(2.4,2.1) node[midway,below right] {$\boldsymbol r$};
\fill (2.4,2.1) circle(2pt) node[right] {$e,\ m$};
\draw (0,1) arc(90:41.19:1);
\node at (.46,1.2) {$\theta$};
\draw[dashed] (2.4,2.1)--(0,2.1);
\end{tikzpicture}
""",
"q5-boundary":r"""
\begin{tikzpicture}[scale=1]
\draw[arr] (-3,0)--(3,0) node[right] {$x$};
\draw[arr] (0,-3)--(0,1.8) node[above] {$z$};
\draw[dashed] (0,0) circle(2.2);
\draw[very thick,blue] (2.2,0) arc(0:-180:2.2);
\draw[arr,blue] (1.91,-1.1)--(1.69,-1.38);
\draw[arr,blue] (-1.1,-1.91)--(-1.4,-1.69);
\fill (2.2,0) circle(2pt) node[above] {静止释放};
\fill (-2.2,0) circle(2pt) node[above] {转向点};
\fill (0,-2.2) circle(2pt) node[below right] {速率最大};
\draw[<->] (0,0)--(-1.56,-1.56) node[midway,left] {$r_0$};
\node[above left] at (0,0) {$O$};
\end{tikzpicture}
""",
"q6-levitation":r"""
\begin{tikzpicture}[scale=1]
\draw[thick] (0,0) ellipse(3 and .8);
\draw[arr] (0,-.3)--(0,4.7) node[above] {$z$};
\draw[thick] (0,3.45) circle(.5);
\draw[dashed] (-.5,3.45) arc(180:360:.5 and .16);
\draw (-.5,3.45) arc(180:0:.5 and .16);
\node[right] at (.6,3.45) {$a,\ \sigma,\ G$};
\draw[<->] (-1.05,0)--(-1.05,3.45) node[midway,left] {$h$};
\draw[<->] (0,0)--(3,0) node[midway,below] {$b$};
\node at (2.4,1.2) {$I_0\cos\omega t$};
\draw[arr] (0,3.45)--(0,4.35) node[left] {$\langle F_z\rangle$};
\draw[arr] (.12,3.2)--(.12,2.2) node[right] {$G$};
\end{tikzpicture}
""",
"q6-current":r"""
\begin{tikzpicture}[scale=1]
\draw[thick] (0,0) circle(1.8);
\draw[arr] (0,-2.3)--(0,2.7) node[above] {$\boldsymbol B_e$};
\draw[dashed] (-1.8,0) arc(180:360:1.8 and .45);
\draw[thick] (-1.8,0) arc(180:0:1.8 and .45);
\draw[arr] (1.42,.29)--(1.05,.37);
\node[right] at (2.0,.2) {$K_\phi=-\dfrac{3B_e}{2\mu_0}\sin\theta$};
\draw[arr,very thick] (0,.65)--(0,-.65);
\node[left] at (-.1,-.6) {$\boldsymbol m$};
\node at (0,-2.8) {感应磁矩与外场反向；球内总场为零};
\end{tikzpicture}
""",
"q7-atmosphere":r"""
\begin{tikzpicture}[scale=.92]
\fill[gray!20] (0,0) circle(1.6);
\draw (0,0) circle(1.6);
\draw (0,0) circle(2.1);
\draw (0,0) circle(2.6);
\draw (0,0) circle(3.1);
\node at (0,0) {地球};
\node[rotate=-45,font=\small] at (45:1.86) {对流层};
\node[rotate=-45,font=\small] at (45:2.36) {同温层};
\node[rotate=-45,font=\small] at (45:2.87) {逆温层};
\node at (0,-3.65) {层厚为示意，不按地球比例绘制};
\end{tikzpicture}
""",
"q7-refraction":r"""
\begin{tikzpicture}[scale=1]
\draw[thick] (-.5,0)--(9,0); \draw[thick] (-.5,2)--(9,2);
\node[left] at (-.5,1) {冷层 $v_i$};
\node[left] at (-.5,2.7) {暖层 $v_o$};
\node[left] at (-.5,-.7) {暖层 $v_o$};
\draw[dashed] (2,1.2)--(2,3.5);
\draw[arr] (1.1,1)--(2,2);
\draw[arr] (2,2)--(3.299,3.2);
\draw[arr,dashed] (2,2)--(2.9,1);
\node at (1.45,2.5) {$\alpha_i<\alpha_c$};
\draw[arr,blue] (3.6,1)--(6,2);
\draw[arr,blue] (6,2)--(8.4,1);
\draw[dashed] (6,1.2)--(6,3.2);
\node at (6.8,2.65) {$\alpha_i>\alpha_c$};
\node at (2.0,-.75) {允许折射};
\node at (6.4,-.75) {全反射，反射角等于入射角};
\end{tikzpicture}
""",
"q7-earth-rays":r"""
\begin{tikzpicture}[scale=.7]
\begin{scope}
\fill[gray!18] (0,0) circle(2.3); \draw (0,0) circle(2.3);
\draw (0,0) circle(2.7); \draw (0,0) circle(3.2);
\draw[arr,thick] (-1.4,2.3)--(1.4,2.3);
\fill (-1.4,2.3) circle(2pt); \fill (1.4,2.3) circle(2pt);
\node at (0,-3.8) {短程：受地球遮挡};
\node at (0,0) {地球};
\end{scope}
\begin{scope}[shift={(8,0)}]
\fill[gray!18] (0,0) circle(2.3); \draw (0,0) circle(2.3);
\draw (0,0) circle(2.7); \draw (0,0) circle(3.2);
\foreach \a in {0,40,...,320}{
\draw[arr,blue,thick] (\a:3.2)--({\a+40}:3.2);
}
\node at (0,0) {地球};
\node at (0,-3.8) {远程：冷层内反复全反射};
\end{scope}
\node at (4,-4.7) {层厚夸大；蓝色弦段给出上界面反射的一类路径};
\end{tikzpicture}
""",
"q8-apparatus":r"""
\begin{tikzpicture}[scale=1]
\draw[rounded corners,thick] (-1,-.8) rectangle(.3,.8);
\node at (-.35,1.25) {X射线管};
\node at (-.35,-1.2) {电子轰击阳极};
\draw[arr,thick] (.3,0)--(3.5,0) node[midway,above] {入射光子};
\draw[thick] (3.5,-.65)--(3.5,.65);
\node at (3.5,-1.05) {材料靶};
\draw[arr] (3.5,0)--(6.3,-1.0) node[right] {X射线光谱仪};
\draw[arr] (3.5,0)--(5.5,1.35) node[right] {电子能谱仪};
\draw[dashed] (3.5,0)--(6.2,0);
\draw (4.3,0) arc(0:-19.65:.8);
\node at (4.65,-.26) {$\theta$};
\end{tikzpicture}
""",
"q8-spectrum":r"""
\begin{tikzpicture}[xscale=1.05,yscale=1]
\draw[arr] (0,0)--(7.4,0) node[right] {$\lambda$};
\draw[arr] (0,0)--(0,3.4) node[above] {相对谱强度};
\draw[thick,domain=.2:7,samples=140]
plot(\x,{.2+2.25*exp(-(\x-2)*(\x-2)/.06)+2.7*exp(-(\x-5)*(\x-5)/.45)});
\draw[dashed] (2,0)--(2,2.5); \draw[dashed] (5,0)--(5,3);
\node[below] at (2,0) {$\lambda_0$}; \node[below] at (5,0) {$\lambda_1$};
\node at (2,3.0) {近弹性峰}; \node at (5,3.5) {康普顿峰};
\node at (3.5,-.9) {峰位与峰宽的定性示意，不作定量读数};
\end{tikzpicture}
""",
"q8-momentum":r"""
\begin{tikzpicture}[scale=1.1]
\coordinate (O) at (0,0); \coordinate (A) at (4,0); \coordinate (B) at (2.6,1.5);
\draw[arr,thick] (O)--(A) node[midway,below] {$\boldsymbol p_0$};
\draw[arr,thick] (O)--(B) node[midway,above left] {$\boldsymbol p_1$};
\draw[arr,thick] (B)--(A) node[midway,right] {$\boldsymbol p_e$};
\draw (1,0) arc(0:29.98:1); \node at (1.22,.35) {$\theta$};
\node at (2,-.8) {$\boldsymbol p_0=\boldsymbol p_1+\boldsymbol p_e$};
\end{tikzpicture}
"""
}
PRE=r"""% !TEX program = xelatex
\documentclass[12pt,fontset=fandol]{ctexart}
\usepackage[margin=5mm]{geometry}
\usepackage{tikz,amsmath,amssymb,graphicx}
\usepackage[active,tightpage]{preview}
\PreviewEnvironment{tikzpicture}
\setlength\PreviewBorder{5pt}
\usetikzlibrary{arrows.meta,calc}
\pagestyle{empty}
\tikzset{arr/.style={-{Stealth[length=2mm]},semithick}}
\begin{document}
\begin{center}
"""
def main():
    (ROOT/'figures').mkdir(exist_ok=True)
    for name,body in FIGS.items():
        (ROOT/'figures'/f'{name}.tikz').write_text(body.strip()+'\n')
        (ROOT/'figures'/f'{name}.tex').write_text(PRE+body+'\n\\end{center}\n\\end{document}\n')
    print(f'{len(FIGS)} editable figures generated')
if __name__=='__main__':main()
