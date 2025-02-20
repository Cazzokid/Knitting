from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import crud, db_init
import schemas

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db_init.init_db()

def get_db():
    yield from db_init.get_db()

@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = crud.create_user(db=db, user=user)
    user_id = user.id
    return {"message": "User registered successfully", "id": user_id}

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.authenticate_user(db=db, credentials=user)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return db_user