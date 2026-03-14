user_input= input()
maze_values = user_input.split(" ")

maze_size_x = int(maze_values[0])
maze_size_y = int(maze_values[1])
start_y = int(maze_values[2])
start_x = int(maze_values[3])
finish_y = int(maze_values[4])
finish_x = int(maze_values[5])
output_type = int(maze_values[6])

casilla_inicio = (start_y,start_x)
casilla_fin = (finish_y,finish_x)

############################################################################################


def vecino_no_visitado(y,x):
  vecinos = []

  if x+1 < maze_size_x and maze[y][x+1] == " ":
    maze[y][x+1] = "X"
    vecinos.append((y,x+1))
    celda_anterior[(y,x+1)]=(y,x)

  if y+1 < maze_size_y and maze[y+1][x] == " ":
    maze[y+1][x] = "X"
    vecinos.append((y+1,x))
    celda_anterior[(y+1,x)]=(y,x)


  if x-1 >= 0 and maze[y][x-1] == " ":
    maze[y][x-1] = "X" 
    vecinos.append((y,x-1))
    celda_anterior[(y,x-1)]=(y,x)

  if y-1 >= 0 and maze[y-1][x] == " ":
    maze[y-1][x] = "X"
    vecinos.append((y-1,x))
    celda_anterior[(y-1,x)]=(y,x)
  
  return vecinos


###########################################################################################
def encontrar_salida(y_inicio, x_inicio, pendiente):

  maze[y_inicio][x_inicio] = "X" 
  
  while len(pendiente) != 0:
    y_actual, x_actual = pendiente.pop(0)

    if (y_actual, x_actual) == casilla_fin:
      maze[y_actual][x_actual] = "O"
      return True

    
    vecinos = vecino_no_visitado(y_actual, x_actual)
    
    for y_vecino, x_vecino in vecinos:
      pendiente.append((y_vecino, x_vecino))

  return False

############################################################################################
def obtener_camino(celda_anterior,casilla_actual):
  if celda_anterior[casilla_actual] == None:
    camino.reverse()
    return 

  y_actual, x_actual = casilla_actual
  y_anterior,x_anterior = celda_anterior[casilla_actual]

  if y_actual == y_anterior+1:
    camino.append("D")
  elif y_actual == y_anterior-1:
    camino.append("U")
  elif x_actual == x_anterior+1:
    camino.append("R")
  elif x_actual == x_anterior-1:
    camino.append("L")

  obtener_camino(celda_anterior,(y_anterior,x_anterior))

############################################################################################

def respuesta(celda_anterior,casilla_fin,tipo_respuesta):
  match tipo_respuesta:
    case 1:
      if casilla_fin in celda_anterior:
        return "True"
      else:
        return "False"
    
    case 2:
      obtener_camino(celda_anterior,casilla_fin)
      return len(camino)
    
    case 3:
      obtener_camino(celda_anterior,casilla_fin)
      return ''.join(camino)

############################################################################################

maze = []
pendiente = [casilla_inicio]
celda_anterior = {
  (start_y,start_x): None
}
camino = []

for i in range(maze_size_y):
  user_input = input()
  maze_row = list(user_input)
  maze.append(maze_row)



encontrar_salida(start_y,start_x,pendiente)
Respuesta = respuesta(celda_anterior,casilla_fin,output_type)
print(Respuesta)
