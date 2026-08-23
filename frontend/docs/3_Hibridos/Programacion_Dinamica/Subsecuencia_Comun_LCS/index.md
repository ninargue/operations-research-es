# Subsecuencia Común más Larga (LCS)

Dadas dos secuencias $X$ e $Y$, encontrar la longitud de la subsecuencia más larga que aparece en ambas preservando el orden relativo de los elementos, resuelta mediante programación dinámica *bottom-up* en $O(m \cdot n)$.

## Archivos

| Archivo | Descripción |
|---|---|
| `fundamentos.md` | Definición del problema, distinción subsecuencia vs. subcadena, aplicaciones por sector |
| `formulacion.md` | Conjuntos, parámetros, variable de decisión, función objetivo, restricciones y recurrencia DP |
| `complejidad.md` | Análisis de complejidad, técnicas de mitigación (Hirschberg, Hunt-Szymanski, optimización de espacio) |
| `ejemplos.md` | Tabla DP completa para el caso base, backtracking detallado y salidas de los programas |
| `caso_base.py` | Implementación DP para X="ABCBDAB", Y="BDCABA"; LCS="BCBA", longitud 4 |
| `caso_extendido.py` | Implementación DP con impresión de la tabla ASCII; X="AGGTAB", Y="GXTXAYB"; LCS="GTAB", longitud 4 |
| `lcs_dp.html` | Visualizador interactivo paso a paso de la construcción de la tabla DP y el backtracking |

## Referencias

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4.a ed.). MIT Press. Capítulo 14: Dynamic Programming (sección LCS).
- Needleman, S. B., & Wunsch, C. D. (1970). A general method applicable to the search for similarities in the amino acid sequence of two proteins. *Journal of Molecular Biology*, 48(3), 443-453.
- Wagner, R. A., & Fischer, M. J. (1974). The string-to-string correction problem. *Journal of the ACM*, 21(1), 168-173.
- Hirschberg, D. S. (1975). A linear space algorithm for computing maximal common subsequences. *Communications of the ACM*, 18(6), 341-343.
- Hunt, J. W., & Szymanski, T. G. (1977). A fast algorithm for computing longest common subsequences. *Communications of the ACM*, 20(5), 350-353.
