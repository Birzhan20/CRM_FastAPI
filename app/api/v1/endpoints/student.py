from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.schemas.student import StudentRead, StudentResponse, StudentCreate, StudentDelete, StudentUpdate
from app.crud.student import read_student, create_student, update_student, delete_student, get_by_name
from app.core.database import get_db

router = APIRouter()


@router.get('/read', response_model=StudentResponse)
async def read_(student: StudentRead, db: AsyncSession = Depends(get_db)):
    existing = await get_by_name(db, name=student.name)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return await read_student(db, student)


@router.post('/create', response_model=StudentResponse)
async def create_(student: StudentCreate, db: AsyncSession = Depends(get_db)):
    existing = await get_by_name(db, name=student.name)
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Student already registered")
    return await create_student(db, student)


@router.post('/update', response_model=StudentResponse)
async def update_(student: StudentUpdate, db: AsyncSession = Depends(get_db)):
    existing = await get_by_name(db, name=student.name)
    if not existing:
        await update_student(db, student)
        return {"detail": "Updated successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")


@router.delete('/delete', response_model=StudentResponse)
async def delete_(student: StudentDelete, db: AsyncSession = Depends(get_db)):
    existing = await get_by_name(db, name=student.name)
    if not existing:
        await delete_student(db, student)
        return {"detail": "Deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
