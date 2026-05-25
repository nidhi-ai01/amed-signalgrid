from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from transformers import pipeline

from app.database import SessionLocal
from app.models.document import Document
from app.ingestion.embedding import generate_embedding
from app.models.chunk import Chunk

import numpy as np
import ast

router = APIRouter()

generator = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)



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


@router.get("/chat")
def chat(
    query: str,
    db: Session = Depends(get_db)
):

    query_embedding = generate_embedding(query)

    chunks = db.query(Chunk).all()
    if not chunks:
        return {
        "answer": "No chunks found"
    }

    scored_docs = []

    for chunk in chunks:
        try:
            stored_embedding = ast.literal_eval(chunk.embedding)

            similarity = cosine_similarity(
                query_embedding,
                stored_embedding
            )

            scored_docs.append({
                "chunk": chunk,
                "score": similarity
            })

        except Exception:
            continue

    if not scored_docs:
        return {
            "answer": "No relevant document found"
        }

    sorted_docs = sorted(
        scored_docs,
        key=lambda x: x["score"],
        reverse=True
    )

    top_docs = sorted_docs[:3]

    contexts = "\n\n".join([
        item["chunk"].chunk_text
        for item in top_docs
    ])

    prompt = f"""
Context:
{contexts}

Question:
{query}

Answer:
"""

    result = generator(
    prompt,
    max_new_tokens=120
)
    
    return {
        "question": query,
        "matched_chunks": [
            {
                "chunk_id": item["chunk"].id,
                "similarity_score": float(item["score"])
            }
            for item in top_docs
        ],
        "answer": result[0]["generated_text"].strip()    }