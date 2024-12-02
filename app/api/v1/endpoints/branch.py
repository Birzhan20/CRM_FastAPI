from fastapi import Depends, HTTPException, APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.models import Branch
from app.schemas.branch import BranchResponse, BranchCreate, BranchUpdate, BranchDelete, BranchRead
from app.crud.branch import get_by_name, create_branch, update_branch, delete_branch, read_branch
from app.core.database import get_db


router = APIRouter()


@router.get('/read', response_model=BranchResponse)
async def read_branch_endpoint(branch: BranchRead, db: AsyncSession = Depends(get_db)):
    existing = await get_by_name(db, name = branch.name)
    if not existing:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Branch not found")
    return await read_branch(db, branch)


@router.post('/create', response_model=BranchResponse)
async def create_branch_endpoint(branch: BranchCreate, db: AsyncSession = Depends(get_db)):
    existing_branch = await get_by_name(db, name=branch.name)
    if existing_branch:
        raise HTTPException(status_code=400, detail='Branch already registered')
    return await create_branch(db, branch)


@router.post('/update', response_model=BranchResponse)
async def update_company_endpoint(branch: BranchUpdate, db: AsyncSession = Depends(get_db)):
    existing_branch = await get_by_name(db, name=branch.name)
    if existing_branch:
        updated = await update_branch(db, branch)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=f"Branch updated successfully"
        )
    raise HTTPException(status_code=404, detail='Branch not found')


@router.delete('/delete', response_model=BranchResponse)
async def delete_company_endpoint(branch: BranchDelete, db: AsyncSession = Depends(get_db)):
    existing_branch = await get_by_name(db, name=branch.name)
    if existing_branch:
        deleted = await delete_branch(db, branch)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=f"Branch deleted successfully"
        )
    raise HTTPException(status_code=404, detail='Branch not found')
