import streamlit as st
from rag.ingestion.ingest_pipeline import IngestionPipeline
from rag.query.query_pipeline import QueryPipeline
import logging

logging.getLogger().setLevel(logging.DEBUG)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)

ingestion_pipeline = IngestionPipeline()
query_pipeline = QueryPipeline()

st.set_page_config(page_title="ToS Risk Analyzer")

st.title("Terms of Service Risk Analyzer")

# ---- Upload ----
uploaded_file = st.file_uploader("Upload Terms of Service (pdf)", type=["pdf"])

if uploaded_file:
    ingestion_pipeline.ingest_document(uploaded_file)
    st.success("File uploaded and ingested")

# ---- Q&A ----
st.subheader("Ask a question")

query = st.text_input("Example: Can they terminate my account?")

if query:
    with st.spinner("Processing", show_time=True):
        answer, context = query_pipeline.query(query)
        st.success(answer)
        st.subheader("Citations")
        st.write(context)
