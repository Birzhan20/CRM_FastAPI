from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.progress import Progress
from app.schemas.progress import ProgressCreate, ProgressUpdate, ProgressDelete, ProgressRead


async def get_progress(db: AsyncSession, student_id: int):
    result = await db.execute(select(Progress).filter(Progress.student_id == student_id))
    return result.scalars().all()


async def read_progress(db: AsyncSession, progress: ProgressRead):
    result = await db.execute(select(Progress).filter(Progress.student_id == progress.student_id))
    return result.scalar_one_or_none()


async def create_progress(db: AsyncSession, progress: ProgressCreate):
    progress_create = ProgressCreate(**progress.model_dump())
    db.add(progress_create)
    await db.commit()
    await db.refresh(progress_create)
    return progress_create


async def update_progress(db: AsyncSession, progress: ProgressUpdate):
    result = await db.execute(select(Progress).filter(Progress.student_id == Progress.student_id))
    progress_update = result.scalar_one_or_none()
    if not progress_update:
        raise ValueError("Student's progress not found")
    for field, value in progress.model_dump(exclude_unset=True).items():
        setattr(progress_update, field, value)
    await db.commit()
    await db.refresh(progress_update)
    return progress_update


async def delete_progress(db: AsyncSession, progress: ProgressDelete):
    result = await db.execute(select(Progress).filter(Progress.student_id == progress.student_id))
    progress_delete = result.scalar_one_or_none()
    if not progress_delete:
        raise ValueError("Student's progress not found")
    await db.delete(progress_delete)
    await db.commit()
    return
