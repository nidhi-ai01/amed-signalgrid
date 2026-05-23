# AMED SignalGrid Backend

<p align="center">
  <img src="backend/static/logo.png" width="250"/>
</p>

AI-powered FastAPI backend for the AMED SignalGrid platform.

---

# Features

- FastAPI backend architecture
- PostgreSQL database integration
- SQLAlchemy ORM
- Swagger/OpenAPI documentation
- Article CRUD APIs
- Static asset support
- Modular backend structure

---

# Tech Stack

- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy
- Uvicorn
- Pydantic

---

# Project Structure

```bash
backend/
│
├── app/
│   ├── ingestion/
│   ├── models/
│   ├── nlp/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── workers/
│   ├── config.py
│   ├── database.py
│   ├── dependencies.py
│   └── main.py
│
├── static/
│   └── logo.png
│
├── requirements.txt
└── .env
```

---

# Run Locally

## 1. Clone Repository

```bash
git clone https://github.com/nidhi-ai01/amed-signalgrid.git
cd amed-signalgrid/backend
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Start Backend Server

```bash
uvicorn app.main:app --reload
```

---

# API Documentation

Swagger Docs:

```bash
http://127.0.0.1:8000/docs
```

---

# Milestone 1 Completed

## Backend Foundation
- FastAPI initialized
- PostgreSQL connected
- Database models created
- CRUD APIs working
- Swagger documentation enabled
- Static asset serving enabled

---

# Upcoming Milestone 2

- PDF ingestion pipeline
- NLP preprocessing
- Text chunking
- Embedding generation
- Semantic search
- Vector database integration

---

# Author

Developed by Nidhi