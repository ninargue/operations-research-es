# Formulación — Subsecuencia Común más Larga (LCS)

## El reto sobre secuencias

Dadas dos secuencias de longitudes $m$ y $n$, el espacio de búsqueda por fuerza bruta es $O(2^m)$: hay $2^m$ subsecuencias posibles de $X$, cada una verificable en $O(n)$ contra $Y$. Para $m = 30$ esto supera $10^9$ operaciones.

Programación dinámica (*dynamic programming*) aprovecha la **subestructura óptima**: la LCS de dos secuencias puede construirse a partir de la LCS de sus prefijos. Al resolver y almacenar todos los subproblemas $\text{dp}[i][j]$ para $i \in \{0,\ldots,m\}$ y $j \in \{0,\ldots,n\}$, se obtiene la solución exacta en tiempo $O(m \cdot n)$ sin repetir cálculos.

---

## Conjuntos y Parámetros

| Símbolo | Tipo | Descripción |
|---|---|---|
| $X = x_1 x_2 \ldots x_m$ | secuencia | Primera secuencia de entrada, longitud $m$ |
| $Y = y_1 y_2 \ldots y_n$ | secuencia | Segunda secuencia de entrada, longitud $n$ |
| $m$ | entero | Longitud de $X$: $m = \|X\|$ |
| $n$ | entero | Longitud de $Y$: $n = \|Y\|$ |
| $\Sigma$ | conjunto | Alfabeto (conjunto de símbolos posibles) |

---

## Variable de decisión

Se construye una tabla bidimensional:

$$\text{dp}[i][j] \;=\; \text{longitud de la LCS de } X[1..i] \text{ e } Y[1..j]$$

para $i \in \{0, 1, \ldots, m\}$ y $j \in \{0, 1, \ldots, n\}$.

Para recuperar la LCS explícita, se almacena adicionalmente la **dirección de backtracking** en cada celda:

$$\text{dir}[i][j] \in \{\text{diagonal}, \;\text{arriba}, \;\text{izquierda}\}$$

| Dirección | Código | Significado |
|---|---|---|
| Diagonal | `D` | $x_i = y_j$: se extiende la LCS con el carácter coincidente |
| Arriba (*up*) | `U` | Se ignora $x_i$; la LCS proviene de $\text{dp}[i-1][j]$ |
| Izquierda (*left*) | `L` | Se ignora $y_j$; la LCS proviene de $\text{dp}[i][j-1]$ |

---

## Función objetivo

$$\max \; z = \text{dp}[m][n]$$

El valor $\text{dp}[m][n]$ es la longitud de la LCS de las dos secuencias completas. Para recuperar la secuencia, se recorre `dir` desde $(m, n)$ hacia $(0, 0)$.

---

## Restricciones

### R1 — Orden relativo (*order preservation*)

La subsecuencia común debe preservar el orden de aparición de los elementos en ambas secuencias originales. Formalmente, si la LCS es $z_1 z_2 \ldots z_k$, entonces existen índices

$$1 \leq i_1 < i_2 < \cdots < i_k \leq m \quad \text{con} \quad x_{i_t} = z_t$$

$$1 \leq j_1 < j_2 < \cdots < j_k \leq n \quad \text{con} \quad y_{j_t} = z_t$$

No se permiten reordenamientos ni repeticiones fuera de las ocurrencias originales.

### R2 — Recurrencia DP

La tabla se llena con la siguiente regla:

$$\text{dp}[i][j] = \begin{cases}
0 & \text{si } i = 0 \text{ o } j = 0 \\[4pt]
\text{dp}[i-1][j-1] + 1 & \text{si } x_i = y_j \\[4pt]
\max\!\bigl(\text{dp}[i-1][j],\; \text{dp}[i][j-1]\bigr) & \text{si } x_i \neq y_j
\end{cases}$$

La fila 0 y la columna 0 actúan como casos base: representan prefijos vacíos, cuya LCS con cualquier secuencia tiene longitud 0.

Cuando $x_i = y_j$ (coincidencia, *match*): el carácter común se añade a la LCS del prefijo anterior $\text{dp}[i-1][j-1]$.

Cuando $x_i \neq y_j$ (no coincidencia, *mismatch*): se toma el máximo entre descartar $x_i$ o descartar $y_j$.

### R3 — Backtracking (*reconstrucción*)

La LCS se reconstruye recorriendo `dir` desde $(m, n)$ hacia $(0, 0)$:

```
i ← m,  j ← n,  lcs ← []
mientras i > 0 y j > 0:
    si dir[i][j] = 'D':
        lcs.prepend(x_i)
        i ← i - 1,  j ← j - 1
    si dir[i][j] = 'U':
        i ← i - 1
    si dir[i][j] = 'L':
        j ← j - 1
```

Los caracteres se agregan en orden inverso; al finalizar se invierten para obtener la LCS en orden correcto.

---

## Herramientas y bibliotecas

| Herramienta | Uso |
|---|---|
| Python estándar | Implementación completa de DP con listas bidimensionales; sin dependencias externas |
| `difflib` (Python stdlib) | Implementación de LCS orientada a texto; usada internamente por `SequenceMatcher` y `unified_diff` |
| Biopython (`Bio.pairwise2`, `Bio.Align`) | Alineamiento de secuencias biológicas (ADN, proteínas); soporta penalizaciones de gap y matrices de sustitución |
| NumPy | Construcción eficiente de la tabla DP con arreglos 2D; beneficioso para secuencias largas |

---

## Diferencia con Cambio de Monedas y Mochila 0/1

| Dimensión | LCS | Mochila 0/1 | Cambio de monedas |
|---|---|---|---|
| Dimensiones de la tabla | 2D: prefijos de $X$ vs. prefijos de $Y$ | 2D: ítems vs. capacidad | 1D: montos posibles |
| Significado de los ejes | Dos secuencias de entrada | Ítems disponibles y capacidad | Denominaciones y monto objetivo |
| Objetivo | Maximizar longitud de subsecuencia común | Maximizar valor sin exceder peso | Minimizar número de monedas |
| Tipo de decisión por celda | Match/no-match; tomar diagonal o max(arriba, izq.) | Incluir o excluir ítem | Usar o no usar denominación |
| Dirección de backtracking | Diagonal (match), arriba, izquierda | Arriba (excluir), diagonal (incluir) | No aplica (reconstrucción opcional) |
| Casos base | Fila 0 y columna 0 = 0 | Fila 0 = 0, columna 0 = 0 | dp[0] = 0 |
