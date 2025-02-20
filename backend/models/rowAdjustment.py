from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class RowAdjustment(Base):
    __tablename__ = "row_adjustments"

    row_number = Column(Integer, nullable=False)
    increases = Column(Integer, default=0)
    decreases = Column(Integer, default=0)

    counter_id = Column(Integer, ForeignKey("counters.id", ondelete="CASCADE"), nullable=False)

    counter = relationship("Counter", back_populates="row_adjustments")
