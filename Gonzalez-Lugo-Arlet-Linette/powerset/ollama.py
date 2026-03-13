import requests

url = "http://localhost:11434/api/generate"
#url2 = "http://100.113.158.78:11434/api/generate"

data = {
    "model": "llama3.2",
    "prompt": "Generame un codigo sobre quicksort",
    "stream": False
}

response = requests.post(url, json=data)
#response = requests.post(url2, json=data)

resultado = response.json()

print(resultado["response"])