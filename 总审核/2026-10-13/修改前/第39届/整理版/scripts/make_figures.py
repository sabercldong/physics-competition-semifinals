#!/usr/bin/env python3
"""Editable figures generated from the equations in the teaching masters."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FIGS={
"q1-michelson":r"""
\begin{tikzpicture}[scale=1]
\draw[arr,blue] (-3,0)--(-.15,0); \node[above] at (-2.3,0) {发散激光};
\draw[very thick] (-.55,-.55)--(.55,.55); \node[below right] at (.6,-.5) {分光片};
\draw[arr,blue] (0,.1)--(0,2.4); \draw[arr,blue] (.12,2.4)--(.12,.2);
\draw[very thick] (-.7,2.5)--(.7,2.5); \node[above] at (0,2.6) {$M_1$};
\draw[arr,red] (.15,0)--(3,0); \draw[arr,red] (3,-.12)--(.2,-.12);
\draw[very thick] (3.1,-.7)--(3.1,.7); \node[right] at (3.2,.5) {$M_2$};
\draw[arr] (0,-.2)--(0,-2); \node[below] at (0,-2) {观察方向};
\draw[<->] (3.8,-.45)--(4.6,-.45); \node at (4.2,-.9) {平移};
\end{tikzpicture}
""",
"q1-rings":r"""
\begin{tikzpicture}[scale=.75]
\foreach \rad in {.5,.85,1.13,1.4,1.67,1.9}{\draw (0,0) circle(\rad);}
\fill (0,0) circle(2pt); \node at (0,-2.45) {初态：20条亮纹};
\foreach \rad in {.6,1.02,1.4,1.74,1.9}{\draw (6,0) circle(\rad);}
\fill (6,0) circle(2pt); \node at (6,-2.45) {末态：17条亮纹};
\draw[arr] (2.25,0)--(3.75,0);
\node[align=center] at (3,1.35) {$d$减小\\视场固定};
\node at (3,-3.1) {示意只画部分环；计数使用中心到边缘的级次跨度};
\end{tikzpicture}
""",
"q1-slab":r"""
\begin{tikzpicture}[scale=1]
\draw[fill=blue!6] (0,0) rectangle(5,-1.7);
\coordinate (O) at (1,0); \coordinate (B) at (2.15,-1.7);
\draw[arr] (-.4,1.4)--(O); \draw[arr] (O)--(B); \draw[arr] (B)--(3.55,-3.1);
\draw[dashed] (1,1.35)--(1,-2.4); \draw[dashed] (2.15,-1.2)--(2.15,-2.8);
\draw (1,.7) arc(90:135:.7); \node at (.65,.85) {$\theta$};
\node at (1.28,-.65) {$i$}; \node at (4,-.8) {$n$};
\draw[<->] (5.35,0)--(5.35,-1.7) node[midway,right] {$t$};
\node at (2.4,1.85) {平行液层：$\sin\theta=n\sin i$};
\node at (2.4,-3.55) {须比较同一出射波前，不能只比较斜程};
\end{tikzpicture}
""",
"q2-solenoid":r"""
\begin{tikzpicture}[scale=.9]
\draw[decorate,decoration={coil,aspect=.45,segment length=5mm,amplitude=4mm},thick] (0,0)--(6,0);
\draw[arr] (.2,-1)--(-1,-1) node[left] {$F_{\rm hold}$};
\draw[arr] (5.8,-1)--(7,-1) node[right] {$F_{\rm hold}$};
\draw[<->] (0,.9)--(6,.9) node[midway,above] {$l$};
\draw (0,0)--(0,-2)--(6,-2)--(6,0);
\draw[fill=white] (2.5,-2.4) rectangle(3.5,-1.6);
\node at (3,-2) {电路}; \node at (3,-2.95) {恒流源或理想闭合回路};
\node at (3,1.65) {$\mathcal L(l)=\mu_0\pi N^2r^2/l$};
\end{tikzpicture}
""",
"q2-branches":r"""
\begin{tikzpicture}[xscale=6,yscale=3]
\draw[arr] (0,0)--(1.13,0) node[right] {$x=l/l_0$};
\draw[arr] (0,0)--(0,1.18) node[above] {$I_0^2/I_c^2$};
\draw[thick,red,domain=.02:.66667,samples=70] plot(\x,{6.75*(1-\x)*\x*\x});
\draw[thick,blue,domain=.66667:1,samples=50] plot(\x,{6.75*(1-\x)*\x*\x});
\draw[dashed] (.66667,0)--(.66667,1)--(0,1);
\node[below] at (.66667,0) {$2/3$}; \node[left] at (0,1) {$1$};
\node[red] at (.3,.75) {不稳定}; \node[blue] at (.93,.95) {稳定};
\node at (.6,-.45) {峰顶是合并点，不是非线性稳定平衡};
\end{tikzpicture}
""",
"q3-flight":r"""
\begin{tikzpicture}[scale=.9]
\draw[thick] (-.8,0)--(8,0); \draw[arr] (0,0)--(8.4,0) node[right] {$x$};
\draw[arr] (0,0)--(0,3.5) node[above] {$y$};
\draw[thick,blue,domain=0:6,samples=80] plot(\x,{1.65*sqrt(\x)-.674*\x});
\draw[arr] (0,.3)--(0,1.25) node[left] {$V$};
\draw[arr] (2.5,3.1)--(3.6,1.8) node[right] {$\boldsymbol g$};
\node at (5,3.8) {$a_x=g\sin\theta,\quad a_y=-g\cos\theta$};
\node at (4,-.7) {每次离面法向速度相同，飞行时间均为$T$};
\end{tikzpicture}
""",
"q3-impact":r"""
\begin{tikzpicture}[scale=1]
\draw[thick] (-2,0)--(2,0); \draw[thick] (0,.8) circle(.8);
\fill (0,.8) circle(1.4pt); \fill (0,0) circle(1.4pt);
\draw[arr] (0,0)--(0,1.8) node[above] {$J_y$};
\draw[arr] (0,0)--(-1.4,0) node[below left] {$J_x$};
\draw[arr] (.3,.8)--(1.6,.8) node[right] {$v_x$};
\draw[arr] (.65,1.5) arc(45:-35:1); \node at (1.3,1.8) {$\omega>0$};
\node at (0,-.7) {顺时针取正，$u=v_x-R\omega$};
\end{tikzpicture}
""",
"q4-rod":r"""
\begin{tikzpicture}[scale=.9]
\draw[dashed] (-3,-2)--(-3,3.4); \fill (-3,0) circle(1.5pt) node[left] {$O$};
\draw[thick] (-3,0)--(0,0); \fill (0,0) circle(2pt) node[below right] {$P$};
\draw[very thick] (0,0)--(2.5,3);
\draw[dashed] (0,0)--(0,3.5);
\draw (0,1.1) arc(90:50.2:1.1); \node at (.45,1.3) {$\theta$};
\fill (1.25,1.5) circle(1.5pt) node[right] {$C$};
\draw[<->] (-3,-.5)--(0,-.5) node[midway,below] {$R$};
\node at (2.5,2.3) {$2a$}; \node at (-3.9,2.5) {$\omega$};
\node at (0,-2.7) {$\varrho(s)=R+s\sin\theta,\quad z(s)=s\cos\theta$};
\end{tikzpicture}
""",
"q4-intersections":r"""
\begin{tikzpicture}[xscale=1.55,yscale=.45]
\draw[arr] (0,0)--(6.6,0) node[right] {$\theta$};
\draw[arr] (0,-4)--(0,4.7) node[above] {$y$};
\begin{scope}\clip (0,-4) rectangle(6.3,4.2);
\draw[thick,blue,domain=0:6.283,samples=140] plot(\x,{3*sin(\x r)+.6});
\foreach \lo/\hi in {0/1.52,1.62/4.66,4.76/6.28}{
\draw[thick,red,domain=\lo:\hi,samples=150] plot(\x,{-tan(\x r)});}
\end{scope}
\foreach \x/\lab in {1.5708/{\pi/2},3.1416/{\pi},4.7124/{3\pi/2},6.2832/{2\pi}}{
\draw[dashed] (\x,-4)--(\x,4.2); \node[below] at (\x,-4.1) {$\lab$};}
\node[blue] at (1.4,5.45) {$A\sin\theta+B$};
\node[red] at (4.65,5.45) {$-\tan\theta$};
\node at (3.1,-6.25) {示例：$A=3,\ B=0.6$，III象限有两交点};
\end{tikzpicture}
""",
"q4-forces":r"""
\begin{tikzpicture}[scale=.68]
\foreach \xx/\yy/\ang/\dir/\lab in {0/0/40/1/I,5/0/130/1/II,0/-6.4/215/1/III短杆,5/-6.4/240/-1/III长杆,10/-6.4/320/1/IV}{
\begin{scope}[shift={(\xx,\yy)}]
\draw[dashed] (-1.4,-2.2)--(-1.4,2.1); \draw[thin] (-1.4,0)--(0,0);
\fill (0,0) circle(2pt); \node[above right] at (0,.1) {$P$};
\coordinate (C) at ({1.35*sin(\ang)},{1.35*cos(\ang)});
\draw[very thick] (0,0)--({2.7*sin(\ang)},{2.7*cos(\ang)});
\draw[arr,blue] (C)--++({1.1*\dir},0) node[above] {$F_\tau$};
\draw[arr,red] (C)--++(0,-1.3) node[right] {$mg$};
\node at (.2,3) {\lab};
\end{scope}}
\node[align=center] at (10,1.3) {$F_\tau$仅等效力矩\\作用点取质心\\非离心力真实合力};
\end{tikzpicture}
""",
"q4-boundary":r"""
\begin{tikzpicture}[xscale=5,yscale=3]
\draw[arr] (0,0)--(1.25,0) node[right] {$h=3R/(4a)$};
\draw[arr] (0,0)--(0,1.25) node[above] {$q=3g/(4a\omega^2)$};
\draw[thick,domain=0:1,samples=90] plot(\x,{(1-\x^(2/3))^(3/2)});
\node at (.26,.25) {III两解}; \node at (.78,.85) {III无解};
\draw[arr] (.75,.45)--(.48,.22);
\node at (.84,.52) {曲线上重根};
\node[below] at (1,0) {$1$}; \node[left] at (0,1) {$1$};
\end{tikzpicture}
""",
"q5-springs":r"""
\begin{tikzpicture}[scale=1]
\draw[thick] (-1,3)--(1,3);
\draw[decorate,decoration={coil,aspect=.4,segment length=3mm,amplitude=3mm}] (0,3)--(0,.6);
\draw[fill=gray!15] (0,.3) circle(.3); \node[right] at (.4,.3) {$m$};
\draw[decorate,decoration={coil,aspect=.4,segment length=3mm,amplitude=3mm}] (0,0)--(0,-2);
\draw[arr] (0,-2)--(0,-3.1) node[right] {$F(t)=\alpha t$};
\draw[<->] (-.8,3)--(-.8,.3) node[midway,left] {$x_1$};
\draw[<->] (.8,.3)--(.8,-2) node[midway,right] {$x_2$};
\node at (1.8,2) {弹簧1}; \node at (1.8,-1.8) {弹簧2};
\draw[arr] (3.7,1.1)--(3.7,-.25);
\node[align=center] at (3.7,-.85) {向下\\为正};
\end{tikzpicture}
""",
"q5-lengths":r"""
\begin{tikzpicture}[xscale=.85,yscale=.55]
\draw[arr] (0,0)--(8,0) node[right] {$\omega t$};
\draw[arr] (0,0)--(0,9.7) node[above] {$kx/(mg)$};
\draw[thick,red,domain=0:7.4,samples=120] plot(\x,{1+\x-sin(\x r)});
\draw[thick,blue,domain=0:7.4,samples=30] plot(\x,{\x});
\draw[dashed] (0,4)--(7.4,4) node[right] {$kL/(mg)$};
\node[red] at (5,7.4) {$x_1$}; \node[blue] at (6,5.5) {$x_2$};
\node at (4,-1.2) {示例$\alpha=mg\omega$；断裂之后曲线仅为数学延拓};
\end{tikzpicture}
""",
"q5-sinc":r"""
\begin{tikzpicture}[xscale=.6,yscale=2.7]
\draw[arr] (0,0)--(13,0) node[right] {$z=kL\omega/\alpha$};
\draw[arr] (0,-.28)--(0,1.15) node[above] {$\sin z/z$};
\draw[thick,blue,domain=.02:12.6,samples=200] plot(\x,{sin(\x r)/\x});
\draw[dashed,red] (0,.13)--(12.6,.13) node[right] {$1/\ell$};
\node at (6,-.7) {曲线高于水平线的区间对应下弹簧先断};
\end{tikzpicture}
""",
"q6-slab":r"""
\begin{tikzpicture}[scale=.9]
\draw[fill=blue!6] (0,-1.8) rectangle(6,1.8);
\draw[very thick] (0,-1.8)--(0,1.8); \draw[very thick] (6,-1.8)--(6,1.8);
\node[above] at (0,1.8) {$\sigma_-$}; \node[above] at (6,1.8) {$\sigma_+$};
\node at (3,.8) {$n=n_0+\delta n,\quad T=T_0+\delta T$};
\node at (3,-.1) {背景电荷密度$+en_0$};
\draw[arr] (-2,-2.5)--(8,-2.5) node[right] {$x$};
\node[below] at (0,-2.5) {$-L$}; \node[below] at (6,-2.5) {$L$};
\node at (-1.2,0) {$E=0$}; \node at (7.2,0) {$E=0$};
\node at (3,-1.1) {$E'=-e\delta n/\varepsilon_0$};
\end{tikzpicture}
""",
"q6-modes":r"""
\begin{tikzpicture}[xscale=2.5,yscale=.9]
\draw[arr] (-1.5,0)--(1.6,0) node[right] {$x/\lambda$};
\draw[arr] (0,-1.8)--(0,2.8);
\draw[thick,blue,domain=-1.2:1.2,samples=70] plot(\x,{(exp(\x)+exp(-\x))/2});
\draw[thick,red,domain=-1.2:1.2,samples=70] plot(\x,{(exp(\x)-exp(-\x))/2});
\node[blue] at (-1.1,2.8) {偶模$\cosh$};
\node[red] at (1.1,-1.7) {奇模$\sinh$};
\node at (.1,-2.6) {表面电荷之和决定偶模，之差决定奇模};
\end{tikzpicture}
""",
"q7-wall":r"""
\begin{tikzpicture}[scale=.95]
\draw[very thick] (4,-2)--(4,2);
\draw[arr] (-.6,0)--(5.5,0) node[right] {$x$};
\draw[arr,blue] (.7,-1.5)--(4,.5); \draw[arr,blue] (4,.5)--(.7,2.5);
\draw[dashed] (4,.5)--(1.5,.5);
\node at (1.7,-1.9) {$p_x=p\cos\theta$};
\node at (2.5,3.1) {$\Delta p_{\rm wall}=2p\cos\theta$};
\node at (4.8,1.5) {$dS$};
\node at (2,-2.3) {撞壁通量还有一因子$c\cos\theta$};
\end{tikzpicture}
""",
"q7-cooling":r"""
\begin{tikzpicture}[xscale=.9,yscale=4]
\draw[arr] (0,0)--(7.6,0) node[right] {$r/r_i$};
\draw[arr] (0,0)--(0,1.2) node[above] {$T/T_i$};
\draw[thick,blue,domain=1:7,samples=90] plot(\x,{1/\x});
\draw[dashed] (1,0)--(1,1)--(0,1);
\draw[dashed] (2.6667,0)--(2.6667,.375)--(0,.375);
\node[below] at (2.6667,0) {$8/3$}; \node[left] at (0,.375) {$3/8$};
\node at (5,.7) {$Tr=\text{常量}$};
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
