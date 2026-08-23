# Fundamentos — Mochila 0/1

## ¿Qué es el problema?

La **Mochila 0/1** es un problema de optimización combinatoria (*combinatorial optimization*) en el que se selecciona un subconjunto de ítems — cada uno con un peso y un valor — para maximizar el valor total transportado sin exceder una capacidad fija. La restricción "0/1" significa que cada ítem se incluye o no se incluye: no se permiten fracciones ni cantidades mayores a una unidad. Pertenece a la clase NP-hard, por lo que la búsqueda exhaustiva (*exhaustive search*) escala de forma exponencial; la **programación dinámica** (*dynamic programming*) resuelve el problema de forma exacta en tiempo pseudopolinomial (*pseudopolynomial*) $O(n \cdot W)$ mediante una tabla de subproblemas (*subproblem table*) que evita recalcular estados repetidos.

---

## Contexto del ejemplo

Una empresa de logística necesita maximizar el valor de los lotes de carga que caben en un camión con capacidad de **6 m³**. Dispone de tres lotes candidatos.

| Lote | Valor ($) | Volumen (m³) |
|---|---|---|
| Lote A | 5 | 4 |
| Lote B | 3 | 2 |
| Lote C | 4 | 3 |

**Relaciones relevantes**: cada lote se toma completo o se deja; no es posible dividirlo. El volumen total no puede superar 6 m³.

| Estrategia | Lotes elegidos | Volumen (m³) | Valor ($) |
|---|---|---|---|
| Intuitiva (mayor valor primero) | A, C | 7 | 9 — **inválido** (excede capacidad) |
| Intuitiva corregida (A solamente) | A | 4 | 5 |
| **Óptima (DP)** | **A + B** | **6** | **$8** |

La programación dinámica obtiene **$8** frente a los $5 de la selección intuitiva corregida: un **60 % de mejora** en valor transportado usando la misma capacidad.

---

## Aplicaciones por sector

| Sector | Caso de uso |
|---|---|
| **Logística / Transporte** | Selección de lotes de carga para maximizar el valor en un camión o contenedor |
| **Finanzas / Inversión** | Cartera de proyectos con presupuesto fijo y retornos esperados |
| **Manufactura** | Corte de material (cutting stock): maximizar el valor de piezas cortadas de una plancha |
| **Cloud / TI (*IT*)** | Asignación de tareas a instancias con memoria o CPU limitados |
| **Salud** | Selección de fármacos o insumos críticos dentro de un presupuesto de abastecimiento |
| **E-commerce / Almacén** | Empaque de pedidos en una caja de volumen fijo para maximizar valor o prioridad |
