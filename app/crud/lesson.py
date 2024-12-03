from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.lesson import Lesson
from app.schemas.lesson import LessonCreate, LessonUpdate, LessonDelete, LessonRead


async def get_by_id(db: AsyncSession, group_id: int):
    result = await db.execute(select(Lesson).filter(Lesson.group_id == group_id))
    return result.scalar_one_or_none()


async def read_lesson(db: AsyncSession, lesson: LessonRead):
    result = await db.execute(select(Lesson).filter(Lesson.group_id == lesson.group_id))
    return result.scalar_one_or_none()


async def create_lesson(db: AsyncSession, lesson: LessonCreate):
    lesson_create = LessonCreate(**lesson.model_dump())
    db.add(lesson_create)
    await db.commit()
    await db.refresh(lesson_create)
    return lesson_create


async def update_lesson(db: AsyncSession, lesson: LessonUpdate):
    result = await db.execute(select(Lesson).filter(Lesson.group_id == lesson.group_id))
    lesson_update = result.scalar_one_or_none()
    if not lesson_update:
        raise ValueError("Lesson not found")
    for field, value in lesson.model_dump(exclude_unset=True).items():
        setattr(lesson_update, field, value)
    await db.commit()
    await db.refresh(lesson_update)
    return lesson_update


async def delete_lesson(db: AsyncSession, lesson: LessonDelete):
    result = await db.execute(select(Lesson).filter(Lesson.group_id == lesson.group_id))
    lesson_delete = result.scalar_one_or_none()
    if not lesson_delete:
        raise ValueError("Lesson not found")
    await db.delete(lesson_delete)
    await db.commit()
    return
