# AMED SignalGrid Backend

FastAPI backend for AMED SignalGrid platform.

## Features
- FastAPI backend
- PostgreSQL integration
- SQLAlchemy ORM
- Swagger API Docs
- Article APIs
- Static asset support

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload

API Docs

http://127.0.0.1:8000/docs


Then commit and push again.

---

# 2. Clean API Architecture

Right now APIs are inside `main.py`.

Next proper step:
move routes into:

```txt id="zfcj4f"
app/routes/