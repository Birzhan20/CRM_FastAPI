from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.schemas.admin import AdminCreate, AdminUpdate, AdminDelete, AdminRead, AdminResponse
from app.crud.admin import read_admin, create_admin, update_admin, delete_admin, get_by_name
from app.core.database import get_db


router = APIRouter()


@router.get('/read', response_model=AdminResponse)
async def read_admin_endpoint(admin: AdminRead, db: AsyncSession = Depends(get_db)):
    existing = await get_by_name(db, name=admin.name)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Admin not found")
    return await read_admin(db, admin)


@router.post('/create', response_model=AdminResponse)
async def create_admin_endpoint(admin: AdminCreate, db: AsyncSession = Depends(get_db)):
    existing = await get_by_name(db, name=admin.name)
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Admin already registered")
    return await create_admin(db, admin)


@router.post('/update', response_model=AdminResponse)
async def update_admin_endpoint(admin: AdminUpdate, db: AsyncSession = Depends(get_db)):
    existing = await get_by_name(db, name=admin.name)
    if not existing:
        await update_admin(db, admin)
        return JSONResponse(status_code=status.HTTP_200_OK, content="Admin updated successfully")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Admin not found")


@router.delete('/delete', response_model=AdminResponse)
async def delete_admin_endpoint(admin: AdminDelete, db: AsyncSession = Depends(get_db)):
    existing = await get_by_name(db, name=admin.name)
    if not existing:
        await delete_admin(db, admin)
        return JSONResponse(status_code=status.HTTP_200_OK, content="Admin deleted successfully")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Admin not found")
