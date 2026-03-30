from sentence_transformers import SentenceTransformer

class TextEmbedder:
    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    def encode_document(self, document):
        return self.model.encode(document)
