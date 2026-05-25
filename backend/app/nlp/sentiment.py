from transformers import pipeline

sentiment_pipeline = pipeline(
    "sentiment-analysis"
)

def analyze_sentiment(text: str):

    if len(text) > 1000:
        text = text[:1000]

    result = sentiment_pipeline(text)

    return result[0]