# Cambio de Monedas

Dado un conjunto de denominaciones de monedas y un monto objetivo, encontrar el número mínimo de monedas necesarias para alcanzar exactamente ese monto con uso ilimitado de cada denominación.
Implementado con **Python estándar** (sin librerías externas) usando programación dinámica bottom-up.

## Contenido

| Archivo | Descripción |
|---|---|
| [fundamentos.md](./fundamentos.md) | Definición del problema, contexto del ejemplo y aplicaciones por sector |
| [formulacion.md](./formulacion.md) | Formulación matemática completa: recurrencia DP, variables y restricciones |
| [complejidad.md](./complejidad.md) | Complejidad computacional y estrategias de mitigación |
| [ejemplos.md](./ejemplos.md) | Datos del problema, vector DP desplegado y salida esperada |
| [caso_base.py](./caso_base.py) | Código — denominaciones {1, 5, 6}, monto 11 |
| [caso_extendido.py](./caso_extendido.py) | Código — denominaciones {1, 3, 4, 7, 11}, monto 25, vector dp impreso |
| [cambio_monedas_dp.html](./cambio_monedas_dp.html) | Visualizador interactivo del vector DP paso a paso |

## Referencias

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms*, 4th ed. MIT Press. Cap. 14.
- Dasgupta, S., Papadimitriou, C., & Vazirani, U. (2006). *Algorithms*. McGraw-Hill. Cap. 6.
- Wright, J. W. (1975). The change-making problem. *Journal of the ACM*, 22(1), 125–128.
