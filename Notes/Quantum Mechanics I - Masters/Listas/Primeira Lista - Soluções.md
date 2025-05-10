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

Podemos normalizar estas bases, tal que
$$
\ket{\lambda_{1}} = 
\frac{1}{\sqrt{2}}\begin{pmatrix}
1 \\ 0 \\ -1
\end{pmatrix},
\quad 
\ket{\lambda_{2}} =
\begin{pmatrix}
0 \\ 1 \\ 0
\end{pmatrix},
\quad
\ket{\lambda_{3}} = 
\frac{1}{\sqrt{2}}\begin{pmatrix}
1 \\ 0 \\ 1
\end{pmatrix}.
$$
## 1.c)

Utilizando a base ortogonal
$$
\{\lambda_1, \lambda_2, \lambda_3\},
$$
criamos a matriz de mudança de base $P$,
$$
P = \begin{pmatrix}
1 & 0 & 1 \\
0 & 1 & 0 \\
-1 & 0 & 1
\end{pmatrix}.
$$
Sendo
$$
B_{ij} = \bra{\lambda_i} B \ket{\lambda_j}
$$
os elementos de matriz de $B$ na base de autoestados de $A$ é possível calcular todos os elementos a partir de $P$ como
$$
B' = P^{T}B P.
$$
Assim
$$
B' = \frac{1}{4}
\begin{pmatrix}
1 & 0 & -1 \\
0 & 1 & 0 \\
1 & 0 & 1
\end{pmatrix}
\begin{pmatrix}
7 & -\sqrt{2} & 1 \\
\sqrt{2} & 6 & \sqrt{2} \\
1 & \sqrt{2} & 7
\end{pmatrix}
\begin{pmatrix}
1 & 0 & 1 \\
0 & 1 & 0 \\
-1 & 0 & 1
\end{pmatrix}
$$
$\therefore$
$$
B' = \frac{1}{4}
\begin{pmatrix}
12 & - 2\sqrt{2} & 0 \\
-2\sqrt{2} & 6 & 0 \\
0 & 0 & 16
\end{pmatrix}.
$$

## 2.a)

Sejam os operadores $\hat{X}$ e $\hat{Y}$ o traço de seu produto é simétrico, *i.e.*,
$$
\operatorname{tr}(\hat{X} \hat{Y}) = \operatorname{tr}(\hat{Y} \hat{X}).
$$

*Prova:*
 Escrevendo $\hat{X}$ e $\hat{Y}$ em uma base qualquer $\ket{i}$, temos 
 $$
 \hat{X} = \sum_{i,j} X_{ij} \ket{i} \bra{j}, \quad \hat{Y} = \sum_{i,j} Y_{ij} \ket{i} \bra{j}.
$$
Tomando o produto $\hat{X}\hat{Y}$ na forma explícita
$$
\hat{X} \hat{Y} = \sum_{i,j,k,\ell} X_{ij} Y_{k\ell} \ket{i} \braket{j|k} \bra{\ell},
$$
que, sendo $\braket{j|k} = \delta_{jk}$, se simplifica para
$$
\hat{X} \hat{Y} = \sum_{i,j,\ell} X_{ij} Y_{j\ell} \ket{i} \bra{\ell}.
$$
Por fim, tomando o traço,
$$
\operatorname{tr}(\hat{X} \hat{Y}) = \sum_{i,j} X_{ij} Y_{ji}.
$$
De forma análoga,
$$
\hat{Y} \hat{X} = \sum_{i,j,k,\ell} Y_{ij} X_{k\ell} \ket{i} \braket{j|k} \bra{\ell} = \sum_{i,j,\ell} Y_{ij} X_{j\ell} \ket{i} \bra{\ell}.
$$
Novamente, tomando o traço,
$$
\operatorname{tr}(\hat{Y} \hat{X}) = \sum_{i,j} Y_{ij} X_{ji}.
$$
Como nas expressões finais temos apenas índices mudos, podemos trocá-los a vontade para evidenciar a igualdade
$$
\operatorname{tr}(\hat{X} \hat{Y}) = \operatorname{tr}(\hat{Y} \hat{X}).
$$

## 2.b)

Seja
$$
\bra{\phi}\hat{A}\ket{\psi} = \bra{\phi}\hat{A}^{\dagger}\ket{\psi}^*
$$
a definição do adjunto de um operador, se $\hat{A} = \hat{X}\hat{Y}$, temos
$$
\langle \phi | \hat{X} \hat{Y} | \psi \rangle = \left( \langle \psi | (\hat{X} \hat{Y})^\dagger | \phi \rangle \right)^*.
$$
Utilizando da associatividade dos elementos no lado esquerdo, vemos que
$$
(\langle \phi | \hat{X})(\hat{Y} | \psi \rangle) = \left( \langle \psi | (\hat{X} \hat{Y})^\dagger | \phi \rangle \right)^*.
$$
Ademais, tomando o adjunto da expressão,
$$
(\langle \phi | \hat{X})^\dagger (\hat{Y} | \psi \rangle)^\dagger = \langle \psi | (\hat{X} \hat{Y})^\dagger | \phi \rangle,
$$
ou, ao aplicar a definição do adjunto no lado esquerdo novamente,
$$
\langle \psi | \hat{Y}^{\dagger} \cdot \hat{X}^\dagger | \phi \rangle = \langle \psi | (\hat{X} \hat{Y})^\dagger | \phi \rangle.
$$
$$
\therefore (\hat{X} \hat{Y})^\dagger = \hat{Y}^\dagger \hat{X}^\dagger
$$
