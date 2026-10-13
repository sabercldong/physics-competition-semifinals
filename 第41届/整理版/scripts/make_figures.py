#!/usr/bin/env python3
"""Editable TikZ diagrams for every question and its principal derivation."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FIGS={
'q1-building':r'''
\begin{tikzpicture}[scale=.92]
\draw[thick](-3,-1.2)--(2,-1.2);
\draw[thick](-3,-1.2)--(-3,1);
\draw[decorate,decoration={zigzag,segment length=4mm,amplitude=2mm}](-3,-.3)--(-.9,-.3);
\node[above]at(-2,.05){$k$};
\draw[fill=gray!12](-.9,-1.1)rectangle(1.1,.5);
\node at(.1,-.3){$M$};
\draw[thick](.1,.5)--(.1,2.5);
\fill(.1,2.5)circle(2pt);
\draw[dashed](.1,2.5)--(.1,.8);
\draw[thick](.1,2.5)--(-.7,1.05);
\filldraw[fill=white](-.7,1.05)circle(.16)node[left=6pt]{$m$};
\node[left]at(-.38,1.9){$l$};
\draw(.1,1.9)arc(-90:-119:.6);
\node at(-.06,1.63){$\theta$};
\draw[->,thick](2,.05)--(1.15,.05)node[midway,above]{$F$};
\draw[->](-.1,-1.8)--(-1.5,-1.8)node[left]{$+x$};
\end{tikzpicture}
''',
'q1-response':r'''
\begin{tikzpicture}
\draw[->](0,0)--(6,0)node[right]{$\omega/\Omega$};
\draw[->](0,0)--(0,2.8)node[above]{$A$};
\draw[blue,thick](.2,.6)..controls(1.0,.7)and(1.5,1.4)..(1.75,2.6);
\draw[blue,thick](1.95,2.6)..controls(2.15,.4)and(2.55,.15)..(3,0);
\draw[blue,thick](3,0)..controls(3.4,.1)and(3.7,.5)..(4.05,2.6);
\draw[blue,thick](4.25,2.6)..controls(4.6,.6)and(5,.4)..(5.7,.2);
\foreach \x/\lab in {1.85/{\omega_-/\Omega},3/{1},4.15/{\omega_+/\Omega}}{\draw[dashed](\x,0)--(\x,2.8);\node[below]at(\x,0){$\lab$};}
\node at(3,3.2){无阻尼响应示意，峰处发散};
\node[below]at(3,-.65){$\omega_0=\Omega$ 为调谐反共振点};
\end{tikzpicture}
''',
'q2-collision':r'''
\begin{tikzpicture}[scale=.9]
\draw[->](-1.5,0)--(3.2,0)node[right]{$x$};
\draw[->](0,-2)--(0,3.5)node[above]{$y$};
\draw[thick](0,0)circle(.5)node[below right=10pt]{$Q$};
\draw[thick](-.5,.866)circle(.5)node[left=14pt]{$T$};
\draw[dashed](-1.5,2.6)--(.55,-.95);
\draw[->,very thick](-.5,.866)--(-1.5,2.598)node[left]{$\boldsymbol v_T$};
\draw[->,very thick](0,0)--(2.25,1.30)node[right]{$\boldsymbol v_{Q0}$};
\draw[->,blue,thick](0,-1.65)--(0,-.6)node[left,midway]{$v_0$};
\draw(0,1.8)arc(90:120:1.8);\node at(-.45,2.02){$\phi$};
\draw(0,.95)arc(90:30:.95);\node at(.7,.85){$\theta$};
\draw(-.15,.2598)--(.1098,.4098)--(.2598,.15);
\node[below]at(1.25,-.7){$\boldsymbol n\perp\boldsymbol t$};
\end{tikzpicture}
''',
'q2-impact':r'''
\begin{tikzpicture}
\draw[thick](-1.6,0)--(1.6,0);
\draw[thick](0,1)circle(1);\fill(0,1)circle(2pt);
\draw[->,thick](-1.4,1.4)--(-.25,1.4);
\node[left]at(-1.4,1.4){$\mathcal J$};
\draw[dashed](-.92,1.4)--(.2,1.4);
\draw[<->](-1.55,0)--(-1.55,1.4)node[midway,left]{$h$};
\draw[<->](.1,0)--(.1,1)node[midway,right]{$R$};
\draw[->,thick](.4,1)--(1.8,1)node[right]{$v_0$};
\draw[->](.5,1.65)arc(52:-30:.82);
\node[right]at(.85,2){$\omega_{0x}<0$};
\node[below]at(0,0){$C$};
\end{tikzpicture}
''',
'q2-spin':r'''
\begin{tikzpicture}
\draw[thick](-1.6,0)--(1.6,0);
\draw[thick](0,1)circle(1);
\fill(0,1)circle(2pt);
\draw[->,thick](-1.4,1.4)--(-.25,1.4)node[midway,above]{$\mathcal J$};
\draw[dashed](-.92,1.4)--(.2,1.4);
\draw[<->](-1.55,0)--(-1.55,1.4)node[midway,left]{$h$};
\draw[<->](.1,0)--(.1,1)node[midway,right]{$R$};
\draw[->,thick](.4,1)--(1.8,1)node[right]{$v_0$};
\draw[->](.5,1.65)arc(52:-30:.82);
\node[right]at(.85,2){$\omega_x<0$};
\node[below]at(0,0){$C$};
\node[below]at(0,-.5){竖直大圆截面};
\begin{scope}[xshift=5cm]
\draw[thick](-1.3,0)--(1.6,0);\draw(0,1)circle(1);
\draw[->,blue,thick](0,1)--(1.5,1)node[right]{$\boldsymbol v$};
\draw[->,red,thick](0,0)--(-1.2,0)node[left]{$\boldsymbol\omega\times\boldsymbol R_C$};
\node[below]at(0,-.5){$\boldsymbol u=\boldsymbol v+\boldsymbol\omega\times\boldsymbol R_C$};
\end{scope}
\end{tikzpicture}
''',
'q2-trajectory':r'''
\begin{tikzpicture}
\draw[->](0,0)--(3.8,0)node[right]{$x$};
\draw[->](0,0)--(0,4)node[above]{$y$};
\draw[blue,thick]plot[domain=0:.247436,samples=50]({15*(.433013*\x-.25*\x*\x)},{15*(.25*\x+.433013*\x*\x)});
\draw[red,thick](1.3776,1.3255)--(2.72,3.34);
\fill(1.3776,1.3255)circle(2pt)node[right=8pt]{纯滚起点};
\draw[->,blue](0,0)--(.9,.52)node[right]{$\boldsymbol v_{Q0}$};
\draw[->,red](1.3776,1.3255)--(1.99,2.245)node[right]{$\boldsymbol v_f$};
\node[blue]at(2.5,.7){滑动段};
\node[red]at(1.4,3.5){纯滚直线};
\node[below]at(1.8,-.55){示例：纯滚入射，$\phi=30^\circ$};
\end{tikzpicture}
''',
'q3-mixing':r'''
\begin{tikzpicture}
\draw[thick](0,0)rectangle(2.5,2.8);
\fill[orange!20](.02,.02)rectangle(2.48,1.4);
\fill[blue!15](.02,1.4)rectangle(2.48,2.78);
\draw[dashed](0,1.4)--(2.5,1.4);
\node at(1.25,.75){剩余石油 $V$};\node at(1.25,2.05){注入水 $V$};
\draw[->,thick](-1.2,2.2)--(-.1,2.2)node[midway,above]{$t_w$};
\draw[->,thick](2.6,2.2)--(4,2.2)node[midway,above]{抽出油 $V$};
\node[below]at(1.25,0){区域总体积 $2V$ 不变};
\begin{scope}[xshift=5.2cm]
\draw[thick](0,0)rectangle(2.5,2.8);\fill[green!15](.02,.02)rectangle(2.48,2.78);
\node at(1.25,1.8){均匀混合};\node at(1.25,1.1){末态 $T_f,\ p_f$};
\node[below]at(1.25,0){体积相等，热容量不同};
\end{scope}
\end{tikzpicture}
''',
'q3-bonds':r'''
\begin{tikzpicture}
\foreach \x in {0,1,2,3,4}{\foreach \y in {0,1,2}{\fill[blue](\x,\y)circle(3pt);}}
\foreach \x in {0,1,2,3}{\foreach \y in {0,1,2}{\draw[gray](\x,\y)--(\x+1,\y);}}
\foreach \x in {0,1,2,3,4}{\foreach \y in {0,1}{\draw[gray](\x,\y)--(\x,\y+1);}}
\draw[dashed](-.3,2.35)--(4.3,2.35)node[right]{表面};
\draw[red,thick](2,2)circle(.22);\draw[red,thick](2,1)circle(.22);
\draw[->](4.7,1.9)--(2.3,2);\node[right]at(4.7,1.9){表面：$\zeta n$};
\draw[->](4.7,.65)--(2.3,1);\node[right]at(4.7,.65){内部：$n$};
\draw[<->](0,-.4)--(1,-.4)node[midway,below]{$D$};
\node[below]at(2.3,-1){邻接示意；实际邻近数不由此二维网格确定};
\end{tikzpicture}
''',
'q4-resolution':r'''
\begin{tikzpicture}
\draw[thick](0,0)circle(1.55);\draw[dashed](-1.55,0)--(1.55,0);
\draw[<->](-1.55,-1.95)--(1.55,-1.95)node[midway,below]{$2r_p$};
\foreach \x in {-1.2,-.9,-.6,-.3,0,.3,.6,.9,1.2}{\draw[gray](\x,-.8)--(\x,.8);}
\draw[<->](.3,1.15)--(.6,1.15)node[midway,above]{$\Delta x$};
\node[right]at(2,.4){$\Delta x=2r_p/200$};
\node[right]at(2,-.3){图中分层间距示意放大};
\draw[->,blue,thick](-3.2,.3)--(-1.7,.3)node[midway,above]{电子};
\end{tikzpicture}
''',
'q4-scattering':r'''
\begin{tikzpicture}
\draw[->](0,0)--(5.8,0)node[right]{$r$};
\draw[->](0,0)--(0,3.4)node[above]{$p$};
\draw[blue,thick]plot[domain=.6:5.2,samples=70](\x,{3*sqrt(1-.5/\x)});
\fill(1.8,2.55)circle(2pt);
\draw[->,red](1.8,2.55)--(2.9,2.8);
\draw[dashed](1.8,2.55)--(2.9,2.55)--(2.9,2.8);
\node[below]at(2.4,2.5){$dr$};\node[right=6pt]at(2.9,2.65){$dp$};
\node at(3.2,1.1){$p^2/(2m)+k_C/r=E$};
\node at(3.1,.5){$v\,dp=k_Cdr/r^2$};
\end{tikzpicture}
''',
'q5-wires':r'''
\begin{tikzpicture}
\draw[dashed](-2,-1.5)rectangle(2,1.5);
\draw[->](-2.7,0)--(3.1,0)node[right]{$x$};\draw[->](0,-2)--(0,2.3)node[above]{$y$};
\node[below left]at(0,0){$O$};\fill(.55,.55)circle(2pt)node[right]{$P(x,y)$};
\foreach \x/\y/\sign in {-2/1.5/+,-2/-1.5/-,2/1.5/-,2/-1.5/+}{
\draw[fill=white,thick](\x,\y)circle(.13);
\if\sign+\fill(\x,\y)circle(1.5pt);\else\draw(\x-.08,\y-.08)--(\x+.08,\y+.08);\draw(\x-.08,\y+.08)--(\x+.08,\y-.08);\fi}
\draw[<->](-2,-2.4)--(2,-2.4)node[midway,below]{$a$};
\draw[<->](2.5,-1.5)--(2.5,1.5);\node[right]at(2.5,.55){$b$};
\node[above left]at(-2,1.5){$+I$};\node[below left]at(-2,-1.5){$-I$};
\node[above right]at(2,1.5){$-I$};\node[below right]at(2,-1.5){$+I$};
\end{tikzpicture}
''',
'q5-trap':r'''
\begin{tikzpicture}
\draw[->](-1.8,0)--(1.9,0)node[right]{$x$};\draw[->](0,-1.4)--(0,1.7)node[above]{$y$};
\foreach \x/\y in {1/1,1/-1,-1/1,-1/-1}{\draw[->,blue,thick](\x,\y)--({.6*\x},{1.4*\y});}
\draw[dashed](0,0)circle(1.3);\node[below]at(0,-1.9){$\boldsymbol B=K_B(-x,y)$};
\begin{scope}[xshift=5.2cm]
\draw[->](-1.8,0)--(1.9,0)node[right]{$x$};\draw[->](0,0)--(0,2.4)node[above]{$W$};
\draw[red,thick](-1.5,1.8)--(0,0)--(1.5,1.8);
\draw[->,red](-1.2,.3)--(-.5,.3);\draw[->,red](1.2,.3)--(.5,.3);
\node[below]at(0,-.55){$W=F_0r,\quad\boldsymbol F=-F_0\boldsymbol e_r$};
\end{scope}
\end{tikzpicture}
''',
'q6-scatter':r'''
\begin{tikzpicture}
\draw[dashed](-3,0)--(4,0);\fill(0,0)circle(3pt)node[below]{太阳};
\draw[dashed](-3,1.3)--(1.7,1.3);
\draw[->,blue,thick](-3,1.3)--(-1.9,1.3)node[midway,above]{$v_0$};
\draw[thick](-1.9,1.3)..controls(-.7,1.3)and(.6,1.2)..(1.45,.94)--(3.8,.10);
\draw[->,thick](2.4,.6)--(3.1,.35);
\draw[<->](-1.1,0)--(-1.1,1.3)node[midway,left]{$b$};
\draw[dashed](1.45,.94)--(3.8,.94);
\draw(2.5,.94)arc(0:-20:1.05);\node[right]at(2.65,.74){$\Delta\varphi$};
\end{tikzpicture}
''',
'q6-orbit':r'''
\begin{tikzpicture}
\fill(0,0)circle(2pt)node[below left]{$O$};
\draw[->](0,0)--(3,0)node[right]{最近点轴};
\draw[blue,thick]plot[domain=-110:110,samples=100]({1.2*cos(\x)/(1+2*cos(\x))},{1.2*sin(\x)/(1+2*cos(\x))});
\draw[dashed](0,0)--(-1.5,2.60);\draw[dashed](0,0)--(-1.5,-2.60);
\draw[->,red](-1.1,-2.2)--(-.6,-1.4)node[right]{入射速度};
\draw[->,red](-.6,1.4)--(-1.1,2.2)node[left]{出射速度};
\draw(.7,0)arc(0:120:.7);\node[above]at(.13,.8){$\theta_{\max}$};
\node[right]at(1.1,-1.6){$\Delta\varphi=2\theta_{\max}-\pi$};
\end{tikzpicture}
''',
'q7-ring':r'''
\begin{tikzpicture}
\draw[thick](0,0)ellipse(2 and .8);\fill(-1.2,-.64)circle(3pt)node[below]{电子};
\draw[dashed](0,0)--(1.5,.53)node[midway,above]{$R$};
\draw[->,very thick](0,-1.2)--(0,1.8)node[above]{$\Phi$};
\draw[->](1.45,-.55)arc(-30:45:1.65 and .65);
\node[right]at(2,.3){正向绕环};
\node[below]at(.7,-1.5){$x=R\theta$};
\end{tikzpicture}
''',
'q7-branches':r'''
\begin{tikzpicture}
\draw[->](-2.5,0)--(2.6,0)node[right]{$f$};\draw[->](0,0)--(0,2.4)node[above]{磁通相关项};
\draw[blue,thick]plot[domain=-.5:.5,samples=80]({4*\x},{6*\x*\x});
\draw[red,thick]plot[domain=-.5:0,samples=40]({4*\x},{6*(\x+.5)^2});
\draw[red,thick]plot[domain=0:.5,samples=40]({4*\x},{6*(\x-.5)^2});
\node[below]at(-2,0){$-1/2$};\node[below]at(2,0){$1/2$};\node[below left]at(0,0){$0$};
\node[blue,right]at(2.2,2){奇数：$f^2$};\node[red,right]at(2.2,1.4){偶数：$(|f|-1/2)^2$};
\node[below]at(0,-.6){仅绘磁通相关项，纵轴单位为 $E_R$};
\end{tikzpicture}
''',
'q7-pairing':r'''
\begin{tikzpicture}
\draw[->](-2.8,1.6)--(3.2,1.6)node[right]{$p'R/\hbar$};
\foreach \x in {-2,-1,0,1,2}{\fill[blue](\x,1.6)circle(3pt);\node[above]at(\x,1.6){$\x$};}
\draw[<->,blue](-2,1.1)--(2,1.1);\draw[<->,blue](-1,.8)--(1,.8);
\node[left]at(-2.8,1.6){$f=0$};
\draw[->](-2.8,-.5)--(3.2,-.5)node[right]{$p'R/\hbar$};
\foreach \x/\lab in {-1.5/{-\frac32},-.5/{-\frac12},.5/{\frac12},1.5/{\frac32}}{\fill[red](\x,-.5)circle(3pt);\node[above]at(\x,-.5){$\lab$};}
\draw[<->,red](-1.5,-1)--(1.5,-1);\draw[<->,red](-.5,-1.3)--(.5,-1.3);
\node[left]at(-2.8,-.5){$f=1/2$};
\end{tikzpicture}
''',
}
def main():
    folder=ROOT/'figures';folder.mkdir(exist_ok=True)
    pre=r'''\documentclass[border=6pt]{standalone}
\usepackage[fontset=fandol]{ctex}
\usepackage{amsmath,amssymb,tikz}
\usetikzlibrary{arrows.meta,calc,decorations.pathmorphing}
\begin{document}
'''
    for name,body in FIGS.items():
        (folder/(name+'.tikz')).write_text(body)
        (folder/(name+'.tex')).write_text(pre+body+'\n\\end{document}\n')
    print(f'Wrote {len(FIGS)} TikZ figures',flush=True)
if __name__=='__main__':main()
