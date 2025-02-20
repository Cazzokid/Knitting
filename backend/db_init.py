import os
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, Session
from models import Base

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()
    try:
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print("Tables in the database:", tables)
    finally:
        db.close()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()