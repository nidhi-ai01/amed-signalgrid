from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.article import Article
from app.schemas.article import ArticleCreate

router = APIRouter()

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create article
@router.post("/articles")
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    new_article = Article(
        title=article.title,
        content=article.content,
        source=article.source
    )

    db.add(new_article)
    db.commit()
    db.refresh(new_article)

    return new_article

# Get all articles
@router.get("/articles")
def get_articles(db: Session = Depends(get_db)):
    articles = db.query(Article).all()
    return articles