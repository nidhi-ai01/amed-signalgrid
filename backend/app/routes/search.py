from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.document import Document
from app.ingestion.embedding import generate_embedding
import numpy as np
import ast

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


@router.get("/semantic-search")
def semantic_search(
    query: str,
    db: Session = Depends(get_db)
):

    query_embedding = generate_embedding(query)

    documents = db.query(Document).all()

    results = []

    for doc in documents:

        try:
            stored_embedding = ast.literal_eval(doc.embedding)

            similarity = cosine_similarity(
                query_embedding,
                stored_embedding
            )

            results.append({
                "document_id": doc.id,
                "filename": doc.filename,
                "similarity_score": float(similarity),
                "sentiment": doc.sentiment_label,
                "preview": doc.extracted_text[:300]
            })

        except Exception:
            continue

    results = sorted(
        results,
        key=lambda x: x["similarity_score"],
        reverse=True
    )

    return results[:5]