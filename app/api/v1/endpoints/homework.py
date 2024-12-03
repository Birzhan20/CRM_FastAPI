from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.schemas.homework import HomeworkRead, HomeworkDelete, HomeworkUpdate, HomeworkCreate, HomeworkResponse
from app.crud.homework import read_homework, create_homework, update_homework, delete_homework, get_by_type
from app.core.database import get_db

router = APIRouter()


@router.get('/read', response_model=HomeworkResponse)
async def read_hw_endpoint(homework: HomeworkRead, db: AsyncSession = Depends(get_db)):
    existing = await get_by_type(db, type=homework.type)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Homework not found")
    return await read_homework(db, homework)


@router.post('/create', response_model=HomeworkResponse)
async def create_hw_endpoint(homework: HomeworkCreate, db: AsyncSession = Depends(get_db)):
    existing = await get_by_type(db, type=homework.type)
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Homework already exists")
    return await create_homework(db, homework)


@router.post('/update', response_model=HomeworkResponse)
async def update_hw_endpoint(homework: HomeworkUpdate, db: AsyncSession = Depends(get_db)):
    existing = await get_by_type(db, type=homework.type)
    if not existing:
        await update_homework(db, homework)
        return {"detail": "Updated successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Homework not found")


@router.delete('/delete', response_model=HomeworkResponse)
async def delete_hw_endpoint(homework: HomeworkDelete, db: AsyncSession = Depends(get_db)):
    existing = await get_by_type(db, type=homework.type)
    if not existing:
        await delete_homework(db, homework)
        return {"detail": "Deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Homework not found")