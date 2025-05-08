from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util
import os

app = FastAPI()
model = SentenceTransformer("all-MiniLM-L6-v2")

# Path to the favicon.ico file
favicon_path = os.path.join(os.path.dirname(__file__), "static", "favicon.ico")

# Mount the "static" directory
app.mount("/static", StaticFiles(directory="static"), name="static")

class SimilarityRequest(BaseModel):
    a: str
    b: str

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

@app.post("/similarity")
async def  get_similarity(data: SimilarityRequest):
    if not data.a or not data.b:
        raise HTTPException(status_code=400, detail="Both 'a' and 'b' are required")

    embeddings = model.encode([data.a, data.b], convert_to_tensor=True)
    similarity = float(util.cos_sim(embeddings[0], embeddings[1]))
    return {"similarity": similarity}
