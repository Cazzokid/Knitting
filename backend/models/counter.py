from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Counter(Base):
    __tablename__ = "counters"  # Changed to plural for consistency

    stitch_counter = Column(Integer, default=0)
    row_counter = Column(Integer, default=0)
    counter_comments = Column(String)

    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)

    project = relationship("Project", back_populates="counters")
    row_adjustments = relationship("RowAdjustment", back_populates="counter", cascade="all, delete-orphan")
