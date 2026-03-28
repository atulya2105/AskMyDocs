# AskMyDocs – AI-Powered RAG Chatbot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-green" />
  <img src="https://img.shields.io/badge/Streamlit-UI-orange" />
  <img src="https://img.shields.io/badge/ChromaDB-VectorDB-purple" />
  <img src="https://img.shields.io/badge/RAG-Agent-red" />
</p>

---

##  Overview

AskMyDocs is an AI-powered chatbot that lets users upload PDFs and ask questions. It uses a **Retrieval-Augmented Generation (RAG)** pipeline with **agent fallback (web search)** and **chat memory** to deliver accurate, context-aware answers.

---

##  Key Features

*  Upload & process PDFs
*  Semantic search via embeddings
*  Context-grounded LLM answers
*  Web search fallback (Agent behavior)
*  Conversational memory (follow-ups)
*  FastAPI backend + Streamlit UI

---

##  Architecture

###  End-to-End Flow

```
PDF → Chunk → Embed → Store (Vector DB)

User Query → Embed → Similarity Search → Context

[Agent]
if context weak → Web Search

(Context + History) → LLM → Answer
```

###  Components

```
ui/app.py            → Streamlit UI
api/main.py         → FastAPI routes
app/rag_pipeline.py → Orchestration (agent + memory)
app/vector_store.py → store_chunks(), query_chunks()
app/chunker.py      → text splitting
app/llm.py          → LLM calls
app/tools/web_search.py → external search
```

---

## How It Works

### 1) Ingestion

* Extract text from PDF
* Split into chunks (with overlap)
* Create embeddings
* Store in ChromaDB

### 2) Query

* Embed user question
* Retrieve top-K similar chunks
* If weak context → call web search
* Combine context + chat history
* Generate answer via LLM

---

##  Agent Logic

```python

---

##  Memory

* Stores last N turns
* Appended to prompt for continuity
* Enables follow-up queries

---

##  Tech Stack

* FastAPI
* Streamlit
* ChromaDB
* Sentence-Transformers
* LLM API (Groq / OpenAI)

---

## Environment Variables

Create a `.env` file:

```
API_KEY=your_llm_api_key
MODEL_NAME=your_model
```

---

##  Setup

### 1. Clone

```
git clone <your-repo-url>
cd AskMyDocs
```

### 2. Install

```
pip install -r requirements.txt
```

### 3. Run Backend

```
uvicorn api.main:app --reload
```

### 4. Run UI

```
streamlit run ui/app.py
```

---

## 🔌 API Endpoints

### Ask Question

```
GET /ask?question=...
```

### Upload PDF

```
POST /upload
```

---

##  Example

**Q:** What is Retrieval-Augmented Generation?

**A:** Combines LLM with external knowledge retrieval to improve accuracy and reduce hallucination.

---


---



## Future Improvements

* Multi-user session memory
* Multi-PDF filtering via metadata
* Re-ranking (improve retrieval quality)
* Streaming responses
* Cloud deployment (AWS / Render)

---

##  Author

**Arvind Pandey**

