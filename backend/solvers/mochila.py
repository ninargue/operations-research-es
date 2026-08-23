"""
Mochila 0/1 - Caso Base
Seleccionar lotes de carga para maximizar el valor transportado
sin exceder la capacidad del camion (programacion dinamica bottom-up).

Solucion optima esperada: valor* = 8, lotes seleccionados: A + B.

Dependencia: Python estandar (sin librerias externas).
"""


def resolver_mochila():
    # -----------------------------------------------------------------------
    # Datos del problema
    # -----------------------------------------------------------------------
    lotes = [
        {"nombre": "Lote A", "valor": 5, "volumen": 4},
        {"nombre": "Lote B", "valor": 3, "volumen": 2},
        {"nombre": "Lote C", "valor": 4, "volumen": 3},
    ]
    capacidad = 6
    n = len(lotes)

    # -----------------------------------------------------------------------
    # Tabla DP  (indices 0..n filas x 0..capacidad columnas)
    # -----------------------------------------------------------------------
    dp = [[0] * (capacidad + 1) for _ in range(n + 1)]
    tomado = [[False] * (capacidad + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        lote = lotes[i - 1]
        for w in range(capacidad + 1):
            sin_lote = dp[i - 1][w]
            if lote["volumen"] <= w:
                con_lote = lote["valor"] + dp[i - 1][w - lote["volumen"]]
                if con_lote >= sin_lote:
                    dp[i][w] = con_lote
                    tomado[i][w] = True
                else:
                    dp[i][w] = sin_lote
            else:
                dp[i][w] = sin_lote

    # -----------------------------------------------------------------------
    # Reconstruccion de la solucion (backtracking)
    # -----------------------------------------------------------------------
    seleccionados = []
    w = capacidad
    for i in range(n, 0, -1):
        if tomado[i][w]:
            seleccionados.append(lotes[i - 1]["nombre"])
            w -= lotes[i - 1]["volumen"]
    seleccionados.reverse()

    # -----------------------------------------------------------------------
    # Resultados
    # -----------------------------------------------------------------------
    valor_optimo = dp[n][capacidad]
    volumen_usado = sum(l["volumen"] for l in lotes if l["nombre"] in seleccionados)

    print("=" * 40)
    print("MOCHILA 0/1 - CASO BASE")
    print("=" * 40)
    print(f"Capacidad del camion : {capacidad} m3")
    print(f"Numero de lotes      : {n}")
    print()
    print("Lotes seleccionados:")
    for nombre in seleccionados:
        lote = next(l for l in lotes if l["nombre"] == nombre)
        print(f"  {nombre}  |  valor: ${lote['valor']}  |  volumen: {lote['volumen']} m3")
    print()
    print(f"Volumen utilizado : {volumen_usado} / {capacidad} m3")
    print(f"Valor total       : ${valor_optimo}")
    print("=" * 40)


if __name__ == "__main__":
    resolver_mochila()
