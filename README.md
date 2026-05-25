# AMED SignalGrid Backend

<p align="center">
  <img src="backend/static/logo.png" width="250" alt="AMED SignalGrid Logo"/>
</p>

<p align="center">
  AI-Powered Institutional Document Intelligence Backend
</p>

---

# Overview

AMED SignalGrid is an AI-powered backend platform designed for intelligent document ingestion, semantic retrieval, contextual AI querying, and institutional knowledge processing.

The backend is built using FastAPI and PostgreSQL with NLP and embedding pipelines that enable semantic understanding of uploaded documents.

This system forms the foundation for scalable institutional intelligence infrastructure capable of powering AI-assisted research, analytics, educational systems, and operational knowledge retrieval.

---

# Core Features

## Backend Infrastructure
- FastAPI backend architecture
- Modular backend structure
- PostgreSQL database integration
- SQLAlchemy ORM support
- REST API architecture
- Swagger/OpenAPI documentation
- Static asset serving

---

## AI Document Intelligence
- PDF upload pipeline
- PDF text extraction
- NLP preprocessing
- Intelligent text chunking
- Embedding generation
- Semantic similarity search
- AI contextual retrieval
- Multi-document querying
- Context-aware AI chat system
- Sentiment analysis pipeline
- Chunk-level retrieval scoring

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Core backend language |
| FastAPI | API framework |
| PostgreSQL | Relational database |
| SQLAlchemy | ORM |
| Transformers | NLP and generation |
| Sentence Transformers | Embedding generation |
| NumPy | Similarity calculations |
| Uvicorn | ASGI server |
| Pydantic | Data validation |

---

# Project Structure

```bash
backend/
│
├── app/
│   │
│   ├── ingestion/
│   │   ├── chunker.py
│   │   ├── embedding.py
│   │   └── pdf_reader.py
│   │
│   ├── models/
│   │   ├── article.py
│   │   ├── chunk.py
│   │   └── document.py
│   │
│   ├── nlp/
│   │   └── sentiment.py
│   │
│   ├── routes/
│   │   ├── article.py
│   │   ├── chat.py
│   │   ├── search.py
│   │   └── upload.py
│   │
│   ├── schemas/
│   ├── services/
│   ├── workers/
│   │
│   ├── config.py
│   ├── database.py
│   ├── dependencies.py
│   └── main.py
│
├── static/
│   └── logo.png
│
├── uploads/
│
├── requirements.txt
├── .env
└── README.md
```

---

# System Workflow

## 1. Document Upload
Users upload PDF documents through the API.

## 2. Text Extraction
The system extracts raw text from uploaded PDFs.

## 3. NLP Processing
Extracted text is preprocessed and segmented into semantic chunks.

## 4. Embedding Generation
Each chunk is converted into vector embeddings using transformer models.

## 5. Semantic Retrieval
User queries are transformed into embeddings and matched against stored vectors using cosine similarity.

## 6. AI Contextual Response
Relevant chunks are retrieved and passed into the language model for contextual AI response generation.

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/nidhi-ai01/amed-signalgrid.git
```

---

## 2. Navigate to Backend

```bash
cd amed-signalgrid/backend
```

---

## 3. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Configure Environment Variables

Create a `.env` file inside the backend directory.

Example:

```env
DATABASE_URL=postgresql://postgres:password@localhost/amed_signalgrid
```

---

## 6. Run Backend Server

```bash
uvicorn app.main:app --reload
```

---

# API Documentation

After starting the server:

## Swagger UI

```bash
http://127.0.0.1:8000/docs
```

---

## ReDoc

```bash
http://127.0.0.1:8000/redoc
```

---

# Available API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/upload-pdf` | POST | Upload and process PDF |
| `/semantic-search` | GET | Perform semantic retrieval |
| `/chat` | GET | Context-aware AI querying |
| `/articles` | CRUD | Article management APIs |

---

# Milestone 1 Completed

## Backend Foundation
- FastAPI project initialized
- PostgreSQL database connected
- SQLAlchemy models implemented
- CRUD APIs developed
- Swagger documentation enabled
- Static asset support configured
- Modular project structure established

---

# Milestone 2 Completed

## AI Intelligence Pipeline
- PDF ingestion pipeline implemented
- Text extraction workflow completed
- NLP preprocessing integrated
- Chunk generation pipeline completed
- Embedding generation system implemented
- Semantic vector retrieval operational
- AI contextual response generation implemented
- Multi-document retrieval working
- Sentiment analysis pipeline integrated
- Chunk-level similarity scoring operational

---

# Current Capabilities

The backend currently supports:

- Intelligent PDF processing
- Semantic document search
- AI contextual querying
- Multi-document knowledge retrieval
- Sentiment analysis
- Chunk-based embedding retrieval
- Transformer-based NLP pipelines
- AI-assisted document intelligence workflows

---

# Future Roadmap

## Planned Enhancements
- Vector database optimization
- Authentication and authorization
- Cloud deployment infrastructure
- Streaming AI responses
- Dashboard frontend integration
- Institution-level analytics
- Advanced Retrieval-Augmented Generation (RAG)
- Distributed processing pipelines
- Real-time collaboration support

---

# Development Notes

This project is currently in active MVP development and serves as the foundational backend infrastructure for the broader AMED SignalGrid institutional intelligence ecosystem.

---

# Author

Developed by Nidhi

---

# License

This project is proprietary and intended for AMED SignalGrid platform development.
