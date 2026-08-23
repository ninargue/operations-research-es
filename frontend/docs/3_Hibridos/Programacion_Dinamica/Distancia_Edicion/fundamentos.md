# Fundamentos — Distancia de Edición

## ¿Qué es el problema?

La **Distancia de Edición** (*Edit Distance*), también conocida como **distancia de Levenshtein**, es una métrica que cuantifica la disimilitud entre dos cadenas de texto. Formalmente, mide el número mínimo de operaciones elementales de edición necesarias para transformar una cadena $s$ en otra cadena $t$.

Las tres operaciones permitidas son:

| Operación | Descripción | Costo |
|---|---|---|
| Inserción (*insert*) | Agregar un carácter en cualquier posición | 1 |
| Eliminación (*delete*) | Eliminar un carácter en cualquier posición | 1 |
| Sustitución (*substitute*) | Reemplazar un carácter por otro | 1 |

La distancia de Levenshtein satisface las propiedades de una **métrica de espacio**:

1. **No negatividad**: $d(s, t) \geq 0$
2. **Identidad**: $d(s, t) = 0 \iff s = t$
3. **Simetría**: $d(s, t) = d(t, s)$
4. **Desigualdad triangular**: $d(s, u) \leq d(s, t) + d(t, u)$

Vladimir Levenshtein introdujo esta métrica en 1965 en el contexto de la teoría de la información y los códigos de corrección de errores. Hoy es omnipresente en procesamiento de lenguaje natural, bioinformática y sistemas de búsqueda.

**Complejidad**: la solución por fuerza bruta es exponencial. La solución mediante **programación dinámica** (*dynamic programming*, DP) resuelve el problema en tiempo $O(m \cdot n)$ y espacio $O(m \cdot n)$, donde $m = |s|$ y $n = |t|$.

---

## Contexto del ejemplo

Un corrector ortográfico (*spell checker*) recibe la palabra mal escrita `"kitten"` y evalúa si la corrección propuesta `"sitting"` es alcanzable con pocas operaciones. La distancia de Levenshtein entre ambas es **3**.

**Secuencia de transformación (edit script mínimo):**

```
kitten  →  sitten   (sustituir k → s, posición 1)
sitten  →  sittin   (sustituir e → i, posición 5)
sittin  →  sitting  (insertar g al final)
```

**Comparación de estrategias:**

| Estrategia | Complejidad temporal | Comentario |
|---|---|---|
| Fuerza bruta (*brute force*) | Exponencial | Enumera todas las secuencias de operaciones |
| Recursión con memoización (*top-down DP*) | $O(m \cdot n)$ | Evita recalcular subproblemas solapados |
| DP iterativo (*bottom-up DP*) | $O(m \cdot n)$ | Llena la tabla en orden; sin overhead de recursión |
| DP con espacio optimizado | $O(\min(m, n))$ | Solo conserva dos filas; no permite reconstrucción |

---

## Diferencia con Longest Common Subsequence (LCS)

Ambos problemas comparten la misma estructura: una tabla 2D donde cada celda $(i, j)$ depende de $(i-1, j)$, $(i, j-1)$ e $(i-1, j-1)$. Sin embargo, sus objetivos son opuestos:

| Característica | LCS | Distancia de Edición |
|---|---|---|
| Objetivo | Maximizar lo común | Minimizar lo diferente |
| Caso de match $(s_i = t_j)$ | $dp[i-1][j-1] + 1$ | $dp[i-1][j-1]$ (sin costo) |
| Caso de mismatch | $\max(dp[i-1][j],\, dp[i][j-1])$ | $1 + \min(dp[i-1][j],\, dp[i][j-1],\, dp[i-1][j-1])$ |
| Respuesta | $dp[m][n]$ (longitud máxima) | $dp[m][n]$ (costo mínimo) |
| Relación | $d_{ins/del}(s,t) = m + n - 2 \cdot \text{LCS}(s,t)$ | — |

La relación entre LCS y distancia de edición (solo con inserciones y eliminaciones, sin sustitución) es: $d(s, t) = m + n - 2 \cdot \text{LCS}(s, t)$.

---

## Aplicaciones por sector

**Bioinformática**: alineamiento de secuencias de ADN, ARN y proteínas (*sequence alignment*). La variante ponderada — con costos diferenciados por tipo de mutación — es la base del algoritmo de Needleman-Wunsch (global) y Smith-Waterman (local).

**Corrección ortográfica (*spell checking*)**: determinar las $k$ palabras del vocabulario más cercanas (menor distancia) a la palabra introducida por el usuario. Motores como Hunspell y LanguageTool lo utilizan.

**Búsqueda aproximada (*fuzzy search*)**: encontrar registros similares aunque no idénticos. Herramientas como `fzf`, Elasticsearch y bases de datos PostgreSQL (módulo `pg_trgm`) aprovechan métricas de edición.

**Deduplicación de registros (*record linkage*)**: unificar entradas duplicadas en bases de datos donde los campos difieren por errores de escritura (nombres de personas, direcciones).

**Traducción automática**: evaluación de calidad de traducciones mediante la métrica TER (*Translation Edit Rate*), que normaliza la distancia de edición por la longitud de la referencia.

**Reconocimiento de voz (*speech recognition*)**: la métrica WER (*Word Error Rate*) aplica distancia de edición a nivel de palabra para evaluar transcripciones automáticas.

**Seguridad informática**: detección de variantes de contraseñas o claves (*password fuzzing*), identificación de dominios de phishing similares a dominios legítimos (*typosquatting detection*).
