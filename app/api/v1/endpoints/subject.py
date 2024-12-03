from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.schemas.subject import SubjectRead, SubjectResponse, SubjectUpdate, SubjectCreate, SubjectDelete
from app.crud.subject import read_subject, create_subject, update_subject, delete_subject, get_subject
from app.core.database import get_db

router = APIRouter()


@router.get('/read', response_model=SubjectResponse)
async def read_(subject: SubjectRead, db: AsyncSession = Depends(get_db)):
    existing = await get_subject(db, name=subject.name)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Subject not found")
    return await read_subject(db, subject)


@router.post('/create', response_model=SubjectResponse)
async def create_(subject: SubjectCreate, db: AsyncSession = Depends(get_db)):
    existing = await get_subject(db, name=subject.name)
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Subject already registered")
    return await create_subject(db, subject)


@router.post('/update', response_model=SubjectResponse)
async def update_(subject: SubjectUpdate, db: AsyncSession = Depends(get_db)):
    existing = await get_subject(db, name=subject.name)
    if not existing:
        await update_subject(db, subject)
        return {"detail": "Updated successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Subject not found")


@router.delete('/delete', response_model=SubjectResponse)
async def delete_(subject: SubjectDelete, db: AsyncSession = Depends(get_db)):
    existing = await get_subject(db, name=subject.name)
    if not existing:
        await delete_subject(db, subject)
        return {"detail": "Deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Subject not found")
