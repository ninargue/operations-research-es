# Formulación — Mochila 0/1

## El reto combinatorio

Con $n$ ítems, el espacio de soluciones candidatas tiene $2^n$ subconjuntos. La búsqueda exhaustiva es intratable para instancias grandes. La **programación dinámica** descompone el problema en subproblemas (*subproblems*) que comparten estructura óptima (*optimal substructure*): el valor máximo para los primeros $i$ ítems con capacidad $w$ se puede expresar en función de subproblemas de menor tamaño.

---

## Conjuntos y Parámetros

| Símbolo | Descripción |
|---|---|
| $I = \{1, \ldots, n\}$ | Conjunto de ítems candidatos |
| $v_i$ | Valor del ítem $i$ |
| $w_i$ | Volumen del ítem $i$ (m³) |
| $W$ | Capacidad máxima de volumen |
| $p_i$ | Peso del ítem $i$ (kg) — caso extendido |
| $P$ | Capacidad máxima de peso (kg) — caso extendido |
| $E \subseteq I \times I$ | Pares de ítems incompatibles — caso extendido |

---

## Variable de Decisión (*Decision Variable*)

| Variable | Tipo | Descripción |
|---|---|---|
| $x_i$ | Binaria $\{0,1\}$ | 1 si el ítem $i$ se incluye, 0 en caso contrario |

La tabla DP no define explícitamente $x_i$: almacena el valor óptimo $dp[i][w]$ para cada par $(i, w)$ y reconstruye $x_i$ en el paso de backtracking.

---

## Función Objetivo (*Objective Function*)

$$\max \quad \sum_{i=1}^{n} v_i \, x_i$$

---

## Restricciones

### R1 — Capacidad: no exceder el peso máximo

$$\sum_{i=1}^{n} w_i \, x_i \leq W$$

### R2 — Recurrencia DP (definición de los subproblemas)

$$dp[i][w] = \begin{cases}
0 & \text{si } i = 0 \text{ o } w = 0 \\
dp[i-1][w] & \text{si } w_i > w \\
\max\!\bigl(dp[i-1][w],\; v_i + dp[i-1][w - w_i]\bigr) & \text{si } w_i \leq w
\end{cases}$$

La fila $i=0$ y la columna $w=0$ son los casos base (valor cero).

### R3 — Naturaleza binaria de las variables

$$x_i \in \{0, 1\} \quad \forall i \in I$$

### R4 — Peso máximo (caso extendido)

Segunda restricción de recurso independiente del volumen:

$$\sum_{i=1}^{n} p_i \, x_i \leq P$$

La tabla DP se extiende a tres dimensiones: $dp[i][v][p]$ = valor máximo para los primeros $i$ ítems con volumen $\leq v$ y peso $\leq p$.

$$dp[i][v][p] = \begin{cases}
0 & \text{si } i = 0 \\
dp[i-1][v][p] & \text{si } w_i > v \text{ o } p_i > p \\
\max\!\bigl(dp[i-1][v][p],\; v_i + dp[i-1][v - w_i][p - p_i]\bigr) & \text{en otro caso}
\end{cases}$$

### R5 — Incompatibilidad entre ítems (caso extendido)

Para cada par $(a, b) \in E$ de ítems en conflicto:

$$x_a + x_b \leq 1$$

**Estrategia de resolución**: descomponer en dos subproblemas independientes — uno excluyendo $a$ y otro excluyendo $b$ — y tomar el de mayor valor óptimo. Esta descomposición es exacta cuando el par incompatible es único; para múltiples pares se generaliza con enumeración de casos o programación entera.

---

## Herramientas de implementación

| Librería | Solver | Aplica a | Licencia | Rendimiento |
|---|---|---|---|---|
| Python estándar (DP) | — | Mochila 0/1, variantes acotadas | PSF | ★★★★★ |
| `ortools` CP-SAT | CP-SAT | MIP binario general | Apache 2.0 | ★★★★☆ |
| `pulp` | CBC / HiGHS | LP, MIP (interfaz agnóstica) | MIT | ★★★☆☆ |
| `gurobipy` | Gurobi | LP, MIP, QP | Comercial | ★★★★★ |

> El rendimiento depende del tipo de problema, tamaño de instancia y configuración del hardware.

Para la Mochila 0/1 pura, **Python estándar con DP bottom-up** es la solución canónica: tiempo $O(n \cdot W)$, espacio $O(n \cdot W)$, sin dependencias externas y con solución exacta. Los solvers MIP como CP-SAT o Gurobi son más flexibles pero añaden overhead innecesario para esta estructura específica.
