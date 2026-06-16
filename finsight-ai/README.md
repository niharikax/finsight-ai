# FinSight AI

FinSight AI is a financial research application that helps users analyse annual reports and compare public companies.

The project combines retrieval augmented generation (RAG), vector search and large language models to answer questions directly from uploaded company reports. It also includes a stock comparison tool that retrieves live market data using Yahoo Finance.

## Why I Built This

I wanted to better understand how modern AI systems retrieve information from documents instead of relying entirely on a model's training data.

Annual reports are often hundreds of pages long and contain valuable information about a company's financial performance, risks and strategy. FinSight AI was built to make exploring those documents faster and more interactive.

The project also gave me practical experience working with embeddings, vector databases, semantic search and LLM integrations.

---

## Features

### Annual Report Analysis

* Upload annual report PDFs
* Extract and process report text
* Ask questions about the report
* Retrieve relevant sections using semantic search
* Generate answers grounded in the document

### Stock Comparison

* Compare public companies using ticker symbols
* Retrieve live market data from Yahoo Finance
* View stock price
* View market capitalisation
* View P/E ratio
* View sector information

---

## How It Works

### 1. Document Processing

The user uploads a PDF annual report.

The application extracts the text using PyPDF and prepares it for further processing.

### 2. Chunking

The report text is split into smaller chunks.

Breaking the document into smaller sections makes retrieval more efficient and improves search quality.

### 3. Embeddings

Each chunk is converted into a vector embedding using the Sentence Transformers model `all-MiniLM-L6-v2`.

These embeddings capture the meaning of the text and allow semantic search.

### 4. Vector Search

The embeddings are stored in ChromaDB.

When a user asks a question, the question is converted into an embedding and compared against the stored document embeddings.

The most relevant chunks are retrieved and used as context.

### 5. Answer Generation

The retrieved chunks are sent to a Llama model hosted on Groq.

The model generates an answer using the retrieved context rather than relying on its own knowledge.

### 6. Stock Analysis

The stock comparison module uses Yahoo Finance data through the `yfinance` library.

Users can compare companies using key financial metrics.

---

## Architecture

```text
PDF Upload
    │
    ▼
Text Extraction
    │
    ▼
Chunking
    │
    ▼
Embeddings
    │
    ▼
ChromaDB
    │
    ▼
Similarity Search
    │
    ▼
Relevant Chunks
    │
    ▼
Groq LLM
    │
    ▼
Answer
```

---

## Tech Stack

### Frontend

* Streamlit

### Document Processing

* PyPDF

### Embeddings

* Sentence Transformers
* all-MiniLM-L6-v2

### Vector Database

* ChromaDB

### LLM

* Groq
* Llama 3.1

### Financial Data

* yfinance

### Language

* Python

---

## Project Structure

```text
finsight-ai/
│
├── app.py
│
├── agents/
│   ├── rag_agent.py
│   └── stock_agent.py
│
├── utils/
│   ├── pdf_loader.py
│   ├── text_chunker.py
│   └── vector_store.py
│
├── screenshots/
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/niharikax/finsight-ai.git
cd finsight-ai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

---

## Future Work

* Research agent for company research
* Evaluation agent for answer assessment
* Support for multiple reports
* Financial summary generation
* Streamlit Cloud deployment
* Automated testing

---

## What I Learned

This project helped me gain experience with:

* Retrieval augmented generation
* Embedding models
* Vector databases
* Semantic search
* Prompt engineering
* LLM APIs
* Financial data APIs
* Streamlit development

---

## Author

Niharika

Built as a personal project to learn more about financial AI systems, retrieval pipelines and LLM applications.
