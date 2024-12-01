from datetime import datetime
from decimal import Decimal
from enum import Enum
from pydantic import BaseModel


class PaymentType(str, Enum):
    cash = 'cash'
    card = 'card'


class PaymentBase(BaseModel):
    student_id: int
    amount: Decimal
    payment_type: PaymentType

    class Config:
        orm_mode = True


class PaymentCreate(PaymentBase):
    pass


class PaymentRead(PaymentBase):
    created_at: datetime


class PaymentUpdate(PaymentBase):
    pass


class PaymentDelete(PaymentBase):
    pass


class PaymentResponse(PaymentBase):
    id: int

    class Config:
        from_attributes = True
