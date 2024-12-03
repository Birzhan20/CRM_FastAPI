from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate, StudentDelete, StudentRead


async def get_by_name(db: AsyncSession, name: str):
    result = await db.execute(select(Student).filter(Student.name == name))
    return result.scalar_one_or_none()


async def read_student(db: AsyncSession, student: StudentRead):
    result = await db.execute(select(Student).filter(Student.name == student.name))
    return result.scalar_one_or_none()


async def create_student(db: AsyncSession, student: StudentCreate):
    student_create = StudentCreate(**student.model_dump())
    db.add(student_create)
    await db.commit()
    await db.refresh(student_create)
    return student_create


async def update_student(db: AsyncSession, student: StudentUpdate):
    result = await db.execute(select(Student).filter(Student.name == student.name))
    student_update = result.scalar_one_or_none()
    if not student_update:
        raise ValueError("Student not found")
    for field, value in student.model_dump(exclude_unset=True).items():
        setattr(student_update, field, value)
    await db.commit()
    await db.refresh(student_update)
    return student_update


async def delete_student(db: AsyncSession, student: StudentDelete):
    result = await db.execute(select(Student).filter(Student.name == student.name))
    student_delete = result.scalar_one_or_none()
    if not student_delete:
        raise ValueError("Student not found")
    await db.delete(student_delete)
    await db.commit()
