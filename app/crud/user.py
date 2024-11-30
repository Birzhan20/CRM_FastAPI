from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserDelete


async def get_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).filter(User.email == email))
    return result.scalars().first()


async def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(
        user=user.username,
        email=user.email,
        hashed_password="hashed_pw"
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def update_user(db: AsyncSession, user: UserUpdate):
    result = await db.execute(select(User).filter(User.email == user.email))
    user_update = result.scalar_one_or_none()  # Получаем первого пользователя или None
    if user_update is None:
        raise ValueError(f"User with email {user.email} not found")
    for field, value in user.dict(exclude_unset=True).items():
        setattr(user_update, field, value)  # Обновляем атрибуты на основе переданных данных
    await db.commit()
    await db.refresh(user_update)
    return user_update


async def delete_user(db: AsyncSession, user: UserDelete):
    result = await db.execute(select(User).filter(User.email == user.email))
    user_del = result.scalar_one_or_none()  # Получаем первого пользователя или None
    if user_del is None:
        raise ValueError(f"User with email {user.email} not found")
    await db.delete(user_del)
    await db.commit()
    return {"message": f"User with email {user.email} deleted successfully."}