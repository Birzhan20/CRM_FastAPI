from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.core.database import Base


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    password = Column(String(100), nullable=False)
    branch_id = Column(Integer, ForeignKey('branches.id', ondelete='SET NULL'), nullable=True)

    branch = relationship('Branch', back_populates='teachers')
    subjects = relationship('Subject', secondary='teacher_subjects', back_populates='teachers')
    lessons = relationship("Lesson", back_populates="teacher")


# Ассоциативная таблица Teacher-Subject
teacher_subjects = Table(
    'teacher_subjects', Base.metadata,
    Column('teacher_id', Integer, ForeignKey(
        'teachers.id', ondelete='CASCADE'
    ), primary_key=True),
    Column('subject_id', Integer, ForeignKey(
        'subjects.id', ondelete='CASCADE'
    ), primary_key=True)
)
