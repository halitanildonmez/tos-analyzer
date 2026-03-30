import logging
import hashlib
import pymupdf
from rag.ingestion.text_embedder import TextEmbedder
from rag.ingestion.chunker import TextChunker
from rag.ingestion.vector_db import VectorDB
from rag.exceptions import IngestError

logger = logging.getLogger(__name__)

def write_pdf_to_text_in_mem(document):
    try:
        with pymupdf.open(stream=document.read(), filetype="pdf") as pdf:
            text = ""
            for page in pdf:
                text += page.get_text("text")  # plain text
            return text
    except Exception as e:
        logger.error(f"Failed to ingest the given document with error: {e}")
        raise IngestError("Failed while ingesting the file") from e

class IngestionPipeline:
    def __init__(self):
        self.text_embedder = TextEmbedder()
        self.chunker = TextChunker()
        self.db = VectorDB()

    def create_chunks_and_embeddings(self, pdf_raw_text):
        try:
            chunks = self.chunker.split_document(pdf_raw_text)
            embeddings = self.text_embedder.encode_document(chunks)
            return pdf_raw_text, chunks, embeddings
        except Exception as e:
            logger.error(f"Failed while ingesting the chunks and embeddings: {e}")
            raise IngestError("Failed to create chunks and embeddings") from e

    def add_to_collection(self, chunks, embeddings):
        try:
            ids = [hashlib.md5(c.encode()).hexdigest() for c in chunks]
            self.db.add_to_collection(chunks, embeddings.tolist(), ids)
            logger.debug(f"Added {len(chunks)} chunks to collection")
        except Exception as e:
            logger.error(f"Failed to save to database: {e}")
            raise IngestError(f"Database write failed: {e}") from e


    def ingest_document(self, pdf_document):
        try:
            pdf_raw_text = write_pdf_to_text_in_mem(pdf_document)
            text, chunks, embeddings = self.create_chunks_and_embeddings(pdf_raw_text)
            self.add_to_collection(chunks, embeddings)
        except IngestError as e:
            logger.error(f"Failed to ingest the chunks and embeddings: {e}")
            raise IngestError("Failed to ingest the chunks and embeddings") from e

