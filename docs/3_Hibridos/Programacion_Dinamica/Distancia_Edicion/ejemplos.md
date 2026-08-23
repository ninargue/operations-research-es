# Ejemplos — Distancia de Edición

## Caso Base — Datos

| Parámetro | Valor |
|---|---|
| Cadena fuente (`src`) | `"kitten"` |
| Cadena destino (`dst`) | `"sitting"` |
| Longitud $m$ | 6 |
| Longitud $n$ | 7 |
| Distancia de edición | **3** |

---

## Tabla DP desplegada

La tabla tiene $(m+1) \times (n+1) = 7 \times 8$ celdas. La fila 0 representa el prefijo vacío de `src`; la columna 0 representa el prefijo vacío de `dst`. Los índices de caracteres van de 1 a $m$ (filas) y de 1 a $n$ (columnas).

```
       ""   s   i   t   t   i   n   g
""      0   1   2   3   4   5   6   7
k       1   1   2   3   4   5   6   7
i       2   2   1   2   3   4   5   6
t       3   3   2   1   2   3   4   5
t       4   4   3   2   1   2   3   4
e       5   5   4   3   2   2   3   4
n       6   6   5   4   3   3   2   3
```

$dp[6][7] = \mathbf{3}$ — la distancia de edición entre `"kitten"` y `"sitting"`.

**Verificación de celdas clave:**

- $dp[1][1]$: `k` $\neq$ `s` → $\min(dp[0][1], dp[1][0], dp[0][0]) + 1 = \min(1,1,0)+1 = 1$
- $dp[2][2]$: `i` $=$ `i` → $dp[1][1] = 1$
- $dp[3][3]$: `t` $=$ `t` → $dp[2][2] = 1$
- $dp[4][4]$: `t` $=$ `t` → $dp[3][3] = 1$
- $dp[5][4]$: `e` $\neq$ `t` → $\min(dp[4][4], dp[5][3], dp[4][3]) + 1 = \min(1,2,2)+1 = 2$
- $dp[6][7]$: `n` $\neq$ `g` → $\min(dp[5][7], dp[6][6], dp[5][6]) + 1 = \min(4,2,3)+1 = 3$

---

## Edit Script reconstruido

El backtracking desde $(6, 7)$ hasta $(0, 0)$ en la tabla de operaciones produce la siguiente secuencia (en orden de aplicación):

| Paso | Operación | Detalle | Cadena resultado |
|---|---|---|---|
| — | Estado inicial | — | `kitten` |
| 1 | Sustitución (*substitute*) | `k` → `s` en posición 1 | `sitten` |
| 2 | Sin cambio (*match*) | `i` = `i` | `sitten` |
| 3 | Sin cambio (*match*) | `t` = `t` | `sitten` |
| 4 | Sin cambio (*match*) | `t` = `t` | `sitten` |
| 5 | Sustitución (*substitute*) | `e` → `i` en posición 5 | `sittin` |
| 6 | Sin cambio (*match*) | `n` = `n` | `sittin` |
| 7 | Inserción (*insert*) | `g` al final | `sitting` |

**Operaciones de costo no nulo: 3** (pasos 1, 5 y 7).

---

## Restricciones desplegadas

**R1 — Casos base verificados:**

$$dp[0][j] = j \quad \Rightarrow \quad dp[0][0]=0,\; dp[0][1]=1,\; \ldots,\; dp[0][7]=7$$
$$dp[i][0] = i \quad \Rightarrow \quad dp[0][0]=0,\; dp[1][0]=1,\; \ldots,\; dp[6][0]=6$$

**R2 — Paso clave $dp[6][7]$:**

`src[6]` = `n`, `dst[7]` = `g` → mismatch.

$$dp[6][7] = 1 + \min\!\bigl(\underbrace{dp[5][7]}_{4},\; \underbrace{dp[6][6]}_{2},\; \underbrace{dp[5][6]}_{3}\bigr) = 1 + 2 = 3$$

El mínimo es $dp[6][6] = 2$ (operación de eliminación de `n`... pero en el backtracking real el algoritmo registra la inserción de `g` al comparar las columnas). La operación registrada en $op[6][7]$ es `I` (inserción de `dst[7]` = `g`).

---

## Solución óptima

$$\boxed{d(\text{``kitten''},\; \text{``sitting''}) = 3}$$

Edit script mínimo (solo operaciones de costo):

1. Sustituir `k` → `s`
2. Sustituir `e` → `i`
3. Insertar `g`

---

## Salida del programa — `caso_base.py`

```
=============================================
DISTANCIA DE EDICION - CASO BASE
=============================================
Cadena fuente  : 'kitten'  (longitud 6)
Cadena destino : 'sitting'  (longitud 7)

Distancia de edicion : 3

Edit script (operaciones minimas):
  Sustituir  : 'k' -> 's' (posicion 1)
  Sustituir  : 'e' -> 'i' (posicion 5)
  Insertar   : 'g' (posicion 7)
=============================================
```

---

## Salida del programa — `caso_extendido.py`

```
=============================================
DISTANCIA DE EDICION - CASO EXTENDIDO
=============================================
Cadena fuente  : 'intention'  (longitud 9)
Cadena destino : 'execution'  (longitud 9)

Tabla DP completa:
      |    |   e|   x|   e|   c|   u|   t|   i|   o|   n|
---------------------------------------------------------
      |   0|   1|   2|   3|   4|   5|   6|   7|   8|   9|
     i|   1|   1|   2|   3|   4|   5|   6|   6|   7|   8|
     n|   2|   2|   2|   3|   4|   5|   6|   7|   7|   7|
     t|   3|   3|   3|   3|   4|   5|   5|   6|   7|   8|
     e|   4|   3|   4|   3|   4|   5|   6|   6|   7|   8|
     n|   5|   4|   4|   4|   4|   5|   6|   7|   7|   7|
     t|   6|   5|   5|   5|   5|   5|   5|   6|   7|   8|
     i|   7|   6|   6|   6|   6|   6|   6|   5|   6|   7|
     o|   8|   7|   7|   7|   7|   7|   7|   6|   5|   6|
     n|   9|   8|   8|   8|   8|   8|   8|   7|   6|   5|

Distancia de edicion : 5

Edit script (operaciones minimas):
  Sustituir  : 'i' -> 'e' (posicion 1)
  Sustituir  : 'n' -> 'x' (posicion 2)
  Sustituir  : 't' -> 'e' (posicion 3)
  Sustituir  : 'e' -> 'c' (posicion 4)
  Sustituir  : 'n' -> 'u' (posicion 5)
=============================================
```

---

## Cómo ejecutar

```bash
# Caso base
python caso_base.py

# Caso extendido (imprime tabla DP completa)
python caso_extendido.py
```

Requiere Python 3.6 o superior. Sin dependencias externas.
