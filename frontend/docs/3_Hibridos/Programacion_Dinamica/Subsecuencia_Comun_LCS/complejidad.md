# Complejidad — Subsecuencia Común más Larga (LCS)

## Clase del problema

La LCS pertenece a la clase **P** (problemas resolubles en tiempo polinomial). La formulación de programación dinámica *bottom-up* proporciona una solución **exacta** con las siguientes garantías:

| Recurso | Complejidad |
|---|---|
| Tiempo | $O(m \cdot n)$ |
| Espacio (tabla completa) | $O(m \cdot n)$ |
| Espacio (optimizado, solo longitud) | $O(\min(m, n))$ |
| Tiempo de reconstrucción | $O(m + n)$ |

A diferencia de problemas NP-completos como la Mochila 0/1 (que es NP-completo en el caso general con pesos no enteros), la LCS no tiene barrera de intratabilidad conocida: se puede resolver exactamente para secuencias de millones de elementos con hardware moderno, aunque con consideraciones de memoria.

La LCS también presenta **subestructura óptima** y **subproblemas traslapados** (*overlapping subproblems*), las dos propiedades que hacen a un problema candidato a programación dinámica.

---

## Crecimiento del tiempo de cómputo

La siguiente tabla ilustra el crecimiento para distintos tamaños de entrada, comparando la fuerza bruta con la solución DP:

| Tamaño $(m \times n)$ | Fuerza bruta $O(2^m \cdot n)$ | DP $O(m \cdot n)$ | Contexto |
|---|---|---|---|
| $100 \times 100$ (pequeño) | $\approx 10^{32}$ operaciones (intratable) | $10^4$ operaciones | Archivos de texto cortos, pruebas unitarias |
| $1\,000 \times 1\,000$ (mediano) | Intratable | $10^6$ operaciones | Documentos, código fuente típico |
| $10\,000 \times 10\,000$ (grande) | Intratable | $10^8$ operaciones; $\approx 800$ MB de RAM (tabla entera) | Genomas bacterianos, logs de sistema |
| $100\,000 \times 100\,000$ (muy grande) | Intratable | $10^{10}$ operaciones; $\approx 80$ GB de RAM | Genomas humanos; requiere técnicas especializadas |

Para el caso de genomas (longitudes del orden de $3 \times 10^9$ bases), la DP estándar es impracticable en memoria. Se recurren a algoritmos de alineamiento aproximado como Smith-Waterman con banda (*banded alignment*) o algoritmos heurísticos como BLAST.

---

## Técnicas de mitigación

### Reducción de espacio a $O(\min(m, n))$

Para calcular únicamente la **longitud** de la LCS (sin reconstruirla), basta con mantener dos filas de la tabla en memoria: la fila actual y la anterior. Esto reduce el espacio de $O(m \cdot n)$ a $O(\min(m, n))$ si se itera sobre la secuencia más corta en las columnas.

```python
def lcs_longitud_optimizada(X, Y):
    # Asegurar que Y sea la secuencia mas corta (columnas)
    if len(X) < len(Y):
        X, Y = Y, X
    m, n = len(X), len(Y)

    anterior = [0] * (n + 1)
    actual   = [0] * (n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                actual[j] = anterior[j - 1] + 1
            else:
                actual[j] = max(anterior[j], actual[j - 1])
        anterior, actual = actual, [0] * (n + 1)

    return anterior[n]
```

**Limitacion:** con esta optimizacion no es posible reconstruir la LCS; solo se obtiene su longitud. Para la reconstruccion completa se necesita la tabla entera o el algoritmo de Hirschberg.

### Algoritmo de Hirschberg — reconstruccion en $O(\min(m,n))$ de espacio

El algoritmo de Hirschberg (1975) combina la tecnica de *divide and conquer* con la reduccion de espacio para reconstruir la LCS completa usando solo $O(\min(m, n))$ de espacio adicional, manteniendo la complejidad temporal en $O(m \cdot n)$.

### Hunt-Szymanski — LCS dispersa (*sparse LCS*)

Cuando las dos secuencias comparten pocos caracteres en comun (es decir, el numero de pares de posiciones coincidentes $r = |\{(i,j) : x_i = y_j\}|$ es pequeno relativo a $m \cdot n$), el algoritmo de Hunt-Szymanski permite resolver LCS en:

$$O(r \log n + m + n)$$

Este enfoque es eficiente cuando $r \ll m \cdot n$, como en la comparacion de secuencias de ADN muy divergentes o archivos de texto con pocos tokens en comun.

**Idea central:** construir la lista de todos los pares coincidentes (*match points*) y encontrar la subsecuencia creciente mas larga (*longest increasing subsequence*, LIS) sobre esos pares ordenados, lo que equivale a la LCS.

### Para secuencias muy largas: enfoques aproximados

| Situacion | Tecnica recomendada |
|---|---|
| Genomas completos | Algoritmos de alineamiento por semillas (*seed-and-extend*): BLAST, BWA |
| Archivos de texto grandes | `difflib.SequenceMatcher` (Python), que usa una heuristica basada en bloques coincidentes |
| Secuencias con muchas repeticiones | Indices de sufijos (*suffix arrays*) para precalcular matches en $O((m+n)\log(m+n))$ |
| Restriccion de tiempo estricta | LCS aproximada con garantias de aproximacion |

---

## Cuándo cambiar de enfoque

| Condicion | Enfoque recomendado | Razon |
|---|---|---|
| $m, n \leq 10\,000$ y se necesita reconstruccion | DP *bottom-up* estandar | Simple, exacto, $O(m\cdot n)$ tiempo y espacio |
| $m, n \leq 10\,000$ y solo se necesita la longitud | DP con dos filas | Mismo tiempo, espacio $O(n)$ |
| $m, n \leq 10^6$ y se necesita reconstruccion | Algoritmo de Hirschberg | Exacto, espacio $O(n)$ |
| $r \ll m \cdot n$ (secuencias dispersas) | Hunt-Szymanski | Mas rapido en practica cuando los matches son escasos |
| $m$ o $n > 10^7$ | Heuristicas (BLAST, Smith-Waterman con banda) | La DP exacta es impracticable en memoria |
