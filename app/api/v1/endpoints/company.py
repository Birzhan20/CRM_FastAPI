from fastapi import Depends, HTTPException, APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.schemas.company import CompanyResponse, CompanyCreate, CompanyUpdate, CompanyDelete, CompanyRead
from app.crud.company import get_by_username, create_company, update_company, delete_company, read_company
from app.core.database import get_db


router = APIRouter()


@router.get('/read', response_model=CompanyResponse)
async def read_company_endpoint(company: CompanyRead, db: AsyncSession = Depends(get_db)):
    existing_company = await get_by_username(db, username=company.username)
    if not existing_company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    return await read_company(db, company)


@router.post('/create', response_model=CompanyResponse)
async def create_company_endpoint(company: CompanyCreate, db: AsyncSession = Depends(get_db)):
    existing_company = await get_by_username(db, username=company.username)
    if existing_company:
        raise HTTPException(status_code=400, detail='Company already registered')
    return await create_company(db, company)


@router.post('/update', response_model=CompanyResponse)
async def update_company_endpoint(company: CompanyUpdate, db: AsyncSession = Depends(get_db)):
    existing_company = await get_by_username(db, username=company.username)
    if existing_company:
        await update_company(db, company)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=f"Company updated successfully"
        )
    raise HTTPException(status_code=404, detail='Company not found')


@router.delete('/delete', response_model=CompanyResponse)
async def delete_company_endpoint(company: CompanyDelete, db: AsyncSession = Depends(get_db)):
    existing_company = await get_by_username(db, username=company.username)
    if existing_company:
        await delete_company(db, company)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=f"Company deleted successfully"
        )
    raise HTTPException(status_code=404, detail='Company not found')
