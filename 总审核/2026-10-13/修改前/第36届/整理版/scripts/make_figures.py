#!/usr/bin/env python3
"""Editable diagrams tied to the geometry and equations of the 2019 paper."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FIGS={
"q1-stool":r"""
\begin{tikzpicture}[scale=.8]
\draw[thick,fill=gray!8] (0,3) ellipse(2 and .55);
\draw[very thick] (0,2.9)--(0,1.6)--(-1.9,.5);
\draw[very thick] (0,1.6)--(1.6,.65); \draw[very thick] (0,1.6)--(.6,-.25);
\draw[dashed] (-1.9,.5)--(1.6,.65)--(.6,-.25)--cycle;
\node[left] at (-1.9,.5) {$A$};\node[right] at (1.6,.65) {$B$};
\node[below] at (.6,-.25) {$C$};\node[below] at (-.7,.08) {$a$};
\fill (0,2.2) circle(2pt) node[right] {$G$};
\fill (0,3) circle(2pt) node[above right] {$O$};
\draw[thick,fill=blue!8] (-2,3.05)--(-2,3.8) arc(180:0:.45 and .12)--(-1.1,3.05);
\draw[thick] (-1.55,3.05) ellipse(.45 and .12);
\draw[arr,red] (0,3)--(-1.95,3) node[midway,below] {$OD$};
\node[left] at (-2,3) {$D$};\node at (-.8,4.25) {杯心移动$R-r$};
\begin{scope}[shift={(6,1.7)}]
\draw[thick] (-1.6,-.92)--(1.6,-.92)--(0,1.85)--cycle;
\node[left] at (-1.6,-.92) {$A$};\node[right] at (1.6,-.92) {$C$};\node[above] at (0,1.85) {$B$};
\draw[dashed] (0,1.85)--(0,-1.2); \fill (0,0) circle(2pt) node[right] {$O'$};
\draw[arr,red] (0,0)--(0,-.65);
\node[right] at (.15,-.55) {移向$AC$};
\node at (0,-1.65) {水平投影：$OD\perp AC$};
\end{scope}
\end{tikzpicture}
""",
"q1-cup":r"""
\begin{tikzpicture}[scale=.9]
\draw[thick] (0,3)--(0,0)--(2,0)--(2,3);
\fill[blue!12] (.02,.02) rectangle(1.98,1.3);
\draw[blue] (0,1.3)--(2,1.3); \node[right] at (2.1,1.3) {$h$};
\draw[very thick] (0,0)--(2,0); \node[below] at (1,-.2) {杯底$m/5$};
\draw[<->] (-.45,0)--(-.45,3) node[midway,left] {$H$};
\fill[red] (1,.65) circle(2pt) node[right] {$h/2$};
\node at (1,3.55) {杯壁$4m/5$};
\begin{scope}[shift={(4.4,.2)},xscale=3,yscale=4]
\draw[arr] (0,0)--(1.15,0) node[right] {$h/H$};
\draw[arr] (0,0)--(0,.65) node[above] {$Y/H$};
\draw[thick,blue,domain=0:1,samples=100] plot(\x,{(.4+\x*\x)/(1+2*\x)});
\draw[gray,dashed] (0,0)--(.58,.58);
\fill[red] (.306226,.306226) circle(.65pt);
\node[above right] at (.32,.31) {$Y=h_*$};
\draw[dashed] (.306226,0)--(.306226,.306226);
\node[below] at (.306226,0) {$h_*/H$};
\end{scope}
\end{tikzpicture}
""",
"q1-support":r"""
\begin{tikzpicture}[scale=1.2]
\coordinate(A) at(-2,-1.155); \coordinate(B) at(0,2.31); \coordinate(C) at(2,-1.155);
\draw[thick] (A)--(B)--(C)--cycle;
\foreach \p in {A,B,C}{\fill (\p) circle(2pt);}
\node[left] at(A) {$A$};\node[above left] at(B) {$B$};\node[right] at(C) {$C$};
\draw[arr,gray] (-2.6,0)--(2.6,0) node[right] {$x$};
\draw[arr,gray] (0,-1.7)--(0,2.6) node[right] {$y$};
\fill (0,0) circle(2pt) node[above right] {$O'$};
\fill[red] (0,-.7) circle(2pt) node[right] {杯心$(0,-s_c)$};
\draw[<->] (-.5,0)--(-.5,-.7) node[midway,left] {$s_c$};
\draw[<->] (2.5,0)--(2.5,-1.155) node[midway,right] {$b_s$};
\node[blue,below] at(-1.8,-1.3) {$\Delta N_A=+X$};
\node[blue,below] at(1.8,-1.3) {$\Delta N_C=+X$};
\node[red,above] at(0,2.85) {$\Delta N_B=-2X$};
\end{tikzpicture}
""",
"q2-cart":r"""
\begin{tikzpicture}[scale=.8]
\draw[thick] (-4,-.2)--(2.2,-.2);
\draw[thick] (0,.8) circle(1);
\draw[thick,gray] (.55,1.1) circle(1);
\draw[very thick] (-3.3,-.05)--(1.1,1.12);
\draw[very thick] (-2.75,.25)--(1.65,1.42);
\draw[thick,fill=gray!15] (-1.1,.535)--(1.1,1.12)--(1.65,1.42)--(-.55,.835)--cycle;
\draw[very thick] (0,.8)--(.55,1.1);
\fill (0,.8) circle(2pt) node[above left] {$O$};
\node[left] at(-3.3,-.05) {把手末端};
\node[right] at(1.65,1.42) {前端};
\node at (-1.55,1.1) {$m$};\node[right] at(2.2,2.15) {平板$2m$};
\draw[arr,gray] (2.2,2.15)--(.8,1.18);
\draw[<->] (-3.35,2.0)--(1.05,3.17) node[midway,above] {$2l$};
\draw[<->] (-1.1,2.2)--(1.1,2.785) node[midway,below] {$l$};
\draw[<->] (0,.8)--(.8,.2) node[midway,right] {$r$};
\node at (-.1,-.75) {两轮各$m$，细轮缘；轴质量忽略};
\begin{scope}[shift={(6.7,.8)}]
\draw[thick] (-3,-1)--(1.6,-1);
\draw[thick] (0,0) circle(1);
\draw[very thick] (-3,-1)--(1,.333);
\draw[dashed] (-3,0)--(1.3,0);
\fill (-.5,-.167) circle(2pt) node[below right] {$C$};
\fill (0,0) circle(2pt) node[above] {$O$};
\node[below] at(-3,-1) {$A$};
\draw[<->] (-3.4,-1)--(-3.4,0) node[midway,left] {$r$};
\draw[<->] (-2.8,-1.5)--(.2,-.5) node[midway,below] {$3l/2$};
\node at (.85,.02) {$\theta$};
\node at (-1,-2.15) {$CO=l/4$，$CA=5l/4$};
\end{scope}
\end{tikzpicture}
""",
"q2-stages":r"""
\begin{tikzpicture}
\foreach \x/\title in {0/碰前定轴,4.8/碰后解锁,9.6/首次纯滚动}{
\begin{scope}[shift={(\x,0)}]
\node at (0,2.9) {\title};
\draw (0,1) circle(.8); \draw[thick] (-1.8,.35)--(.7,1.3);
\draw[thick] (-2,.2)--(1,.2);
\fill (0,1) circle(1.8pt);
\end{scope}}
\node at(0,-.35) {$\omega_f>0,\quad v_O=0$};
\node at(4.8,-.35) {$v=v_0,\quad\omega_w=0$};
\node at(9.6,-.35) {$v=v_1=r\omega_w$};
\draw[arr] (1.7,1.4)--(2.8,1.4) node[midway,above] {碰撞};
\draw[arr] (6.5,1.4)--(7.6,1.4) node[midway,above] {滑动};
\draw[arr,blue] (4.8,1)--(5.9,1);
\draw[arr,blue] (9.6,1)--(10.7,1);
\node[red] at (7.3,-1.15) {$u=v-r\omega_w\searrow0$};
\end{tikzpicture}
""",
"q2-forces":r"""
\begin{tikzpicture}[scale=.95]
\foreach \xx/\lab/\sgn in {0/阶段I：滑动/-1,7/阶段II：滚动/1}{
\begin{scope}[shift={(\xx,0)}]
\node at(0,2.75) {\lab};
\draw[thick] (0,1) circle(1); \draw[thick] (-1.5,0)--(1.8,0);
\draw[arr] (0,0)--(0,.35); \node at(-.6,-.35) {$N_w$};
\draw[gray] (-.45,-.2)--(0,.18);
\draw[arr] (-.2,1)--(-.2,.5); \node[left] at(-1.3,.62) {$2mg$};
\draw[gray] (-1.25,.62)--(-.25,.72);
\draw[arr,blue] (.25,1)--(.25,.25); \node[right] at(1.25,.5) {$-Y$};
\draw[gray] (1.15,.5)--(.3,.62);
\draw[arr,blue] (0,1)--({-\sgn*1.25},1);
\ifnum\sgn<0 \node[blue,right] at(1.25,1) {$-X$};
\else \node[blue,left] at(-1.25,1) {$-X$};\fi
\draw[arr,red] (0,0)--(\sgn*1.2,0);
\ifnum\sgn<0 \node[red,left] at(-1.25,0) {$-\mu N_w$};
\else \node[red,right] at(1.25,0) {$f_2$};\fi
\end{scope}}
\begin{scope}[shift={(3.4,-3.2)}]
\draw[very thick] (-3,0)--(1,1.33);
\fill (0,1) circle(2pt) node[above] {$O$};
\fill (-.5,.833) circle(2pt) node[above left] {$C$};
\draw[arr] (-3,0)--(-3,1) node[above] {$N$};
\draw[arr,red] (-3,0)--(-4.1,0) node[left] {$\mu N$};
\draw[arr] (-.5,.833)--(-.5,-.15) node[below] {$4mg$};
\draw[arr,blue] (0,1)--(0,2) node[above] {$Y$};
\draw[arr,blue] (0,1)--(1.2,1) node[right] {$X$};
\node at (0,-1) {车架无角加速度，绕$C$取矩};
\end{scope}
\end{tikzpicture}
""",
"q3-rails":r"""
\begin{tikzpicture}[scale=.95]
\begin{scope}[rotate=18]
\draw[thick,fill=gray!12] (0,0) rectangle(6,.22);
\draw[thick,fill=gray!12] (0,1.15) rectangle(6,1.37);
\draw[thick,fill=blue!15] (3.2,.22) rectangle(3.42,1.15);
\node[above] at(3.7,2.9) {弹丸$m,R$};
\draw[arr,gray] (3.7,2.65)--(3.31,1.1);
\draw[arr,red] (.2,.1)--(1.8,.1) node[midway,below] {$I$};
\draw[arr,red] (1.8,1.26)--(.2,1.26);
\draw[arr,red] (3.31,.35)--(3.31,1.05);
\draw[thick] (0,.1)--(-.7,.1)--(-.7,1.26)--(0,1.26);
\node[left] at(-.7,.7) {恒流源};
\draw[arr,blue] (3.6,.65)--(4.8,.65) node[right] {$v$};
\draw[<->] (0,1.95)--(6,1.95) node[midway,above] {$L$};
\draw[<->] (2.7,.22)--(2.7,1.15) node[midway,left] {$d$};
\draw[<->] (6.4,0)--(6.4,.22) node[midway,right] {$2b$};
\end{scope}
\draw[dashed] (0,0)--(5,0); \node at(1.3,.18) {$\theta$};
\end{tikzpicture}
""",
"q3-field":r"""
\begin{tikzpicture}[scale=1.1]
\draw[thick] (-2,0) circle(.5); \draw[thick] (2,0) circle(.5);
\node at(-2,0) {$\odot I$};\node at(2,0) {$\otimes I$};
\draw[very thick,blue] (-1.5,0)--(1.5,0);
\draw[arr,blue] (-.7,0)--(.5,0) node[midway,above] {$I$};
\draw[arr,blue] (.4,.25)--(.4,.9) node[right] {$B$};
\node[red] at(0,1.35) {$\odot F_B$沿轨道};
\node[below] at(0,-.45) {两端点磁场同向};
\draw[<->] (-2,-1.15)--(0,-1.15) node[midway,below] {$q$};
\draw[<->] (0,-1.15)--(2,-1.15) node[midway,below] {$s-q$};
\draw[<->] (-1.5,-2)--(1.5,-2) node[midway,below] {$d$};
\draw[<->] (-2,.8)--(-1.5,.8) node[midway,above] {$b$};
\node at(0,2.1) {$b\le q\le b+d,\quad s=2b+d$};
\end{tikzpicture}
""",
"q3-energy":r"""
\begin{tikzpicture}
\node[draw,rounded corners,minimum width=2.5cm,minimum height=.9cm] (S) at(0,0) {源功$W_s$};
\node[draw] (J) at(5,1.7) {焦耳热$Q_J$};
\node[draw] (K) at(5,0) {机械能$\Delta K+\Delta U_g$};
\node[draw] (B) at(5,-1.7) {磁场能$\Delta U_B$};
\draw[arr] (S.east)--(2,0)--(2,1.7)--(J.west);
\draw[arr,blue] (S.east)--(K.west);
\draw[arr,red] (S.east)--(2,0)--(2,-1.7)--(B.west);
\node[blue,right] at(7,0) {$\frac12\kappa_LI^2L$};
\node[red,right] at(7,-1.7) {$\frac12\kappa_LI^2L$};
\node at(4,-2.7) {恒流时：非焦耳源功在两者之间平分};
\end{tikzpicture}
""",
"q4-resonator":r"""
\begin{tikzpicture}[scale=.9]
\fill[brown!18] (-3,0) rectangle(0,3);
\foreach \x in {-2.6,-2,-1.4,-.8,-.2}{
\foreach \y in {.4,.9,1.4,1.9,2.4}{
\fill[brown!75!black] (\x-.04,\y-.16) rectangle(\x+.04,\y+.16);}}
\node at(-1.5,-.45) {长方形微孔阵列};
\draw[thick,fill=gray!10] (1,0) rectangle(4.6,.35);
\draw[thick] (1,.35)--(1,3)--(4.6,3)--(4.6,.35);
\foreach \x in {1.2,1.8,2.4,3,3.6,4.2}{\draw[thick,fill=gray!30] (\x,2.5) rectangle(\x+.35,3);}
\node at(2.8,1.25) {板后空气层};
\draw[arr] (4.7,2.75)--(5.7,2.75);
\draw[thick] (6.1,3.3)--(6.1,2.2)--(5.7,2.2)--(5.7,0)--(7.1,0)--(7.1,2.2)--(6.7,2.2)--(6.7,3.3);
\draw[dashed] (6.1,3.3)--(6.7,3.3);
\node at(6.4,1) {$V_0$};
\draw[<->] (7.3,2.2)--(7.3,3.3) node[midway,right] {$l$};
\draw[<->] (6.1,3.8)--(6.7,3.8) node[midway,above] {$S$};
\node at(6.4,-.45) {单孔等效模型};
\end{tikzpicture}
""",
"q4-oscillator":r"""
\begin{tikzpicture}[scale=1.1]
\draw[thick] (-2,1.5)--(-.4,1.5)--(-.4,2.5);
\draw[thick] (.4,2.5)--(.4,1.5)--(2,1.5)--(2,-1)--(-2,-1)--(-2,1.5);
\fill[blue!12] (-.4,1.8) rectangle(.4,2.5);
\draw[dashed] (-.6,2.15)--(.6,2.15);
\draw[arr,blue] (1,2.15)--(1,3) node[above] {$x>0$向外};
\draw[arr,red] (0,1.9)--(0,1.1) node[below] {$S\Delta p$};
\node at(0,-.1) {$\Delta V=Sx$};
\node at(0,-.6) {$\Delta p=-\kappa Sx/V_0$};
\node[left] at(-.5,2.55) {$M_p=\rho Sl$};
\node at(0,3.7) {$K_p=\kappa S^2/V_0$};
\end{tikzpicture}
""",
"q4-response":r"""
\begin{tikzpicture}[xscale=2.1,yscale=2]
\draw[arr] (0,0)--(1.9,0) node[right] {$S/S_*$};
\draw[arr] (0,0)--(0,1.6) node[above] {$f/f_*$};
\draw[thick,blue,domain=.03:1.6,samples=90] plot(\x,{sqrt(\x)});
\fill[red] (.36,.6) circle(1pt); \fill[red] (1,1) circle(1pt);
\draw[dashed] (.36,0)--(.36,.6)--(0,.6);
\node[below] at(.36,0) {$0.36$};\node[left] at(0,.6) {$0.60$};
\begin{scope}[shift={(3.3,0)}]
\draw[arr] (.2,0)--(2.1,0) node[right] {$\omega/\omega_0$};
\draw[arr] (.2,0)--(.2,1.3) node[above] {吸收功率};
\draw[thick,red,domain=.25:1.95,samples=180] plot(\x,{.09*\x*\x/((1-\x*\x)^2+.09*\x*\x)});
\draw[dashed] (1,0)--(1,1);
\node[below] at(1,0) {$1$};
\end{scope}
\end{tikzpicture}
""",
"q5-coupling":r"""
\begin{tikzpicture}[scale=1.25]
\draw[dashed] (-3.3,0)--(4.8,0);
\draw[thick,fill=blue!4] (0,0) circle(1.5);
\foreach \h in {.33,-.33}{
\draw[arr,blue] (-3.2,\h)--(-1.464,\h);
\draw[thick,blue] (-1.464,\h)--(1.496,{.33333*\h})--(2.25,0);
}
\draw[thick] (2.25,-.6) rectangle(4.6,.6);
\draw[thick] (2.25,-.24)--(4.6,-.24); \draw[thick] (2.25,.24)--(4.6,.24);
\node[fill=white,inner sep=1pt] at(3.7,0) {$n_1=1.46$};
\node at(3.7,.43) {$n_2=1.45$};
\node at(0,.65) {$n=1.50$};
\fill (0,0) circle(1.5pt) node[below] {$C$};
\node[below] at(1.5,0) {$O$};\node[below] at(2.25,-.65) {光纤端面};
\draw[<->] (-1.5,1.95)--(1.5,1.95) node[midway,above] {$D$};
\draw[<->] (-2.8,-.33)--(-2.8,.33) node[midway,left] {$d_b$};
\end{tikzpicture}
""",
"q5-acceptance":r"""
\begin{tikzpicture}
\draw[thick] (0,-1) rectangle(6,1);
\draw[thick] (0,-.55)--(6,-.55); \draw[thick] (0,.55)--(6,.55);
\draw[dashed] (-2,0)--(6.5,0);
\draw[thick,red] (-1.7,.62)--(0,0)--(2,-.55)--(5.9,.52);
\draw[arr,red] (3.5,-.138)--(4.4,.11);
\draw[dashed] (2,-1.2)--(2,.4);
\node at(-1.05,.12) {$\theta$};\node at(.75,-.12) {$\alpha_f$};
\node at(2.25,-.15) {$i_f$};
\node at(5,0) {$n_1$};\node at(5,.8) {$n_2$};\node at(-1.2,1) {$n_0$};
\node at(2,-1.85) {$n_0\sin\theta=n_1\sin\alpha_f,\quad i_f+\alpha_f=\pi/2$};
\end{tikzpicture}
""",
"q5-focus":r"""
\begin{tikzpicture}[scale=1.2]
\draw[dashed] (-.7,0)--(5.2,0);
\draw[thick] (1.5,0) circle(1.5);
\draw[thick,blue] (-.7,.35)--(.041,.35)--(2.998,.1167)--(3.75,0);
\draw[dashed,red] (.041,.35)--(4.5,0);
\foreach \x/\lab in {0/V_1,1.5/C,3/V_2,3.75/F,4.5/I_1}{
\fill (\x,0) circle(1.5pt); \node[below] at(\x,-.15) {$\lab$};}
\draw[<->] (3,1.8)--(3.75,1.8) node[midway,above] {$0.75\ \mathrm{mm}$};
\draw[<->] (1.5,-1.95)--(3.75,-1.95) node[midway,below] {$f_e=2.25\ \mathrm{mm}$};
\draw[<->] (0,2.6)--(4.5,2.6) node[midway,above] {$z_1=4.50\ \mathrm{mm}$};
\end{tikzpicture}
""",
"q6-decay":r"""
\begin{tikzpicture}
\node[draw,circle] (P) at(0,0) {$\pi$静止};
\draw[arr,blue,very thick] (.9,0)--(3,0) node[right] {$\mu:\ E_\mu^*,\,p^*$};
\draw[arr,red,very thick] (-.9,0)--(-3,0) node[left] {$\bar\nu_\mu:\ p^*c,\, -p^*$};
\node at(0,1.5) {$S_*:\quad E_\mu^*+p^*c=m_\pi c^2$};
\draw[arr] (-2,-1.5)--(2,-1.5) node[right] {$S_*$相对$S$以$v$运动};
\node at(0,-2.25) {实验室能量由发射角决定};
\end{tikzpicture}
""",
"q6-range":r"""
\begin{tikzpicture}[xscale=3.1,yscale=3.2]
\draw[arr] (-1.1,.52)--(1.3,.52) node[right] {$\cos\vartheta_*$};
\draw[arr] (-1.1,.52)--(-1.1,1.18) node[above] {$E_\mu/E_{\max}$};
\draw[thick,blue,domain=-1:1] plot(\x,{(1+.26188772*\x)/1.26188772});
\fill[red] (-1,.584953) circle(.65pt);\fill[red] (1,1) circle(.65pt);
\node[below] at(-1,.52) {$-1$};\node[below] at(1,.52) {$1$};
\node at(-.45,.86) {$u_{\min}=0.939713c$};
\node[above right] at(.7,1.08) {$u_{\max}=0.979791c$};
\node at(.1,.27) {固定质量：能量越大，速率越大};
\end{tikzpicture}
""",
"q6-survival":r"""
\begin{tikzpicture}[xscale=1.4,yscale=3.4]
\draw[arr] (0,0)--(5.4,0) node[right] {$h/h_{1/2}$};
\draw[arr] (0,0)--(0,1.18) node[above] {$P$};
\draw[thick,blue,domain=0:5,samples=120] plot(\x,{2^(-\x)});
\draw[dashed] (1,0)--(1,.5)--(0,.5);
\node[left] at(0,.5) {$1/2$};\node[below] at(1,0) {$1$};
\fill[red] (4.47,.04518) circle(.8pt);
\node[above] at(4.2,.22) {10 km：约$4.52\%$};
\node at(2.5,-.4) {$\Delta\tau=h/(\gamma_\mu u)$};
\end{tikzpicture}
""",
"q7-cloud":r"""
\begin{tikzpicture}[scale=.85]
\draw[thick,fill=gray!8] (-2,3.5) ellipse(2 and .45);
\draw[thick] (-4,3.5)--(-4,2.1) arc(180:360:2 and .45)--(0,3.5);
\draw[dashed] (-4,2.1) arc(180:0:2 and .45);
\foreach \x in {-3.4,-2.7,-2,-1.3,-.6}{\node[red] at(\x,3.5) {$+$};\node[blue] at(\x,2.1) {$-$};}
\draw[arr] (-2,3.15)--(-2,2.45) node[right] {$E$};
\draw[<->] (.7,2.1)--(.7,3.5) node[midway,right] {$d_c=1\ \mathrm{km}$};
\draw[<->] (-2,4.25)--(0,4.25) node[midway,above] {$R_c=2.5\ \mathrm{km}$};
\draw[thick] (-5,0)--(1.8,0) node[right] {导体地面};
\draw[dashed] (-2,2.1)--(-2,0);
\draw[<->] (-4.7,0)--(-4.7,2.1) node[midway,left] {$h_c=6\ \mathrm{km}$};
\draw[blue,thick] (-2,1.8)--(-2.2,1.5)--(-1.85,1.15)--(-2.15,.8)--(-2,0);
\end{tikzpicture}
""",
"q7-images":r"""
\begin{tikzpicture}[scale=.8]
\draw[thick] (-3,0)--(3,0) node[right] {$z=0$};
\draw[arr] (-2.8,-3.8)--(-2.8,4.5) node[above] {$z$};
\foreach \y/\q/\lab in {3.8/{+Q_c}/{h_c+d_c},2.5/{-Q_c}/{h_c},-2.5/{+Q_c}/{-h_c},-3.8/{-Q_c}/{-(h_c+d_c)}}{
\draw[fill=gray!10] (0,\y) circle(.22);
\node[right] at(.5,\y) {$\q,\ z=\lab$};
\draw[dashed] (-2.8,\y)--(-.23,\y);
}
\fill (0,0) circle(2pt);
\draw[arr,blue,very thick] (0,.1)--(0,1.3) node[right] {净场向上};
\node at(0,-4.6) {下半空间：等效镜像，上半空间场相同};
\end{tikzpicture}
""",
"q7-channel":r"""
\begin{tikzpicture}[scale=1.1]
\fill[blue!5] (0,0) circle(1.7);
\draw[thick] (0,0) circle(1.7);
\draw[dashed] (0,0) circle(1.1);
\fill[gray] (0,0) circle(.12);
\foreach \a in {0,60,120,180,240,300}{
\draw[arr,red] ({1.5*cos(\a)},{1.5*sin(\a)})--({.75*cos(\a)},{.75*sin(\a)});}
\draw[<->] (0,-2.15)--(1.7,-2.15) node[midway,below] {$a_{\rm ch}$};
\node at(0,2.3) {$E_r=-E_b$};
\node at(0,-3) {核心$a_0$以外取同轴高斯柱面};
\begin{scope}[shift={(4.5,-1)},xscale=2,yscale=1.4]
\draw[arr] (0,0)--(1.3,0) node[right] {$r/a_{\rm ch}$};
\draw[arr] (0,0)--(0,2) node[above] {$|\rho_q|$};
\draw[thick,blue,domain=.22:1,samples=100] plot(\x,{.4/\x});
\draw[dashed] (.22,0)--(.22,1.82);
\node at(.85,1.65) {$\propto1/r$};
\node at(.6,-.65) {有符号密度为负};
\end{scope}
\end{tikzpicture}
""",
"q7-ring":r"""
\begin{tikzpicture}[scale=.9]
\draw[thick] (-4.5,0)--(4.7,0) node[right] {地面};
\draw[thick] (-4.5,2)--(4.7,2) node[right] {电离层底面};
\draw[blue] (2,0) arc(0:180:2);
\draw[red,thick] (3.2,0) arc(0:180:3.2);
\draw[gray,dashed] (4,0) arc(0:180:4);
\fill (0,0) circle(2pt) node[below] {$O$};
\fill (0,2) circle(2pt) node[above left] {$A$};
\fill (2.498,2) circle(2pt) node[above right] {$B$};
\draw[arr,red] (0,0)--(2.498,2) node[midway,below right] {$ct$};
\draw[<->] (-4.1,0)--(-4.1,2) node[midway,left] {$H_i$};
\draw[<->] (0,1.55)--(2.498,1.55) node[midway,below] {$r_i$};
\draw[arr] (2.55,2.1)--(3.46,2.1);
\node at(.1,4.65) {球面波以$c$传播，交线的径向速度可大于$c$};
\node at(.1,-.8) {$r_i^2+H_i^2=c^2t^2$};
\end{tikzpicture}
""",
"q7-balloon":r"""
\begin{tikzpicture}[xscale=.42,yscale=3]
\draw[arr] (0,0)--(13,0) node[right] {$z/\mathrm{km}$};
\draw[arr] (0,0)--(0,1.22) node[above] {归一化量};
\draw[thick,red,domain=0:12] plot(\x,{1-5*\x/290});
\draw[thick,blue,domain=0:12,samples=100] plot(\x,{(1-5*\x/290)^5.8399519});
\draw[dashed] (12,0)--(12,1.1); \node[below] at(12,0) {$12$};
\node[red] at(7,1.1) {$T/T_0$}; \node[blue] at(8,.42) {$\rho/\rho_0$};
\begin{scope}[shift={(21,.2)},xscale=2.38,yscale=.3333]
\draw[thick,fill=blue!8] (0,1.25) ellipse(.9 and 1.1);
\node at(0,1.5) {氦气};
\draw (0,.15)--(0,-.4); \draw[fill=gray!15] (-.35,-.8) rectangle(.35,-.4);
\draw[arr,blue] (0,2.4)--(0,3.5) node[above] {$\rho_bgV_b$};
\draw[arr,red] (.9,1.3)--(.9,.2) node[right] {$\rho_{\rm He}gV_b$};
\draw[arr,red] (0,-.8)--(0,-1.7) node[below] {$m_Lg$};
\end{scope}
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
