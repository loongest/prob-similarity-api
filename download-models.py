from sentence_transformers import SentenceTransformer
import os

# Create a directory to store the model
# model_name = "all-MiniLM-L6-v2"
model_name = "paraphrase-albert-small-v2"

# model_dir = "models/all-MiniLM-L6-v2"
model_dir = "models/"+model_name
os.makedirs(model_dir, exist_ok=True)

# Download and save the model
# model = SentenceTransformer("all-MiniLM-L6-v2")
model = SentenceTransformer(model_name)
model.save(model_dir)

print(f"Model saved to {model_dir}")