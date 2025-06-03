![[Segunda Lista.pdf]]

## 1.a)

Podemos simplificar $[A, BC]$ somando e subtraindo um termo de $BAC$, tal que
$$
[A, BC] = ABC - BCA + BAC - BAC = B[A, C] + [A, B]C.
$$
Utilizando isto como base, temos
$$
[AB, CD] = C[AB, D] + [AB, C]D.
$$
Invertendo os comutadores identificamos
$$
[AB, CD] = -C[D, AB] - [C, AB]D,
$$
onde podemos iterativamente aplicar a primeira expressão. Assim,
$$
[AB, CD] = -CA[D, B] - C[D, A]B - A[C, B]D - [C, A]BD.
$$
Logo, invertendo os comutadores mais uma vez, encontramos que
$$
[AB, CD] = [A, C]BD + C[A, D]B + A[B, C]D + CA[B, D].
$$
Entretanto, podemos partir dos comutadores invertidos, *i.e.*,
$$
-[CD, AB] = -A[CD, B] - [CD,A]B.
$$
Iterando analogamente,
$$
-[CD, AB] = AC[B,D] + A[B, C]D + C[A, D]B + [A, C]DB = [AB, CD].
$$

## 1.b)

Considerando o anticomutador
$$
\{A, B\} = AB + BA
$$
temos que o comutador
$$
[A, BC] = ABC - BCA = ABC - BCA +BAC - BAC
$$
pode ser escrito como
$$
[A, BC] = \{A, B\}C - B\{A, C\}.
$$
