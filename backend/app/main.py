from fastapi import FastAPI

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