# Ejemplos — Subsecuencia Común más Larga (LCS)

## Caso Base — Datos

| Parámetro | Valor |
|---|---|
| Secuencia $X$ | `"ABCBDAB"` |
| Longitud $m$ | 7 |
| Secuencia $Y$ | `"BDCABA"` |
| Longitud $n$ | 6 |
| LCS óptima | `"BCBA"` (o `"BDAB"`) |
| Longitud óptima $z^*$ | 4 |

---

## Tabla DP desplegada

La tabla tiene $(m+1) \times (n+1) = 8 \times 7$ celdas. La fila 0 y la columna 0 son todo ceros (casos base: prefijo vacío).

Cada celda $\text{dp}[i][j]$ se calcula con la recurrencia:

$$\text{dp}[i][j] = \begin{cases}
0 & \text{si } i = 0 \text{ o } j = 0 \\
\text{dp}[i-1][j-1] + 1 & \text{si } X[i] = Y[j] \\
\max(\text{dp}[i-1][j],\; \text{dp}[i][j-1]) & \text{si } X[i] \neq Y[j]
\end{cases}$$

```
        ""   B   D   C   A   B   A
   ""    0   0   0   0   0   0   0
    A    0   0   0   0   1   1   1
    B    0   1   1   1   1   2   2
    C    0   1   1   2   2   2   2
    B    0   1   1   2   2   3   3
    D    0   1   2   2   2   3   3
    A    0   1   2   2   3   3   4
    B    0   1   2   2   3   4   4
```

### Registro de decisiones por fila

| $i$ / $X[i]$ | $j$ / $Y[j]$ | Coincidencia | Valor $\text{dp}[i][j]$ | Fuente |
|---|---|---|---|---|
| 1 / A | 1 / B | No | 0 | max(dp[0][1]=0, dp[1][0]=0) = 0 |
| 1 / A | 2 / D | No | 0 | max(dp[0][2]=0, dp[1][1]=0) = 0 |
| 1 / A | 3 / C | No | 0 | max(dp[0][3]=0, dp[1][2]=0) = 0 |
| **1 / A** | **4 / A** | **Si** | **1** | dp[0][3]+1 = 0+1 = 1 (diagonal) |
| 1 / A | 5 / B | No | 1 | max(dp[0][5]=0, dp[1][4]=1) = 1 |
| **1 / A** | **6 / A** | **Si** | **1** | dp[0][5]+1 = 0+1 = 1 (diagonal) |
| **2 / B** | **1 / B** | **Si** | **1** | dp[1][0]+1 = 0+1 = 1 (diagonal) |
| 2 / B | 2 / D | No | 1 | max(dp[1][2]=0, dp[2][1]=1) = 1 |
| 2 / B | 3 / C | No | 1 | max(dp[1][3]=0, dp[2][2]=1) = 1 |
| 2 / B | 4 / A | No | 1 | max(dp[1][4]=1, dp[2][3]=1) = 1 |
| **2 / B** | **5 / B** | **Si** | **2** | dp[1][4]+1 = 1+1 = 2 (diagonal) |
| 2 / B | 6 / A | No | 2 | max(dp[1][6]=1, dp[2][5]=2) = 2 |
| 3 / C | 1 / B | No | 1 | max(dp[2][1]=1, dp[3][0]=0) = 1 |
| 3 / C | 2 / D | No | 1 | max(dp[2][2]=1, dp[3][1]=1) = 1 |
| **3 / C** | **3 / C** | **Si** | **2** | dp[2][2]+1 = 1+1 = 2 (diagonal) |
| 3 / C | 4 / A | No | 2 | max(dp[2][4]=1, dp[3][3]=2) = 2 |
| 3 / C | 5 / B | No | 2 | max(dp[2][5]=2, dp[3][4]=2) = 2 |
| 3 / C | 6 / A | No | 2 | max(dp[2][6]=2, dp[3][5]=2) = 2 |
| **4 / B** | **1 / B** | **Si** | **1** | dp[3][0]+1 = 0+1 = 1 (diagonal) |
| 4 / B | 2 / D | No | 1 | max(dp[3][2]=1, dp[4][1]=1) = 1 |
| 4 / B | 3 / C | No | 2 | max(dp[3][3]=2, dp[4][2]=1) = 2 |
| 4 / B | 4 / A | No | 2 | max(dp[3][4]=2, dp[4][3]=2) = 2 |
| **4 / B** | **5 / B** | **Si** | **3** | dp[3][4]+1 = 2+1 = 3 (diagonal) |
| 4 / B | 6 / A | No | 3 | max(dp[3][6]=2, dp[4][5]=3) = 3 |
| 5 / D | 1 / B | No | 1 | max(dp[4][1]=1, dp[5][0]=0) = 1 |
| **5 / D** | **2 / D** | **Si** | **2** | dp[4][1]+1 = 1+1 = 2 (diagonal) |
| 5 / D | 3 / C | No | 2 | max(dp[4][3]=2, dp[5][2]=2) = 2 |
| 5 / D | 4 / A | No | 2 | max(dp[4][4]=2, dp[5][3]=2) = 2 |
| 5 / D | 5 / B | No | 3 | max(dp[4][5]=3, dp[5][4]=2) = 3 |
| 5 / D | 6 / A | No | 3 | max(dp[4][6]=3, dp[5][5]=3) = 3 |
| 6 / A | 1 / B | No | 1 | max(dp[5][1]=1, dp[6][0]=0) = 1 |
| 6 / A | 2 / D | No | 2 | max(dp[5][2]=2, dp[6][1]=1) = 2 |
| 6 / A | 3 / C | No | 2 | max(dp[5][3]=2, dp[6][2]=2) = 2 |
| **6 / A** | **4 / A** | **Si** | **3** | dp[5][3]+1 = 2+1 = 3 (diagonal) |
| 6 / A | 5 / B | No | 3 | max(dp[5][5]=3, dp[6][4]=3) = 3 |
| **6 / A** | **6 / A** | **Si** | **4** | dp[5][5]+1 = 3+1 = 4 (diagonal) |
| **7 / B** | **1 / B** | **Si** | **1** | dp[6][0]+1 = 0+1 = 1 (diagonal) |
| 7 / B | 2 / D | No | 2 | max(dp[6][2]=2, dp[7][1]=1) = 2 |
| 7 / B | 3 / C | No | 2 | max(dp[6][3]=2, dp[7][2]=2) = 2 |
| 7 / B | 4 / A | No | 3 | max(dp[6][4]=3, dp[7][3]=2) = 3 |
| **7 / B** | **5 / B** | **Si** | **4** | dp[6][4]+1 = 3+1 = 4 (diagonal) |
| 7 / B | 6 / A | No | 4 | max(dp[6][6]=4, dp[7][5]=4) = 4 |

Las filas en **negrita** corresponden a celdas donde hubo coincidencia (match) y se usó la diagonal.

---

## Reconstrucción (backtracking)

Partiendo de $\text{dp}[7][6] = 4$ y siguiendo las direcciones almacenadas hasta llegar a la esquina $(0, 0)$:

| Paso | $(i, j)$ | $\text{dp}[i][j]$ | Dirección | Caracter tomado |
|---|---|---|---|---|
| 1 | (7, 6) | 4 | Arriba (B $\neq$ A, dp[6][6]=4 $\geq$ dp[7][5]=4) | — |
| 2 | (6, 6) | 4 | **Diagonal** (A = A) | **A** |
| 3 | (5, 5) | 3 | Arriba (D $\neq$ B, dp[4][5]=3 $\geq$ dp[5][4]=2) | — |
| 4 | (4, 5) | 3 | **Diagonal** (B = B) | **B** |
| 5 | (3, 4) | 2 | Izquierda (C $\neq$ A, dp[3][3]=2 $>$ dp[2][4]=1) | — |
| 6 | (3, 3) | 2 | **Diagonal** (C = C) | **C** |
| 7 | (2, 2) | 1 | Izquierda (B $\neq$ D, dp[2][1]=1 $>$ dp[1][2]=0) | — |
| 8 | (2, 1) | 1 | **Diagonal** (B = B) | **B** |
| 9 | (1, 0) | 0 | Fin del backtracking | — |

LCS reconstruida (en orden inverso: A, B, C, B → invertida): **BCBA**

---

## Solución óptima

| Elemento | Valor |
|---|---|
| Secuencia $X$ | `"ABCBDAB"` ($m = 7$) |
| Secuencia $Y$ | `"BDCABA"` ($n = 6$) |
| Longitud LCS $z^*$ | **4** |
| LCS recuperada | `"BCBA"` |
| LCS alternativa válida | `"BDAB"` |
| Celdas procesadas | $7 \times 6 = 42$ |
| Coincidencias (matches) en tabla | 10 |

---

## Salida del programa — `caso_base.py`

```
========================================
LCS - CASO BASE
========================================
Secuencia X : ABCBDAB  (longitud 7)
Secuencia Y : BDCABA  (longitud 6)

Longitud LCS : 4
LCS          : BCBA
========================================
```

---

## Salida del programa — `caso_extendido.py`

Con $X =$ `"AGGTAB"` ($m = 6$) e $Y =$ `"GXTXAYB"` ($n = 7$):

```
========================================
LCS - CASO EXTENDIDO
========================================
Secuencia X : AGGTAB  (longitud 6)
Secuencia Y : GXTXAYB  (longitud 7)

Tabla DP:
     ""   G   X   T   X   A   Y   B
""    0   0   0   0   0   0   0   0
 A    0   0   0   0   0   1   1   1
 G    0   1   1   1   1   1   1   1
 G    0   1   1   1   1   1   1   1
 T    0   1   1   2   2   2   2   2
 A    0   1   1   2   2   3   3   3
 B    0   1   1   2   2   3   3   4

Longitud LCS : 4
LCS          : GTAB
========================================
```

---

## Cómo ejecutar

```bash
# Caso base
python caso_base.py

# Caso extendido (imprime la tabla DP completa)
python caso_extendido.py
```

Requisitos: Python 3.6 o superior. Sin dependencias externas.
