"""
Balanceo de Línea de Ensamblaje — Solver
Recibe parámetros del problema y devuelve la solución óptima como dict.

Solución esperada caso base: C* = 80 segundos.

Dependencia: pip install ortools
"""

from ortools.sat.python import cp_model


def resolver(
    tiempos: list[int],
    nombres: list[str],
    num_estaciones: int,
    precedencias: list[tuple[int, int]],
    incompatibilidades: list[tuple[int, int]] | None = None,
    limite_espacio: list[int] | None = None,
    espacio: list[int] | None = None,
) -> dict:
    # -------------------------------------------------------------------------
    # Modelo CP-SAT
    # -------------------------------------------------------------------------
    model = cp_model.CpModel()
    num_tareas = len(tiempos)

    x = {
        (i, k): model.new_bool_var(f"x_{i}_{k}")
        for i in range(num_tareas)
        for k in range(num_estaciones)
    }
    C = model.new_int_var(0, sum(tiempos), "C")

    # -------------------------------------------------------------------------
    # Restricciones
    # -------------------------------------------------------------------------

    # R1 — Asignación única
    for i in range(num_tareas):
        model.add_exactly_one(x[i, k] for k in range(num_estaciones))

    # R2 — Cota Minimax
    for k in range(num_estaciones):
        model.add(sum(tiempos[i] * x[i, k] for i in range(num_tareas)) <= C)

    # R3 — Precedencia
    for u, v in precedencias:
        estacion_u = sum(k * x[u, k] for k in range(num_estaciones))
        estacion_v = sum(k * x[v, k] for k in range(num_estaciones))
        model.add(estacion_u <= estacion_v)

    # R4 — Incompatibilidad (opcional)
    if incompatibilidades:
        for u, v in incompatibilidades:
            for k in range(num_estaciones):
                model.add_at_most_one([x[u, k], x[v, k]])

    # R5 — Límite de espacio físico (opcional)
    if espacio and limite_espacio:
        for k in range(num_estaciones):
            model.add(sum(espacio[i] * x[i, k] for i in range(num_tareas)) <= limite_espacio[k])

    # -------------------------------------------------------------------------
    # Función objetivo
    # -------------------------------------------------------------------------
    model.minimize(C)

    # -------------------------------------------------------------------------
    # Resolución
    # -------------------------------------------------------------------------
    solver = cp_model.CpSolver()
    status = solver.solve(model)

    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return {"status": solver.status_name(status)}

    ciclo = solver.value(C)
    estaciones = []
    for k in range(num_estaciones):
        tareas_k = [i for i in range(num_tareas) if solver.value(x[i, k]) == 1]
        tiempo_k = sum(tiempos[i] for i in tareas_k)
        estacion = {
            "numero": k + 1,
            "tareas": [nombres[i] for i in tareas_k],
            "tiempo": tiempo_k,
            "ocio": ciclo - tiempo_k,
        }
        if espacio:
            estacion["espacio"] = sum(espacio[i] for i in tareas_k)
        estaciones.append(estacion)

    resultado = {
        "status": solver.status_name(status),
        "ciclo_optimo": ciclo,
        "tasa_produccion": round(3600 / ciclo, 1),
        "estaciones": estaciones,
    }

    if espacio and limite_espacio:
        eficiencia = (sum(tiempos) / (num_estaciones * ciclo)) * 100
        resultado["eficiencia"] = round(eficiencia, 1)

    return resultado


if __name__ == "__main__":
    resultado = resolver(
        tiempos=[30, 15, 45, 20, 35],
        nombres=["Inspección", "Etiquetado", "Empaquetado", "Cupón", "Sellado"],
        num_estaciones=2,
        precedencias=[(0, 1), (1, 2), (1, 3), (2, 4), (3, 4)],
    )
    print(resultado)
