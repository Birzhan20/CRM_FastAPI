from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False, unique=True)  # Логин
    password = Column(String(255), nullable=False)  # Пароль
    logo = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())

    branches = relationship('Branch', back_populates='companies', cascade="all, delete-orphan")
    chapters = relationship('Chapter', back_populates='companies', cascade="all, delete-orphan")
    materials = relationship('Material', back_populates='companies', cascade="all, delete-orphan")
