## How to run project 

```bash
git clone
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Build and run in docker (optional)
```
docker build -t prob-similarity-api .
docker run -p 8000:8000 prob-similarity-api
```

## local test
```
uvicorn similarity_api:app --reload

 -- or specify port --

uvicorn similarity:app --host 0.0.0.0 --port 8000
```

## Test
```bash
curl -X POST http://localhost:8000/similarity -H "Content-Type: application/json" -d '{"a": "General Expense", "b": "Rental Expense"}'
```


## Deploying FastAPI App on Vercel
* Using Vercel’s GitHub integration
* A Vercel account (sign up at vercel.com)
* Prepare the FastAPI Project for Deployment
* In the project directory, update the code in a Python file, similarity_api.py. 
* You will need to create a static folder and save a placeholder favicon.ico (Vercel looks for this file when deploying the API using the FastHTML Framework)