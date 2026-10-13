#!/usr/bin/env python3
"""Equation-linked editable figures, with the two original JPEGs embedded verbatim."""
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
FIGS={
"q1-orbit":r"""
\begin{tikzpicture}[scale=.85]
\fill[blue!10] (0,0) circle(1.5); \draw[thick] (0,0) circle(1.5);
\draw[thick,blue] (.8,0) ellipse(2.3 and 2.156);
\fill (0,0) circle(2pt) node[below] {$O$};
\fill (3.1,0) circle(2pt) node[right] {$P:r_0=R+h$};
\draw[arr,red] (3.1,0)--(3.1,1.4) node[right] {$v_0$};
\draw[dashed] (0,0)--(3.1,0); \draw[arr] (0,0)--(-1.5,0) node[midway,above] {$R$};
\node[left] at(-1.7,0) {$r_{\rm p}$};
\node at(.8,-2.65) {临界椭圆与地表相切；焦点在地心};
\end{tikzpicture}""",
"q1-effective":r"""
\begin{tikzpicture}[xscale=1.15,yscale=1.7]
\draw[arr] (.5,-1.1)--(6.5,-1.1) node[right] {$r$};
\draw[arr] (.7,-1.2)--(.7,1.2) node[above] {$U_{\rm eff}/m$};
\draw[blue,thick,domain=.75:6,samples=100] plot(\x,{1.5/(\x*\x)-2/\x});
\draw[red] (.8,-.4)--(6,-.4) node[right] {$\varepsilon$};
\draw[dashed] (1.2,-1.05)--(1.2,.25) node[above] {$R$};
\draw[dashed] (4.08,-1.05)--(4.08,-.4) node[above] {$r_0$};
\node at(3.8,.8) {$U_{\rm eff}/m=j^2/(2r^2)-GM/r$};
\end{tikzpicture}""",
"q1-anomaly":r"""
\begin{tikzpicture}[scale=.85]
\draw[gray,dashed] (0,0) circle(2.5); \draw[blue,thick] (0,0) ellipse(2.5 and 1.6);
\fill (0,0) circle(2pt) node[below] {$C$};\fill(1.92,0) circle(2pt) node[below] {$O$};
\coordinate(P) at(-1.25,1.386); \fill(P) circle(2pt) node[above] {$P$};
\draw (0,0)--(-1.25,2.165); \draw[dashed] (-1.25,2.165)--(-1.25,0);
\draw[arr] (.6,0) arc(0:120:.6) node[midway,above] {$E$};
\node at(0,-2.8) {$r=a_{\rm K}(1-e\cos E),\quad n_{\rm K}t=E-e\sin E$};
\end{tikzpicture}""",
"q2-spring":r"""
\begin{tikzpicture}[scale=.9]
\draw[thick](-4,-.3)--(4,-.3); \draw[thick](-4,-.3)--(-4,1.1);
\draw[decorate,decoration={coil,aspect=.4,segment length=4pt,amplitude=4pt}](-4,.3)--(-1.8,.3);
\draw[thick,fill=gray!15](-1.8,0)rectangle(-1.2,.6); \node at(-1.5,.3){$m$};
\draw[arr](-4,-.8)--(4.5,-.8)node[right]{$x$};
\draw[dashed](0,-1)--(0,1)node[above]{$O$};\node[below]at(-1.5,-.8){$-A_0$};
\draw[arr,red](-1.2,.6)--(.2,.6)node[above]{$kx$的回复方向};
\draw[arr,blue](-1.8,0)--(-3,0)node[below]{$f=\mu mg$};
\end{tikzpicture}""",
"q2-map":r"""
\begin{tikzpicture}[scale=.85]
\draw[arr](-5,0)--(5,0)node[right]{$x$};
\fill[green!15](-.7,-.3)rectangle(.7,.3);
\node[below]at(-.7,-.3){$-b$};\node[below]at(.7,-.3){$b$};
\foreach \x/\s in {-4/A_0,2.6/A_0-2b,-1.2/4b-A_0}{\fill(\x,0)circle(2pt);}
\draw[arr,blue](-4,.8)--(2.6,.8)node[midway,above]{右行：$x_1=-2b-x_0$};
\draw[arr,red](2.6,1.7)--(-1.2,1.7)node[midway,above]{左行：$x_2=2b-x_1$};
\node at(0,-1.1){停在静摩擦带内时，不能直接续用转折点递推};
\end{tikzpicture}""",
"q2-band":r"""
\begin{tikzpicture}[xscale=1.1,yscale=.85]
\draw[arr](0,0)--(8,0)node[right]{$A_0/b$};
\draw[arr](0,-1.4)--(0,1.8)node[above]{$x_f/b$};
\draw[blue,thick](0,0)--(1,-1)--(3,1)--(5,-1)--(7,1);
\draw[dashed](0,1)--(7.4,1);\draw[dashed](0,-1)--(7.4,-1);
\foreach \x in {1,3,5,7}{\draw[dashed](\x,-1.1)--(\x,1.2);\node[below]at(\x,-1.2){$\x$};}
\node at(4,2){终点在$[-b,b]$内呈折线变化};
\end{tikzpicture}""",
"q3-impact":r"""
\begin{tikzpicture}[scale=.9]
\draw[arr](0,0)--(3.2,0)node[right]{$x$};\draw[arr](0,-3.5)--(0,1)node[above]{$y$};
\draw[very thick](0,0)--(0,-3);\node[above left]at(0,0){$O=A$};
\fill(0,-2)circle(3pt)node[left]{$D,\ OD=2l/3$};\node[left]at(0,-3){$B$};
\draw[arr,red](2,-2)--(.2,-2)node[midway,above]{$v_0$};
\fill(2,-2)circle(3pt)node[right]{$m$};\node[left]at(0,-1){$M,l$};
\end{tikzpicture}""",
"q3-force":r"""
\begin{tikzpicture}[scale=1.05]
\coordinate(C)at(-1.55,-1.85); \draw[very thick](0,0)--(-2.57,-3.06);
\node[above]at(0,0){$O$};\fill(C)circle(2pt)node[left]{$C$};
\draw[dashed](0,0)--(0,-3.3);\draw (0,-.7) arc(-90:-130:.7)node[below]{$\theta$};
\draw[arr,blue](0,0)--(1.2,0)node[above]{$N_x$};
\draw[arr,blue](0,0)--(0,1)node[right]{$N_y$};
\draw[arr,red](C)--++(0,-1.1)node[right]{$(M+m)g$};
\draw[arr,gray](C)--++(.8,.95);\node[left]at(-1.6,-.9){$s\omega^2$};
\node at(1.6,-2.5){$s=OC$};
\end{tikzpicture}""",
"q3-flight":r"""
\begin{tikzpicture}[scale=.8]
\draw[arr](-1,0)--(7,0)node[right]{$x$};\draw[arr](0,-1)--(0,4.3)node[above]{$y$};
\draw[very thick](0,0)--(0,3.5);\fill(0,2.1)circle(2pt)node[left]{$C(0)=s$};\node[above]at(0,3.5){$B$};
\draw[arr,red](0,2.1)--(1.5,2.1)node[above]{$s\omega_*$};
\draw[blue,dashed,domain=0:5,samples=40]plot(\x,{2.1-.045351*\x*\x});
\draw[very thick](.563,1.051)--(3.825,2.319);\fill(2.52,1.812)circle(2pt)node[below right]{$C(t)$};
\draw[arr](2.8,2.8)arc(115:30:.6);
\node at(3.1,5.0){质心平抛，杆相对质心匀速转动};
\end{tikzpicture}""",
"q4-wires":r"""
\begin{tikzpicture}[scale=1.2]
\draw[arr](-2,0)--(2,0)node[right]{$x$};\draw[arr](0,-2)--(0,2)node[above]{$y$};
\draw[dashed](-1,1)--(1,1)--(1,-1)--(-1,-1)--cycle;
\foreach \x/\y/\n/\s in {-1/1/1/\otimes,1/1/2/\odot,1/-1/3/\otimes,-1/-1/4/\odot}
{\node at(\x,\y){$\s$};\node[above right]at(\x,\y){$\n$};}
\node[below]at(.5,0){$a$};\node[left]at(0,.5){$a$};
\node at(0,-2.5){$\otimes:-z,\quad\odot:+z,\quad\mathbf B_0=B_0\mathbf k$};
\end{tikzpicture}""",
"q4-local":r"""
\begin{tikzpicture}[scale=1.15]
\draw[arr](-2,0)--(2,0)node[right]{$x$};\draw[arr](0,-2)--(0,2)node[above]{$y$};
\foreach \x in {-1.4,-.7,.7,1.4}{\foreach \y in {-1.4,-.7,.7,1.4}{\draw[arr,blue](\x,\y)--++({.3*\x},{-.3*\y});}}
\draw[red,thick](0,0)circle(1.3);\draw[arr,red](1.3,0)--(.6,0);
\node at(0,-2.5){$\mathbf B_\perp=K(x,-y),\quad \mathbf F_\perp=-\mu K^2(x,y)/B_0$};
\end{tikzpicture}""",
"q4-barrier":r"""
\begin{tikzpicture}[xscale=1.1,yscale=2]
\draw[arr](0,0)--(6.6,0)node[right]{$\rho/a$};
\draw[arr](0,0)--(0,1.5)node[above]{$|\mathbf B_\perp|/(\mu_0I/\pi a)$};
\draw[blue,thick,domain=0:6,samples=120]plot(\x,{4*\x/(\x^4+4)});
\draw[dashed](1.07457,0)--(1.07457,.806);
\fill[red](1.07457,.806)circle(1.4pt)node[above right]{轴上鞍点};
\node at(3.8,1.15){固定半径时，轴向场最弱};
\end{tikzpicture}""",
"q5-frames":r"""
\begin{tikzpicture}[scale=.95]
\draw[arr](0,0)--(3.5,0)node[right]{$x$};\draw[arr](0,0)--(0,3.5)node[above]{$y$};
\draw[arr,blue](0,0)--(2.9,1.68)node[right]{$x'$};
\draw[arr,blue](0,0)--(-1.68,2.9)node[above]{$y'$};
\draw[arr](1,0)arc(0:30:1)node[midway,right]{$\omega_Lt$};
\node at(4,2.5){$\boldsymbol\Omega=\omega_L\mathbf k$};
\node at(3,-1){$\mathbf v=\mathbf v'+\boldsymbol\Omega\times\mathbf r$};
\end{tikzpicture}""",
"q5-modes":r"""
\begin{tikzpicture}[scale=.95]
\foreach \xx/\lab/\ang in {0/{\Omega_\perp+\omega_L}/55,4/{\Omega_\perp-\omega_L}/-55}
{\begin{scope}[shift={(\xx,0)}]
\draw[blue,thick](0,0)circle(1.3);\draw[arr](1.3,0)arc(0:\ang:1.3);
\draw[arr,gray](-1.7,0)--(1.7,0);\draw[arr,gray](0,-1.7)--(0,1.7);
\node at(0,-2.1){$\lab$};\end{scope}}
\node at(2,2.2){两个相反旋向的横向圆运动};
\end{tikzpicture}""",
"q5-spectrum":r"""
\begin{tikzpicture}[xscale=1.15,yscale=.9]
\draw[arr](0,0)--(7.5,0)node[right]{$\omega$};
\draw[very thick,blue](2,0)--(2,2.2);\draw[very thick,red](4,0)--(4,2.7);
\draw[very thick,blue](6,0)--(6,2.2);
\node[below]at(2,0){$\Omega_\perp-\omega_L$};\node[below]at(4,-.5){$\omega_0$};\node[below]at(6,0){$\Omega_\perp+\omega_L$};
\draw[<->](2,1.1)--(4,1.1)node[midway,above]{$\simeq\omega_L$};
\draw[<->](4,1.1)--(6,1.1)node[midway,above]{$\simeq\omega_L$};
\end{tikzpicture}""",
"q6-shell":r"""
\begin{tikzpicture}[scale=.9]
\fill[gray!15](0,0)circle(2.5);\fill[white](0,0)circle(2.1);\fill[blue!15](0,0)circle(.55);
\draw[thick](0,0)circle(2.5);\draw[thick](0,0)circle(2.1);\draw[thick](0,0)circle(.55);
\draw[arr](0,0)--(.39,.39)node[above]{$r$};
\draw[arr](0,0)--(-1.82,1.05)node[midway,above]{$R_1$};
\draw[arr](0,0)--(2.16,-1.25)node[midway,below]{$R_2$};
\node at(0,-.25){$T_0$};\node at(-2.9,0){$T_1$};\node at(2.9,0){$T_2$};
\node at(0,3.2){真空层：辐射；球壳：导热；外界$T_b$};
\end{tikzpicture}""",
"q6-network":r"""
\begin{tikzpicture}[scale=.85]
\draw[arr](0,0)--(10,0)node[right]{$Q/\sigma$};
\foreach \x/\lab in {0/T_0^4,3/{J_0/\sigma},6/{J_1/\sigma},9/T_1^4}{\fill(\x,0)circle(2pt);\node[above]at(\x,0){$\lab$};}
\foreach \x/\lab in {1.5/{(1-e)/(eA_0)},4.5/{1/A_0},7.5/{(1-E)/(EA_1)}}
{\draw[thick,fill=white](\x-.55,-.2)rectangle(\x+.55,.2);\node[below]at(\x,-.5){$\lab$};}
\node at(4.5,1.4){辐射电阻串联；流量为$Q/\sigma$};
\end{tikzpicture}""",
"q6-temperature":r"""
\begin{tikzpicture}[xscale=2.8,yscale=.021]
\draw[arr](.15,70)--(1.15,70)node[right]{$R$};
\draw[arr](.15,70)--(.15,260)node[above]{$T/{\rm K}$};
\fill(.2,216.906)circle(.9pt)node[right]{$T_0$};
\draw[thick,blue,domain=.9:1,samples=30]plot(\x,{88.64+350.14*(1/\x-1)});
\fill(.9,127.55)circle(.9pt)node[above left]{$T_1$};\fill(1,88.64)circle(.9pt)node[above right]{$T_2$};
\node at(.55,175){真空中没有物质温度曲线};
\end{tikzpicture}""",
"q7-unroll":r"""
\begin{tikzpicture}[scale=1.1]
\draw[thick](0,0)--(1.2,0)--(1.2,4.478)--cycle;
\node[below]at(.6,0){$p$};\node[right]at(1.2,2.3){$2\pi R$};
\draw[dashed](-1.2,0)--(0,4.478);
\draw[red,thick](0,0)--(-1.1196,.3)node[midway,above]{$d_2$};
\draw[dotted](0,0)--(0,1.5);
\draw (0,.75)arc(90:75:.75);\node[right]at(.22,1){$\alpha$};
\node at(4.5,3){$\alpha=\phi/2$};\node at(4.5,2){$d_2=p\cos\alpha$};
\node at(4.5,1){$2\pi R=p\cot\alpha$};
\end{tikzpicture}""",
"q7-fringes":r"""
\begin{tikzpicture}[xscale=1.1,yscale=2]
\draw[arr](-3.4,0)--(3.7,0)node[right]{$X$};
\draw[blue,thick,domain=-3:3,samples=190]plot(\x,{exp(-.21*\x*\x)*(cos(360*\x))^2});
\draw[red,dashed,domain=-3:3,samples=100]plot(\x,{exp(-.21*\x*\x)});
\draw[<->](0,-.22)--(.5,-.22)node[midway,below]{短周期};
\node at(0,1.35){包络示意；实测时沿垂直细丝的方向取点};
\end{tikzpicture}""",
"q8-recoil":r"""
\begin{tikzpicture}[scale=.9]
\node[left]at(0,2.55){发射};\fill[blue](1,1.8)circle(4pt);
\draw[arr,red](1.4,1.8)--(4.2,1.8)node[midway,above]{$E_\gamma/c$};
\draw[arr,blue](.7,1.8)--(-1.2,1.8)node[midway,below]{$p_{\rm recoil}$};
\node[left]at(0,.55){吸收};\draw[arr,red](-2,-.2)--(.6,-.2)node[midway,above]{$E_\gamma/c$};
\fill[blue](1,-.2)circle(4pt);\draw[arr,blue](1.4,-.2)--(3.7,-.2)node[midway,below]{$p_{\rm recoil}$};
\node at(2,-1.1){发射少$E_R$；吸收多$E_R$};
\end{tikzpicture}""",
"q8-windows":r"""
\begin{tikzpicture}[xscale=1.1]
\draw[arr](0,0)--(8,0)node[right]{$E$};
\draw[very thick,blue](1.3,.5)--(2.1,.5); \draw[very thick,red](5.3,.5)--(6.1,.5);
\draw[dashed](1.7,0)--(1.7,1.1)node[above]{$E_0-E_R$};
\draw[dashed](5.7,0)--(5.7,1.1)node[above]{$E_0+E_R$};
\draw[<->](1.7,-.6)--(5.7,-.6)node[midway,below]{$2E_R\gg2\Gamma$};
\node at(4,1.8){图中窗口宽度放大，真实尺度差约$4.2\times10^5$};
\end{tikzpicture}""",
"q8-scan":r"""
\begin{tikzpicture}[xscale=1.1,yscale=2]
\draw[arr](-3.2,0)--(3.4,0)node[right]{$u$};
\draw[arr](-3.2,0)--(-3.2,1.3)node[above]{吸收强度};
\draw[blue,thick,domain=-3:3,samples=100]plot(\x,{1/(1+20*(\x-1)^2)});
\draw[dashed](1,0)--(1,1)node[above]{$u_* \simeq c\delta$};
\node at(-.7,.9){调节速度使频率补偿};
\end{tikzpicture}""",
}

def photo(filename,label,clip_fraction=1):
    p=ROOT/"sources"/filename
    im=Image.open(p); w,h=im.size
    width=283.465; height=width*h/w; cw=width*clip_fraction
    # ASCIIHex + DCT filters preserve the original JPEG bytes exactly.
    # pdf:literal (without "direct") positions the image at the TeX box origin.
    literal=(f"q 0 0 {cw:.5f} {height:.5f} re W n "
             f"q {width:.5f} 0 0 {height:.5f} 0 0 cm "
             f"BI /W {w} /H {h} /BPC 8 /CS /RGB /F [/AHx /DCT] ID "
             +p.read_bytes().hex()+" > EI Q Q")
    cmh=height/28.3465; cmw=cw/28.3465
    return (r"\begin{tikzpicture}"+"\n"+
        r"\node[inner sep=0,anchor=south west] at(0,0){\hbox{\special{pdf:literal "+literal+
        r"}\phantom{\rule{"+f"{cw:.5f}bp"+"}{"+f"{height:.5f}bp"+r"}}}};"+"\n"+
        f"\\draw[<->,thick] ({cmw+.45:.5f},0)--({cmw+.45:.5f},{cmh:.5f}) "
        f"node[midway,right,align=center] {{实际尺寸\\\\{label}}};\n"+
        f"\\draw ({cmw:.5f},0)--({cmw+.7:.5f},0); "
        f"\\draw ({cmw:.5f},{cmh:.5f})--({cmw+.7:.5f},{cmh:.5f});\n"+
        r"\end{tikzpicture}")

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
    FIGS["q7-photo-a"]=photo("q7-original-23-0.jpg","7.8 cm",671/692)
    FIGS["q7-photo-b"]=photo("q7-original-24-0.jpg","9.4 cm")
    out=ROOT/"figures";out.mkdir(exist_ok=True)
    for name,body in FIGS.items():
        (out/(name+".tikz")).write_text(body.strip()+"\n")
        (out/(name+".tex")).write_text(TEMPLATE.replace("%BODY%",body))
    print(f"{len(FIGS)} figures: 23 editable schematics and 2 original measurement photos")
if __name__=="__main__":main()
