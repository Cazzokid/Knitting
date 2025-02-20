from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Project(Base):
    __tablename__ = "projects"  # Changed to plural for consistency

    project_name = Column(String, nullable=False)
    project_description = Column(String)
    needle_size = Column(Integer)
    yarn = Column(String)
    project_comments = Column(String)
    project_picture = Column(String)

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    user = relationship("User", back_populates="projects")
    counters = relationship("Counter", back_populates="project", cascade="all, delete-orphan")  # Added
