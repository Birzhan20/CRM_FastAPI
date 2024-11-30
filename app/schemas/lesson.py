from pydantic import BaseModel, field_validator
from enum import Enum
from datetime import datetime


class LessonType(str, Enum):
    individual = 'individual'
    group = 'group'


class LessonBase(BaseModel):
    student_id: int
    lesson_time: datetime
    lesson_type: LessonType

    @field_validator('lesson_time')
    def check_lesson_time(cls, value):
        if value < datetime.now():
            raise ValueError('lesson_time must be in the future')
        return value


class LessonCreate(LessonBase):
    pass


class LessonRead(LessonBase):
    id: int
    branch_id: int
    teacher_id: int
    subject_id: int
    group_id: int
    room: str

    class Config:
        orm_mode = True


class LessonUpdate(LessonBase):
    pass


class LessonDelete(BaseModel):
    id: int

    class Config:
        orm_mode = True
