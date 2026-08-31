---
description: Programación Lineal Binaria en Python — variables de decisión 0/1, formulación matemática y casos de uso como balanceo de línea y asignación de recursos.
---

# Programación Lineal Binaria (PLB)

La Programación Lineal Binaria es un caso especial de la Programación Entera donde **todas las variables de decisión son binarias**: solo pueden tomar los valores 0 o 1.

## Forma General

**Minimizar (o maximizar):**

$$z = \sum_{j} c_j x_j$$

**Sujeto a:**

$$\sum_{j} a_{ij} x_j \leq b_i \quad \forall i$$

$$x_j \in \{0, 1\} \quad \forall j$$

## ¿Cuándo se usa?

Se aplica cuando las decisiones son de naturaleza **sí/no, asignar/no asignar, incluir/excluir**. La variable binaria codifica exactamente ese tipo de elección discreta.

## Ejemplos de uso típico

| Tipo de problema | Variable binaria representa |
|---|---|
| Asignación de tareas a recursos | 1 si la tarea i va al recurso k |
| Selección de proyectos con presupuesto | 1 si el proyecto j se ejecuta |
| Ruteo de vehículos | 1 si el vehículo recorre el arco (i,j) |
| Localización de instalaciones | 1 si se abre la planta en la ubicación j |
| Balanceo de líneas de ensamblaje | 1 si la tarea i se asigna a la estación k |

## Casos desarrollados

| Caso | Descripción | Archivos |
|---|---|---|
| [Balanceo de Línea](./Balanceo_de_Linea/) | Minimización de cuello de botella (Minimax) en línea de ensamblaje | `README.md`, `caso_simple.py`, `caso_extendido.py` |

## 🔗 Demo en vivo

*Próximamente — API de prueba interactiva*
