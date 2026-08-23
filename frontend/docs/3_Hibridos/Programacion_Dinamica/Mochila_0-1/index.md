# Mochila 0/1

Selecciona un subconjunto de ítems con peso y valor para maximizar el valor total sin exceder la capacidad disponible.
Implementado con **Python estándar** (sin librerías externas) usando programación dinámica bottom-up.

## Contenido

| Archivo | Descripción |
|---|---|
| [fundamentos.md](./fundamentos.md) | Definición del problema, contexto del ejemplo y aplicaciones por sector |
| [formulacion.md](./formulacion.md) | Formulación matemática completa: recurrencia DP, variables y restricciones |
| [complejidad.md](./complejidad.md) | Complejidad computacional y estrategias de mitigación |
| [ejemplos.md](./ejemplos.md) | Datos del problema, tabla DP desplegada y salida esperada |
| [caso_base.py](./caso_base.py) | Código — 3 lotes, capacidad 6 m³ |
| [caso_extendido.py](./caso_extendido.py) | Código — 5 lotes, DP 3D (volumen + peso), incompatibilidad C-D |

## Referencias

- Bellman, R. (1957). *Dynamic Programming*. Princeton University Press.
- Kellerer, H., Pferschy, U., & Pisinger, D. (2004). *Knapsack Problems*. Springer.
- Cormen, T. H. et al. (2022). *Introduction to Algorithms*, 4th ed. MIT Press. Cap. 14.
