import os
from pathlib import Path
import logging

logging.getLogger().setLevel(logging.DEBUG)

BASE_DIR = Path(__file__).parent
RESOURCES_DIR = BASE_DIR / "resources"
RESOURCES_DIR.mkdir(exist_ok=True)

CHROMA_PATH = str(os.getenv("CHROMA_PATH", RESOURCES_DIR / "chroma"))
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "rag-collection")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "phi")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 50))
TOP_K = int(os.getenv("TOP_K", 3))
NUM_RETRIES = int(os.getenv("NUM_RETRIES", 3))
OLLAMA_HOST = str(os.getenv("OLLAMA_HOST", "http://localhost:11434"))