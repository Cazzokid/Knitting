from sqlalchemy.orm import Session
import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# User CRUD
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(
        email=user.email,
        display_name=user.display_name,
        password_hash=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, credentials: schemas.UserLogin):
    user = get_user_by_email(db, email=credentials.email)
    if not user or not pwd_context.verify(credentials.password, user.password_hash):
        return None
    return user