# 🔬 ResearchLens — AI Research Paper Assistant


## 📌 Overview

**ResearchLens** is an AI-powered research assistant that allows you to upload multiple research papers and ask questions about them using natural language.

It uses **Retrieval-Augmented Generation (RAG)** to find relevant information from your documents before generating an answer, with source citations for easier verification.

### ✨ Features

- 📄 Upload multiple research paper PDFs
- 🧠 RAG-based question answering
- 🔍 Hybrid search using **Dense + BM25**
- ⚡ Reciprocal Rank Fusion (RRF)
- 📚 Source citations with page numbers
- 🤖 Gemini, Ollama & Hugging Face support
- 🧩 One-column and two-column PDF support
- 🖥️ Clean and interactive Streamlit UI

---

## 🏗️ Architecture

```text
PDF Upload
    ↓
PDF Text Extraction
    ↓
Section-Aware Chunking
    ↓
Dense + BM25 Indexing
    ↓
Qdrant Vector Database
    ↓
Hybrid Retrieval + RRF
    ↓
LLM
    ↓
Answer + Source Citations
```
---

```text
🛠️ Tech Stack
Technology	   Purpose
Python	     Core application
Streamlit	   Web interface
LangChain	   RAG pipeline
Qdrant	     Vector database
FastEmbed	   Embeddings
BM25	       Keyword retrieval
Gemini	     LLM
Ollama	     Local LLM
Hugging Face LLM support
Docker	     Qdrant deployment
```

---
```
## Project Structure
.
├── app.py
├── requirements.txt
├── docker-compose.yaml
├── html_template.py
├── assets/
├── data/
├── qdrant_data/
├── notebooks/
└── src/
    ├── chunk_splitter.py
    ├── embeddings.py
    ├── llm.py
    ├── pdf_loader.py
    ├── rag.py
    └── vector_db.py
```
## Installation

Clone the repository:

```bash
git clone https://github.com/Sayanijana23/AI-Research-Lens.git
cd AI-Research-Lens
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

```bash
# On Windows:
.venv\Scripts\activate

# On macOS or Linux:
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file for Gemini and Hugging Face support:

```env
GOOGLE_API_KEY=your_google_api_key_here

HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token_here
```

## Run Qdrant

Make sure **Docker Desktop** is installed and running.

Start Qdrant with Docker Compose:

```bash
docker compose up -d
```

Check that Qdrant is running:

```bash
docker compose ps
```

Stop Qdrant with:

```bash
docker compose down
```

## Run Ollama

Install Ollama:

https://ollama.com/download

Pull the required model:

```bash
ollama pull llama3.2
```

Check installed models:

```bash
ollama list
```

## Run the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

Open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```



## Limitations

- Answer quality depends on PDF text extraction quality.
- The system only answers from uploaded documents and does not use external knowledge.
- Large PDFs or many uploaded files can increase processing time.
- Scanned PDFs may require OCR before they can be processed accurately.


## Demo

<img width="1600" height="757" alt="demo_1" src="https://github.com/user-attachments/assets/e815475f-b64a-4451-baab-9a8fdaff3780" />
<img width="1600" height="764" alt="demo_2" src="https://github.com/user-attachments/assets/b124ccb7-6007-44bd-923d-25b2117f267e" />
<img width="1600" height="740" alt="demo_3" src="https://github.com/user-attachments/assets/40ab9663-93a1-4571-ba56-cfbcd3de1afd" />




