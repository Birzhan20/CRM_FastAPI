from pydantic import BaseModel


class TeacherBase(BaseModel):
    name: str
    branch_id: int


class TeacherCreate(TeacherBase):
    pass


class TeacherRead(TeacherBase):
    pass


class TeacherUpdate(TeacherBase):
    pass


class TeacherDelete(TeacherBase):
    pass


class TeacherResponse(TeacherBase):
    id: int

    class Config:
        orm_mode = True
