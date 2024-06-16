# y-combinator

Application of y combinator to factorial

## Definitions

Let $\text{Y} = (\lambda f . \lambda x . f(xx))(\lambda f . \lambda x . f(xx))$.

Let $\text{F} = \lambda f . \lambda n . [\text{if } n == 0 \text{ then } 1 \text{ else } n * f (n-1)]$.

### Notice

$\text{YF} = \text{F} (\text{YF})$

## $\text{YF}3$

$$
\begin{align}
    \text{YF} \ 3 &= \text{F}(\text{YF}) \ 3 \\
                         &= (\lambda f. \lambda n . [\text{if } n == 0 \text{ then } 1 \text{ else } n * f (n-1)]) (\text{YF}) \ 3 \\
                         &= (\lambda n . [\text{if } n == 0 \text{ then } 1 \text{ else } n * \text{YF}(n-1)]) \ 3 \\
                         &= \text{if } 3 == 0 \text{ then } 1 \text{ else } 3 * \text{YF}(3-1) \\
                         &= 3 * \text{YF} \ 2 \\
                         &= 3 * \text{F}(\text{YF}) \ 2 \\
                         &= 3 * (\lambda f. \lambda n . [\text{if } n == 0 \text{ then } 1 \text{ else } n * f (n-1)]) (\text{YF}) \ 2 \\
                         &= 3 * (\lambda n . [\text{if } n == 0 \text{ then } 1 \text{ else } n * \text{YF}(n-1)]) \ 2 \\
                         &= 3 * (\text{if } 2 == 0 \text{ then } 1 \text{ else } 2 * \text{YF}(2-1)) \\
                         &= 3 * 2 * \text{YF} \ 1 \\
                         &= 3 * 2 * \text{F} (\text{YF}) 1 \\
                         &= 3 * 2 * (\lambda f. \lambda n . [\text{if } n == 0 \text{ then } 1 \text{ else } n * f (n-1)]) (\text{YF}) \ 1 \\
                         &= 3 * 2 * (\lambda n . [\text{if } n == 0 \text{ then } 1 \text{ else } n * \text{YF}(n-1)]) \ 1 \\
                         &= 3 * 2 * (\text{if } 1 == 0 \text{ then } 1 \text{ else } 1 * \text{YF}(1-1)) \\
                         &= 3 * 2 * 1 * \text{YF} \ 0 \\
                         &= 3 * 2 * 1 * (\lambda f. \lambda n . [\text{if } n == 0 \text{ then } 1 \text{ else } n * f (n-1)]) (\text{YF}) \ 0 \\
                         &= 3 * 2 * 1 * (\lambda n . [\text{if } n == 0 \text{ then } 1 \text{ else } n * \text{YF}(n-1)]) \ 0 \\
                         &= 3 * 2 * 1 * 1 \\
                         &= 6.
\end{align}
$$
