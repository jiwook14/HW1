from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.analyzer import analyze_sentence

# Initialize FastAPI app
app = FastAPI(
    title="News/Sentence Analysis API",
    description="A lightweight API for text classification, keyword extraction, and importance scoring.",
    version="1.0.0"
)

# Request schema
class AnalyzeRequest(BaseModel):
    text: str

# Response schema
class AnalyzeResponse(BaseModel):
    category: str
    keywords: List[str]
    importance_score: int

@app.get("/")
def health_check():
    """
    Health check endpoint to ensure the API is running correctly.
    """
    return {"status": "ok", "message": "API server is running"}

@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest):
    """
    Analyzes a given sentence or news headline and returns its category, 
    key keywords, and an importance score.
    """
    result = analyze_sentence(request.text)
    return AnalyzeResponse(
        category=result["category"],
        keywords=result["keywords"],
        importance_score=result["importance_score"]
    )
