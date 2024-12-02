from sqlalchemy import ForeignKey, Column, Integer, DateTime, String, Enum as SQLAEnum
from sqlalchemy.orm import relationship
from  enum import Enum
from app.core.database import Base


class LessonType(str, Enum):
    individual = 'individual'
    group = 'group'


class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True, autoincrement=True)
    branch_id = Column(Integer, ForeignKey('branches.id'), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id'), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)
    room = Column(String, nullable=False)
    lesson_time = Column(DateTime, nullable=False)
    lesson_type = Column(SQLAEnum(LessonType), nullable=False)

    # Relationships
    branch = relationship("Branch", back_populates="lessons")
    teacher = relationship("Teacher", back_populates="lessons")
    subject = relationship("Subject", back_populates="lessons")
    group = relationship("Group", back_populates="lessons")
