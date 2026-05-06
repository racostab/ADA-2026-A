from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM

app = FastAPI()

MODEL_PATH = "/model"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)

class Request(BaseModel):
    prompt: str
    max_tokens: int = 100

@app.post("/generate")
def generate(req: Request):
    inputs = tokenizer(req.prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=req.max_tokens)

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": response}

    from pydantic import BaseModel

class CompletionRequest(BaseModel):
    prompt: str
    max_tokens: int = 100

@app.post("/v1/completions")
def completions(req: CompletionRequest):
    inputs = tokenizer(req.prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=req.max_tokens)

    text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {
        "choices": [
            {
                "text": text
            }
        ]
    }

