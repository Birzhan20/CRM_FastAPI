from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Branch(Base):
    __tablename__ = 'branches'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id', ondelete='CASCADE'), nullable=False)

    company = relationship('Company', back_populates='branches')
    admins = relationship('Admin', back_populates='branch', cascade="all, delete-orphan")
    teachers = relationship('Teacher', back_populates='branch', cascade="all, delete-orphan")
    students = relationship('Student', back_populates='branch', cascade="all, delete-orphan")
    lessons = relationship("Lesson", back_populates="branch")
