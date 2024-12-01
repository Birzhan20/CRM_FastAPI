from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.admin import Admin
from app.schemas.admin import AdminCreate, AdminUpdate, AdminDelete, AdminRead


async def get_by_name(db: AsyncSession, name: str):
    result = await db.execute(select(Admin).filter(Admin.name == name))
    return result.scalars().first()


async def create_admin(db: AsyncSession, admin: AdminCreate):
    admin_create = AdminCreate(**admin.model_dump())
    db.add(admin_create)
    await db.commit()
    await db.refresh(admin_create)
    return admin_create


async def read_admin(db: AsyncSession, admin: AdminRead):
    result = await db.execute(select(Admin).filter(Admin.name == admin.name))
    return result.scalar_one_or_none()


async def update_admin(db: AsyncSession, admin: AdminUpdate):
    result = await db.execute(select(Admin).filter(Admin.name == admin.name))
    admin_update = result.scalar_one_or_none()
    if not admin_update:
        raise ValueError(f"Admin not found")
    for field, value in admin.model_dump(exclude_unset=True).items():
        setattr(admin_update, field, value)
    await db.commit()
    await db.refresh(admin_update)
    return admin_update


async def delete_admin(db: AsyncSession, admin: AdminDelete):
    result = await db.execute(select(Admin).filter(Admin.name == admin.name))
    admin_delete = result.scalar_one_or_none()
    if not admin_delete:
        raise ValueError(f"Admin not found")
    await db.delete(admin_delete)
    await db.commit()
    return
