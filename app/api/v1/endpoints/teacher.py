from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.schemas.teacher import TeacherRead, TeacherResponse, TeacherCreate, TeacherDelete, TeacherUpdate
from app.crud.teacher import read_teacher, create_teacher, update_teacher, delete_teacher, get_teacher
from app.core.database import get_db

router = APIRouter()


@router.get('/read', response_model=TeacherResponse)
async def read_(teacher: TeacherRead, db: AsyncSession = Depends(get_db)):
    existing = await get_teacher(db, name=teacher.name)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
    return await read_teacher(db, teacher)


@router.post('/create', response_model=TeacherResponse)
async def create_(teacher: TeacherCreate, db: AsyncSession = Depends(get_db)):
    existing = await get_teacher(db, name=teacher.name)
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Teacher already registered")
    return await create_teacher(db, teacher)


@router.post('/update', response_model=TeacherResponse)
async def update_(teacher: TeacherUpdate, db: AsyncSession = Depends(get_db)):
    existing = await get_teacher(db, name=teacher.name)
    if not existing:
        await update_teacher(db, teacher)
        return {"detail": "Updated successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")


@router.delete('/delete', response_model=TeacherResponse)
async def delete_(teacher: TeacherDelete, db: AsyncSession = Depends(get_db)):
    existing = await get_teacher(db, name=teacher.name)
    if not existing:
        await delete_teacher(db, teacher)
        return {"detail": "Deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
