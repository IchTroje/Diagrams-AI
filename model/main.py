from fastapi import FastAPI, Request
from pydantic import BaseModel
from llama_cpp import Llama

app = FastAPI()

llm = Llama(model_path="mistral.gguf", n_ctx=512)


class Prompt(BaseModel):
    prompt: str


@app.post("/generate")
def generate(prompt: Prompt):
    output = llm(prompt.prompt, max_tokens=100)
    return {"response": output["choices"][0]["text"]}
