import pymupdf

def pdf_to_text_in_mem(pdf_document) -> str:
    with pymupdf.open(stream=pdf_document.read(), filetype="pdf") as pdf:
        text = ""
        for page in pdf_document:
            text += page.get_text("text")  # plain text
        return text