from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.material import Material
from app.schemas.material import MaterialCreate, MaterialUpdate, MaterialDelete, MaterialRead


async def read_material(db: AsyncSession, material: MaterialRead):
    result = await db.execute(select(Material).where(Material.name == material.name))
    return result.scalar_one_or_none()


async def create_material(db: AsyncSession, material: MaterialCreate):
    material_create = MaterialCreate(**material.model_dump())
    db.add(material_create)
    await db.commit()
    await db.refresh(material_create)
    return material_create


async def update_material(db: AsyncSession, material: MaterialUpdate):
    result = await db.execute(select(Material).where(Material.name == material.name))
    material_update = result.scalar_one_or_none()
    if not material_update:
        raise ValueError('Material not found')
    for field, value in material.model_dump(exclude_unset=True).items():
        setattr(material_update, field, value)
    await db.commit()
    await db.refresh(material_update)
    return material_update


async def delete_material(db: AsyncSession, material: MaterialDelete):
    result = await db.execute(select(Material).where(Material.name == material.name))
    material_delete = result.scalar_one_or_none()
    if not material_delete:
        raise ValueError('Material not found')
    await db.delete(material_delete)
    await db.commit()
    return
