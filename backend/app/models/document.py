from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String, nullable=False)

    extracted_text = Column(Text, nullable=False)

    sentiment_label = Column(String)

    sentiment_score = Column(String)

    embedding = Column(Text)