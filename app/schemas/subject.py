from pydantic import BaseModel


class SubjectBase(BaseModel):
    name: str
    company_id: int


class SubjectCreate(SubjectBase):
    pass


class SubjectRead(SubjectBase):
    pass


class SubjectUpdate(SubjectBase):
    pass


class SubjectDelete(SubjectBase):
    pass


class SubjectResponse(SubjectBase):
    id: int

    class Config:
        orm_mode = True
