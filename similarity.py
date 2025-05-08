from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util
import os

app = FastAPI()

# Dynamically get model name (or use default)
model_name = os.getenv("MODEL_NAME", "all-MiniLM-L6-v2")
model_path = os.path.join(os.path.dirname(__file__), "models", model_name)

# Try loading the local model
try:
    print(f"Loading model from: {model_path}")
    model = SentenceTransformer(model_path)
    print("✅ Model loaded successfully.")
except Exception as e:
    print(f"❌ Failed to load model: {e}")
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

    if not data.a or not data.b:
        raise HTTPException(status_code=400, detail="Both 'a' and 'b' are required")

    embeddings = model.encode([data.a, data.b], convert_to_tensor=True)
    similarity = float(util.cos_sim(embeddings[0], embeddings[1]))

    return {"similarity": similarity}

# Vercel support
handler = app