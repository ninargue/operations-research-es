# Complejidad — Mochila 0/1

## Clase del problema

La Mochila 0/1 es **NP-hard** (en la clasificación de problemas de optimización). Su versión de decisión ("¿existe una selección de valor ≥ $k$?") es **NP-completa**. En la práctica esto significa que no se conoce un algoritmo de tiempo polinomial en el tamaño de la entrada que resuelva el caso general de forma exacta. Sin embargo, la programación dinámica lo resuelve en tiempo **pseudopolinomial** (*pseudopolynomial*) $O(n \cdot W)$: polinomial en $n$ y en la capacidad $W$, pero $W$ puede crecer exponencialmente respecto al número de bits necesarios para representarlo.

---

## Crecimiento del espacio de búsqueda (*Search Space*)

Sin DP, la búsqueda exhaustiva (*exhaustive search*) evalúa todos los $2^n$ subconjuntos posibles:

| Tamaño | $n$ | Subconjuntos $2^n$ | DP $O(n \cdot W)$ | Comentario |
|---|---|---|---|---|
| Pequeño | ≤ 20 | ≤ 1 M | < 0.01 s | Trivial con DP |
| Mediano | 20–50 | ≤ 10¹⁵ | < 1 s | DP escala bien |
| Grande | 50–500 | Astronómico | 1–60 s | DP viable si $W$ acotado |
| Muy grande | > 500 | Inviable exacto | minutos–horas | Heurísticas o FPTAS |

Los rangos asumen $W \sim 10^4$; para $W \sim 10^6$ el DP requiere más memoria y tiempo.

---

## Técnicas de mitigación

### Relajación LP (*LP Relaxation*) — mochila fraccionaria
Resolver el problema permitiendo fracciones de ítems: cada ítem se ordena por densidad (*density ratio*) $v_i / w_i$ y se toma de forma greedy. Proporciona una cota superior (*upper bound*) al óptimo entero en $O(n \log n)$.

```python
lotes_sorted = sorted(lotes, key=lambda l: l["valor"] / l["volumen"], reverse=True)
```

### FPTAS (Fully Polynomial-Time Approximation Scheme)
Escalar los valores $v_i$ por un factor $K = \varepsilon \cdot \max(v_i) / n$ y aplicar DP sobre los valores escalados. Garantiza solución a factor $(1 - \varepsilon)$ del óptimo en tiempo $O(n^2 / \varepsilon)$.

### Límite de tiempo con solvers MIP
Si se migra a OR-Tools CP-SAT para instancias grandes:

```python
solver.parameters.max_time_in_seconds = 60
```

### Warm start con solución greedy
Inicializar el solver con la solución heurística de la relajación LP:

```python
# OR-Tools CP-SAT
for i, seleccionado in enumerate(solucion_greedy):
    model.add_hint(x[i], int(seleccionado))
```

### Reducción de espacio a $O(W)$
Si solo se necesita el valor óptimo (sin backtracking), la tabla DP puede comprimirse a un solo vector de tamaño $W+1$ recorriendo las capacidades de mayor a menor:

```python
dp = [0] * (W + 1)
for lote in lotes:
    for w in range(W, lote["volumen"] - 1, -1):
        dp[w] = max(dp[w], lote["valor"] + dp[w - lote["volumen"]])
```

---

## ¿Cuándo cambiar de enfoque?

| Enfoque | Tipo de problema | Instancia | Licencia | Velocidad relativa |
|---|---|---|---|---|
| DP Python estándar | Mochila 0/1 clásica | $n \leq 500$, $W \leq 10^5$ | PSF | Referencia para este caso |
| OR-Tools CP-SAT | MIP binario con restricciones complejas | Mediano–grande | Apache 2.0 | Alta (open source) |
| PuLP + HiGHS | MIP con formulación LP | Mediano | MIT | Media-alta |
| Gurobi | MIP, QP, instancias industriales | Mediano–muy grande | Comercial | Referencia de mercado |
| FPTAS / Greedy | Aproximación aceptable, $n$ muy grande | Sin límite práctico | — | $O(n \log n)$ |
