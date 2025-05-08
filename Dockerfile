FROM python:3.10-slim

WORKDIR /app

# Install required system tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all Python files and pre-downloaded model
COPY . .
COPY models/ ./models/

# Tell sentence-transformers to load from local path
ENV TRANSFORMERS_CACHE=/app/models
ENV MODEL_NAME=all-MiniLM-L6-v2

# Expose port
EXPOSE 5001

# Launch the API
CMD ["uvicorn", "similarity:app", "--host", "0.0.0.0", "--port", "5001"]
