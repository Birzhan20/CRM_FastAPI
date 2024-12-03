from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.payment import Payment
from app.schemas.payment import PaymentRead, PaymentCreate, PaymentUpdate, PaymentDelete


async def get_by_student_id(db: AsyncSession, student_id: int):
    result = await db.execute(select(Payment).where(Payment.student_id == student_id))
    return result.scalar_one_or_none()


async def read_payment(db: AsyncSession, payment: PaymentRead):
    result = await db.execute(select(Payment).filter(Payment.student_id == payment.student_id))
    return result.scalar_one_or_none()


async def create_payment(db: AsyncSession, payment: PaymentCreate):
    payment_create = PaymentCreate(**payment.model_dump())
    db.add(payment_create)
    await db.commit()
    await db.refresh(payment_create)
    return payment_create


async def update_payment(db: AsyncSession, payment: PaymentUpdate):
    result = await db.execute(select(Payment).filter(Payment.student_id == payment.student_id))
    payment_update = result.scalar_one_or_none()
    if not payment_update:
        raise ValueError("Payment not found")
    for field, value in payment.model_dump(exclude_unset=True).items():
        setattr(payment_update, field, value)
    await db.commit()
    await db.refresh(payment_update)
    return payment_update


async def delete_payment(db: AsyncSession, payment: PaymentDelete):
    result = await db.execute(select(Payment).filter(Payment.student_id == payment.student_id))
    payment_delete = result.scalar_one_or_none()
    if not payment_delete:
        raise ValueError("Payment not found")
    await db.delete(payment_delete)
    await db.commit()
    return
