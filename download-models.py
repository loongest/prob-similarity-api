from sentence_transformers import SentenceTransformer
import os

# Create a directory to store the model
model_dir = "models/all-MiniLM-L6-v2"
os.makedirs(model_dir, exist_ok=True)

# Download and save the model
model = SentenceTransformer("all-MiniLM-L6-v2")
model.save(model_dir)

print(f"Model saved to {model_dir}")