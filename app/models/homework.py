from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base


class Homework(Base):
    __tablename__ = 'homeworks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    material_id = Column(Integer, ForeignKey('materials.id', ondelete='CASCADE'), nullable=False)
    type = Column(String(50), nullable=False)  # Тип (listening, reading, etc.)

    material = relationship('Material', back_populates='homeworks')
