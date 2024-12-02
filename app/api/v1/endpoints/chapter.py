from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from typing import List

from app.schemas.chapter import ChapterCreate, ChapterUpdate, ChapterDelete, ChapterRead
from app.crud.chapter import create_chapter, update_chapter, delete_chapter, read_chapters
from app.core.database import get_db

router = APIRouter()

@router.get('/read', response_model=List[ChapterRead])
async def read_chapters_api(chapter: ChapterRead, db: AsyncSession = Depends(get_db)):
    existing = await read_chapters(db, name=chapter.name)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chapter not found")
    return existing

@router.post('/create', response_model=ChapterCreate)
async def create_chapter_api(chapter: ChapterCreate, db: AsyncSession = Depends(get_db)):
    existing = await read_chapters(db, name=chapter.name)
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Chapter with this name already exists")
    await create_chapter(db, chapter)
    return chapter

@router.post('/update', response_model=ChapterUpdate)
async def update_chapter_api(chapter: ChapterUpdate, db: AsyncSession = Depends(get_db)):
    existing = await read_chapters(db, name=chapter.name)
    if existing:
        await update_chapter(db, chapter)
        return chapter
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chapter not found")

@router.delete('/delete', response_model=ChapterDelete)
async def delete_chapter_api(chapter: ChapterDelete, db: AsyncSession = Depends(get_db)):
    existing = await read_chapters(db, name=chapter.name)
    if existing:
        await delete_chapter(db, chapter)
        return {"detail": "Deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chapter not found")
