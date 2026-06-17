import requests

local = "localhost"
remote = "100.113.158.78"

urls = [
    f"http://{local}:11434/api/generate",
    f"http://{remote}:11434/api/generate"
]

modelos = [
    "deepseek-coder:latest",
    "deepseek-r1:latest",
    "qwen3:4b",
    "llama3:latest"
]


def generar_codigo(modelo, prompt):
    payload = {
        "model": modelo,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(
            urls[0],
            json=payload,
            timeout=300
        )

        if response.status_code != 200:

            print("\nError de Ollama")
            print("URL:", urls[0])
            print("Status:", response.status_code)
            print("Respuesta:")
            print(response.text)

            return None

        datos = response.json()

        return datos["response"]

    except requests.exceptions.RequestException as e:
        print("\nError de conexion con Ollama")
        print(e)

        return None
