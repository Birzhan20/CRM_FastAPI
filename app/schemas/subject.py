from pydantic import BaseModel


class SubjectBase(BaseModel):
    name: str


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
        from_attributes = True
