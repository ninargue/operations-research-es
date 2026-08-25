# Técnicas de Implementación

## Top-down con memoización (*Memoization*)

La técnica *top-down* con memoización resuelve el problema de forma **recursiva**, exactamente como se escribe la recurrencia, pero antes de retornar cada resultado lo almacena en una estructura de caché (normalmente un diccionario o arreglo llamado `memo`). Si un subproblema ya fue resuelto, se devuelve el resultado almacenado en lugar de recomputarlo.

**Patrón genérico:**

```python
memo = {}

def dp(estado):
    if estado in memo:
        return memo[estado]
    if es_caso_base(estado):
        return valor_base(estado)
    resultado = min_o_max(dp(subestado) for subestado in transiciones(estado))
    memo[estado] = resultado
    return resultado
```

**Ventajas:**
- Calcula únicamente los subproblemas que son necesarios para la respuesta final; si el grafo de dependencias es disperso, esto puede ahorrar tiempo y memoria de forma significativa.
- La estructura recursiva refleja directamente la recurrencia matemática, lo que facilita la escritura y verificación correcta del código.
- El orden de evaluación de los subproblemas es implícito: la pila de llamadas garantiza que un subproblema se resuelve antes de que su resultado sea necesario.

**Desventajas:**
- Cada llamada recursiva introduce *overhead* de la pila de llamadas (*call stack overhead*), que en lenguajes como Python puede ser significativo.
- Python impone un límite de profundidad de recursión (`sys.getrecursionlimit()`, por defecto 1000). Para instancias grandes con estados que generan cadenas de llamadas largas, esto produce `RecursionError`.
- La caché basada en diccionario tiene mayor latencia de acceso que un arreglo indexado.

---

## Bottom-up con tabulación (*Tabulation*)

La técnica *bottom-up* con tabulación resuelve los subproblemas en un **orden predeterminado**, de los más pequeños a los más grandes, llenando una tabla explícita. Cuando se necesita calcular un estado, todos sus subproblemas dependientes ya están disponibles en la tabla.

**Patrón genérico:**

```python
tabla = inicializar_casos_base()

for estado in orden_topologico(todos_los_estados):
    tabla[estado] = min_o_max(tabla[subestado] for subestado in transiciones(estado))

respuesta = tabla[estado_final]
```

**Ventajas:**
- Sin *overhead* de pila de llamadas; el flujo de control es iterativo y predecible.
- Control explícito del orden de llenado permite razonar sobre la corrección del algoritmo de forma sencilla.
- Abre la posibilidad de **compresión de dimensiones**: si la tabla solo necesita las últimas $k$ filas para calcular la siguiente, se puede reducir el uso de memoria de $O(n^2)$ a $O(k \cdot m)$ o incluso $O(1)$.

**Desventajas:**
- Puede calcular subproblemas que no son necesarios para la respuesta final, desperdiciando tiempo y memoria si el grafo de dependencias es disperso.
- El programador debe determinar explícitamente el orden correcto de iteración, lo que puede ser no trivial para recurrencias complejas.

---

## Tabla de trade-offs

| Dimensión | Top-down (Memoización) | Bottom-up (Tabulación) |
|---|---|---|
| Flujo de cálculo | Recursivo, dirigido por la demanda | Iterativo, dirigido por el orden de llenado |
| Uso de memoria | Caché en diccionario + pila de llamadas | Arreglo/tabla con índices directos |
| Velocidad en la práctica | Puede ser más lento (overhead de función) | Generalmente más rápido (acceso por índice) |
| Facilidad de depuración | Alta: la traza de pila muestra el camino de decisiones | Media: se requiere inspeccionar la tabla manualmente |
| Riesgo de RecursionError en Python | Sí, en instancias grandes | No |
| Reducción de memoria posible | Difícil (estructura recursiva lo complica) | Sí, si la dependencia es local (sliding window) |

---

## Cuándo preferir cada enfoque

**Prefiera top-down (memoización) cuando:**
- Solo una fracción pequeña de los subproblemas es necesaria para la respuesta. Por ejemplo, en problemas sobre grafos con muchos nodos aislados o irrelevantes.
- El grafo de dependencias entre subproblemas es irregular o difícil de recorrer en orden topológico sin un análisis previo.
- La velocidad de implementación y la claridad del código son prioritarias en un prototipo o concurso.

**Prefiera bottom-up (tabulación) cuando:**
- La solución requiere calcular prácticamente todos los subproblemas de todas formas.
- La memoria es un factor crítico y se desea aplicar compresión de dimensiones (*rolling array*).
- Se trabaja en un lenguaje con límite de recursión estricto o sin optimización de llamadas de cola (*tail-call optimization*).
- El orden de evaluación es simple (por ejemplo, iterar $i$ de $0$ a $n$).

---

## Ejemplo comparativo — Fibonacci

Los cuatro enfoques siguientes calculan $F(n)$ con la recurrencia $F(n) = F(n-1) + F(n-2)$, $F(0) = 0$, $F(1) = 1$.

### Versión recursiva ingenua — $O(2^n)$ tiempo, $O(n)$ espacio (pila)

```python
def fib_ingenuo(n: int) -> int:
    """Recursión pura sin caché. Exponencial en tiempo."""
    if n <= 1:
        return n
    return fib_ingenuo(n - 1) + fib_ingenuo(n - 2)
```

Cada llamada genera dos subclamadas, y los subproblemas se recalculan sin ningún ahorro. El árbol de llamadas tiene $O(2^n)$ nodos.

---

### Top-down con memoización — $O(n)$ tiempo, $O(n)$ espacio

```python
def fib_memo(n: int, memo: dict = None) -> int:
    """Top-down con diccionario de memoización."""
    if memo is None:
        memo = {}
    if n in memo:                    # subproblema ya resuelto
        return memo[n]
    if n <= 1:                       # caso base
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]
```

Cada subproblema $F(k)$ se calcula exactamente una vez. La tabla `memo` actúa como un registro de todos los resultados parciales.

---

### Bottom-up con tabulación — $O(n)$ tiempo, $O(n)$ espacio

```python
def fib_tabla(n: int) -> int:
    """Bottom-up iterativo con tabla de tamaño n+1."""
    if n <= 1:
        return n
    tabla = [0] * (n + 1)
    tabla[1] = 1
    for i in range(2, n + 1):       # orden de menor a mayor
        tabla[i] = tabla[i - 1] + tabla[i - 2]
    return tabla[n]
```

Los casos base se inicializan explícitamente. El bucle llena la tabla en el único orden posible que garantiza que `tabla[i-1]` y `tabla[i-2]` estén disponibles al calcular `tabla[i]`.

---

### Bottom-up con espacio $O(1)$ — compresión de dimensión

```python
def fib_optimo(n: int) -> int:
    """Bottom-up con solo dos variables: espacio O(1)."""
    if n <= 1:
        return n
    prev2, prev1 = 0, 1             # F(0), F(1)
    for _ in range(2, n + 1):
        actual = prev1 + prev2
        prev2, prev1 = prev1, actual
    return prev1
```

Como $F(n)$ solo depende de $F(n-1)$ y $F(n-2)$, no es necesario almacenar toda la tabla. Dos variables deslizan la ventana de dependencia (*sliding window*), reduciendo el espacio de $O(n)$ a $O(1)$.

---

### Resumen de complejidades

| Versión | Tiempo | Espacio |
|---|---|---|
| Recursiva ingenua | $O(2^n)$ | $O(n)$ (pila) |
| Top-down (memoización) | $O(n)$ | $O(n)$ |
| Bottom-up (tabulación) | $O(n)$ | $O(n)$ |
| Bottom-up (espacio óptimo) | $O(n)$ | $O(1)$ |
