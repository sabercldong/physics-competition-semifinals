#!/usr/bin/env python3
"""Create editable TikZ sources. No original files are modified."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
F = ROOT / "figures"
F.mkdir(exist_ok=True)
FIGS = {}
FIGS["q1-network"] = r"""
\begin{tikzpicture}[x=1.1cm,y=1.1cm]
\coordinate (A) at (0,3); \coordinate (B) at (3,0);
\coordinate (C) at (-3,0); \coordinate (D) at (0,1);
\draw[thick] (A)--node[fill=white,sloped,above] {$16\kappa$}(C)
 --node[fill=white,below] {$\kappa$}(B)
 --node[fill=white,sloped,above] {$\kappa/9$}(A);
\draw[thick,dashed] (A)--node[fill=white,right] {$\kappa$}(D);
\draw[thick,dashed] (C)--node[fill=white,sloped,above] {$8\kappa$}(D)
 --node[fill=white,sloped,above] {$16\kappa$}(B);
\foreach \p/\pos in {A/above,B/right,C/left,D/below}
 {\fill (\p) circle (1.5pt); \node[\pos] at (\p) {$\p$};}
\draw (A)--(4.1,3)--(4.1,1.7);
\draw (B)--(4.1,0)--(4.1,1.3);
\draw[thick] (3.85,1.7)--(4.35,1.7);
\draw[thick] (3.97,1.3)--(4.23,1.3);
\node[right] at (4.35,1.5) {$V_0$};
\node at (0,-.75) {$I_{ij}=c_{ij}(V_i-V_j)^3$};
\end{tikzpicture}
"""
FIGS["q1-potentials"] = r"""
\begin{tikzpicture}[x=1cm,y=1cm]
\node[dot,label=above:{$A:\ V_0$}] (A) at (0,3) {};
\node[dot,label=left:{$C:\ 2V_0/3$}] (C) at (-2,2) {};
\node[dot,label=right:{$D:\ V_0/3$}] (D) at (2,1) {};
\node[dot,label=below:{$B:\ 0$}] (B) at (0,0) {};
\draw[arr] (A)--node[fill=white,above left] {$16/27$}(C);
\draw[arr] (A)--node[fill=white,above right] {$8/27$}(D);
\draw[arr] (C)--node[fill=white,below left] {$8/27$}(B);
\draw[arr] (D)--node[fill=white,below right] {$16/27$}(B);
\draw[arr] (C)--node[fill=white,above] {$8/27$}(D);
\draw[arr,dashed] (A)--node[fill=white,right,pos=.28] {$1/9$}(B);
\node at (0,-.9) {电流标签的单位：$\kappa V_0^3$};
\end{tikzpicture}
"""
FIGS["q2-model"] = r"""
\begin{tikzpicture}
\draw[thick] (-1,0)--(5,0); \node[below] at (4.6,0) {地面};
\coordinate (O) at (0,0); \coordinate (P) at (.75,3.5);
\draw[thick,decorate,decoration={zigzag,segment length=5pt,amplitude=2pt}] (O)--(P);
\fill (O) circle (2pt) node[below] {$O$};
\fill (P) circle (4pt) node[above] {$m$};
\draw[arr] (O)--(3,0) node[below] {$x$};
\draw[arr] (0,0)--(0,4.1) node[left] {竖直};
\draw[arr] (P)--(.75,2.55) node[right] {$mg$};
\draw[arr] (P)--(1.8,3.27) node[right] {$r\dot\varphi\,\hat{\boldsymbol e}_\varphi$};
\draw[arr] (.3,3.65)--(.07,2.58) node[left] {$\dot r\,\hat{\boldsymbol e}_r$};
\draw[<->] (-.9,.1)--(-.15,3.6) node[midway,left] {$r$};
\draw[arr] (1.1,0) arc(0:78:1.1) node[midway,right] {$\varphi$};
\draw[arr] (.1,3.1) arc(100:60:1.2);
\node[right] at (1.4,3.9) {顺时针};
\end{tikzpicture}
"""
FIGS["q2-compression"] = r"""
\begin{tikzpicture}[x=1.6cm,y=1.1cm]
\draw[arr] (-.2,0)--(4.15,0) node[right] {$t$};
\draw[arr] (0,-2.35)--(0,.8) node[above] {$r-l_0$};
\draw[blue!65!black,thick,domain=0:2.65164,samples=100]
 plot(\x,{.5*(1-cos(57.29578*\x))-2*sin(57.29578*\x)});
\draw[dashed] (1.32582,0)--(1.32582,-1.56);
\fill (1.32582,-1.56155) circle (1.5pt);
\node[below] at (1.32582,-1.65) {$-d_{\max}$};
\node[above] at (1.32582,0) {$t'/2$};
\node[above] at (2.65164,0) {$t'$};
\node[below left] at (0,0) {$0$};
\node at (2.5,-2.3) {支撑期：$r<l_0$};
\end{tikzpicture}
"""
FIGS["q3-model"] = r"""
\begin{tikzpicture}
\fill[gray!12] (-3,-1) rectangle (3,0);
\draw[thick] (-3,0)--(3,0);
\draw[arr] (0,-1.3)--(0,3.4) node[above] {$z$};
\draw[arr] (-3.3,0)--(3.4,0) node[right] {$x$};
\coordinate (P) at (0,2);
\fill (P) circle (2pt);
\draw[arr,thick] (P)--(1.1,3.1) node[right] {$\boldsymbol m$};
\draw[dashed] (P)--(0,3.1);
\draw[arr] (0,2.65) arc(90:45:.65) node[midway,above] {$\theta$};
\draw[<->] (-.6,0)--(-.6,2) node[midway,left] {$h$};
\node at (2,1) {真空 $\mu_0$};
\node at (0,-.6) {超导体或软磁体};
\end{tikzpicture}
"""
FIGS["q3-images"] = r"""
\begin{tikzpicture}
\foreach \xx/\txt/\sgn in {0/超导体/-1,5/软磁体/1} {
 \begin{scope}[shift={(\xx,0)}]
 \fill[gray!10] (-1.8,-2.4) rectangle (1.8,0);
 \draw[thick] (-1.8,0)--(1.8,0);
 \fill (0,1.4) circle(2pt); \fill (0,-1.4) circle(2pt);
 \draw[arr,thick] (0,1.4)--(1,2.2) node[right] {$\boldsymbol m$};
 \ifnum\sgn=-1
  \draw[arr,thick] (0,-1.4)--(1,-2.2) node[right] {$\boldsymbol m_{\rm S}$};
 \else
  \draw[arr,thick] (0,-1.4)--(-1,-.6) node[left] {$\boldsymbol m_{\rm I}$};
 \fi
 \draw[dashed] (0,1.4)--(0,-1.4);
 \node[left] at (0,1.15) {$h$}; \node[left] at (0,-1.15) {$-h$};
 \node at (0,2.85) {\txt};
 \end{scope}
}
\end{tikzpicture}
"""
FIGS["q4-orbit"] = r"""
\begin{tikzpicture}
\fill[gray!14] (-2.8,-1.5) rectangle (3.5,-.8);
\draw[thick] (-2.8,-.8)--(3.5,-.8);
\node at (.5,-1.17) {地球表面（局部示意）};
\draw[thick] (0,0)--(0,3);
\fill (0,0) circle(3pt) node[left] {接触器 $m_2$};
\fill (0,3) circle(4pt) node[left] {卫星 $m_1$};
\draw[arr,thick] (.12,.5)--(.12,2.4) node[midway,right] {$I$};
\draw[arr] (0,3)--(2.2,3) node[above] {$v_0$};
\draw[arr] (-1,1)--(-1,2.4) node[left] {$\hat{\boldsymbol r}$};
\draw[<->] (.8,0)--(.8,3) node[midway,right] {$L$};
\foreach \x in {-2,2.8}\foreach \y in {.2,1.4,2.6}
 \node at (\x,\y) {$\otimes$};
\node at (3.2,3.5) {$\boldsymbol B$};
\node at (.8,-2) {$+\hat{\boldsymbol z}$ 指向纸内};
\end{tikzpicture}
"""
FIGS["q4-torques"] = r"""
\begin{tikzpicture}
\draw[arr] (0,0)--(0,3.4) node[above] {$\hat{\boldsymbol r}$};
\draw[arr] (0,0)--(3.3,0) node[right] {$\hat{\boldsymbol\phi}$};
\coordinate (S) at (.8,1.8); \coordinate (C) at (-1.6,-3.6);
\draw[thick] (C)--(S);
\fill (S) circle(3pt) node[right] {$m_1$};
\fill (C) circle(3pt) node[left] {$m_2$};
\fill (0,0) circle(2pt) node[above left] {质心};
\draw[arr] (S)--(-.4,2.33);
\draw[arr] (-.4,-.9)--(-1.6,-.37);
\draw[arr] (-.8,-1.8)--(-2,-1.27) node[left] {$d\boldsymbol F_L$};
\draw[arr] (-1.2,-2.7)--(-2.4,-2.17);
\node[fill=white,right] at (.35,.75) {$l_1$};
\node[fill=white,right] at (-.85,-2.25) {$l_2$};
\draw[arr] (0,1) arc(90:66:1) node[midway,above] {$\theta$};
\draw[arr] (1.5,-2.7)--(1.5,-1.9) node[right] {$F_r>0$};
\draw[arr] (1.5,-2.7)--(.7,-2.7) node[below] {$F_\phi<0$};
\node at (1.8,-4.1) {$\tau_{g,z}<0,\ \tau_{L,z}>0$};
\end{tikzpicture}
"""
FIGS["q5-equilibrium"] = r"""
\begin{tikzpicture}
\fill[blue!7] (-3.3,-2) rectangle (3.3,.25);
\fill[gray!15] (-2,-1.5) rectangle (2,1.5);
\fill[blue!12] (-2,-1.5) rectangle (2,.25);
\draw[thick] (-2,-1.5) rectangle (2,1.5);
\draw[blue!65!black] (-3.3,.25)--(3.3,.25) node[right] {液面};
\fill (0,0) circle(2pt) node[right] {$G$};
\fill (0,-.625) circle(2pt) node[right] {$B$};
\draw[<->] (-2,1.85)--(2,1.85) node[midway,above] {$2a$};
\draw[<->] (-2.4,-1.5)--(-2.4,1.5) node[midway,left] {$2b$};
\draw[<->] (2.45,-1.5)--(2.45,.25) node[midway,right] {$h$};
\draw[arr] (0,-.6)--(0,1) node[left] {$F_b$};
\draw[arr] (.35,0)--(.35,-1.1) node[right] {$mg$};
\end{tikzpicture}
"""
FIGS["q5-centroid"] = r"""
\begin{tikzpicture}
\fill[gray!10] (-2,-1.5) rectangle (2,1.5);
\fill[blue!12] (-2,-1.5)--(2,-1.5)--(2,.59)--(-2,-.29)--cycle;
\draw[thick] (-2,-1.5) rectangle (2,1.5);
\draw[blue!65!black] (-3,-.51)--(3,.81) node[right] {液面};
\draw[arr] (-2.8,0)--(2.8,0) node[right] {$x$};
\draw[arr] (0,-1.9)--(0,2.5) node[above] {$y$};
\fill (0,0) circle(2pt) node[below left] {$G$};
\coordinate (B) at (.1778,-.655);
\fill (B) circle(2pt) node[right] {$B'$};
\draw[arr,thick] (B)--(-.3,1.518);
\draw[dashed] (B)--(0,.153);
\fill (0,.153) circle(2pt);
\draw[thin] (0,.153)--(-1,.8) node[left] {$M$};
\fill[blue!30] (1.45,-1.5)--(1.58,-1.5)--(1.58,.4976)--(1.45,.469)--cycle;
\draw[<->] (1.74,-1.5)--(1.74,.48) node[midway,right] {$H(x)$};
\node at (1.4,-1.78) {$dx$};
\draw (1.1,0) arc(0:12.4:1.1) node[midway,above] {$\theta$};
\node at (0,-2.4) {$y=h-b+x\tan\theta$};
\end{tikzpicture}
"""
FIGS["q6-slab"] = r"""
\begin{tikzpicture}
\fill[blue!5] (0,-1.2) rectangle (6,1.2);
\fill[red!15] (0,-1.2) rectangle (.55,1.2);
\fill[blue!18] (6,-1.2) rectangle (6.55,1.2);
\draw[dashed] (0,-1.4)--(0,1.5) (6,-1.4)--(6,1.5);
\draw[thick] (.55,-1.2) rectangle (6.55,1.2);
\foreach \y in {-.7,0,.7} {
 \node at (.27,\y) {$+$}; \node at (6.27,\y) {$-$};}
\draw[arr,thick] (1,0)--(5.4,0) node[midway,above] {$E_x=n_0e\xi/\varepsilon_0$};
\draw[<->] (0,-1.6)--(.55,-1.6) node[midway,below] {$\xi$};
\draw[<->] (6,-1.6)--(6.55,-1.6) node[midway,below] {$\xi$};
\draw[<->] (0,1.7)--(6,1.7) node[midway,above] {$L$};
\draw[arr] (6.8,0)--(8,0) node[right] {$x$};
\node at (3,-2.4) {正离子固定；电子层右移 $\xi>0$};
\end{tikzpicture}
"""
FIGS["q6-screening"] = r"""
\begin{tikzpicture}[x=1.4cm,y=3cm]
\draw[arr] (-.15,0)--(4.7,0) node[right] {$r/\lambda_{\rm D}$};
\draw[arr] (0,-.08)--(0,1.16) node[above] {$\varphi/\varphi_{\rm C}$};
\draw[blue!65!black,thick,domain=0:4.2,samples=90] plot(\x,{exp(-\x)});
\draw[dashed] (1,0)--(1,.367879)--(0,.367879);
\node[below] at (1,0) {$1$}; \node[left] at (0,1) {$1$};
\node[left] at (0,.367879) {$e^{-1}$};
\node at (2.7,.7) {$\varphi_{\rm C}=Q/(4\pi\varepsilon_0r)$};
\node at (2.8,.52) {$\varphi/\varphi_{\rm C}=e^{-r/\lambda_{\rm D}}$};
\end{tikzpicture}
"""
FIGS["q6-dispersion"] = r"""
\begin{tikzpicture}[x=1.7cm,y=1.2cm]
\draw[arr] (-.15,0)--(3.7,0) node[right] {$ck/\omega_{\rm p}$};
\draw[arr] (0,-.15)--(0,4) node[above] {$\omega/\omega_{\rm p}$};
\draw[dashed,gray] (0,0)--(3.3,3.3) node[right] {真空};
\draw[blue!65!black,thick,domain=0:3.3,samples=90] plot(\x,{sqrt(1+\x*\x)});
\fill (0,1) circle(1.8pt) node[left] {$1$};
\draw[dashed] (1,0)--(1,1.4142)--(0,1.4142);
\node[left] at (0,1.4142) {$\sqrt2$};
\node[below] at (1,0) {$1$};
\node at (2.4,1.1) {$\omega^2=\omega_{\rm p}^2+c^2k^2$};
\end{tikzpicture}
"""
FIGS["q7-layers"] = r"""
\begin{tikzpicture}
\fill[gray!10] (-2,1.9) rectangle (0,4);
\fill[blue!12] (0,1.9) rectangle (2,4);
\draw[thick] (0,1.9)--(0,4);
\draw[arr] (-1.8,3.5)--(-.25,3.5) node[midway,above] {$E_i$};
\draw[arr] (-.25,2.7)--(-1.8,2.7) node[midway,above] {$E_r$};
\draw[arr] (.2,3.3)--(1.8,3.3) node[midway,above] {$E_t$};
\node at (-1,2.2) {$n_1$}; \node at (1,2.2) {$n_2$};
\node at (0,1.5) {$x=0$};
\fill[gray!10] (-2,-1.3) rectangle (0,.6);
\fill[gray!10] (6.4,-1.3) rectangle (7.5,.6);
\node at (-1,-.8) {$n_1$}; \node at (7,-.6) {$n_1$};
\foreach \p in {0,1,2,3} {
 \fill[blue!16] (1.6*\p,-1.3) rectangle (1.6*\p+.65,.6);
 \fill[gray!10] (1.6*\p+.65,-1.3) rectangle (1.6*\p+1.6,.6);
 \draw (1.6*\p,-1.3)--(1.6*\p,.6);
 \node at (1.6*\p+.325,-.6) {$n_2$};
 \node at (1.6*\p+1.12,-.6) {$n_1$};}
\draw[arr] (-2,-.3)--(-.2,-.3) node[midway,above] {入射};
\draw[arr] (-2,-1.3)--(8,-1.3) node[right] {$x$};
\draw[<->] (0,.9)--(.65,.9) node[midway,above] {$d_2$};
\draw[<->] (.65,.9)--(1.6,.9) node[midway,above] {$d_1$};
\draw[<->] (0,-1.9)--(6.4,-1.9) node[midway,below] {$N$ 个完整周期（示意）};
\node[below] at (0,-1.3) {$0$};
\end{tikzpicture}
"""
FIGS["q7-paths"] = r"""
\begin{tikzpicture}
\draw[thick] (0,-1.5)--(0,2.2) node[above] {$x=pa$};
\draw[thick] (2,-1.5)--(2,2.2) node[above] {$x=pa+d_2$};
\draw[thick] (4.8,-1.5)--(4.8,2.2) node[above] {$x=(p+1)a$};
\fill[blue!7] (0,-1.5) rectangle (2,1.8);
\node at (1,-1.15) {$n_2,d_2$};
\node at (3.4,-1.15) {$n_1,d_1$};
\draw[arr] (-2,1.1)--(0,1.1);
\draw[arr] (0,.7)--(-2,.7);
\draw[arr] (-2,-.1)--(2,-.1);
\draw[arr] (2,-.5)--(-2,-.5);
\node[left] at (-2,.7) {$r e^{2ipkS}$};
\node[left] at (-2,-.5) {$-r e^{2ik(pS+n_2d_2)}$};
\end{tikzpicture}
"""
FIGS["q7-interference"] = r"""
\begin{tikzpicture}[x=.68cm,y=.9cm]
\foreach \p in {0,1,2,3,4} \draw[arr] (\p*1.2,1)--(\p*1.2+1,1);
\node at (3,1.75) {$2kS=2m\pi$：各周期同相};
\draw[arr] (0,-1.4)--(1.5,-1.4);
\draw[arr] (3,-1.4)--(1.5,-1.4);
\node at (5,-1.4) {$r-r e^{2il\pi}=0$};
\node at (3,-2.1) {缺级：同周期内相消};
\begin{scope}[shift={(12,-1)},x=1cm,y=1cm]
\draw[arr] (-1.5,0)--(1.6,0) node[right] {$\epsilon$};
\draw[arr] (0,-.2)--(0,2) node[above] {$|r_{\rm tot}|$};
\draw[thick,blue!65!black] (-1.2,1.4)--(0,0)--(1.2,1.4);
\node[below] at (0,0) {$0$};
\end{scope}
\end{tikzpicture}
"""

PRE = r"""\documentclass[tikz,border=8pt]{standalone}
\usepackage[UTF8,fontset=fandol]{ctex}
\usepackage{amsmath,amssymb,bm}
\usetikzlibrary{arrows.meta,calc,decorations.pathmorphing}
\tikzset{arr/.style={-{Stealth[length=2mm]},semithick},
dot/.style={circle,fill,inner sep=1.5pt}}
\begin{document}
\small
"""
if __name__ == "__main__":
    for name, body in FIGS.items():
        (F / f"{name}.tikz").write_text(body.strip()+"\n",encoding="utf-8")
        (F / f"{name}.tex").write_text(PRE+body+r"\end{document}"+"\n",encoding="utf-8")
    print(f"Created {len(FIGS)} TikZ figures")
