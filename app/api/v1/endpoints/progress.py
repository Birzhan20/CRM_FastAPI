from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.schemas.progress import ProgressRead, ProgressDelete, ProgressUpdate, ProgressCreate, ProgressResponse
from app.crud.progress import read_progress, create_progress, update_progress, delete_progress, get_progress
from app.core.database import get_db

router = APIRouter()


@router.get('/read', response_model=ProgressResponse)
async def read_admin_endpoint(progress: ProgressRead, db: AsyncSession = Depends(get_db)):
    existing = await get_progress(db, student_id=progress.student_id)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Progress not found")
    return await read_progress(db, progress)


@router.post('/create', response_model=ProgressResponse)
async def create_admin_endpoint(progress: ProgressCreate, db: AsyncSession = Depends(get_db)):
    existing = await get_progress(db, student_id=progress.student_id)
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Progress already registered")
    return await create_progress(db, progress)


@router.post('/update', response_model=ProgressResponse)
async def update_admin_endpoint(progress: ProgressUpdate, db: AsyncSession = Depends(get_db)):
    existing = await get_progress(db, student_id=progress.student_id)
    if not existing:
        await update_progress(db, progress)
        return {"detail": "Updated successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Progress not found")


@router.delete('/delete', response_model=ProgressResponse)
async def delete_admin_endpoint(progress: ProgressDelete, db: AsyncSession = Depends(get_db)):
    existing = await get_progress(db, student_id=progress.student_id)
    if not existing:
        await delete_progress(db, progress)
        return {"detail": "Deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Progress not found")
