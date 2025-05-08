from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util
import os

app = FastAPI()

# Load model from local files with error handling
try:
    model_path = os.path.join(os.path.dirname(__file__), "models", "all-MiniLM-L6-v2")
    model = SentenceTransformer(model_path)
except Exception as e:
    print(f"Model load error: {e}")
    model = None

class SimilarityRequest(BaseModel):
    a: str
    b: str

@app.get("/")
async def health_check():
    return {"status": "OK", "model_loaded": model is not None}

@app.post("/similarity")
async def get_similarity(data: SimilarityRequest):
    if not model:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    embeddings = model.encode([data.a, data.b], convert_to_tensor=True)
    similarity = float(util.cos_sim(embeddings[0], embeddings[1]))
    return {"similarity": similarity}

# Vercel requirement
handler = app