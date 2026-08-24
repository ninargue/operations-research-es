# Formulación Matemática — Balanceo de Línea (Minimax)

## El reto: la función `max()` es no lineal

El objetivo conceptual del problema es:

$$\min \max_{k \in K} \left( \sum_{i \in I} t_i \cdot x_{ik} \right)$$

Pero `max(·)` es no lineal y no diferenciable: no puede resolverse directamente con Simplex ni Branch & Bound estándar.

## Técnica de linealización: variable cota auxiliar C

Se introduce una variable continua **C** que actúa como cota superior del tiempo de todas las estaciones. Como el objetivo es minimizar C, el solver lo empujará hacia abajo hasta que toque exactamente el tiempo de la estación más cargada. El modelo lineal equivalente es:

$$\min C$$

---

## Conjuntos y Parámetros

| Símbolo | Descripción |
|---|---|
| $I = \{1, \dots, n\}$ | Conjunto de tareas |
| $K = \{1, \dots, m\}$ | Conjunto de estaciones de trabajo |
| $P \subseteq I \times I$ | Conjunto de pares de precedencia $(u, v)$: la tarea $u$ debe ejecutarse antes que $v$ |
| $t_i \geq 0$ | Tiempo de procesamiento de la tarea $i$ |
| $s_i \geq 0$ | Demanda de espacio físico de la tarea $i$ (caso extendido) |
| $S_k \geq 0$ | Capacidad de espacio disponible en la estación $k$ (caso extendido) |

---

## Variables de Decisión

| Variable | Tipo | Descripción |
|---|---|---|
| $x_{ik} \in \{0, 1\}$ | Binaria | 1 si la tarea $i$ se asigna a la estación $k$; 0 en caso contrario |
| $C \geq 0$ | Continua | Tiempo de ciclo máximo — el cuello de botella a minimizar |

Total de variables binarias: $n \times m$

---

## Función Objetivo

$$\min C$$

---

## Restricciones

### R1 — Cota Minimax por estación

La carga acumulada de cada estación no puede superar el tiempo de ciclo C:

$$\sum_{i \in I} t_i \cdot x_{ik} \leq C \quad \forall k \in K$$

### R2 — Asignación única

Cada tarea debe asignarse a exactamente una estación:

$$\sum_{k \in K} x_{ik} = 1 \quad \forall i \in I$$

En OR-Tools CP-SAT se puede expresar de forma más eficiente con `add_exactly_one`, que aplica propagación de restricciones basada en cliques:

```python
# Equivalente a sum(...) == 1, pero más eficiente en CP-SAT
model.add_exactly_one(x[i, k] for k in range(m))
```

### R3 — Precedencia tecnológica

La estación asignada a la tarea predecesora $u$ debe ser menor o igual a la de la sucesora $v$. La estación de la tarea $i$ se expresa como $\sum_{k \in K} k \cdot x_{ik}$:

$$\sum_{k \in K} k \cdot x_{uk} \leq \sum_{k \in K} k \cdot x_{vk} \quad \forall (u, v) \in P$$

### R4 — Incompatibilidad de tareas *(caso extendido)*

Cuando dos tareas no pueden compartir estación (herramientas incompatibles, contaminación cruzada, etc.), como máximo una del par puede asignarse a cada estación:

$$x_{uk} + x_{vk} \leq 1 \quad \forall k \in K, \; (u, v) \in \text{Incompatibles}$$

En OR-Tools CP-SAT:

```python
model.add_at_most_one([x[u, k], x[v, k]])
```

### R5 — Límite de espacio físico por estación *(caso extendido)*

La suma del espacio requerido por las tareas asignadas no puede superar la capacidad de la estación:

$$\sum_{i \in I} s_i \cdot x_{ik} \leq S_k \quad \forall k \in K$$

### Naturaleza de las variables

$$x_{ik} \in \{0, 1\} \quad \forall i \in I, \; k \in K$$
$$C \geq 0$$
