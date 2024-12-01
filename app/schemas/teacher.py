from typing import List
from pydantic import BaseModel


class TeacherBase(BaseModel):
    name: str
    branch_id: int | None = None

    class Config:
        from_attributes = True


class TeacherCreate(TeacherBase):
    password: str

    class Config:
        from_attributes = True


class TeacherRead(TeacherBase):
    id: int
    name: str
    branch_id: int
    branch_name: str
    subjects: List[str]

    class Config:
        from_attributes = True


class TeacherUpdate(TeacherBase):
    name: str | None = None
    password: str | None = None
    branch_id: str | None = None

    class Config:
        from_attributes = True


class TeacherDelete(TeacherBase):
    id: int

    class Config:
        from_attributes = True


class TeacherResponse(TeacherBase):
    id: int

    class Config:
        from_attributes = True
