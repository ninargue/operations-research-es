"""
Caminos mas Cortos: Floyd-Warshall - Caso Base
Calcular la distancia minima entre todos los pares de nodos en un grafo
dirigido ponderado (programacion dinamica bottom-up, actualizacion in-place).

Instancia: red logistica de 4 bodegas.
  Aristas: 0->1(3), 0->3(7), 1->0(8), 1->2(2), 2->0(5), 2->3(1), 3->0(2)

Solucion optima esperada (verificada iteracion por iteracion):
  dist[0][3] = 6   (camino: 0->1->2->3)
  dist[1][3] = 3   (camino: 1->2->3)
  dist[1][0] = 5   (camino: 1->2->3->0)
  dist[2][0] = 3   (camino: 2->3->0)
  dist[2][1] = 6   (camino: 2->3->0->1)
  dist[3][1] = 5   (camino: 3->0->1)
  Sin ciclos negativos (diagonal = 0).

Dependencia: Python estandar (sin librerias externas).
"""


def resolver_floyd_warshall():
    # -----------------------------------------------------------------------
    # Datos del problema
    # -----------------------------------------------------------------------
    INF = float("inf")
    n = 4
    # Matriz de adyacencia (W[i][j] = peso de i->j, INF si no existe arista)
    dist = [
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0],
    ]

    # Matriz de reconstruccion: siguiente[i][j] = primer nodo en camino i->j
    siguiente = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] < INF:
                siguiente[i][j] = j

    # -----------------------------------------------------------------------
    # Algoritmo Floyd-Warshall (triple bucle)
    # -----------------------------------------------------------------------
    # Orden: k exterior (nodo intermedio), i medio (origen), j interior (destino)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    siguiente[i][j] = siguiente[i][k]

    # -----------------------------------------------------------------------
    # Deteccion de ciclos negativos
    # -----------------------------------------------------------------------
    ciclo_negativo = any(dist[i][i] < 0 for i in range(n))

    # -----------------------------------------------------------------------
    # Reconstruccion de caminos
    # -----------------------------------------------------------------------
    def reconstruir_camino(u, v):
        """Retorna la lista de nodos del camino mas corto de u a v."""
        if siguiente[u][v] is None:
            return []
        camino = [u]
        while u != v:
            u = siguiente[u][v]
            camino.append(u)
        return camino

    # -----------------------------------------------------------------------
    # Resultados
    # -----------------------------------------------------------------------
    print("=" * 50)
    print("FLOYD-WARSHALL - CASO BASE")
    print("=" * 50)

    if ciclo_negativo:
        print("ADVERTENCIA: Se detecto un ciclo negativo.")
    else:
        print("Matriz de distancias minimas:")
        header = "     " + "  ".join(f"{j:>4}" for j in range(n))
        print(header)
        print("     " + "-" * (n * 6))
        for i in range(n):
            fila = "  ".join(
                f"{dist[i][j]:>4}" if dist[i][j] < INF else " INF"
                for j in range(n)
            )
            print(f"  {i}  | {fila}")

        print()
        print("Ejemplos de caminos:")
        ejemplos = [(1, 3), (3, 1), (0, 2)]
        for u, v in ejemplos:
            camino = reconstruir_camino(u, v)
            ruta = " -> ".join(str(x) for x in camino)
            print(f"  {u} -> {v}: {ruta}  (costo: {dist[u][v]})")

    print("=" * 50)


if __name__ == "__main__":
    resolver_floyd_warshall()
