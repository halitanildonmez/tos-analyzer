from rag.ingestion.vector_db import VectorDB
from rag.ingestion.text_embedder import TextEmbedder
from rag.exceptions import QueryError, CollectionEmptyError, EmbeddingError, LLMError
from rag.query.agent import  prompt_agent, query_ollama_http

class QueryPipeline:
    def __init__(self):
        self.db = VectorDB()
        self.text_embedder = TextEmbedder()

    def verify_query(self, query):
        if not query.strip() or query.strip() == "":
            raise QueryError("Empty query")

        if self.db.get_collection_count() == 0:
            raise CollectionEmptyError("Database is empty")

    def get_context(self, query_embedded):
        try:
            results = self.db.query_collection(query_embedded)
            relevant_chunks = results["documents"][0]
            return "\n\n".join(relevant_chunks)
        except Exception as e:
            raise QueryError(f"failed to retrieve context {e}") from e

    def prompt_agent(self, query, context) -> str:
        try:
            response = prompt_agent(query, context)
            return response.response
        except LLMError as llm_error:
            print(llm_error)
            raise llm_error
        except Exception as e:
            raise LLMError(f"Failed to prompt the llm agent {e}") from e

    def query(self, query) -> str:
        self.verify_query(query)

        try:
            query_embedded = self.text_embedder.encode_document([query]).tolist()
        except Exception as e:
            raise EmbeddingError(f"failed to encode query {e}") from e

        context = self.get_context(query_embedded)

        return self.prompt_agent(query, context)
