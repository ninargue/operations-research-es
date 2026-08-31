---
description: Balanceo de Línea de Ensamblaje — minimización del cuello de botella (Minimax) con Python y OR-Tools CP-SAT. Incluye código, formulación y demo interactivo.
---

# Balanceo de Línea de Ensamblaje

Minimización de cuello de botella (problema Minimax) aplicado a una línea de ensamblaje logística.  
Implementado con **Python + Google OR-Tools CP-SAT**.

## Contenido

| Archivo | Descripción |
|---|---|
| [fundamentos.md](./fundamentos.md) | Definición del problema, contexto del ejemplo y aplicaciones por sector |
| [formulacion.md](./formulacion.md) | Formulación matemática completa: variables, función objetivo y restricciones |
| [ejemplos.md](./ejemplos.md) | Descripción de los dos casos y salida esperada |
| [caso_simple.py](./caso_simple.py) | Código — modelo base con precedencias |
| [caso_extendido.py](./caso_extendido.py) | Código — agrega incompatibilidades y límite de espacio físico |

## 🔗 Demo en vivo

*Próximamente — API de prueba interactiva*

## Referencias

- Scholl, A. (1999). *Balancing and Sequencing of Assembly Lines*. Physica-Verlag.
- Talbot, F. B., & Patterson, J. H. (1984). An integer programming algorithm with network cuts for solving the assembly line balancing problem. *Management Science*.
- Google OR-Tools CP-SAT: https://developers.google.com/optimization/reference/python/sat/python/cp_model
