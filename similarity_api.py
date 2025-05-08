from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util

app = FastAPI()
model = SentenceTransformer("all-MiniLM-L6-v2")

class SimilarityRequest(BaseModel):
    a: str
    b: str

@app.post("/similarity")
def get_similarity(data: SimilarityRequest):
    if not data.a or not data.b:
        raise HTTPException(status_code=400, detail="Both 'a' and 'b' are required")

    embeddings = model.encode([data.a, data.b], convert_to_tensor=True)
    similarity = float(util.cos_sim(embeddings[0], embeddings[1]))

    return {"similarity": similarity}
