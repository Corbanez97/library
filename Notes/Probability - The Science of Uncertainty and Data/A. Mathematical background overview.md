..This appendix covers a few selected topics that should come in hand when studying [[1. Probability models and axioms|Probability Theory]].
![[A01.pdf]]

## Set properties

$$S \cup T = T \cup S$$
$$S\cup (T\cup U) = (S\cup T) \cup U$$
$$S \cap (T\cup U) = (S\cap T) \cup (S\cap U)$$
$$S\cup (T\cap U) = (S\cup T) \cap (S\cup U)$$
$$(S^c)^c = S$$
$$S\cap S^c = \emptyset$$
$$S \cup \Omega = \Omega \; \forall\; S \subseteq \Omega$$
$$S\cap \Omega = S \; \forall S \subseteq \Omega $$

## De Morgan's laws

$$\bigg(\bigcup_n S_n\bigg)^c = \bigcap_n S^c_n,$$
$$\bigg(\bigcap_n S_n\bigg)^c = \bigcup_n S^c_n.$$

See the [Wiki link](https://en.wikipedia.org/wiki/De_Morgan%27s_laws) for a formal proof of the laws. A good visualization of these laws are shown in the picture below.

![[de_morgans_laws.png]]
***GPT Addendum:***
	In the context of set theory and probability, De Morgan’s Laws are two rules that allow us to relate the complement of the union of sets to the intersection of their complements, and vice versa. These laws are named after the British mathematician Augustus De Morgan. The laws are as follows:
	 The complement of the union of two sets is equal to the intersection of their complements. Mathematically, this is represented as:
    $$
    (A\cup B)^c=A^c\cup B^c
    $$
    In the context of your Venn diagram, this means that the area outside both sets A and B (i.e., the complement of their union) is the same as the area that is outside A and outside B (i.e., the intersection of their complements).
    The complement of the intersection of two sets is equal to the union of their complements. This is represented as:
    $$
    (A\cap B)^c=A^c \cup B^c
    $$
    In your Venn diagram, this means that the area outside the intersection of sets A and B (i.e., the complement of their intersection) is the same as the area that is either outside A or outside B (i.e., the union of their complements). 
## Bonferroni's inequality
$$
P(A_1 \cap A_2 \cap ... \cap A_n) \geq P(A_1 \cup A_2 \cup ... \cup A_n) - (n - 1)
$$
**Proof**: 
	Beginning with,
	$$
	1 - P(A_1\cap A_2\cap ... \cap A_n) = P((A_1\cap A_2\cap ... \cap A_n)^c),
	$$
	[[A. Mathematical background overview#De Morgan's laws|De Morgan's law]] tell us that the right hand side of the above equation can be written as
	$$
	P((A_1\cap A_2\cap ... \cap A_n)^c) = P(A_1^c \cup A_2^c \cup ...\cup A_n^c).
	$$
	We can rewrite this as
	$$
	1 - P(A_1\cap A_2\cap ... \cap A_n)  = P(A_1^c \cup A_2^c \cup ...\cup A_n^c),
	$$
	where by the [[1. Probability models and axioms#Probability axioms|union bound]] we know that
	$$
	P(A_1^c \cup A_2^c \cup ... \cup A_n^c) \leq P(A_1^c) + P(A_2^c) + ... + P(A_n^c) = 1 - P(A_{1}) + 1 - P(A_{2}) +...+ 1 - P(A_{n}).
	$$
	 This inequality occurs $n$ times. Thus, by replacing the above relation into the third equation we find:
	$$
	P(A_{1}) + P(A_{2}) +...+ P(A_{n}) - n + 1 \leq P(A_{1} \cap A_{2} \cap ... \cap A_{n}).
	$$
$\square$