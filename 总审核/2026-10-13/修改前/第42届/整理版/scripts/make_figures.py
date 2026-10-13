#!/usr/bin/env python3
"""Editable TikZ question and derivation diagrams for the 42nd semifinal."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FIGS={
"q1-trap":r"""
\begin{tikzpicture}[scale=.85]
\draw[->](-2,0)--(2.2,0)node[right]{$x$};
\draw[->](0,1.6)--(0,-2.7)node[below]{$z$};
\draw[blue,thick] plot[domain=-1.5:1.5,samples=60](\x,{.65*\x*\x+.3});
\foreach \x/\y in {-.7/.15,-.2/.4,.3/.1,.65/.32,.12/-.15,-.4/-.12}
 \fill[blue](\x,\y)circle(2pt);
\node[left] at(-.9,.65){原子云};
\draw[dashed](-1.8,-2)--(1.8,-2)node[right]{$z=h$};
\draw[fill=gray!20](-1.5,-2.2)rectangle(1.5,-2);
\node[below] at(0,-2.2){探测平面};
\draw[->,thick](1,-.4)--(1,-1.4)node[midway,right]{$g$};
\node[above right] at(0,0){$O$};
\end{tikzpicture}
""",
"q1-phase":r"""
\begin{tikzpicture}
\draw[->](-2,0)--(2.5,0)node[right]{$z_0$};
\draw[->](0,-1.5)--(0,1.8)node[above]{$v_{z0}$};
\draw[blue,thick] (0,0)ellipse(1.6 and .9);
\draw[red,thick](-1.4,1.2)--(1.8,-.8);
\node[red,right] at(1.6,-.6){$z_0+t v_{z0}=h-\frac12gt^2$};
\node[blue,above]at(-1.1,.8){初始高斯等密度线};
\end{tikzpicture}
""",
"q1-peaks":r"""
\begin{tikzpicture}
\draw[->](0,0)--(5.6,0)node[right]{$t/t_0$};
\draw[->](0,0)--(0,2.6)node[above]{归一化信号};
\draw[blue,thick] plot[domain=.45:1.7,samples=120]({3*\x},{2.1*exp(-(\x-1)^2/.018)});
\draw[red,dashed,thick] plot[domain=.45:1.7,samples=120]({3*\x},{2.1*exp(-(\x-.97)^2/.018)});
\draw[dotted](3,0)--(3,2.4);
\node[below]at(3,0){$1$};
\node[blue]at(4.2,2){零温中心 $t_0$};
\node[red]at(1.5,1.7){低温峰提前};
\node[below]at(2.2,-.45){示意：实际峰宽由曲率确定};
\end{tikzpicture}
""",
"q2-probe":r"""
\begin{tikzpicture}[scale=.9]
\fill[gray!15](0,0)circle(1.45);
\node at(0,-.75){等离子体 $\Phi$};
\draw[->,thick](-3,1.4)--(-.4,.4)node[midway,above=7pt,fill=white,inner sep=2pt]{一次离子 $q_1,K_1$};
\fill(-.4,.4)circle(2pt);
\draw[->,thick](-.4,.4)--(3,1.1)node[midway,above=7pt,fill=white,inner sep=2pt]{二次离子 $q_2$};
\draw[very thick](3,.4)--(3.2,1.6);
\node[right]at(3.2,1){能量分析器 $K_2$};
\node[below]at(-.4,.4){测量位置};
\node at(.6,-.1){$\otimes\,B$};
\end{tikzpicture}
""",
"q2-analyzer":r"""
\begin{tikzpicture}[scale=.85]
\draw[very thick](-1,2)--(6,2)node[right]{$V_A$};
\draw[very thick](-1,.8)--(.3,.8);
\draw[very thick](1,.8)--(3.7,.8);
\draw[very thick](4.4,.8)--(6,.8)node[right]{$V=0$};
\draw[<->](-1.3,.8)--(-1.3,2)node[midway,left]{$d$};
\draw[blue,thick](0,-.5)--(.7,.8);
\draw[blue,thick] plot[domain=.7:4.1,samples=50](\x,{.8+1.1*(1-((\x-2.4)/1.7)^2)});
\draw[blue,thick](4.1,.8)--(4.8,-.5);
\draw[very thick](-.5,.3)--(.5,-1.3);
\draw[very thick](4.3,-1.3)--(5.3,.3);
\draw[<->](0,-1.65)--(4.8,-1.65)node[midway,below]{$X_D$};
\draw[dashed](0,-.5)--(4.8,-.5);
\draw[<->](.1,-.5)--(.1,.8)node[midway,left]{$Y_{D1}$};
\draw[<->](4.9,-.5)--(4.9,.8)node[midway,right]{$Y_{D2}$};
\draw[blue] (.42,-.5) arc(0:62:.42);\node[blue]at(.55,-.2){$\theta_I$};
\draw(.65,-.5) arc(0:-58:.65);\node[right]at(.6,-.92){$\theta_a$};
\draw(4.15,-.5) arc(180:238:.65);\node[left]at(4.2,-.92){$\theta_b$};
\draw[->] (0,-.5)--(.5,-1.3);\draw[->] (4.8,-.5)--(4.3,-1.3);
\node at(-.45,-.75){$l$}; \node at(5.15,-.8){$s$};
\node at(2.5,2.4){电场向下；图中高度与角度为示意};
\end{tikzpicture}
""",
"q2-focus":r"""
\begin{tikzpicture}
\draw[->](0,0)--(5.5,0)node[right]{$\Delta\theta_I$};
\draw[->](2.7,-1.2)--(2.7,1.5)node[above]{$\Delta X_D$};
\draw[blue,thick]plot[domain=-1:1,samples=60]({2.7+2*\x},{-\x*\x*\x});
\draw[dashed](1.1,0)--(4.3,0);
\node[below]at(2.7,-1.25){二级聚焦：一、二阶均消失，首项为三阶};
\end{tikzpicture}
""",
"q3-device":r"""
\begin{tikzpicture}
\draw[fill=blue!8](-2,-.55)--(-1.35,-.55)--(-1.35,-1.15)--(-1.05,-1.15)--(-1.05,-.55)--(-.15,-.55)--(-.15,-1.15)--(.15,-1.15)--(.15,-.55)--(1.05,-.55)--(1.05,-1.15)--(1.35,-1.15)--(1.35,-.55)--(2,-.55)--(2,.55)--(1.35,.55)--(1.35,1.15)--(1.05,1.15)--(1.05,.55)--(.15,.55)--(.15,1.15)--(-.15,1.15)--(-.15,.55)--(-1.05,.55)--(-1.05,1.15)--(-1.35,1.15)--(-1.35,.55)--(-2,.55)--cycle;
\node[left]at(-2,0){1};\node[right]at(2,0){5};
\foreach \x/\n in {-1.2/2,0/3,1.2/4}\node[above]at(\x,1.15){\n};
\foreach \x/\n in {-1.2/8,0/7,1.2/6}\node[below]at(\x,-1.15){\n};
\node at(0,0){$\odot\,B$};
\end{tikzpicture}
""",
"q3-equivalent":r"""
\begin{tikzpicture}[scale=.85]
\foreach \i/\a in {1/180,2/135,3/90,4/45,5/0,6/-45,7/-90,8/-135}{
 \coordinate (p\i) at(\a:2.6);
 \coordinate (t\i) at(\a:4.3);
 \draw (p\i)--(t\i);
 \node[draw,fill=white,inner sep=2pt]at(\a:3.12){$r$};
 \node[draw,fill=white,inner sep=2pt]at(\a:3.72){$R_{c\number\i}$};
 \node at(\a:4.68){$\number\i$};
 \fill(p\i)circle(1.5pt);
}
\foreach \i/\j in {1/2,2/3,3/4,4/5,5/6,6/7,7/8,8/1}{
 \draw[->] (p\i)--node[fill=white,inner sep=1pt]{$E_{\number\i,\number\j}$}(p\j);
}
\node[font=\small] at(0,.45){受控电源环};
\node[font=\scriptsize] at(0,-.05){$E_{ij}=r(I_i+I_j)$};
\node[font=\scriptsize] at(0,-.55){$C_{i+1}-C_i=E_{i,i+1}$};
\end{tikzpicture}
""",
"q3-series":r"""
\begin{tikzpicture}
\foreach \x/\s in {0/a,5/b}{
 \draw[fill=blue!8](\x-1,-.7)rectangle(\x+1,.7);
 \node at(\x,0){器件 $\s$};
 \foreach \dx/\dy/\n in {-1/0/1,1/0/5,0/.7/3,0/-.7/7}{
  \coordinate(\s\n)at(\x+\dx,\dy);
  \node at(\x+\dx*1.25,\dy*1.4){$\n\s$};
 }
}
\draw[->](-2.3,0)--(a1)node[midway,above]{$I$};
\draw(a5)--(b1);\node[above]at(1.8,.08){主连接};
\draw[->](b5)--(7.3,0)node[midway,above]{$I$};
\draw(a7)--(0,-1.6)--(2.7,-1.6)--(2.7,-.18) to[out=0,in=0](2.7,.18)--(2.7,1.6)--(5,1.6)--(b3);
\node[below]at(1.5,-1.6){可断开的补偿连接};
\draw(a3)--(0,1.6)node[above]{$U_{3a}$};
\draw(b7)--(5,-1.6)node[below]{$U_{7b}$};
\end{tikzpicture}
""",
"q3-parallel":r"""
\begin{tikzpicture}[scale=.8]
\draw[fill=blue!8](-3,-3)rectangle(-1,3);
\draw[fill=blue!8](1,-3)rectangle(3,3);
\node at(-2,0){$a$};\node at(2,0){$b$};
\foreach \y/\i in {2.2/2,1/3,-1/6,-2.2/7}{
 \draw(-1,\y)--(1,\y);
 \node[left,fill=blue!8,inner sep=1pt]at(-1,\y){$\i a$};
 \node[right,fill=blue!8,inner sep=1pt]at(1,\y){$\i b$};
}
\draw(-3,0)--(-3.8,0)--(-3.8,3.7)--(3.8,3.7)--(3.8,0)--(3,0);
\node[above]at(0,3.7){$A:\ 1a,1b$};
\draw(-2,-3)--(-2,-3.8)--(2,-3.8)--(2,-3);
\node[below]at(0,-3.8){$B:\ 5a,5b$};
\node[above,font=\small]at(0,2.2){浮置连接};
\node[above]at(0,1){$C:\ 3a,3b$};
\node[above,font=\small]at(0,-1){浮置连接};
\node[above]at(0,-2.2){$D:\ 7a,7b$};
\end{tikzpicture}
""",
"q3-orders":r"""
\begin{tikzpicture}
\draw[->](0,0)--(6,0);
\foreach \x/\t in {0.5/主回路,2.2/一次补偿,4/二次补偿}
 \node[draw,rounded corners,fill=white]at(\x,0){\t};
\node at(.5,1){$O(\epsilon)$};
\node at(2.2,1){$O(\epsilon^2)$};
\node at(4,1){$O(\epsilon^3)$};
\node at(2.6,-.8){误差阶来自小电流与小接触压降的乘积};
\end{tikzpicture}
""",
"q4-wave":r"""
\begin{tikzpicture}
\draw[->](0,0)--(5,0)node[right]{$z$};
\draw[->](1,0)--(1,1.7)node[above]{$E_x$};
\draw[->](1,0)--(.1,-.8)node[left]{$B_y$};
\draw[blue,thick]plot[domain=0:4.6,samples=100](\x,{.75*cos(180*\x)});
\node at(3,1.5){$\mathbf E\times\mathbf B\parallel+\hat{\mathbf z}$};
\node[below]at(3,-1){电子电荷 $-e$，受力为 $-e(\mathbf E+\mathbf v\times\mathbf B)$};
\end{tikzpicture}
""",
"q4-orbit":r"""
\begin{tikzpicture}
\draw[->](-2.6,0)--(.7,0)node[right]{$kx$};
\draw[->](0,0)--(0,5)node[above]{$kz$};
\draw[blue,thick]plot[domain=0:720,samples=180]({1.1*(cos(\x)-1)},{1.21/4*(\x*pi/180-sin(2*\x)/2)});
\node at(-2.1,4.6){初静止电子};
\node at(-2.1,4.1){相位参数 $\psi=\omega t-kz$};
\end{tikzpicture}
""",
"q5-junction":r"""
\begin{tikzpicture}
\draw[fill=blue!12](-2,-1.5)rectangle(-.3,1.5);
\draw[fill=gray!40](-.3,-1.5)rectangle(.3,1.5);
\draw[fill=blue!12](.3,-1.5)rectangle(2,1.5);
\node at(-1.25,1){超导体1};\node at(1.25,1){超导体2};
\draw[dashed](-.7,-1.5)--(-.7,1.5);\draw[dashed](.7,-1.5)--(.7,1.5);
\draw[<->](-.7,-1.9)--(.7,-1.9)node[midway,below]{$d+2\lambda$};
\draw[->](-2.8,0)--(2.8,0)node[right]{$x$};
\draw[->](0,-1.5)--(0,2.2)node[above]{$y$};
\node[fill=white,inner sep=2pt] at(0,.15){$\odot B_z$};
\node at(-1.2,-.8){$\varphi_1$};\node at(1.2,-.8){$\varphi_2$};
\end{tikzpicture}
""",
"q5-fringe":r"""
\begin{tikzpicture}
\draw[->](-4,0)--(4,0)node[right]{$\Phi/\Phi_0$};
\draw[->](0,0)--(0,2.5)node[above]{$I_{\max}/I_0$};
\draw[blue,thick]plot[domain=-3.5:-.01,samples=180](\x,{2*abs(sin(180*\x)/(\x*pi))});
\draw[blue,thick]plot[domain=.01:3.5,samples=180](\x,{2*abs(sin(180*\x)/(\x*pi))});
\foreach \x in {-3,-2,-1,1,2,3}\node[below]at(\x,0){$\x$};
\node at(2,2){$|\sin u/u|$ 包络};
\end{tikzpicture}
""",
"q5-rcsj":r"""
\begin{tikzpicture}
\coordinate(A)at(0,0);\coordinate(B)at(5,0);
\draw[->](-1,0)--(A)node[midway,above]{$I$};
\draw(A)--(0,1.4)--(5,1.4)--(B);
\node[draw,fill=white]at(2.5,1.4){$R$};
\draw(A)--(B); \node[draw,fill=white]at(2.5,0){$J:\ I_0\sin\delta$};
\draw(A)--(0,-1.4)--(5,-1.4)--(B);
\node[draw,fill=white]at(2.5,-1.4){$C$};
\draw[->](B)--(6,0);
\draw[<->](.4,-2)--(4.6,-2)node[midway,below]{$U=\hbar\dot\delta/(2e)$};
\end{tikzpicture}
""",
"q5-potential":r"""
\begin{tikzpicture}
\draw[->](-.5,0)--(7,0)node[right]{$\delta$};
\draw[->](0,-2)--(0,1.7)node[above]{$V$};
\draw[blue,thick]plot[domain=0:6.8,samples=130](\x,{-cos(\x*180/pi)-.12*\x});
\fill(.12,-1.007)circle(2pt);
\node[below]at(1,-1.4){势阱底};
\node[above]at(3,1){势垒顶};
\node at(4.5,-2.2){恒定偏置产生倾斜};
\end{tikzpicture}
""",
"q6-rotor":r"""
\begin{tikzpicture}
\draw[very thick](0,-2.6)--(0,2.6);
\draw[->](0,2.6)--(0,3)node[above]{$z$};
\draw[->](0,0)--(2.5,0)node[right]{$x$};
\draw[thick](-1.3,1.7)--(1.3,-1.7);
\filldraw[fill=blue!20](-1.3,1.7)circle(.18)node[left=4pt]{$a,m_1$};
\filldraw[fill=blue!20](1.3,-1.7)circle(.18)node[right=4pt]{$b,m_2$};
\draw(-.8,0)arc(180:128:.8);
\node at(-.35,.95){$\theta$};
\node[right]at(0,1.45){$A,\ z=h$};\node[right]at(0,-1.45){$B,\ z=-h$};
\draw[<->](-1.7,1.6)--(-.15,.05)node[midway,left]{$l$};
\node[below left]at(0,0){$O$};
\draw[->](2.4,1.6)--(2.4,.6)node[midway,right]{$g$};
\node at(-1.7,-1.7){盘簧恢复力矩 $k\theta$};
\end{tikzpicture}
""",
"q6-energy":r"""
\begin{tikzpicture}
\draw[->](0,0)--(5.5,0)node[right]{$\theta$};
\draw[->](0,0)--(0,3.5)node[above]{$V_{\rm eff}$};
\draw[blue,thick]plot[domain=.35:2.8,samples=90]({1.7*\x},{.22/(sin(\x*180/pi)^2)+.28*\x*\x});
\draw[dashed](.5,1.25)--(5,1.25)node[right]{$E$};
\node at(2,2.9){$P_z^2/(2J\sin^2\theta)+k\theta^2/2$};
\node[below]at(1.6,0){$\theta_0$};
\end{tikzpicture}
""",
"q7-fiber":r"""
\begin{tikzpicture}
\draw[gray](-.6,-.6)--(5.4,1.2);
\draw[gray](-.6,.6)--(5.4,2.4);
\draw[gray](-.6,0)ellipse(.25 and .6);
\draw[gray](5.4,1.8)ellipse(.25 and .6);
\draw[->](-.6,0)--(6,1.98)node[right]{$z$};
\draw[blue,thick]plot[domain=0:720,samples=160]({-.6+\x/120+.12*cos(\x)},{.3*\x/120+.45*sin(\x)});
\node at(2,-1){渐变折射率将光线持续弯向轴心};
\end{tikzpicture}
""",
"q7-ellipse":r"""
\begin{tikzpicture}
\draw[->](-2.8,0)--(2.8,0)node[right]{$x$};
\draw[->](0,-1.8)--(0,1.8)node[above]{$y$};
\draw[blue,thick,rotate=25](0,0)ellipse(2.3 and 1);
\draw[dashed](0,0)--(2.084,.971)node[right]{$\rho_{\max}$};
\draw[dashed](0,0)--(-.4226,.9063)node[above]{$\rho_{\min}$};
\draw[->,red](1.3,.45)--(1.8,1.1);
\node[anchor=west]at(2.35,.5){切线方向示意};
\node at(-1.7,-1.5){横截面投影为椭圆};
\end{tikzpicture}
"""
}
PREAMBLE=r"""\documentclass[border=4pt]{standalone}
\usepackage[fontset=fandol]{ctex}
\usepackage{amsmath,amssymb,bm,tikz}
\usetikzlibrary{arrows.meta,calc,decorations.pathmorphing}
\pagestyle{empty}
\begin{document}
"""
def main():
    folder=ROOT/"figures"; folder.mkdir(exist_ok=True)
    for name,body in FIGS.items():
        (folder/(name+".tikz")).write_text(body.strip()+"\n")
        (folder/(name+".tex")).write_text(PREAMBLE+body+"\n\\end{document}\n")
    print(f"{len(FIGS)} editable diagrams generated")
if __name__=="__main__":main()
