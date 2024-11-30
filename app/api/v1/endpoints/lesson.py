from datetime import timedelta, datetime

from fastapi import Depends, HTTPException, APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.schemas.user import UserResponse, UserCreate, UserUpdate, UserDelete
from app.crud.user import get_by_email, create_user, update_user, delete_user
from app.core.database import get_db

router = APIRouter()


@router.post("/lessons/")
async def create_lesson(client_id: int, teacher_id: int, start_time: datetime, duration: int,
                        db: AsyncSession = Depends(get_db)):
    # Проверка клиента
    result = await db.execute(select(Client).where(Client.id == client_id))
    client = result.scalar_one_or_none()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    # Проверка баланса
    lesson_cost = 100  # фиксированная стоимость занятия
    if client.balance < lesson_cost:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    # Создание занятия
    end_time = start_time + timedelta(minutes=duration)
    lesson = Lesson(client_id=client_id, teacher_id=teacher_id, start_time=start_time, end_time=end_time)
    db.add(lesson)

    # Списание средств
    client.balance -= lesson_cost
    transaction = Transaction(client_id=client_id, amount=-lesson_cost, type="deduction")
    db.add(transaction)

    await db.commit()
    return {"message": "Lesson scheduled", "remaining_balance": client.balance}


# Получение расписания
@router.get("/schedule/")
async def get_schedule(teacher_id: int, date: datetime, db: AsyncSession = Depends(get_db)):
    start_date = date.replace(hour=0, minute=0, second=0)
    end_date = date.replace(hour=23, minute=59, second=59)
    result = await db.execute(
        select(Lesson).where(
            Lesson.teacher_id == teacher_id,
            Lesson.start_time >= start_date,
            Lesson.start_time <= end_date,
        )
    )
    lessons = result.scalars().all()
    return lessons