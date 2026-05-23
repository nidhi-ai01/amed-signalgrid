from fastapi import FastAPI
from app.database import engine, Base
from app.models.article import Article
from sqlalchemy.orm import Session
from fastapi import Depends
from app.dependencies import get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AMED SignalGrid API",
    version="1.0.0"
)

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