from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


class Progress(Base):
    __tablename__ = 'progresses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'), nullable=False)
    homework_id = Column(Integer, ForeignKey('homeworks.id', ondelete='CASCADE'), nullable=False)
    success_rate = Column(Float, nullable=False)  # Процент выполнения

    student = relationship('Student', back_populates='progresses')
    homework = relationship('Homework', back_populates='progresses')
