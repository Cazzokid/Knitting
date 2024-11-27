from fastapi import FastAPI

app = FastAPI()
 
# uvicorn main:app --reload
# http://127.0.0.1:8000

@app.get("/")
def read_root():
    return {"message": "Welcome to CazzoKnit API!"}
