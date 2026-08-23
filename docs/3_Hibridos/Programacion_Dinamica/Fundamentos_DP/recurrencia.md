# Formulación de Recurrencias DP

## ¿Qué es una recurrencia DP?

Una **recurrencia DP** es una función que expresa el valor óptimo (o el conteo) de un subproblema en términos de subproblemas estrictamente "menores" en algún orden parcial bien definido. El término "menor" puede referirse a un índice más pequeño, una cadena más corta, un conjunto con menos elementos, una capacidad residual menor, etc.; lo esencial es que no haya ciclos en las dependencias.

Toda recurrencia DP se articula mediante tres componentes:

| Componente | Descripción | Pregunta que responde |
|---|---|---|
| **Estado** (*state*) | Los parámetros que describen completamente un subproblema | ¿Qué información necesito para definir de qué subproblema hablo? |
| **Transición** (*transition*) | La ecuación que relaciona el valor del estado actual con los estados menores | ¿Cómo se construye la solución óptima a partir de soluciones de subproblemas? |
| **Caso base** (*base case*) | Los estados cuyo valor se conoce directamente, sin recurrir a la recurrencia | ¿En qué punto deja de ser necesario descomponer el problema? |

---

## Plantilla de formulación (6 pasos)

Los siguientes seis pasos proporcionan un proceso sistemático para formular cualquier recurrencia DP desde cero. Aplicarlos en orden evita los errores más frecuentes.

### Paso 1 — Identificar el estado

Pregunta: ¿qué información describe completamente un subproblema, de modo que su solución no dependa de cómo se llegó a él?

El estado debe ser lo suficientemente rico para que la transición sea determinista dado ese estado, pero tan compacto como sea posible para que el número total de subproblemas sea manejable.

- Un estado demasiado estrecho produce recurrencias incorrectas (la transición no tiene toda la información que necesita).
- Un estado demasiado ancho aumenta el número de subproblemas sin necesidad, elevando la complejidad.

### Paso 2 — Definir el valor

Pregunta: ¿qué almacena cada estado? Puede ser:

- El costo mínimo de lograr cierto objetivo desde ese estado.
- El valor máximo acumulable hasta ese estado.
- El número de formas (conteo) de alcanzar ese estado.
- Un booleano (¿es posible alcanzar ese estado?).

La definición debe ser precisa y consistente a lo largo de toda la formulación.

### Paso 3 — Escribir la transición

La transición expresa el valor del estado actual en términos de los valores de estados menores. Normalmente toma la forma:

$$dp[\text{estado}] = \min / \max / \sum_{\text{subestado} \in \text{transiciones}(\text{estado})} \bigl( \text{costo}(\text{estado}, \text{subestado}) + dp[\text{subestado}] \bigr)$$

La transición debe referenciar **únicamente** estados de menor "tamaño" que el estado actual. Si esto no se cumple, la recurrencia tiene ciclos y no es válida para DP.

### Paso 4 — Identificar los casos base

Los casos base son los estados cuyo valor se conoce sin aplicar la transición. Son el punto de anclaje de la recurrencia. Sin casos base correctos, la recursión no termina y la tabulación no tiene con qué inicializar la tabla.

Verificación: el caso base no debe depender de la recurrencia; su valor debe ser computable directamente.

### Paso 5 — Determinar el orden de evaluación

Para la técnica bottom-up, es necesario establecer en qué orden llenar la tabla para que, al calcular `dp[estado]`, todos los subproblemas referenciados en la transición ya tengan su valor correcto en la tabla.

- Si el estado es un índice $i$ y la transición solo mira $i-1$ e $i-2$: iterar $i$ de menor a mayor.
- Si el estado es un par $(i, j)$ y la transición mira $(i+1, j)$ y $(i, j-1)$: iterar $i$ de mayor a menor y $j$ de menor a mayor, o viceversa según la dirección de las dependencias.
- Si las dependencias forman un grafo acíclico dirigido (DAG) no trivial: usar un orden topológico.

### Paso 6 — Leer la respuesta

Una vez llenada la tabla (o ejecutada la recursión con memoización), ¿qué celda contiene la solución al problema original? La respuesta puede ser:

- Un único estado: `dp[n]`, `dp[n][W]`.
- El mínimo o máximo sobre un conjunto de estados: `max(dp[n][j] for j in range(m))`.
- Una reconstrucción del camino óptimo si se guardaron decisiones durante el llenado.

---

## Señales de que una recurrencia es correcta

Antes de implementar, conviene verificar estas propiedades formales de la recurrencia:

1. **El caso base no depende de la recurrencia.** El valor de los estados base es computable directamente.
2. **La transición no genera ciclos.** Cada estado en el lado derecho de la recurrencia es estrictamente menor que el estado del lado izquierdo en el orden parcial elegido.
3. **La respuesta final se puede obtener de la tabla sin información adicional.** Si para responder hay que recordar decisiones intermedias, se debe extender el estado o guardar una tabla de seguimiento (*traceback table*).

---

## Antipatrones comunes

| Antipatrón | Descripción del error | Cómo detectarlo |
|---|---|---|
| **Estado insuficiente** | El estado no captura toda la información relevante; la transición necesita contexto que no está en el estado. | La transición correcta requiere parámetros adicionales que no forman parte del estado definido. |
| **Estado redundante** | El estado incluye información que puede derivarse de otros parámetros, inflando innecesariamente el espacio de subproblemas. | Al simplificar el estado, la transición sigue siendo determinista y correcta. |
| **Orden de evaluación incorrecto** | La tabla bottom-up se llena en un orden en el que `dp[subestado]` aún no tiene su valor final cuando se usa. | Al verificar la transición, se descubre que referencia un estado que se llenará *después* en el orden de iteración elegido. |
| **Caso base incorrecto** | El caso base tiene un valor erróneo o está mal posicionado, contaminando todos los estados que dependen de él. | Al trazar manualmente casos pequeños (por ejemplo $n = 0, 1, 2$), el resultado difiere del esperado. |

---

## Aplicación de la plantilla — Mochila 0/1

La *Mochila 0/1* (*0/1 Knapsack*) es el ejemplo de referencia de DP 2D. Se describen $n$ ítems, cada uno con peso $w_i$ y valor $v_i$, y una mochila de capacidad $W$. El objetivo es maximizar el valor total sin exceder la capacidad, eligiendo cada ítem a lo sumo una vez.

**Paso 1 — Estado:**

$$dp[i][w] \quad \text{donde } i \in \{0, \ldots, n\},\ w \in \{0, \ldots, W\}$$

Representa el valor máximo obtenible considerando los primeros $i$ ítems con una capacidad residual de $w$.

**Paso 2 — Valor almacenado:** valor máximo acumulable (entero no negativo).

**Paso 3 — Transición:**

$$dp[i][w] = \begin{cases}
dp[i-1][w] & \text{si } w_i > w \quad \text{(ítem no cabe)} \\
\max\bigl(dp[i-1][w],\ v_i + dp[i-1][w - w_i]\bigr) & \text{si } w_i \leq w
\end{cases}$$

En ambos casos el lado derecho referencia la fila $i-1 < i$, garantizando la ausencia de ciclos.

**Paso 4 — Caso base:**

$$dp[0][w] = 0 \quad \forall\, w \in \{0, \ldots, W\}$$

Con cero ítems disponibles, el valor máximo es siempre 0.

**Paso 5 — Orden de evaluación:** iterar $i$ de $1$ a $n$ (externo) y $w$ de $0$ a $W$ (interno). Al calcular `dp[i][w]` la fila $i-1$ está completamente llenada.

**Paso 6 — Respuesta:** `dp[n][W]`, el valor máximo considerando todos los ítems con la capacidad completa.

Para la implementación completa y la reconstrucción de la solución, véase `../Mochila_0-1/formulacion.md`.
