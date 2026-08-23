# Fundamentos — Subsecuencia Común más Larga (LCS)

## ¿Qué es el problema?

La *Longest Common Subsequence* (LCS) o **Subsecuencia Común más Larga** es uno de los problemas clásicos sobre secuencias en ciencias de la computación. Dado un par de secuencias $X$ e $Y$, se busca la subsecuencia de mayor longitud que aparece en ambas respetando el **orden relativo** de los elementos, aunque no necesariamente en posiciones contiguas.

Es fundamental distinguir dos conceptos que suelen confundirse:

| Concepto | Definición | Ejemplo con X="ABCBD", Y="ACB" |
|---|---|---|
| Subsecuencia (*subsequence*) | Subconjunto de elementos en orden relativo, no necesariamente contiguos | "ACB" es subsecuencia de X |
| Subcadena (*substring*) | Segmento contiguo de la secuencia original | "ABC" es substring de X, pero no de Y |

La LCS no exige contigüidad: basta con que el orden relativo se preserve en ambas secuencias. Esto la hace aplicable a dominios donde los elementos pueden estar separados por otros intermedios.

### Complejidad y estrategia

La búsqueda exhaustiva consideraría las $2^m$ subsecuencias posibles de $X$ y las $2^n$ de $Y$, lo que es inviable para entradas grandes. Programación dinámica (*dynamic programming*, DP) explota la **subestructura óptima** del problema:

$$\text{LCS}(X[1..m], Y[1..n]) \text{ depende de } \text{LCS}(X[1..m-1], Y[1..n-1])$$

Esto permite resolverlo en tiempo $O(m \cdot n)$ y espacio $O(m \cdot n)$, con variantes que reducen el espacio a $O(\min(m, n))$.

---

## Contexto del ejemplo

Un **sistema de control de versiones** (*version control system*) necesita identificar qué líneas se conservan entre dos versiones de un archivo de configuración. Las líneas comunes en orden constituyen la LCS; las que difieren corresponden a las inserciones y eliminaciones que reporta el comando `diff`.

Para el caso base:

- $X =$ `"ABCBDAB"` — versión original (longitud $m = 7$)
- $Y =$ `"BDCABA"` — versión nueva (longitud $n = 6$)
- LCS: `"BCBA"` o `"BDAB"` (ambas son válidas), longitud $= 4$

La LCS representa las líneas que permanecen sin cambios. Todo elemento de $X$ no en la LCS fue eliminado; todo elemento de $Y$ no en la LCS fue insertado.

### Comparativa de estrategias

| Estrategia | Complejidad temporal | Complejidad espacial | Observaciones |
|---|---|---|---|
| Fuerza bruta (*brute force*) | $O(2^m \cdot n)$ | $O(m)$ | Enumera todas las subsecuencias de $X$ y verifica en $Y$ |
| Recursión con memorización (*memoization*) | $O(m \cdot n)$ | $O(m \cdot n)$ | Evita recalcular subproblemas; puede tener overhead de pila |
| DP *bottom-up* | $O(m \cdot n)$ | $O(m \cdot n)$ | Solución iterativa, sin recursión |
| DP optimizado en espacio | $O(m \cdot n)$ | $O(\min(m, n))$ | Solo mantiene dos filas; no permite reconstrucción completa |
| Hunt-Szymanski (*sparse LCS*) | $O(r \log n)$ | $O(r)$ | Óptimo cuando los matches $r$ son escasos (secuencias dispersas) |

---

## Aplicaciones por sector

| Sector | Aplicación | Descripción |
|---|---|---|
| Bioinformática | Alineamiento de secuencias | Comparar secuencias de ADN, ARN o proteínas para identificar regiones conservadas evolutivamente |
| Control de versiones | `git diff` | Identificar líneas añadidas, eliminadas o conservadas entre dos versiones de un archivo |
| Procesamiento de lenguaje natural | Similitud entre documentos | Medir cuánto texto comparten dos documentos preservando el orden de las palabras |
| Detección de plagio | Texto en común | Encontrar fragmentos comunes entre documentos para evidenciar copia |
| Compresión de datos | Delta encoding | Almacenar solo las diferencias entre versiones consecutivas de un archivo |
| Reconocimiento de voz | Corrección de transcripciones | Comparar la secuencia de fonemas reconocida con la referencia esperada |
| Sistemas de recomendación | Secuencias de acciones de usuario | Comparar patrones de navegación de distintos usuarios para identificar comportamientos similares |
