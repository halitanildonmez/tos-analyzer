import config
import chromadb

class VectorDB:
    def __init__(self):
        self.chroma_client = chromadb.PersistentClient(path=config.CHROMA_PATH)
        self.collection = self.chroma_client.get_or_create_collection(name=config.COLLECTION_NAME)

    def add_to_collection(self, chunks, embeddings, ids):
        self.collection.upsert(
            ids=ids,
            embeddings=embeddings,
            documents=chunks
        )

    def get_collection_count(self):
        return self.collection.count()

    def query_collection(self, embeddings, n_results=config.TOP_K):
        return self.collection.query(query_embeddings=embeddings, n_results=n_results)

    def clean_collection(self):
        self.chroma_client.delete_collection(self.collection.name)
        self.collection = self.chroma_client.get_or_create_collection(name=self.collection.name)