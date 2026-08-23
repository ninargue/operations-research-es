"""
Distancia de Edicion - Caso Base
Calcular el numero minimo de operaciones (insercion, eliminacion, sustitucion)
para transformar una cadena en otra (distancia de Levenshtein, DP bottom-up).

Solucion optima esperada: distancia = 3 ("kitten" -> "sitting").

Dependencia: Python estandar (sin librerias externas).
"""


def resolver_distancia_edicion():
    # -----------------------------------------------------------------------
    # Datos del problema
    # -----------------------------------------------------------------------
    src = "kitten"
    dst = "sitting"
    m, n = len(src), len(dst)

    # -----------------------------------------------------------------------
    # Tabla DP  (m+1 filas x n+1 columnas)
    # -----------------------------------------------------------------------
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # 'M'=match (sin cambio), 'S'=sustitucion, 'D'=eliminacion, 'I'=insercion
    op = [[""] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
        op[i][0] = "D"
    for j in range(n + 1):
        dp[0][j] = j
        op[0][j] = "I"
    op[0][0] = ""

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if src[i - 1] == dst[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                op[i][j] = "M"
            else:
                eliminacion = dp[i - 1][j] + 1
                insercion = dp[i][j - 1] + 1
                sustitucion = dp[i - 1][j - 1] + 1
                dp[i][j] = min(eliminacion, insercion, sustitucion)
                if dp[i][j] == sustitucion:
                    op[i][j] = "S"
                elif dp[i][j] == eliminacion:
                    op[i][j] = "D"
                else:
                    op[i][j] = "I"

    # -----------------------------------------------------------------------
    # Reconstruccion del edit script (backtracking)
    # -----------------------------------------------------------------------
    edit_script = []
    i, j = m, n
    while i > 0 or j > 0:
        operacion = op[i][j]
        if operacion == "M":
            edit_script.append(f"  Sin cambio : '{src[i-1]}' (posicion {i})")
            i -= 1; j -= 1
        elif operacion == "S":
            edit_script.append(f"  Sustituir  : '{src[i-1]}' -> '{dst[j-1]}' (posicion {i})")
            i -= 1; j -= 1
        elif operacion == "D":
            if i > 0:
                edit_script.append(f"  Eliminar   : '{src[i-1]}' (posicion {i})")
                i -= 1
            else:
                j -= 1
        else:  # "I"
            if j > 0:
                edit_script.append(f"  Insertar   : '{dst[j-1]}' (posicion {j})")
                j -= 1
            else:
                i -= 1
    edit_script.reverse()

    # -----------------------------------------------------------------------
    # Resultados
    # -----------------------------------------------------------------------
    print("=" * 45)
    print("DISTANCIA DE EDICION - CASO BASE")
    print("=" * 45)
    print(f"Cadena fuente  : '{src}'  (longitud {m})")
    print(f"Cadena destino : '{dst}'  (longitud {n})")
    print()
    print(f"Distancia de edicion : {dp[m][n]}")
    print()
    print("Edit script (operaciones minimas):")
    ops_no_triviales = [e for e in edit_script if "Sin cambio" not in e]
    for paso in ops_no_triviales:
        print(paso)
    print("=" * 45)


if __name__ == "__main__":
    resolver_distancia_edicion()
