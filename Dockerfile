FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y curl zstd && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN curl -fsSL https://ollama.com/install.sh | sh

COPY . .

#ollama serve & sleep 5 && ollama pull phi &&
CMD sh -c "ollama serve & sleep 5 && ollama pull phi && streamlit run app.py --server.port=8501 --server.address=0.0.0.0 --logger.level=debug"