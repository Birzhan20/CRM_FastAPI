from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.branch import Branch
from app.schemas.branch import BranchCreate, BranchUpdate, BranchDelete, BranchRead


async def get_by_name(db: AsyncSession, name: str):
    result = await db.execute(select(Branch).filter(Branch.name == name))
    return result.scalars().first()


async def create_branch(db: AsyncSession, branch: BranchCreate):
    db_branch = Branch(**branch.model_dump())
    db.add(db_branch)
    await db.commit()
    await db.refresh(db_branch)
    return db_branch


async def read_branch(db: AsyncSession, branch: BranchRead):
    result = await db.execute(select(Branch).filter(Branch.name == branch.name))
    branch_read = result.scalar_one_or_none()
    return branch_read


async def update_branch(db: AsyncSession, branch: BranchUpdate):
    result = await db.execute(select(Branch).filter(Branch.name == branch.name))
    branch_update = result.scalar_one_or_none()  # Получаем первого пользователя или None
    if branch_update is None:
        raise ValueError(f"Branch with name {branch.name} not found")
    for field, value in branch.model_dump(exclude_unset=True).items():
        setattr(branch_update, field, value)  # Обновляем атрибуты на основе переданных данных
    await db.commit()
    await db.refresh(branch_update)
    return branch_update


async def delete_branch(db: AsyncSession, branch: BranchDelete):
    result = await db.execute(select(Branch).filter(Branch.name == branch.name))
    branch_del = result.scalar_one_or_none()  # Получаем первый branch или None
    if branch_del is None:
        raise ValueError(f"Branch with name {branch.name} not found")
    await db.delete(branch_del)
    await db.commit()
    return
