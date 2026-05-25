from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database import engine, Base

from app.routes.article import router as article_router
from app.routes.upload import router as upload_router
from app.models.document import Document
from app.routes.search import router as search_router
from app.routes.chat import router as chat_router
from app.models.chunk import Chunk

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="AMED SignalGrid API",
    version="1.0.0"
)

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(article_router)
app.include_router(upload_router)
app.include_router(search_router)
app.include_router(chat_router)

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "AMED SignalGrid Backend Running"
    }

# Health check endpoint
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }