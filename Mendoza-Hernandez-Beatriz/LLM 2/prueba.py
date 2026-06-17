import ollama

response = ollama.generate(
    model="llama3.2",
    prompt="Hola"
)

print(response["response"])