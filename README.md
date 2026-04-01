# Terms of Service Risk Analyzer (RAG-based)

## Overview

Most users accept Terms of Service (ToS) without reading or understanding the risks.

This project is a **Retrieval-Augmented Generation (RAG)** application that allows users to:

* Upload Terms of Service documents
* Ask natural language questions
* Receive grounded, context-based answers

Aim of this is ease and simplicity of use. It is running offline without a need for an API key.

---

## Demo Features

### 1. Document Q&A

* Ask questions like:

  * "Can they terminate my account?"
  * "What data do they collect?"
* Answers are generated **only from the uploaded document**

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
* Ollama (LLM)
* HuggingFace (Encodings)
* Chroma (vector database)

---

## Design Decisions

### 1. Local LLMs over API

This decision was made for learning purposes. I did not want to pay for experimentation. 
Therefore this system is "offline" and the models running are not exposed to internet

### 2. Simplicity over overengineering

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


## How to Run

### 1. Via Docker

Just type: 

```
docker-compose up --build
```

This will start the application. You can navigate to http://localhost:8501 

### 2. Locally

First start ollama. It should be running under http://localhost:11434
Then you can just run the command:
```
streamlit run app.py
```
and frontend will send requests to ollama backend

---

## Limitations

* No advanced reranking or hybrid search
* Model is too small and larger models causes crashes
* Not optimized for large-scale datasets

## Small Local Models

The application is using phi, which is a small Ollama model.This is due to restrictions of my own hardware and 
not wanting to pay for model interactions (since this is a learning attempt). 

Even with a small model, average response time is around 40 seconds and as expected, results sometimes vary. This 
is expected since the aim is to create the system. 

## No Evaluation (yet)

Due to using a small model locally, this also limited my ability to use evaluation frameworks such as Ragas. I have tried
adding it however it proved too much for my computer to handle. Even with small number of iterations (generating a test
dataset of 10 question/answer pairs, I had to kill the instance due to CPU usage). 

I tried to implement it myself by asking LLM to evaluate it based on responses I expected, however that also yielded
the same results. 

Eventually I will probably be able to use an external GPU or end up paying for an LLM but for the purposes of this 
project, I believe this will be enough for now.

---

## Future Improvements

* better evaluation metrics
* hybrid search (keyword + semantic)
* deployment as a web service (API)
* risk analysis

---

## Key Takeaways

This project demonstrates:

* practical implementation of RAG systems
* ability to design under constraints
* understanding of LLM limitations (hallucination control via retrieval)

---

