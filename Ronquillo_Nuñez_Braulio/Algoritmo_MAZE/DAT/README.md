## Algoritmo MAZE

Esta carpeta contiene casos de prueba basados en el documento `MAZE.pdf`.

### Archivos

- `input_o1.txt`: entrada del ejemplo del documento con `O = 1`.
- `output_o1.txt`: salida esperada segun el documento para `O = 1`.
- `input_o2.txt`: entrada del ejemplo del documento con `O = 2`.
- `output_o2.txt`: salida esperada segun el documento para `O = 2`.
- `input_o3.txt`: entrada del ejemplo del documento con `O = 3`.
- `output_o3.txt`: salida esperada segun el documento para `O = 3`.

### Ejecucion

Desde la raiz del proyecto:

```powershell
Get-Content Algoritmo_MAZE\DAT\input_o1.txt | python Algoritmo_MAZE\SRC\maze_COACH.py
Get-Content Algoritmo_MAZE\DAT\input_o2.txt | python Algoritmo_MAZE\SRC\maze_COACH.py
Get-Content Algoritmo_MAZE\DAT\input_o3.txt | python Algoritmo_MAZE\SRC\maze_COACH.py
```

### Nota

Los archivos `output_o1.txt`, `output_o2.txt` y `output_o3.txt` reproducen las salidas publicadas en el PDF.

El script actual `maze_COACH.py` coincide con `O = 1`, pero para `O = 2` y `O = 3` produce una salida distinta porque calcula una ruta mas corta.
