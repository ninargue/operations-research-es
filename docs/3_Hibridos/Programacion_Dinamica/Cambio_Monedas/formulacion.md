# Formulación — Cambio de Monedas

## El reto combinatorio

Con un conjunto de denominaciones $D$ de tamaño $n$ y un monto objetivo $C$, el espacio de búsqueda es en principio exponencial: el número de formas de escribir $C$ como suma ordenada de elementos de $D$ crece sin cota polinomial. La búsqueda exhaustiva (*exhaustive search*) resulta intratable para instancias medianas. La **programación dinámica** descompone el problema en subproblemas con **estructura óptima** (*optimal substructure*): el número mínimo de monedas para el monto $c$ puede expresarse en función del número mínimo para montos estrictamente menores, eliminando recálculos redundantes (*overlapping subproblems*). Esto reduce la complejidad total a $O(n \cdot C)$.

---

## Conjuntos y Parámetros

| Símbolo | Descripción |
|---|---|
| $D = \{d_1, d_2, \ldots, d_k\}$ | Conjunto de denominaciones disponibles |
| $C \in \mathbb{Z}^+$ | Monto objetivo a alcanzar exactamente |
| $n = \lvert D \rvert$ | Número de denominaciones distintas |

---

## Variable de Decisión (*Decision Variable*)

| Variable | Dominio | Descripción |
|---|---|---|
| $dp[c]$ | $\mathbb{Z}^+ \cup \{\infty\}$ | Número mínimo de monedas para alcanzar exactamente el monto $c$, para $c \in \{0, \ldots, C\}$ |
| $\text{moneda\_usada}[c]$ | $D \cup \{-1\}$ | Denominación $d \in D$ que produjo el mínimo en $dp[c]$; usada para reconstrucción |

---

## Función Objetivo (*Objective Function*)

$$\min \quad dp[C]$$

---

## Restricciones

### R1 — Monto exacto

La suma de las monedas seleccionadas debe igualar exactamente $C$:

$$\sum_{j=1}^{dp[C]} d_{\sigma(j)} = C$$

donde $\sigma(j)$ es la secuencia de denominaciones elegidas en la reconstrucción por backtracking.

### R2 — Recurrencia DP

$$dp[c] = \begin{cases}
0 & \text{si } c = 0 \\
\infty & \text{si } c > 0 \text{ y } \nexists\, d \in D : d \leq c \text{ con } dp[c-d] < \infty \\
\displaystyle\min_{d \in D,\; d \leq c}\bigl(1 + dp[c - d]\bigr) & \text{si } c > 0
\end{cases}$$

El caso base $dp[0] = 0$ refleja que el monto cero se alcanza sin ninguna moneda. Para todo $c > 0$, la recurrencia evalúa cada denominación $d \leq c$ y elige la que minimiza $1 + dp[c - d]$.

### R3 — Denominaciones válidas

Solo se pueden usar denominaciones del conjunto $D$:

$$d \in D \quad \forall\, d \text{ usada en la solución}$$

---

## Herramientas de implementación

| Librería | Solver | Aplica a | Licencia | Rendimiento |
|---|---|---|---|---|
| Python estándar (DP) | — | Coin Change, variantes ilimitadas | PSF | ★★★★★ |
| `ortools` CP-SAT | CP-SAT | MIP entero general | Apache 2.0 | ★★★★☆ |
| `pulp` | CBC / HiGHS | LP, MIP (interfaz agnóstica) | MIT | ★★★☆☆ |
| `gurobipy` | Gurobi | LP, MIP, QP | Comercial | ★★★★★ |

Para el Cambio de Monedas con estructura de uso ilimitado, **Python estándar con DP bottom-up** es la solución canónica: tiempo $O(n \cdot C)$, espacio $O(C)$, sin dependencias externas y con solución exacta. Los solvers MIP añaden overhead innecesario para esta estructura específica.

---

## Diferencia con Mochila 0/1

| Característica | Cambio de Monedas | Mochila 0/1 |
|---|---|---|
| Dimensión del vector/tabla | 1D — vector $dp[0 \ldots C]$ | 2D — tabla $dp[0 \ldots n][0 \ldots W]$ |
| Uso de cada elemento | Ilimitado (*unbounded*) | Binario (0 o 1 vez) |
| Tipo de optimización | Minimización (monedas mínimas) | Maximización (valor máximo) |
| Recorrido del bucle interno | De $1$ a $C$ (orden ascendente) | De $W$ a $w_i$ (orden descendente para reducción de espacio) |
| Dependencia en recurrencia | $dp[c - d]$ para todo $d \in D$ | $dp[i-1][w - w_i]$ para ítem $i$ |
