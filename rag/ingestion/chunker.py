from langchain_text_splitters import RecursiveCharacterTextSplitter
import config
class TextChunker:
    def __init__(self, chunk_size: int = config.CHUNK_SIZE, chunk_overlap: int = config.CHUNK_OVERLAP, is_separator_regex: bool = False):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.is_separator_regex = is_separator_regex
        self.text_splitter = RecursiveCharacterTextSplitter(
            separators=[
                "\n\n", "\n", " ", ".", ",", "\u200b",
                "\uff0c", "\u3001", "\uff0e", "\u3002", "",
            ], chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap,
                length_function=len, is_separator_regex=self.is_separator_regex)


    def split_document(self, document):
        return self.text_splitter.split_text(document)