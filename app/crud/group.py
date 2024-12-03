from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.group import Group
from app.schemas.group import GroupCreate, GroupUpdate, GroupDelete, GroupRead


async def get_by_name(db: AsyncSession, name: str):
    result = await db.execute(select(Group).filter(Group.name == name))
    return result.scalar_one_or_none()


async def read_group(db: AsyncSession, group: GroupRead):
    result = await db.execute(select(Group).filter(Group.name == group.name))
    return result.scalar_one_or_none()


async def create_group(db: AsyncSession, group: GroupCreate):
    group_create = GroupCreate(**group.model_dump())
    db.add(group_create)
    await db.commit()
    await db.refresh(group_create)
    return group_create


async def update_group(db: AsyncSession, group: GroupUpdate):
    result = await db.execute(select(Group).filter(Group.name == group.name))
    group_update = result.scalar_one_or_none()
    if not group_update:
        raise ValueError("Group not found")
    for field, value in group.model_dump(exclude_unset=True).items():
        setattr(group_update, field, value)
    await db.commit()
    await db.refresh(group_update)
    return group_update


async def delete_group(db: AsyncSession, group: GroupDelete):
    result = await db.execute(select(Group).filter(Group.name == group.name))
    group_delete = result.scalar_one_or_none()
    if not group_delete:
        raise ValueError("Group not found")
    await db.delete(group_delete)
    await db.commit()
    return
