from pydantic import BaseModel


class StudentBase(BaseModel):
    name: str
    branch_id: int
    group_id: int
    balance: float


class StudentCreate(StudentBase):
    pass


class StudentRead(StudentBase):
    pass


class StudentUpdate(StudentBase):
    pass


class StudentDelete(StudentBase):
    pass


class StudentResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True
