from fastapi import Depends, HTTPException, APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user import UserResponse, UserCreate, UserUpdate, UserDelete
from app.crud.user import get_by_email, create_user, update_user, delete_user
from app.core.database import get_db


router = APIRouter()


# Создание клиента
@router.post("/clients/")
async def create_client(name: str, db: AsyncSession = Depends(get_db)):
    client = Client(name=name)
    db.add(client)
    await db.commit()
    await db.refresh(client)
    return client


# Пополнение баланса
@router.post("/clients/{client_id}/deposit/")
async def deposit_balance(client_id: int, amount: float, db: AsyncSession = Depends(get_db)):
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")

    result = await db.execute(select(Client).where(Client.id == client_id))
    client = result.scalar_one_or_none()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    client.balance += amount
    transaction = Transaction(client_id=client_id, amount=amount, type="deposit")
    db.add(transaction)
    await db.commit()
    return {"balance": client.balance}