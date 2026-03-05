# Se requiere
#   pip install ollama
#
import ollama

response = ollama.generate(
    #model='llama3.2',
    model='qwen3:4B',
    prompt='Como funciona el algoritmo del cartero?'
)

print(response['response'])
