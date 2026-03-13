# Se requiere
#   pip install ollama
#
import ollama

response = ollama.generate(
    model='llama3.2',
    #model='gpt-oss:20b',
    prompt='How to implement the Shell sort algorithm?'
)

print(response['response'])