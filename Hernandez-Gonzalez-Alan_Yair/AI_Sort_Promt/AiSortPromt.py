import ollama
from pathlib import Path
import subprocess

base_dir = Path(__file__).parent
file_name = "InsertionSort.py"
file_path =  f"{base_dir}/{file_name}"
prompts = ['Me puedes dar el algoritmo de ordenamiento Insertion sort en python y sin explicaciones, listo para escribirlo en un archivo. El algoritmo se debe encontrar dentro de una función llamada insertion_sort que reciba un array y devuelva el array ordenado'
          'Me pudes generar un conjunto de números dentro de una lista en python, los cuales van a estar organizados de la siguiente manera. Cada elemento de la lista debe ser un arreglo, en total la lista debe tener 10 elementos y se llamará numbers. A su vez cada arreglo debe contener 15 números aleatorios en desorden, que los números sean diferentes para cada arreglo. Requiero los números, no el codigo para generarlo',
          'Me puedes dar el codigo para interar una lista llamada numbers y pasarle cada elemento de la lista a una funcion en python llamada insertion_sort. La lista tiene dentro una serie de arreglos, por lo cual debe ser iterada. Después de que la funcion regrese el arreglo ordenado, deseo que se imprima cada arreglo en una lína diferente. Requiero unicamente esa porción de código, ya cuento con la función del algoritomo de ordenamiento, sin explicaciones y listo para escribir en un archivo.']
responses = {}

for i in range(len(prompts)):
    responses[i] = ollama.generate(
        #model='llama3.2',
        model='qwen3:4B',
        prompt=prompts[i]
    )
    ollama.generate
print('========================= Ollama responses =========================') 
for response in responses.values():
    print(response['response'])

def writeFile(content, dir):
    with open(f"{dir}/{file_name}", "w") as f:
        for response in responses.values():
            f.write(f'{response['response']}\n')



def runFile(file_program):
    result = subprocess.run(
        ["python3", file_program],
        input='',
        text=True,
        capture_output=True
    )  
    print('========================= Program execution =========================')  
    print("STDOUT:")
    print(result.stdout)

    print("STDERR:")
    print(result.stderr)

writeFile(responses, base_dir)
runFile(file_path)