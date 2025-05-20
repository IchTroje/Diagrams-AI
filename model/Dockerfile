FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN CMAKE_ARGS="-DLLAMA_AVX2=ON -DLLAMA_CUBLAS=OFF" \
    pip install llama-cpp-python --force-reinstall --no-cache-dir

RUN wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf \
-O mistral.gguf

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
