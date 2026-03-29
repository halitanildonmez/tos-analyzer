FROM python:3.11-slim

WORKDIR /app

# System deps for pymupdf
RUN apt-get update && apt-get install -y \
    libmupdf-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Persistent storage for ChromaDB and processed files
VOLUME ["/app/db", "/app/data"]

ENTRYPOINT ["python", "-m", "rag"]