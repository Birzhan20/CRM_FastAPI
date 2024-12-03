from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.homework import Homework
from app.schemas.homework import HomeworkCreate, HomeworkUpdate, HomeworkDelete, HomeworkRead


async def get_by_type(db: AsyncSession, type: str):
    result = await db.execute(select(Homework).filter(Homework.type == type))
    return result.scalar_one_or_none()


async def read_homework(db: AsyncSession, homework: HomeworkRead):
    result = await db.execute(select(Homework).filter(Homework.type == homework.type))
    return result.scalar_one_or_none()


async def create_homework(db: AsyncSession, homework: HomeworkCreate):
    homework_create = HomeworkCreate(**homework.model_dump())
    db.add(homework_create)
    await db.commit()
    await db.refresh(homework_create)
    return homework_create


async def update_homework(db: AsyncSession, homework: HomeworkUpdate):
    result = await db.execute(select(Homework).filter(Homework.type == homework.type))
    homework_update = result.scalar_one_or_none()
    if not homework_update:
        raise ValueError("homework not found")
    for key, value in homework.model_dump(exclude_unset=True).items():
        setattr(homework_update, key, value)
    await db.commit()
    await db.refresh(homework_update)
    return homework_update


async def delete_homework(db: AsyncSession, homework: HomeworkDelete):
    result = await db.execute(select(Homework).filter(Homework.type == homework.type))
    homework_delete = result.scalar_one_or_none()
    if not homework_delete:
        raise ValueError("homework not found")
    await db.delete(homework_delete)
    await db.commit()
