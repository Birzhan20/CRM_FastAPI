from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.schemas.lesson import LessonRead, LessonDelete, LessonCreate, LessonUpdate, LessonResponse
from app.crud.lesson import read_lesson, create_lesson, update_lesson, delete_lesson, get_by_id
from app.core.database import get_db

router = APIRouter()


@router.get('/read', response_model=LessonResponse)
async def read_admin_endpoint(lesson: LessonRead, db: AsyncSession = Depends(get_db)):
    existing = await get_by_id(db, group_id=lesson.group_id)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")
    return await read_lesson(db, lesson)


@router.post('/create', response_model=LessonResponse)
async def create_admin_endpoint(lesson: LessonCreate, db: AsyncSession = Depends(get_db)):
    existing = await get_by_id(db, group_id=lesson.group_id)
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Lesson already registered")
    return await create_lesson(db, lesson)


@router.post('/update', response_model=LessonResponse)
async def update_admin_endpoint(lesson: LessonUpdate, db: AsyncSession = Depends(get_db)):
    existing = await get_by_id(db, group_id=lesson.group_id)
    if not existing:
        await update_lesson(db, lesson)
        return {"detail": "Updated successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")


@router.delete('/delete', response_model=LessonResponse)
async def delete_admin_endpoint(lesson: LessonDelete, db: AsyncSession = Depends(get_db)):
    existing = await get_by_id(db, group_id=lesson.group_id)
    if not existing:
        await delete_lesson(db, lesson)
        return {"detail": "Deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")