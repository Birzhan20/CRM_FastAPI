from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float, Enum, func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'), nullable=False)
    amount = Column(Float, nullable=False)
    payment_type = Column(Enum('cash', 'card', name='payment_types'), nullable=False)
    created_at = Column(DateTime, default=func.now())

    student = relationship('Student', back_populates='payments')
