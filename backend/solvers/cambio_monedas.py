"""
Cambio de Monedas - Caso Base
Encontrar el numero minimo de monedas para alcanzar un monto exacto
(programacion dinamica bottom-up, uso ilimitado de cada denominacion).

Solucion optima esperada: 2 monedas (5 + 6 = 11).

Dependencia: Python estandar (sin librerias externas).
"""


def resolver_cambio():
    # -----------------------------------------------------------------------
    # Datos del problema
    # -----------------------------------------------------------------------
    denominaciones = [1, 5, 6]
    monto = 11

    INF = float("inf")
    n = len(denominaciones)

    # -----------------------------------------------------------------------
    # Tabla DP — vector de tamano (monto + 1)
    # -----------------------------------------------------------------------
    dp = [INF] * (monto + 1)
    moneda_usada = [-1] * (monto + 1)
    dp[0] = 0

    for c in range(1, monto + 1):
        for d in denominaciones:
            if d <= c and dp[c - d] + 1 < dp[c]:
                dp[c] = dp[c - d] + 1
                moneda_usada[c] = d

    # -----------------------------------------------------------------------
    # Reconstruccion de la solucion (backtracking)
    # -----------------------------------------------------------------------
    monedas_elegidas = []
    c = monto
    while c > 0:
        d = moneda_usada[c]
        monedas_elegidas.append(d)
        c -= d
    monedas_elegidas.sort(reverse=True)

    # -----------------------------------------------------------------------
    # Resultados
    # -----------------------------------------------------------------------
    print("=" * 40)
    print("CAMBIO DE MONEDAS - CASO BASE")
    print("=" * 40)
    print(f"Denominaciones       : {denominaciones}")
    print(f"Monto objetivo       : {monto}")
    print()
    if dp[monto] == INF:
        print("No existe solucion con las denominaciones dadas.")
    else:
        print("Monedas seleccionadas:")
        from collections import Counter
        conteo = Counter(monedas_elegidas)
        for den in sorted(conteo.keys(), reverse=True):
            print(f"  Denominacion {den:>3}  x{conteo[den]}")
        print()
        print(f"Total de monedas  : {dp[monto]}")
        print(f"Verificacion      : {' + '.join(str(m) for m in monedas_elegidas)} = {sum(monedas_elegidas)}")
    print("=" * 40)


if __name__ == "__main__":
    resolver_cambio()
