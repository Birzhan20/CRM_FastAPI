from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.teacher import Teacher
from app.schemas.teacher import TeacherCreate, TeacherUpdate, TeacherDelete, TeacherRead


async def get_teacher(db: AsyncSession, name: str):
    result = await db.execute(select(Teacher).where(Teacher.name == name))
    return result.scalar_one_or_none()


async def read_teacher(db: AsyncSession, teacher:TeacherRead):
    result = await db.execute(select(Teacher).filter(Teacher.name == teacher.name))
    return result.scalar_one_or_none()


async def create_teacher(db: AsyncSession, teacher:TeacherCreate):
    created_teacher = TeacherCreate(**teacher.model_dump())
    db.add(created_teacher)
    await db.commit()
    await db.refresh(created_teacher)
    return created_teacher


async def update_teacher(db: AsyncSession, teacher:TeacherUpdate):
    result = await db.execute(select(Teacher).filter(Teacher.name == teacher.name))
    teacher_update = result.scalar_one_or_none()
    if not teacher_update:
        raise ValueError("Teacher not found")
    for field, value in teacher.model_dump(exclude_unset=True).items():
        setattr(teacher_update, field, value)
    await db.commit()
    await db.refresh(teacher_update)
    return teacher_update


async def delete_teacher(db: AsyncSession, teacher:TeacherDelete):
    result = await db.execute(select(Teacher).filter(Teacher.name == teacher.name))
    teacher_delete = result.scalar_one_or_none()
    if not teacher_delete:
        raise ValueError("Teacher not found")
    await db.delete(teacher_delete)
    await db.commit()
