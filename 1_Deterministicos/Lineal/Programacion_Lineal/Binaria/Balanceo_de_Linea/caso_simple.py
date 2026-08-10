"""
Balanceo de Línea de Ensamblaje — Caso Simple
Minimización de cuello de botella (Minimax) con OR-Tools CP-SAT.

Problema: 5 tareas, 2 estaciones, restricciones de precedencia.
Solución óptima esperada: C* = 80 segundos.

Dependencia: pip install ortools
"""

from ortools.sat.python import cp_model


def resolver_balanceo_linea():
    # -------------------------------------------------------------------------
    # Datos del problema
    # -------------------------------------------------------------------------
    # Tareas indexadas en 0: 0=Inspección, 1=Etiquetado, 2=Empaquetado,
    #                        3=Cupón, 4=Sellado
    tiempos = [30, 15, 45, 20, 35]
    nombres = ["Inspección", "Etiquetado", "Empaquetado", "Cupón", "Sellado"]
    num_tareas = len(tiempos)
    num_estaciones = 2

    # Pares (u, v): la tarea u debe ejecutarse antes que la tarea v
    precedencias = [
        (0, 1),  # Inspección → Etiquetado
        (1, 2),  # Etiquetado → Empaquetado
        (1, 3),  # Etiquetado → Cupón
        (2, 4),  # Empaquetado → Sellado
        (3, 4),  # Cupón → Sellado
    ]

    # -------------------------------------------------------------------------
    # Modelo CP-SAT
    # -------------------------------------------------------------------------
    model = cp_model.CpModel()

    # Variables de decisión
    # x[i, k] = 1 si la tarea i se asigna a la estación k
    x = {
        (i, k): model.new_bool_var(f"x_{i}_{k}")
        for i in range(num_tareas)
        for k in range(num_estaciones)
    }

    # C = tiempo de ciclo máximo (cuello de botella)
    C = model.new_int_var(0, sum(tiempos), "C")

    # -------------------------------------------------------------------------
    # Restricciones
    # -------------------------------------------------------------------------

    # R1 — Asignación única: cada tarea va a exactamente una estación
    for i in range(num_tareas):
        model.add(sum(x[i, k] for k in range(num_estaciones)) == 1)

    # R2 — Cota Minimax: la carga de cada estación no supera C
    for k in range(num_estaciones):
        model.add(
            sum(tiempos[i] * x[i, k] for i in range(num_tareas)) <= C
        )

    # R3 — Precedencia: estación(u) <= estación(v)
    # La estación asignada a la tarea i se expresa como sum(k * x[i,k])
    for u, v in precedencias:
        estacion_u = sum(k * x[u, k] for k in range(num_estaciones))
        estacion_v = sum(k * x[v, k] for k in range(num_estaciones))
        model.add(estacion_u <= estacion_v)

    # -------------------------------------------------------------------------
    # Función objetivo: minimizar el cuello de botella
    # -------------------------------------------------------------------------
    model.minimize(C)

    # -------------------------------------------------------------------------
    # Resolución
    # -------------------------------------------------------------------------
    solver = cp_model.CpSolver()
    status = solver.solve(model)

    # -------------------------------------------------------------------------
    # Resultados
    # -------------------------------------------------------------------------
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        ciclo = solver.value(C)
        print("=" * 50)
        print("  SOLUCIÓN ÓPTIMA — BALANCEO DE LÍNEA (SIMPLE)")
        print("=" * 50)
        print(f"  Tiempo de ciclo óptimo C* = {ciclo} s")
        print(f"  Tasa de producción        = {3600 / ciclo:.1f} kits/hora")
        print()

        for k in range(num_estaciones):
            tareas_k = [i for i in range(num_tareas) if solver.value(x[i, k]) == 1]
            tiempo_k = sum(tiempos[i] for i in tareas_k)
            print(f"  Estación {k + 1}:")
            print(f"    Tareas   : {[nombres[i] for i in tareas_k]}")
            print(f"    Tiempo   : {tiempo_k} s")
            print(f"    Ocio     : {ciclo - tiempo_k} s")
            print()
    else:
        print(f"No se encontró solución factible. Estado: {solver.status_name(status)}")


if __name__ == "__main__":
    resolver_balanceo_linea()
