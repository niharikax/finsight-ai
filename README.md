# FinSight AI

FinSight AI is a multi-agent financial research platform that combines retrieval augmented generation (RAG), vector search, large language models and financial market data.

The platform helps users analyse annual reports, compare public companies, evaluate AI-generated answers and perform broader company research through specialised AI agents.

---
## Live Demo

[Open FinSight AI](https://financialinsightai.streamlit.app)


## Features

### Annual Report Analysis

- Upload annual report PDFs
- Extract and process report text
- Ask questions about report contents
- Retrieve relevant sections using semantic search
- Generate source-grounded answers using RAG
- Quick analysis buttons:
  - Summarise Report
  - Find Key Risks
  - Revenue Drivers
  - Future Outlook
- Download generated answers

### Stock Analysis

- Compare companies using ticker symbols
- Retrieve live market data through Yahoo Finance
- View:
  - Stock Price
  - Market Capitalisation
  - P/E Ratio
  - Sector
  - 52 Week High
  - 52 Week Low
  - Profit Margin
  - Dividend Yield
  - Beta
  - Analyst Recommendation

### Evaluation Agent

- Evaluates generated answers
- Scores:
  - Faithfulness
  - Relevance
  - Completeness
  - Clarity
- Provides feedback on answer quality

### Research Agent

- Generates company research summaries
- Analyses:
  - Business Model
  - Growth Drivers
  - Risks
  - Competitive Position
  - Future Outlook
- Download research summaries

---

## Architecture

### RAG Agent

PDF Upload

↓

Text Extraction

↓

Chunking

↓

Embeddings

↓

ChromaDB

↓

Similarity Search

↓

Relevant Chunks

↓

Groq LLM

↓

Answer

### Evaluation Agent

Question

+

Answer

+

Retrieved Context

↓

Evaluation Agent

↓

Quality Scores

### Stock Agent

Ticker Symbol

↓

Yahoo Finance

↓

Financial Metrics

↓

Company Comparison

### Research Agent

Research Question

↓

Groq LLM

↓

Structured Company Analysis

---

## Tech Stack

### Frontend

- Streamlit

### Document Processing

- PyPDF

### Embeddings

- Sentence Transformers
- all-MiniLM-L6-v2

### Vector Database

- ChromaDB

### LLM

- Groq
- Llama 3.1

### Financial Data

- yfinance

### Language

- Python

---

## Project Structure

```text
finsight-ai/
│
├── app.py
│
├── agents/
│   ├── rag_agent.py
│   ├── stock_agent.py
│   ├── evaluator_agent.py
│   └── research_agent.py
│
├── utils/
│   ├── pdf_loader.py
│   ├── text_chunker.py
│   └── vector_store.py
│
├── screenshots/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How It Works

### RAG Pipeline

When a PDF is uploaded, the application extracts the text, splits it into smaller chunks and converts those chunks into embeddings.

The embeddings are stored in ChromaDB. When a user asks a question, the application retrieves the most relevant chunks and sends them to a Groq-hosted Llama model to generate a grounded answer.

### Evaluation Pipeline

Generated answers are passed to an Evaluation Agent which scores them for faithfulness, relevance, completeness and clarity.

### Stock Analysis Pipeline

The Stock Agent retrieves live market data from Yahoo Finance and displays financial metrics for company comparison.

### Research Pipeline

The Research Agent answers broader company research questions and produces structured financial research summaries.

---

## Future Improvements

- Multi-document analysis
- Financial health scoring
- Analyst report generation
- Interactive stock charts
- Live web search integration
- Streamlit Cloud deployment

---

## What I Learned

This project helped me gain practical experience with:

- Retrieval augmented generation
- Embedding models
- Vector databases
- Semantic search
- Prompt engineering
- LLM evaluation
- Financial data APIs
- Streamlit development
- Multi-agent system design

---

## Author

Niharika

Built as a personal project to explore financial AI systems, retrieval pipelines and multi-agent architectures.