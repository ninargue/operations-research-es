# Fundamentos — Cambio de Monedas

## ¿Qué es el problema?

El **Cambio de Monedas** (*Coin Change*) es un problema de optimización combinatoria (*combinatorial optimization*) cuyo objetivo es encontrar el número mínimo de monedas necesarias para alcanzar exactamente un monto objetivo $C$, dado un conjunto de denominaciones $D = \{d_1, d_2, \ldots, d_k\}$ y uso ilimitado de cada denominación (*unbounded use*).

Es una variante de la **mochila sin límite de uso** (*unbounded knapsack*): a diferencia de la Mochila 0/1, donde cada ítem se toma a lo sumo una vez, aquí cada denominación puede usarse tantas veces como sea necesario. El problema pertenece a la clase **NP-hard** en el caso general (denominaciones arbitrarias sin estructura especial), pero la **programación dinámica** (*dynamic programming*) lo resuelve de forma exacta en tiempo **pseudopolinomial** $O(n \cdot C)$, donde $n = |D|$ es el número de denominaciones y $C$ es el monto objetivo. El espacio de almacenamiento requerido es $O(C)$.

---

## Contexto del ejemplo

Una caja registradora necesita dar cambio exacto de **11 unidades** usando monedas de denominaciones $\{1, 5, 6\}$. Se comparan tres estrategias posibles:

| Estrategia | Selección | Total de monedas |
|---|---|---|
| Greedy (mayor denominación primero) | 6 + 1 + 1 + 1 + 1 + 1 | 6 monedas — subóptimo |
| Greedy alternativo (menor error residual) | 5 + 5 + 1 | 3 monedas — subóptimo |
| **DP — óptimo global** | **5 + 6** | **2 monedas** |

La estrategia greedy que elige siempre la denominación mayor disponible falla porque la denominación 6 impide descubrir la combinación óptima 5 + 6 = 11. La programación dinámica evalúa todas las combinaciones posibles a través de subproblemas solapados (*overlapping subproblems*) y garantiza el óptimo global con solo **2 monedas**.

---

## Aplicaciones por sector

| Sector | Caso de uso |
|---|---|
| **Banca / Finanzas** | Dispensadores ATM: entregar el efectivo solicitado con el menor número de billetes posible |
| **Logística / Distribución** | Optimizar el desglose de paquetes en unidades estandarizadas (cajas de 1, 5, 10, 25 unidades) |
| **Manufactura** | Corte de piezas: cubrir longitudes exactas a partir de longitudes estándar disponibles en bodega |
| **Telecomunicaciones** | Segmentación de paquetes de datos en tramas de tamaño fijo minimizando el número de tramas |
| **Criptografía / Blockchain** | Construcción de transacciones con el menor número de UTXOs (*Unspent Transaction Outputs*) |
| **E-commerce** | Cálculo de cambio en pagos en efectivo, minimizando la cantidad de fichas devueltas al cliente |
