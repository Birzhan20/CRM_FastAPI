from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


class Chapter(Base):
    __tablename__ = 'chapters'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id', ondelete='CASCADE'), nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id', ondelete='CASCADE'), nullable=False)

    subject = relationship('Subject', back_populates='chapters')
    company = relationship('Company', back_populates='chapters')

