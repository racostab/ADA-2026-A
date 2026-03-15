# API Para conectarse de forma remota a LLM (CLAUDE)
import anthropic

client = anthropic.Anthropic(
    api_key="APIKEY"
)

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=300,
    messages=[{"role": "user", "content": "Hola, dame una prueba corta"}],
)

for block in message.content:
    if block.type == "text":
        print(block.text)
