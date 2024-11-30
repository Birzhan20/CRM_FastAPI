from enum import Enum
from pydantic import BaseModel


class PaymentType(str, Enum):
    cash = 'cash'
    card = 'card'


class PaymentBase(BaseModel):
    student_id: int
    amount: float
    payment_type: PaymentType

    class Config:
        orm_mode = True


class PaymentCreate(PaymentBase):
    pass


class PaymentRead(PaymentBase):
    pass


class PaymentUpdate(PaymentBase):
    pass


class PaymentDelete(PaymentBase):
    pass


class PaymentResponse(PaymentBase):
    id: int

    class Config:
        orm_mode = True
