import json
import time
import csv
import matplotlib.pyplot as plt
from smp import *

N = []
Tiempos_algoritmo = []
Tiempos_lectura = []
Archivo = []

for i in range(1,26):
  
  tiempo_inicio_lectura= time.time()
  file = f"../DAT/input{i}.json"
  with open(file,"r") as json_file:
    data = json.load(json_file)

  num_parejas = data["num_parejas"]
  men_pref = data["men_pref"]
  women_pref = data["women_pref"]
  tiempo_fin_lectura = time.time()

  tiempo_inicio_algoritmo = time.time()

  S = smp(men_pref,women_pref)

  tiempo_fin_algoritmo = time.time()
  tiempo_total_algoritmo = tiempo_fin_algoritmo - tiempo_inicio_algoritmo
  tiempo_total_lectura = tiempo_fin_lectura - tiempo_inicio_lectura

  Archivo.append(i)
  N.append(num_parejas)
  Tiempos_algoritmo.append(tiempo_total_algoritmo*1000)
  Tiempos_lectura.append(tiempo_total_lectura*1000)

with open('../DAT/Resultados.cvs','w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerows([Archivo,N,Tiempos_algoritmo,Tiempos_lectura])

plt.plot(N,Tiempos_algoritmo,'o:b')
#plt.title("Comportamiento temporal del algoritmo Gale-Shapley (Escala lineal)")
plt.xlabel("Numero de parejas (n)")
plt.ylabel("Tiempo (Milisegundos)")
plt.grid()
plt.savefig('../DAT/fig1.png', dpi=300, bbox_inches='tight')


plt.cla()
plt.plot(N,Tiempos_algoritmo,'o:r')
plt.grid()
plt.xlabel("Numero de parejas (n)")
plt.ylabel("Tiempo (Milisegundos)")
#plt.title("Comportamiento temporal del algoritmo Gale-Shapley (Escala logarítmica)")
plt.xscale('log',base=2)
plt.savefig('../DAT/fig2.png', dpi=300, bbox_inches='tight')

plt.cla()
plt.plot(N,Tiempos_lectura, 'o:k')
plt.grid()
plt.xlabel("Numero de parejas (n)")
plt.ylabel("Tiempo (Milisegundos)")
plt.savefig('../DAT/Fig3.png')