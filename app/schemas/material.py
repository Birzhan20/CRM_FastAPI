from pydantic import BaseModel
from datetime import datetime


class MaterialBase(BaseModel):
    name: str
    chapter_id: int
    company_id: int


class MaterialCreate(MaterialBase):
    pass


class MaterialUpdate(MaterialBase):
    pass


class MaterialRead(MaterialBase):
    created_at: datetime


class MaterialDelete(MaterialBase):
    pass


class MaterialResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True
