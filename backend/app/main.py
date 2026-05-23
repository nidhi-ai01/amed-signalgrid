from fastapi import FastAPI
from app.database import engine, Base
from app.models.article import Article
from sqlalchemy.orm import Session
from fastapi import Depends
from app.dependencies import get_db
from fastapi.staticfiles import StaticFiles

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AMED SignalGrid API",
    description="AI-powered backend services for SignalGrid platform",
    version="1.0.0",
    contact={
        "name": "AMED SignalGrid Team"
    }
)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return {
        "message": "AMED SignalGrid Backend Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/articles")
def create_article(
    title: str,
    content: str,
    source: str = None,
    db: Session = Depends(get_db)
):
    article = Article(
        title=title,
        content=content,
        source=source
    )

    db.add(article)
    db.commit()
    db.refresh(article)

    return article

@app.get("/articles")
def get_articles(db: Session = Depends(get_db)):
    articles = db.query(Article).all()
    return articles