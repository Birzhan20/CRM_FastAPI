from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.schemas.payment import PaymentRead, PaymentCreate, PaymentResponse, PaymentDelete, PaymentUpdate
from app.crud.payment import read_payment, create_payment, update_payment, delete_payment, get_by_student_id
from app.core.database import get_db

router = APIRouter()


@router.get('/read', response_model=PaymentResponse)
async def read_(payment: PaymentRead, db: AsyncSession = Depends(get_db)):
    existing = await get_by_student_id(db, student_id=payment.student_id)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
    return await read_payment(db, payment)


@router.post('/create', response_model=PaymentResponse)
async def create_admin_endpoint(payment: PaymentCreate, db: AsyncSession = Depends(get_db)):
    return await create_payment(db, payment)


@router.post('/update', response_model=PaymentResponse)
async def update_admin_endpoint(payment: PaymentUpdate, db: AsyncSession = Depends(get_db)):
    existing = await get_by_student_id(db, student_id=payment.student_id)
    if not existing:
        await update_payment(db, payment)
        return {"detail": "Updated successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")


@router.delete('/delete', response_model=PaymentResponse)
async def delete_admin_endpoint(payment: PaymentDelete, db: AsyncSession = Depends(get_db)):
    existing = await get_by_student_id(db, student_id=payment.student_id)
    if not existing:
        await delete_payment(db, payment)
        return {"detail": "Deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
