from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.chapter import Chapter
from app.schemas.chapter import ChapterCreate, ChapterUpdate, ChapterDelete, ChapterRead


async def get_by_name(db: AsyncSession, name: str):
    result = await db.execute(select(Chapter).filter(Chapter.name == name))
    return result.scalar_one_or_none()


async def read_chapters(chapter: ChapterRead, db: AsyncSession):
    result = await db.execute(select(Chapter).filter(Chapter.name == chapter.name))
    return result.scalar_one_or_none()


async def create_chapter(db: AsyncSession, chapter: ChapterCreate):
    chapter_create = ChapterCreate(**chapter.model_dump())
    db.add(chapter_create)
    await db.commit()
    await db.refresh(chapter_create)
    return chapter_create


async def update_chapter(db: AsyncSession, chapter: ChapterUpdate):
    result = await db.execute(select(Chapter).filter(Chapter.name == chapter.name))
    chapter_update = result.scalar_one_or_none()  # Получаем первого пользователя или None
    if chapter_update is None:
        raise ValueError(f"Chapter not found")
    for field, value in chapter.model_dump(exclude_unset=True).items():
        setattr(chapter_update, field, value)  # Обновляем атрибуты на основе переданных данных
    await db.commit()
    await db.refresh(chapter_update)
    return chapter_update


async def delete_chapter(db: AsyncSession, chapter: ChapterDelete):
    result = await db.execute(select(Chapter).filter(Chapter.name == chapter.name))
    chapter_delete = result.scalar_one_or_none()
    if chapter_delete is None:
        raise ValueError(f"Chapter not found")
    await db.delete(chapter_delete)
    await db.commit()
    return