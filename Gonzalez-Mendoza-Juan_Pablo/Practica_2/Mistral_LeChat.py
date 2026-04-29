"""
LeChat funciona con el modelo mistral, por lo tanto 
el algoritmo que se va a implementar se usa usando este modelo.

"""

import ollama

response = ollama.generate(
    model='mistral:latest',
    prompt='Como funciona el algoritmo Cocktail Shaker Sort?'
)
print(response.response)
