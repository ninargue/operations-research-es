"""
Balanceo de Línea de Ensamblaje — Caso Extendido
Agrega incompatibilidad de tareas (R4) y límite de espacio físico (R5).

Cambios respecto al caso base:
  - R4: tareas incompatibles no pueden compartir estación
  - R5: límite de espacio físico (m²) por estación

Solución óptima esperada: C* = 90 segundos (vs 80 s en el caso base).

Dependencia: pip install ortools
"""

from solvers.balanceo_de_linea import resolver


if __name__ == "__main__":
    resultado = resolver(
        tiempos=[30, 15, 45, 20, 35],
        nombres=["Inspección", "Etiquetado", "Empaquetado", "Cupón", "Sellado"],
        num_estaciones=2,
        precedencias=[(0, 1), (1, 2), (1, 3), (2, 4), (3, 4)],
        incompatibilidades=[(1, 3)],
        espacio=[2, 1, 3, 2, 3],
        limite_espacio=[8, 8],
    )
    print("=======================================================")
    print("  SOLUCIÓN ÓPTIMA — BALANCEO DE LÍNEA (EXTENDIDO)")
    print("=======================================================")
    print(f"  Tiempo de ciclo C*     = {resultado['ciclo_optimo']} s")
    print(f"  Tasa de producción     = {resultado['tasa_produccion']} kits/hora")
    print(f"  Eficiencia de la línea = {resultado['eficiencia']}%")
    for est in resultado["estaciones"]:
        print(f"\n  Estación {est['numero']}:")
        print(f"    Tareas   : {est['tareas']}")
        print(f"    Tiempo   : {est['tiempo']} s  (ocio: {est['ocio']} s)")
        print(f"    Espacio  : {est['espacio']} m² / 8 m²")
