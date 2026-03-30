class RAGError(Exception):
    """Base exception for all RAG errors."""

class IngestError(RAGError):
    """Raised when ingestion fails (bad PDF, chunking, embedding, or DB write)."""

class QueryError(RAGError):
    """Raised when a query fails (embedding, retrieval, or LLM call)."""

class EmbeddingError(RAGError):
    """Raised when the embedding model fails."""

class LLMError(RAGError):
    """Raised when the LLM fails after all retries."""

class CollectionEmptyError(QueryError):
    """Raised when the collection has no documents yet."""