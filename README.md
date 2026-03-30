# Terms of Service Risk Analyzer (RAG-based)

## Overview

Most users accept Terms of Service (ToS) without reading or understanding the risks.

This project is a **Retrieval-Augmented Generation (RAG)** application that allows users to:

* Upload Terms of Service documents
* Ask natural language questions
* Receive grounded, context-based answers
* Generate a structured **risk analysis summary**

The system is designed to demonstrate **practical AI engineering skills under real-world constraints**, focusing on simplicity, reliability, and usability.

---

## Demo Features

### 1. Document Q&A

* Ask questions like:

  * "Can they terminate my account?"
  * "What data do they collect?"
* Answers are generated **only from the uploaded document**

### 2. Risk Analysis (Key Feature)

Automatically analyzes the document and returns:

* Data Collection Risk (Low / Medium / High)
* Account Termination Risk
* Liability Risk
* Arbitration Clause (Yes / No)

This simulates a real-world AI use case: **helping users understand legal risks quickly**

---

## Architecture

User Input → Retriever → Vector Database → Context → LLM → Response

### Pipeline Steps

1. Document ingestion (TXT)
2. Text chunking
3. Embedding generation (API-based)
4. Storage in vector database
5. Semantic retrieval (top-k)
6. Context-aware answer generation

---

## Tech Stack

* Python
* Streamlit (UI)
* OpenAI API (LLM + embeddings)
* Chroma (vector database)

---

## Project Structure

```
tos-rag-analyzer/
│
├── app.py                  # Streamlit UI
├── pipeline.py             # Core RAG pipeline
│
├── rag/
│   ├── loader.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── vectorstore.py
│   ├── retriever.py
│   └── generator.py
│
├── evaluation/
│   └── eval.py             # Lightweight evaluation
│
├── data/                   # Sample ToS documents
├── README.md
├── requirements.txt
└── .env
```

---

## Design Decisions

### 1. API-based models instead of local LLMs

Local models were avoided due to hardware constraints.
Using APIs ensures:

* stability
* faster iteration
* lower setup complexity

### 2. Lightweight evaluation instead of heavy frameworks

Instead of using complex evaluation tools, a simple keyword-based evaluation approach is used to validate outputs.

### 3. Simplicity over overengineering

The system is intentionally minimal:

* no agent frameworks
* no complex orchestration
* focus on clarity and correctness

---

## Evaluation

A lightweight evaluation approach is implemented:

* predefined test questions
* expected keywords
* simple matching-based scoring

This validates:

* answer relevance
* grounding in context

Example:

```
Question: Can they terminate my account?
Expected keywords: ["terminate", "suspend"]
```

---

## Example Output

### Question

"Can they terminate my account?"

### Answer

"The service reserves the right to suspend or terminate accounts in cases of policy violations..."

---

### Risk Analysis

```
Data Collection Risk: High
Account Termination Risk: Medium
Liability Risk: High
Arbitration Clause: Yes
```

---

## How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Add API key

Create a `.env` file:

```
OPENAI_API_KEY=your_key_here
```

### 3. Run the app

```
streamlit run app.py
```

---

## Limitations

* Works best with clean text (TXT input)
* No advanced reranking or hybrid search
* Evaluation is heuristic-based (not exhaustive)
* Not optimized for large-scale datasets

---

## Future Improvements

* PDF parsing improvements
* citation highlighting in answers
* better evaluation metrics
* hybrid search (keyword + semantic)
* deployment as a web service (API)

---

## Key Takeaways

This project demonstrates:

* practical implementation of RAG systems
* ability to design under constraints
* product-oriented thinking (risk analysis feature)
* understanding of LLM limitations (hallucination control via retrieval)

---

