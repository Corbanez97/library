![[Primeira lista de Quântica I-2025.pdf]]

## 1.a)

Sejam as matrizes $A$ e $B$,
$$
A = \frac{1}{2} \begin{pmatrix}
3 & 0 & 1 \\
0 & 2 & 0 \\
1 & 0 & 3
\end{pmatrix}, \quad
B = \frac{1}{4} \begin{pmatrix}
7 & -\sqrt{2} & 1 \\
-\sqrt{2} & 6 & \sqrt{2} \\
1 & \sqrt{2} & 7
\end{pmatrix}
$$
Podemos ver que 
$$
AB = \frac{1}{8} \begin{pmatrix}
21 + 1 & -3\sqrt{2} + \sqrt{2} & 3 + 7 \\
-2\sqrt{2} & 12 & 2\sqrt{2} \\
7 + 3 & -\sqrt{2} + 3\sqrt{2} & 21 + 1
\end{pmatrix}
= \frac{1}{8} \begin{pmatrix}
22 & -2\sqrt{2} & 10 \\
-2\sqrt{2} & 12 & 2\sqrt{2} \\
10 & 2\sqrt{2} & 22
\end{pmatrix}
$$

e

$$
BA = \frac{1}{8} \begin{pmatrix}
21 + 1 & -2\sqrt{2} & 7 + 3 \\
-3\sqrt{2} + \sqrt{2} & 12 & 3\sqrt{2} - \sqrt{2} \\
3 + 7 & 2\sqrt{2} & 21 + 1
\end{pmatrix}
= \frac{1}{8} \begin{pmatrix}
22 & -2\sqrt{2} & 10 \\
-2\sqrt{2} & 12 & 2\sqrt{2} \\
10 & 2\sqrt{2} & 22
\end{pmatrix}.
$$
Portanto,
$$
[A, B] = AB - BA = \frac{1}{8}
\begin{pmatrix}
22 & -2\sqrt{2} & 10 \\
-2\sqrt{2} & 12 & 2\sqrt{2} \\
10 & 2\sqrt{2} & 22
\end{pmatrix}
-
\frac{1}{8}
\begin{pmatrix}
22 & -2\sqrt{2} & 10 \\
-2\sqrt{2} & 12 & 2\sqrt{2} \\
10 & 2\sqrt{2} & 22
\end{pmatrix}
= 0
$$

## 1.b) 

Os autovalores de $A$ podem ser encontrados a partir da equação característica
$$
A - \lambda I = \begin{pmatrix}
\frac{3}{2} - \lambda & 0 & \frac{1}{2} \\
0 & 1 - \lambda & 0 \\
\frac{1}{2} & 0 & \frac{3}{2} - \lambda
\end{pmatrix},
$$
tal que o determinante seja nulo, *i.e.*,
$$\det(A - \lambda I) = (1 - \lambda) \left[\left(\frac{3}{2} - \lambda\right)^2 - \frac{1}{4} \right].
$$
Portanto,
$$
\quad \lambda_1 = 1, \quad \lambda_2 = 1, \quad \lambda_3 = 2.
$$
Utilizando estes valores e supondo $\ket{\lambda_{i}}$, temos
$$
\frac{1}{2} \begin{pmatrix}
3 & 0 & 1 \\
0 & 2 & 0 \\
1 & 0 & 3
\end{pmatrix}
\begin{pmatrix}
a \\
b \\
c
\end{pmatrix}
= 
\begin{pmatrix}
a \\
b \\
c
\end{pmatrix}
\Rightarrow
\begin{cases}
2b = 2b \Rightarrow b = b \\
3a + c = 2a \Rightarrow c = -a
\end{cases}
\Rightarrow
\lvert \lambda_{1,2} \rangle =
\begin{pmatrix}
a \\
b \\
-a
\end{pmatrix}
$$
e
$$
\frac{1}{2} \begin{pmatrix}
3 & 0 & 1 \\
0 & 2 & 0 \\
1 & 0 & 3
\end{pmatrix}
\begin{pmatrix}
e \\
f \\
g
\end{pmatrix}
=
\begin{pmatrix}
2e \\
2f \\
2g
\end{pmatrix}
\Rightarrow
\begin{cases}
3e + g = 4e \Rightarrow g = e \\
f = f
\end{cases}
\Rightarrow
\lvert \lambda_3 \rangle =
\begin{pmatrix}
e \\
0 \\
e
\end{pmatrix}.
$$
Encontramos assim que os autoestados $\ket{\lambda_1}$ e $\ket{\lambda_2}$ estão no subespaço definido por dois parâmetros $\{a, b\}$ e o autoestado $\ket{\lambda_3}$ no subespaço unidimensional definido por $e$. Por fim, podemos definir uma base ortogonal como
$$
\ket{\lambda_{1}} = 
\begin{pmatrix}
1 \\ 0 \\ -1
\end{pmatrix},
\quad 
\ket{\lambda_{2}} =
\begin{pmatrix}
0 \\ 1 \\ 0
\end{pmatrix},
\quad
\ket{\lambda_{3}} = 
\begin{pmatrix}
1 \\ 0 \\ 1
\end{pmatrix}.
$$