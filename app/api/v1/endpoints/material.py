from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.schemas.material import MaterialRead, MaterialDelete, MaterialUpdate, MaterialCreate, MaterialResponse
from app.crud.material import read_material, create_material, update_material, delete_material, get_by_name
from app.core.database import get_db

router = APIRouter()


@router.get('/read', response_model=MaterialResponse)
async def read_(material: MaterialRead, db: AsyncSession = Depends(get_db)):
    existing = await get_by_name(db, name=material.name)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Material not found")
    return await read_material(db, material)


@router.post('/create', response_model=MaterialResponse)
async def create_(material: MaterialCreate, db: AsyncSession = Depends(get_db)):
    existing = await get_by_name(db, name=material.name)
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Material already registered")
    return await create_material(db, material)


@router.post('/update', response_model=MaterialResponse)
async def update_(material: MaterialUpdate, db: AsyncSession = Depends(get_db)):
    existing = await get_by_name(db, name=material.name)
    if not existing:
        await update_material(db, material)
        return {"detail": "Updated successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Material not found")


@router.delete('/delete', response_model=MaterialResponse)
async def delete_(material: MaterialDelete, db: AsyncSession = Depends(get_db)):
    existing = await get_by_name(db, name=material.name)
    if not existing:
        await delete_material(db, material)
        return {"detail": "Deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Material not found")
