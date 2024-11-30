from pydantic import BaseModel


class HomeworkBase(BaseModel):
    material_id: int
    type: str


class HomeworkCreate(HomeworkBase):
    pass


class HomeworkRead(HomeworkBase):
    pass


class HomeworkUpdate(HomeworkBase):
    pass


class HomeworkDelete(HomeworkBase):
    pass


class HomeworkResponse(HomeworkBase):
    id: int

    class Config:
        orm_mode = True
