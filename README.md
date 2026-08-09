<p align="center">
  <img src="./banner.svg" alt="Operations Research en Español" width="100%"/>
</p>

> **Referencia técnica y práctica de Investigación de Operaciones:**  
> conceptos, algoritmos, código Python ejecutable y demos por sector.

Este repositorio tiene como objetivo reunir en un solo lugar los principales modelos matemáticos de la Investigación de Operaciones, explicados en español, con ejemplos aplicados a sectores reales: industria, banca, logística, transporte y servicios.

Cada tema incluye:
- 📖 Explicación conceptual y fundamentos matemáticos
- 🐍 Código Python ejecutable (notebooks Jupyter)
- 🏭 Casos de uso por sector
- 🔗 Demo interactiva (API de prueba)

---

## 🗺️ Mapa de Contenidos

```mermaid
graph LR
    ROOT(["🔬 Operations Research\nModelos Matemáticos"])

    ROOT --> D["📐 Determinísticos"]
    ROOT --> E["🎲 Estocásticos"]
    ROOT --> H["🔀 Híbridos"]

    D --> DL["Lineal"]
    D --> DNL["No Lineal"]

    DL --> PL["Programación Lineal"]
    DL --> MR["Modelo de Redes"]

    PL --> PB["Binaria"]
    PL --> PE["Entera"]
    PL --> PC["Continua"]
    PL --> PM["Mixta"]

    DNL --> PNL["Prog. No Lineal"]
    DNL --> MCL["Métodos Clásicos"]
    DNL --> MB["Métodos de Búsqueda"]

    E --> MKOV["Procesos de Markov"]
    E --> PES["Procesos Estocásticos"]
    E --> TDJ["Teoría Decisiones y Juegos"]
    E --> PEST["Programación Estocástica"]
    E --> AD["Árboles de Decisión"]

    MKOV --> PF["Proceso de Feller"]
    MKOV --> CM["Cadena de Markov"]

    PES --> CA["Camino Aleatorio"]
    PES --> MRT["Martingala"]
    PES --> LEV["Proceso de Lévy"]
    PES --> PG["Proceso Gaussiano"]
    PES --> CALT["Campos Aleatorios"]
    PES --> PREV["Proc. de Renovación"]
    PES --> PRAM["Proc. de Ramificación"]

    H --> TI["Teoría de Inventarios"]
    H --> PERT["PERT / CPM"]
    H --> SIM["Simulación"]
    H --> PHEUR["Prog. Heurística"]
    H --> PD["Prog. Dinámica"]

    click D "https://github.com/ninargue/operations-research-es/tree/main/1_Deterministicos" "Ver Modelos Determinísticos"
    click E "https://github.com/ninargue/operations-research-es/tree/main/2_Estocasticos" "Ver Modelos Estocásticos"
    click H "https://github.com/ninargue/operations-research-es/tree/main/3_Hibridos" "Ver Modelos Híbridos"

    style ROOT fill:#1e3a5f,color:#fff,stroke:#1e3a5f
    style D fill:#7b5ea7,color:#fff,stroke:#7b5ea7
    style E fill:#c75b7a,color:#fff,stroke:#c75b7a
    style H fill:#3a86b4,color:#fff,stroke:#3a86b4
```

---

## 📂 Estructura del Repositorio

| Rama | Descripción |
|------|-------------|
| [📐 1\_Deterministicos](./1_Deterministicos/) | Modelos donde los parámetros son conocidos con certeza |
| [🎲 2\_Estocasticos](./2_Estocasticos/) | Modelos que incorporan incertidumbre y probabilidad |
| [🔀 3\_Hibridos](./3_Hibridos/) | Técnicas que combinan elementos determinísticos y estocásticos |

---

## 🚀 Cómo usar este repositorio

### Requisitos

```bash
pip install -r requirements.txt
```

### Ejecutar notebooks

```bash
jupyter notebook
```

Navega a la carpeta del tema de interés y abre el archivo `.ipynb` correspondiente.

---

## 🏭 Aplicaciones por Sector

Los modelos de este repositorio tienen aplicación directa en:

| Sector | Ejemplos de uso |
|--------|-----------------|
| **Industria** | Planificación de producción, corte de materiales, scheduling |
| **Banca y Finanzas** | Gestión de portafolios, evaluación de riesgo, scoring crediticio |
| **Logística** | Ruteo de vehículos, distribución, gestión de almacenes |
| **Transporte** | Flujo en redes, asignación de rutas, timetabling |
| **Servicios** | Programación de turnos, asignación de recursos, colas |
| **Salud** | Programación quirúrgica, distribución de medicamentos |
| **Energía** | Despacho económico, planificación de redes eléctricas |

---

## 🤝 ¿Necesitas ayuda con alguno de estos modelos?

Si tu organización enfrenta un problema de optimización, simulación, toma de decisiones o planificación, puedes contactarme:

- 📧 **Email:** `[tu@email.com]`
- 💼 **LinkedIn:** *(agregar enlace)*
- 🔗 **Demos disponibles:** Cada tema cuenta con una API de prueba para que puedas interactuar con el modelo directamente.

---

## 📄 Licencia

[MIT](./LICENSE) — Libre uso con atribución.
