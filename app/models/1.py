from sqlalchemy import (
    Column, Integer, String, ForeignKey, DateTime, Float, Text, Boolean, Enum, create_engine, Table
)
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

# Таблица компании (Company)
class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False, unique=True)  # Логин
    password = Column(String(255), nullable=False)  # Пароль
    logo = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())

    branches = relationship('Branch', back_populates='company', cascade="all, delete-orphan")
    subjects = relationship('Subject', back_populates='company', cascade="all, delete-orphan")
    chapters = relationship('Chapter', back_populates='company', cascade="all, delete-orphan")
    materials = relationship('Material', back_populates='company', cascade="all, delete-orphan")

# Таблица филиалов (Branch)
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

# Таблица админов (Admin)
class Admin(Base):
    __tablename__ = 'admins'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    branch_id = Column(Integer, ForeignKey('branches.id', ondelete='CASCADE'), nullable=False)

    branch = relationship('Branch', back_populates='admins')

# Таблица учителей (Teacher)
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    branch_id = Column(Integer, ForeignKey('branches.id', ondelete='SET NULL'), nullable=True)

    branch = relationship('Branch', back_populates='teachers')
    subjects = relationship('Subject', secondary='teacher_subjects', back_populates='teachers')
    lessons = relationship("Lesson", back_populates="teacher")

# Ассоциативная таблица Teacher-Subject
teacher_subjects = Table(
    'teacher_subjects', Base.metadata,
    Column('teacher_id', Integer, ForeignKey('teachers.id', ondelete='CASCADE'), primary_key=True),
    Column('subject_id', Integer, ForeignKey('subjects.id', ondelete='CASCADE'), primary_key=True)
)

# Таблица студентов (Student)
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    branch_id = Column(Integer, ForeignKey('branches.id', ondelete='SET NULL'), nullable=True)
    group_id = Column(Integer, ForeignKey('groups.id', ondelete='SET NULL'), nullable=True)
    balance = Column(Float, default=0)

    branch = relationship('Branch', back_populates='students')
    group = relationship('Group', back_populates='students')

# Таблица предметов (Subject)
class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id', ondelete='CASCADE'), nullable=False)

    company = relationship('Company', back_populates='subjects')
    teachers = relationship('Teacher', secondary=teacher_subjects, back_populates='subjects')
    lessons = relationship("Lesson", back_populates="subject")

# Таблица глав (Chapter)
class Chapter(Base):
    __tablename__ = 'chapters'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id', ondelete='CASCADE'), nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id', ondelete='CASCADE'), nullable=False)

    subject = relationship('Subject', back_populates='chapters')
    company = relationship('Company', back_populates='chapters')

# Таблица материалов (Material)
class Material(Base):
    __tablename__ = 'materials'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    chapter_id = Column(Integer, ForeignKey('chapters.id', ondelete='CASCADE'), nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id', ondelete='CASCADE'), nullable=False)

    chapter = relationship('Chapter', back_populates='materials')
    company = relationship('Company', back_populates='materials')

# Таблица групп (Group)
class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id', ondelete='SET NULL'), nullable=True)
    room = Column(String(50), nullable=True)

    subject = relationship('Subject', back_populates='groups')
    students = relationship('Student', back_populates='group')
    lessons = relationship("Lesson", back_populates="group")


class LessonType(Enum):
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
    date_time = Column(DateTime, nullable=False)
    lesson_type = Column(Enum(LessonType), nullable=False)

    # Relationships
    branch = relationship("Branch", back_populates="lessons")
    teacher = relationship("Teacher", back_populates="lessons")
    subject = relationship("Subject", back_populates="lessons")
    group = relationship("Group", back_populates="lessons")


# Таблица домашнего задания (Homework)
class Homework(Base):
    __tablename__ = 'homeworks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    material_id = Column(Integer, ForeignKey('materials.id', ondelete='CASCADE'), nullable=False)
    type = Column(String(50), nullable=False)  # Тип (listening, reading, etc.)

    material = relationship('Material', back_populates='homeworks')

# Таблица прогресса (Progress)
class Progress(Base):
    __tablename__ = 'progress'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'), nullable=False)
    homework_id = Column(Integer, ForeignKey('homeworks.id', ondelete='CASCADE'), nullable=False)
    success_rate = Column(Float, nullable=False)  # Процент выполнения

    student = relationship('Student', back_populates='progresses')
    homework = relationship('Homework', back_populates='progresses')

# Таблица оплаты (Payment)
class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'), nullable=False)
    amount = Column(Float, nullable=False)
    payment_type = Column(Enum('cash', 'card', name='payment_types'), nullable=False)
    created_at = Column(DateTime, default=func.now())

    student = relationship('Student', back_populates='payments')
