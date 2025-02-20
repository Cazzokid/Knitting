from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = "users"

    email = Column(String, unique=True, index=True, nullable=False)
    display_name = Column(String)
    password_hash = Column(String, nullable=False)

    projects = relationship("Project", back_populates="user", cascade="all, delete-orphan")
