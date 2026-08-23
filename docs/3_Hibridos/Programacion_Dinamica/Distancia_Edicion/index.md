# Distancia de Edición (Edit Distance / Levenshtein)

Número mínimo de operaciones de edición (inserción, eliminación, sustitución) para transformar una cadena en otra, resuelto con programación dinámica en tiempo $O(m \cdot n)$.

## Archivos

| Archivo | Descripción |
|---|---|
| `fundamentos.md` | Definición del problema, contexto, diferencia con LCS y aplicaciones por sector |
| `formulacion.md` | Formulación matemática: conjuntos, variable de decisión, función objetivo y restricciones |
| `complejidad.md` | Análisis de complejidad y técnicas de mitigación para cadenas largas |
| `ejemplos.md` | Tabla DP desplegada, edit script reconstruido y salida esperada de los programas |
| `caso_base.py` | Solución DP para `"kitten"` → `"sitting"` (distancia = 3) |
| `caso_extendido.py` | Solución DP para `"intention"` → `"execution"` (distancia = 5), imprime tabla DP completa |
| `distancia_edicion_dp.html` | Visualizador interactivo paso a paso con coloreado de dependencias y edit script |

## Ejecución

```bash
python caso_base.py
python caso_extendido.py
```

Abrir `distancia_edicion_dp.html` directamente en el navegador (no requiere servidor).

## Instancias

| Instancia | src | dst | Distancia |
|---|---|---|---|
| Base | `kitten` | `sitting` | 3 |
| Extendida | `intention` | `execution` | 5 |

## Referencias

- Levenshtein, V. I. (1966). "Binary codes capable of correcting deletions, insertions, and reversals." *Soviet Physics Doklady*, 10(8), 707–710.
- Wagner, R. A., & Fischer, M. J. (1974). "The string-to-string correction problem." *Journal of the ACM*, 21(1), 168–173.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.), Capítulo 14. MIT Press.
