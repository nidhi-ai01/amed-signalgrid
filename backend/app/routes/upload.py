import os

from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.ingestion.pdf_reader import extract_text_from_pdf
from app.ingestion.embedding import generate_embedding
from app.ingestion.chunker import chunk_text

from app.models.document import Document
from app.models.chunk import Chunk

from app.nlp.sentiment import analyze_sentiment

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/upload-pdf")
async def upload_pdf(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    extracted_text = extract_text_from_pdf(file_path)

    chunks = chunk_text(extracted_text)

    sentiment = analyze_sentiment(extracted_text)

    embedding = generate_embedding(extracted_text[:1000])

    new_document = Document(
        filename=file.filename,
        extracted_text=extracted_text,
        sentiment_label=sentiment["label"],
        sentiment_score=str(sentiment["score"]),
        embedding=str(embedding)
    )

    db.add(new_document)
    db.commit()
    db.refresh(new_document)

    for chunk in chunks:

        chunk_embedding = generate_embedding(chunk)

        new_chunk = Chunk(
            document_id=new_document.id,
            chunk_text=chunk,
            embedding=str(chunk_embedding)
        )

        db.add(new_chunk)

    db.commit()

    return {
        "document_id": new_document.id,
        "filename": new_document.filename,
        "sentiment": sentiment,
        "chunks_created": len(chunks),
        "text_preview": extracted_text[:1000]
    }