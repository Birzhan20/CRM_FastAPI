from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.subject import Subject
from app.schemas.subject import SubjectCreate, SubjectUpdate, SubjectDelete, SubjectRead


async def get_subject(db: AsyncSession, name: str):
    result = await db.execute(select(Subject).filter(Subject.name == name))
    return result.scalar_one_or_none()


async def read_subject(db: AsyncSession, subject: SubjectRead):
    result = await db.execute(select(Subject).filter(Subject.name == subject.name))
    return result.scalar_one_or_none()


async def create_subject(db: AsyncSession, subject: SubjectCreate):
    subject_create = SubjectCreate(**subject.model_dump())
    db.add(subject_create)
    await db.commit()
    await db.refresh(subject_create)
    return subject_create


async def update_subject(db: AsyncSession, subject: SubjectUpdate):
    result = await db.execute(select(Subject).filter(Subject.name == subject.name))
    subject_update = result.scalar_one_or_none()
    if not subject_update:
        raise ValueError("Subject not found")
    for key, value in subject.model_dump(exclude_unset=True).items():
        setattr(subject_update, key, value)
    await db.commit()
    await db.refresh(subject_update)
    return subject_update


async def delete_subject(db: AsyncSession, subject: SubjectDelete):
    result = await db.execute(select(Subject).filter(Subject.name == subject.name))
    subject_delete = result.scalar_one_or_none()
    if not subject_delete:
        raise ValueError("Subject not found")
    await db.delete(subject_delete)
    await db.commit()
