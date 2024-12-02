from pydantic import BaseModel


class ProgressBase(BaseModel):
    student_id: int
    homework_id: int
    success_rate: float


class ProgressCreate(ProgressBase):
    pass


class ProgressRead(ProgressBase):
    pass


class ProgressUpdate(ProgressBase):
    pass


class ProgressDelete(ProgressBase):
    pass


class ProgressResponse(ProgressBase):
    id: int

    class Config:
        from_attributes = True
