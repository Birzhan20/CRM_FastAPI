from pydantic import BaseModel


class StudentBase(BaseModel):
    name: str
    branch_id: int
    group_id: int


class StudentCreate(StudentBase):
    password: str


class StudentRead(StudentBase):
    pass


class StudentUpdate(StudentBase):
    password: str


class StudentDelete(StudentBase):
    pass


class StudentResponse(BaseModel):
    id: int

    class Config:
        from_attributes = True
