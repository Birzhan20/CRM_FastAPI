from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    branch_id = Column(Integer, ForeignKey('branches.id', ondelete='SET NULL'), nullable=True)
    group_id = Column(Integer, ForeignKey('groups.id', ondelete='SET NULL'), nullable=True)
    balance = Column(Float, default=0)

    branch = relationship('Branch', back_populates='students')
    group = relationship('Group', back_populates='students')
