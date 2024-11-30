from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate, CompanyDelete


async def get_by_bin(db: AsyncSession, name: str):
    result = await db.execute(select(Company).filter(Company.name == name))
    return result.scalars().first()


async def create_company(db: AsyncSession, company: CompanyCreate):
    db_company = Company(name=company.name)
    db.add(db_company)
    await db.commit()
    await db.refresh(db_company)
    return db_company


async def update_company(db: AsyncSession, company: CompanyUpdate):
    result = await db.execute(select(Company).filter(Company.name == company.name))
    company_update = result.scalar_one_or_none()
    if company_update is None:
        raise HTTPException(status_code=404, detail=f"Company with bin {company.bin} not found")
    for field, value in company.dict(exclude_unset=True).items():
        setattr(company_update, field, value)
    await db.commit()
    await db.refresh(company_update)
    return company_update

async def delete_company(db: AsyncSession, company: CompanyDelete):
    result = await db.execute(select(Company).filter(Company.name == company.name))
    company_del = result.scalar_one_or_none()  # Получаем первый branch или None
    if company_del is None:
        raise ValueError(f"Company with bin {company.bin} not found")
    await db.delete(company_del)
    await db.commit()
    return
