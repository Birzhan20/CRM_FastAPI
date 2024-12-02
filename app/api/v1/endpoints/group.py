from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.schemas.group import GroupCreate, GroupRead, GroupDelete, GroupUpdate, GroupResponse
from app.crud.group import read_group, create_group, update_group, delete_group
from app.core.database import get_db


router = APIRouter()


@router.get('/read', response_model=GroupRead)
async def read_admin_endpoint(group: GroupRead, db: AsyncSession = Depends(get_db)):
    existing = await read_group(db, name=group.name)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
    return await read_group(db, group)


@router.post('/create', response_model=GroupResponse)
async def create_admin_endpoint(group: GroupCreate, db: AsyncSession = Depends(get_db)):
    existing = await read_group(db, name=group.name)
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Group already registered")
    return await create_group(db, group)


@router.post('/update', response_model=GroupResponse)
async def update_admin_endpoint(group: GroupUpdate, db: AsyncSession = Depends(get_db)):
    existing = await read_group(db, name=group.name)
    if not existing:
        await update_group(db, group)
        return {"detail": "Updated successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")


@router.delete('/delete', response_model=GroupResponse)
async def delete_admin_endpoint(group: GroupDelete, db: AsyncSession = Depends(get_db)):
    existing = await read_group(db, name=group.name)
    if not existing:
        await delete_group(db, group)
        return {"detail": "Deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")