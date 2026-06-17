# Práctica SMP: Stable Marriage Problem (Algoritmo de Gale-Shapley)

Esta carpeta contiene la implementación, experimentación y documentación formal de la solución al Problema de los Matrimonios Estables (Stable Marriage Problem - SMP) mediante el **Algoritmo de Gale-Shapley**. 

El objetivo principal de esta práctica es implementar el algoritmo en dos lenguajes de programación distintos (**Python** y **C++**) para realizar un análisis comparativo formal de su complejidad temporal y eficiencia de ejecución bajo diferentes tamaños de entrada ($n$).

## Estructura del Directorio

El proyecto está organizado en tres carpetas principales para mantener un flujo de trabajo limpio entre el código fuente, los datos de prueba y la documentación.

### 1. `SRC/` (Código Fuente)
Contiene todos los scripts de implementación y utilidades:
* `1_Medir_tiempo.py`: Script orquestador que automatiza la ejecución del algoritmo en ambos lenguajes, pasando los datasets generados y registrando los tiempos de ejecución.
* `2_gale_shapley.py`: Implementación pura en **Python** del algoritmo de Gale-Shapley. Soporta la optimización orientada tanto a hombres (`m`) como a mujeres (`w`).
* `3_Graph.cpp` y `4_G_and_S.cpp`: Implementación optimizada en **C++** enfocada en el alto rendimiento computacional.
* `5_dataset_generator.py`: Generador automático de casos de prueba. Crea matrices de preferencias aleatorias asegurando el formato exacto que requieren los algoritmos.

### 2. `DAT/` (Datasets y Resultados)
Almacena los entornos de experimentación:
* **Casos de prueba (`dataset_*.txt`)**: Archivos de texto generados dinámicamente con múltiples tamaños de entrada (desde $n=5$ hasta $n=1000$) y sus respectivas repeticiones (ej. `rep0`, `rep1`, `rep2`) para obtener un promedio estadístico sólido. Están divididos según quién propone (*men* `_m_` o *women* `_w_`).
* **Registros de tiempo (`timing_*.txt`)**: Archivos de salida donde se guardan los tiempos de CPU en milisegundos para C++ y Python respectivamente.

### 3. `Reporte-Juan_Pablo-Gonzalez/` (Documentación IEEE)
Contiene la entrega teórica y analítica:
* `Reporte_main.tex`: Documento fuente escrito en **LaTeX** utilizando el formato de artículo de la IEEE (`IEEEtran.cls`).
* `Juan_Pablo_González_Mendoza.pdf`: El reporte compilado final. En él se abordan el modelado matemático, la demostración de correctitud del algoritmo y las gráficas comparativas de rendimiento (complejidad empírica $\mathcal{O}(n^2)$ vs tiempo de cómputo real).
* `Diagrams/`: Carpeta con los recursos gráficos insertados en el reporte LaTeX.

## ¿Cómo reproducir la práctica?

1. **Generar los datasets**:
   Ejecuta `5_dataset_generator.py` para construir nuevas matrices de preferencias de diferentes tamaños en la carpeta `DAT/`.
2. **Compilar C++**:
   Asegúrate de compilar los archivos `.cpp` (ej. `g++ 4_G_and_S.cpp -o gs_cpp`).
3. **Correr el Benchmark**:
   Ejecuta `1_Medir_tiempo.py`. Este programa alimentará de manera automatizada a los ejecutables de Python y C++ con los archivos de `DAT/` y escribirá los resultados en los archivos `timing_results.txt`.
