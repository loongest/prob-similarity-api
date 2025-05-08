## How to run project 

mkdir sentence_similarity_api
cd sentence_similarity_api

git clone
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


## Build and run in docker
docker build -t prob-similarity-api .
docker run -p 8000:8000 prob-similarity-api

## Test
curl -X POST http://localhost:5001/similarity \
  -H "Content-Type: application/json" \
  -d '{"a": "General Expense", "b": "Rental Expense"}'


# Deploy FastAPI on Vercel: How to Host Your Python APIs for Free     