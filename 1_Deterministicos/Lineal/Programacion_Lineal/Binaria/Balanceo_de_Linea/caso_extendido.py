"""
Balanceo de Línea de Ensamblaje — Caso Extendido
Agrega restricciones de incompatibilidad de tareas y límite de espacio físico.

Cambios respecto al caso simple:
  - R1: AddExactlyOne (más eficiente que sum() == 1 en CP-SAT)
  - R4: AddAtMostOne para pares de tareas incompatibles por estación
  - R5: Límite de espacio físico (m²) por estación

Solución óptima esperada: C* = 90 segundos (vs 80 s en el caso simple).

Dependencia: pip install ortools
"""

from ortools.sat.python import cp_model


def resolver_balanceo_con_restricciones_avanzadas():
    # -------------------------------------------------------------------------
    # Datos del problema
    # -------------------------------------------------------------------------
    nombres = ["Inspección", "Etiquetado", "Empaquetado", "Cupón", "Sellado"]
    tiempos = [30, 15, 45, 20, 35]          # segundos por tarea
    espacio = [2, 1, 3, 2, 3]               # m² requeridos por tarea
    num_tareas = len(tiempos)
    num_estaciones = 2
    limite_espacio = [8, 8]                  # m² disponibles por estación

    precedencias = [
        (0, 1),  # Inspección → Etiquetado
        (1, 2),  # Etiquetado → Empaquetado
        (1, 3),  # Etiquetado → Cupón
        (2, 4),  # Empaquetado → Sellado
        (3, 4),  # Cupón → Sellado
    ]

    # Tareas que NO pueden compartir estación (herramientas incompatibles)
    # Tarea 1 (Etiquetado) y Tarea 3 (Cupón) generan interferencia operativa
    incompatibilidades = [(1, 3)]

    # -------------------------------------------------------------------------
    # Modelo CP-SAT
    # -------------------------------------------------------------------------
    model = cp_model.CpModel()

    x = {
        (i, k): model.new_bool_var(f"x_{i}_{k}")
        for i in range(num_tareas)
        for k in range(num_estaciones)
    }

    C = model.new_int_var(0, sum(tiempos), "C")

    # -------------------------------------------------------------------------
    # Restricciones
    # -------------------------------------------------------------------------

    # R1 — Asignación única (método nativo CP-SAT, más eficiente que sum==1)
    for i in range(num_tareas):
        model.add_exactly_one(x[i, k] for k in range(num_estaciones))

    # R2 — Cota Minimax: carga de cada estación <= C
    for k in range(num_estaciones):
        model.add(
            sum(tiempos[i] * x[i, k] for i in range(num_tareas)) <= C
        )

    # R3 — Precedencia: estación(u) <= estación(v)
    for u, v in precedencias:
        estacion_u = sum(k * x[u, k] for k in range(num_estaciones))
        estacion_v = sum(k * x[v, k] for k in range(num_estaciones))
        model.add(estacion_u <= estacion_v)

    # R4 — Incompatibilidad: como máximo una tarea del par puede ir a la estación k
    for u, v in incompatibilidades:
        for k in range(num_estaciones):
            model.add_at_most_one([x[u, k], x[v, k]])

    # R5 — Límite de espacio físico por estación
    for k in range(num_estaciones):
        model.add(
            sum(espacio[i] * x[i, k] for i in range(num_tareas)) <= limite_espacio[k]
        )

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
        tiempo_total = sum(tiempos)
        eficiencia = (tiempo_total / (num_estaciones * ciclo)) * 100

        print("=" * 55)
        print("  SOLUCIÓN ÓPTIMA — BALANCEO DE LÍNEA (EXTENDIDO)")
        print("=" * 55)
        print(f"  Tiempo de ciclo C*     = {ciclo} s")
        print(f"  Tasa de producción     = {3600 / ciclo:.1f} kits/hora")
        print(f"  Eficiencia de la línea = {eficiencia:.1f}%")
        print()

        for k in range(num_estaciones):
            tareas_k = [i for i in range(num_tareas) if solver.value(x[i, k]) == 1]
            tiempo_k = sum(tiempos[i] for i in tareas_k)
            espacio_k = sum(espacio[i] for i in tareas_k)

            print(f"  Estación {k + 1}:")
            print(f"    Tareas   : {[nombres[i] for i in tareas_k]}")
            print(f"    Tiempo   : {tiempo_k} s  (ocio: {ciclo - tiempo_k} s)")
            print(f"    Espacio  : {espacio_k} m² / {limite_espacio[k]} m²")
            print()
    else:
        print(f"No se encontró solución factible. Estado: {solver.status_name(status)}")


if __name__ == "__main__":
    resolver_balanceo_con_restricciones_avanzadas()
