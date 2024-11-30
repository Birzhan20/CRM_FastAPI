from fastapi import Depends, HTTPException, APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.schemas.user import UserResponse, UserCreate, UserUpdate, UserDelete
from app.crud.user import get_by_email, create_user, update_user, delete_user
from app.core.database import get_db


router = APIRouter()


@router.post('/create', response_model=UserResponse)
async def create_user_endpoint(user: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await get_by_email(db, email=user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail='Email already registered')
    return await create_user(db, user)


@router.post('/update', response_model=UserResponse)
async def update_user_endpoint(user: UserUpdate, db: AsyncSession = Depends(get_db)):
    existing_user = await get_by_email(db, email=user.email)
    if existing_user:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=f"User updated successfully"
        )
    raise HTTPException(status_code=404, detail='User not found')


@router.delete('/delete', response_model=UserResponse)
async def delete_user_endpoint(user: UserDelete, db: AsyncSession = Depends(get_db)):
    existing_user = await get_by_email(db, email=user.email)
    if existing_user:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=f"User deleted successfully"
        )
    raise HTTPException(status_code=404, detail='User not found')

