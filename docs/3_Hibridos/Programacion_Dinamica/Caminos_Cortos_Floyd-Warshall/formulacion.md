# Formulacion — Caminos mas Cortos: Floyd-Warshall

## El reto en grafos

Para un grafo de $V$ nodos, existen $V^2$ pares ordenados $(i, j)$. Conocer la
distancia minima entre todos ellos es fundamental para cualquier sistema que necesite
responder consultas de ruta en tiempo constante tras un pre-computo unico.

**Comparacion de estrategias para APSP:**

- **Dijkstra $\times\, V$ veces** (solo grafos sin pesos negativos):
  $O\!\bigl(V \cdot (E + V \log V)\bigr)$. Optimo cuando $E \ll V^2$.

- **Floyd-Warshall**: $O(V^3)$ independientemente de $E$. Ventajoso para grafos densos
  donde $E \approx V^2$, y acepta pesos negativos (sin ciclos negativos).

- **Johnson's algorithm**: $O(VE + V^2 \log V)$. Combina Bellman-Ford para re-ponderar
  el grafo (*reweighting*) y luego Dijkstra $V$ veces. Optimo para grafos dispersos
  con pesos negativos.

---

## Conjuntos y Parametros

| Simbolo | Descripcion |
|---|---|
| $V$ | Conjunto de nodos (vertices) del grafo; $n = \lvert V \rvert$ |
| $E$ | Conjunto de aristas dirigidas (*directed edges*) |
| $W[i][j]$ | Peso de la arista $i \to j$; $W[i][j] = 0$ si $i = j$; $W[i][j] = \infty$ si no existe arista |
| $n$ | Numero total de nodos ($n = \lvert V \rvert$) |

---

## Variable de decision

Se mantienen dos matrices de $n \times n$:

1. **`dist[i][j]`**: distancia minima actual de $i$ a $j$. Se actualiza *in-place*
   durante el algoritmo.

2. **`siguiente[i][j]`**: primer nodo en el camino mas corto de $i$ a $j$. Permite
   reconstruir la ruta completa sin almacenar cada camino explicitamente.

---

## Funcion objetivo

Para cada par $(i, j) \in V \times V$:

$$\text{minimizar} \quad \text{dist}[i][j]$$

La solucion es la matriz completa `dist` con las distancias minimas entre todos
los pares de nodos, y la matriz `siguiente` para reconstruccion de caminos.

---

## Restricciones

**R1 — Inicializacion:**

$$\text{dist}[i][j] = W[i][j] \quad \forall\, i, j \in V$$
$$\text{dist}[i][i] = 0 \quad \forall\, i \in V$$
$$\text{siguiente}[i][j] = j \quad \text{si} \; W[i][j] < \infty, \; i \neq j$$

**R2 — Recurrencia DP** (triple bucle, nodo intermedio $k$ exterior):

$$\text{dist}[i][j] \leftarrow \min\!\bigl(\text{dist}[i][j],\; \text{dist}[i][k] + \text{dist}[k][j]\bigr)$$

para cada $k \in \{0, \ldots, n-1\}$ (exterior), $i \in V$ (medio), $j \in V$ (interior).

Si se produce una mejora, se actualiza ademas:
$$\text{siguiente}[i][j] \leftarrow \text{siguiente}[i][k]$$

**Interpretacion del estado DP:** tras procesar el nodo intermedio $k$, `dist[i][j]`
contiene la distancia minima de $i$ a $j$ usando unicamente nodos de $\{0, \ldots, k\}$
como intermedios.

**Actualizacion *in-place*:** es correcto usar una sola matriz porque, en la iteracion $k$,
los valores `dist[i][k]` y `dist[k][j]` no cambian: cualquier camino $i \to k$ o
$k \to j$ que usara $k$ como intermedio implicaria un ciclo en $k$, lo que solo ocurre
si hay un ciclo negativo (detectado por R3).

**R3 — Deteccion de ciclos negativos:**

$$\text{si} \; \text{dist}[i][i] < 0 \; \text{para algun} \; i \in V \;\Rightarrow\; \text{existe ciclo negativo}$$

Tras ejecutar el algoritmo, se verifica la diagonal. Un valor negativo indica que
existe un camino de $i$ a si mismo con costo total negativo, lo que invalida los
resultados para todos los nodos alcanzables desde $i$.

**R4 — Reconstruccion de caminos:**

```
funcion reconstruir(i, j):
    si siguiente[i][j] == nulo: retornar []
    camino = [i]
    mientras i != j:
        i = siguiente[i][j]
        camino.agregar(i)
    retornar camino
```

---

## Herramientas y bibliotecas

| Herramienta | Funcion | Observacion |
|---|---|---|
| Python estandar (este modulo) | Implementacion DP pura | Sin dependencias externas |
| `networkx.all_pairs_shortest_path_length` | APSP en grafos de NetworkX | Usa BFS/Dijkstra; no Floyd-Warshall directamente |
| `scipy.sparse.csgraph.floyd_warshall` | Floyd-Warshall optimizado en C | Acepta matrices dispersas; muy eficiente para $n > 500$ |
| `numpy` | Representacion matricial | Combinado con Cython acelera el triple bucle |

---

## Diferencia con otros problemas de DP en este repositorio

| Caracteristica | Mochila 0/1 | Floyd-Warshall |
|---|---|---|
| Estructura de datos | Tabla 2D (capacidad × items) | Matriz cuadrada $n \times n$ de distancias |
| "Tabla DP" | Separada de los datos de entrada | **Es** la propia matriz de distancias |
| Reconstruccion | Backtracking sobre la tabla DP | Matriz auxiliar `siguiente` separada |
| Actualizacion | Fila nueva a partir de fila anterior | In-place con un solo array |
| Dimension del espacio de estados | Capacidad $\times$ items | Pares $(i, j)$ con intermedios $k$ |
