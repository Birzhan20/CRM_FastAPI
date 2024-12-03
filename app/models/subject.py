from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.teacher import teacher_subjects


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)

    teachers = relationship('Teacher', secondary=teacher_subjects, back_populates='subjects')
    lessons = relationship("Lesson", back_populates="subjects")
