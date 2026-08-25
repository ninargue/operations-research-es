# Complejidad — Cambio de Monedas

## Clase del problema

El Cambio de Monedas es **NP-hard** en el caso general (denominaciones arbitrarias). Su versión de decisión ("¿existe una selección de a lo sumo $k$ monedas que sume exactamente $C$?") es **NP-completa**. En la práctica, no se conoce un algoritmo de tiempo polinomial en el tamaño de la entrada que resuelva el caso general de forma exacta. Sin embargo, cuando las denominaciones son enteros acotados, la programación dinámica lo resuelve en tiempo **pseudopolinomial** (*pseudopolynomial*) $O(n \cdot C)$: polinomial en $n = |D|$ y en el monto $C$, pero $C$ puede crecer exponencialmente respecto al número de bits necesarios para representarlo. El espacio de almacenamiento es $O(C)$ para el vector dp más $O(C)$ para el arreglo de reconstrucción.

---

## Crecimiento del espacio de búsqueda (*Search Space*)

Sin DP, la búsqueda exhaustiva evalúa un espacio exponencial de combinaciones ordenadas. Con DP, se resuelven exactamente $C$ subproblemas, cada uno con $n$ operaciones:

| Tamaño | $n$ (denominaciones) | $C$ (monto) | Búsqueda exhaustiva | DP $O(n \cdot C)$ | Comentario |
|---|---|---|---|---|---|
| Pequeño | ≤ 5 | ≤ 100 | Manejable | < 0.001 s | Trivial con DP |
| Mediano | 5–20 | ≤ 10 000 | Impracticable | < 0.1 s | DP escala bien |
| Grande | 20–100 | ≤ 100 000 | Astronómico | 1–10 s | DP viable |
| Muy grande | > 100 | > 10⁶ | Inviable exacto | minutos | Heurísticas o BFS |

---

## Técnicas de mitigación

### Verificación de infactibilidad temprana (mcd)

Si el máximo común divisor (*greatest common divisor*) de las denominaciones no divide exactamente al monto $C$, no existe solución. Esta verificación toma $O(n \log(\max D))$ y evita ejecutar el DP completo en casos infactibles:

```python
from math import gcd
from functools import reduce

def es_factible(denominaciones, monto):
    g = reduce(gcd, denominaciones)
    return monto % g == 0
```

### Reducción de espacio

El vector $dp$ ya es $O(C)$ — no es posible reducir el espacio de la tabla principal sin perder la capacidad de reconstrucción. Si solo se necesita el valor óptimo (sin backtracking), el arreglo `moneda_usada` puede eliminarse, dejando el espacio total en $O(C)$.

### BFS (*Breadth-First Search*) como alternativa para monto pequeño

Para montos pequeños, BFS sobre el grafo de estados (donde cada nodo es un submonto y cada arco es una denominación) también encuentra el mínimo número de monedas en $O(C \cdot n)$ con garantía de optimalidad:

```python
from collections import deque

def bfs_cambio(denominaciones, monto):
    visitado = [False] * (monto + 1)
    cola = deque([(0, 0)])  # (monto_actual, num_monedas)
    visitado[0] = True
    while cola:
        actual, monedas = cola.popleft()
        if actual == monto:
            return monedas
        for d in denominaciones:
            siguiente = actual + d
            if siguiente <= monto and not visitado[siguiente]:
                visitado[siguiente] = True
                cola.append((siguiente, monedas + 1))
    return -1  # sin solucion
```

### Aproximación greedy con denominaciones canónicas

Para sistemas de monedas canónicos (como $\{1, 5, 10, 25\}$ en EE. UU. o $\{1, 2, 5, 10, 20, 50, 100, 200\}$ en la zona euro), el algoritmo greedy —tomar siempre la denominación más grande que no exceda el monto restante— produce la solución óptima. Esta propiedad no se cumple para denominaciones arbitrarias (como el ejemplo $\{1, 5, 6\}$ con monto 11, donde greedy da 6 monedas en lugar de 2).

---

## ¿Cuándo cambiar de enfoque?

| Enfoque | Tipo de problema | Instancia | Licencia | Velocidad relativa |
|---|---|---|---|---|
| DP Python estándar | Coin Change clásico | $n \leq 200$, $C \leq 10^6$ | PSF | Referencia para este caso |
| BFS | Monto pequeño con muchas denominaciones | $C \leq 10^4$ | PSF | $O(C \cdot n)$, overhead de cola |
| OR-Tools CP-SAT | MIP entero con restricciones adicionales | Mediano–grande | Apache 2.0 | Alta (open source) |
| PuLP + HiGHS | MIP con formulación LP | Mediano | MIT | Media-alta |
| Greedy | Sistemas de monedas canónicos | Sin límite práctico | — | $O(n \log n)$ ordenamiento |
