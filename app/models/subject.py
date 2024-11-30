from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id', ondelete='CASCADE'), nullable=False)

    company = relationship('Company', back_populates='subjects')
    teachers = relationship('Teacher', secondary=teacher_subjects, back_populates='subjects')
    lessons = relationship("Lesson", back_populates="subject")
