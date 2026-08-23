"""
Subsecuencia Comun mas Larga (LCS) - Caso Base
Encontrar la subsecuencia de mayor longitud comun a dos cadenas
preservando el orden relativo de los caracteres (programacion dinamica bottom-up).

Solucion optima esperada: longitud LCS = 4 (ej. "BCBA" o "BDAB").

Dependencia: Python estandar (sin librerias externas).
"""


def resolver_lcs():
    # -----------------------------------------------------------------------
    # Datos del problema
    # -----------------------------------------------------------------------
    X = "ABCBDAB"
    Y = "BDCABA"
    m, n = len(X), len(Y)

    # -----------------------------------------------------------------------
    # Tabla DP  (indices 0..m filas x 0..n columnas)
    # -----------------------------------------------------------------------
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # 'U'=arriba, 'L'=izquierda, 'D'=diagonal (match)
    direccion = [[""] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                direccion[i][j] = "D"
            elif dp[i - 1][j] >= dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
                direccion[i][j] = "U"
            else:
                dp[i][j] = dp[i][j - 1]
                direccion[i][j] = "L"

    # -----------------------------------------------------------------------
    # Reconstruccion de la LCS (backtracking diagonal)
    # -----------------------------------------------------------------------
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if direccion[i][j] == "D":
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif direccion[i][j] == "U":
            i -= 1
        else:
            j -= 1
    lcs.reverse()

    # -----------------------------------------------------------------------
    # Resultados
    # -----------------------------------------------------------------------
    print("=" * 40)
    print("LCS - CASO BASE")
    print("=" * 40)
    print(f"Secuencia X : {X}  (longitud {m})")
    print(f"Secuencia Y : {Y}  (longitud {n})")
    print()
    print(f"Longitud LCS : {dp[m][n]}")
    print(f"LCS          : {''.join(lcs)}")
    print("=" * 40)


if __name__ == "__main__":
    resolver_lcs()
