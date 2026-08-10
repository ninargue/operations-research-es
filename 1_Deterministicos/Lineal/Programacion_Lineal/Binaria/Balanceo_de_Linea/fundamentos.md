# Fundamentos — Balanceo de Línea de Ensamblaje

## ¿Qué es el problema de Balanceo de Línea?

El **Balanceo de Línea de Ensamblaje** consiste en distribuir un conjunto de tareas entre un número fijo de estaciones de trabajo, respetando relaciones de precedencia tecnológica, de modo que se minimice el tiempo de la estación más lenta — el **cuello de botella**.

Desde el punto de vista de la Investigación de Operaciones, este es un problema **Minimax**: minimizar el máximo de los tiempos acumulados en todas las estaciones.

---

## Contexto del Ejemplo

**Escenario:** Una línea de ensamblaje prepara kits promocionales en un centro de despacho logístico. Se deben ejecutar **5 tareas** en **2 estaciones de trabajo**.

| Tarea | Descripción | Tiempo (s) | Precedencia |
|---|---|---|---|
| 1 | Inspección visual | 30 | — |
| 2 | Etiquetado con código de barras | 15 | Requiere Tarea 1 |
| 3 | Empaquetado primario | 45 | Requiere Tarea 2 |
| 4 | Inserción de cupón promocional | 20 | Requiere Tarea 2 |
| 5 | Sellado térmico y embalaje | 35 | Requiere Tareas 3 y 4 |

**Grafo de precedencias:** 1 → 2 → 3 → 5 y 2 → 4 → 5

---

## Asignación Intuitiva vs. Optimizada

| | Estación 1 | Estación 2 | Cuello de botella | Kits/hora |
|---|---|---|---|---|
| **Intuitiva** | Tareas 1,2,3 → 90 s | Tareas 4,5 → 55 s | **90 s** | 40 |
| **Optimizada** | Tareas 1,2,4 → 65 s | Tareas 3,5 → 80 s | **80 s** | 45 |

La optimización reduce el cuello de botella en 10 segundos → **+12.5% de productividad sin inversión adicional**.

---

## Aplicaciones por Sector

| Sector | Caso de uso |
|---|---|
| **Manufactura / Industria** | Balanceo de líneas de ensamblaje automotriz, electrónica, alimentos |
| **Logística / e-commerce** | Asignación de operaciones en centros de fulfillment |
| **Salud** | Distribución de procedimientos quirúrgicos entre quirófanos |
| **Construcción** | Asignación de actividades a cuadrillas o equipos de trabajo |
| **Servicios** | Programación de tareas en call centers o procesos de backoffice |

