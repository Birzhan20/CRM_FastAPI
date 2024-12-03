from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True, unique=True)
    subject_id = Column(Integer, ForeignKey('subjects.id', ondelete='SET NULL'), nullable=True)
    room = Column(String(50), nullable=True)

    subject = relationship('Subject', back_populates='groups')
    students = relationship('Student', back_populates='groups')
    lessons = relationship("Lesson", back_populates="groups")
