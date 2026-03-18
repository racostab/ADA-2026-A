# pip install ollama
import ollama

prompt = """
Dame el codigo en Python del algoritmo Radix Sort.
Debe estar en una funcion llamada radix_sort(arr).
No agregues comentarios ni explicaciones.
"""

for i in range(1, 6):
    response = ollama.generate(
        model='mistral',
        prompt=prompt
    )

    codigo = response['response']

    with open(f"radix_sort_{i}.py", "w", encoding="utf-8") as f:
        f.write(codigo)

print("Se generaron 5 archivos .py")