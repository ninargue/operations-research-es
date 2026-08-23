# Fundamentos de Programación Dinámica

Este módulo presenta la *programación dinámica* (*dynamic programming*, DP) como paradigma de diseño antes de abordar los problemas concretos del repositorio. El punto de partida teórico es el **principio de optimalidad de Bellman (1957)**: toda política óptima tiene la propiedad de que las decisiones restantes, tomadas a partir del estado alcanzado por la primera decisión, constituyen también una política óptima para el subproblema correspondiente. Entender este principio —y sus condiciones de aplicabilidad— es esencial para diseñar y verificar correctamente cualquier algoritmo DP.

---

## Tabla de contenidos

| Archivo | Descripción |
|---|---|
| `README.md` (este archivo) | Punto de entrada, guía de lectura y referencias bibliográficas |
| [`paradigma.md`](paradigma.md) | Qué es la DP, subestructura óptima, subproblemas traslapados y diferencias con otros paradigmas (Divide y Vencerás, Greedy) |
| [`tecnicas.md`](tecnicas.md) | Técnicas de implementación: top-down con memoización y bottom-up con tabulación; comparación y ejemplo en Fibonacci |
| [`recurrencia.md`](recurrencia.md) | Plantilla de 6 pasos para formular recurrencias DP; antipatrones comunes; aplicación a Mochila 0/1 |
| [`clasificacion.md`](clasificacion.md) | Taxonomía por estructura del estado, guía de selección rápida y mapeo de carpetas del repositorio a categorías |

---

## Cómo usar este módulo

### Para el lector sin experiencia previa en DP

Seguir los archivos en el orden en que aparecen en la tabla de contenidos:

1. **`paradigma.md`** — Comprender qué propiedades debe tener un problema para que la DP sea aplicable.
2. **`tecnicas.md`** — Aprender los dos patrones de implementación y cuándo usar cada uno.
3. **`recurrencia.md`** — Practicar la formulación sistemática de recurrencias con la plantilla de 6 pasos.
4. **`clasificacion.md`** — Identificar a qué categoría pertenece un nuevo problema para elegir la recurrencia correcta.
5. **Elegir un problema concreto** — Ir a cualquiera de las carpetas del repositorio (`Mochila_0-1/`, `Cambio_Monedas/`, etc.) con la base conceptual ya establecida.

### Para el lector con experiencia previa en DP

Ir directamente a [`clasificacion.md`](clasificacion.md) para ubicar el problema de interés dentro de la taxonomía del repositorio y luego navegar a la carpeta correspondiente. Los otros archivos sirven como referencia cuando sea necesario revisar la justificación teórica de alguna propiedad.

---

## Referencias

- Bellman, R. (1957). *Dynamic Programming*. Princeton University Press.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms*, 4th ed. MIT Press. Cap. 14.
- Dasgupta, S., Papadimitriou, C., & Vazirani, U. (2006). *Algorithms*. McGraw-Hill. Cap. 6.
