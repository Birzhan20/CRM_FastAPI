from pydantic import BaseModel


class GroupBase(BaseModel):
    name: str
    subject_id: int
    room: str | None = None


class GroupCreate(GroupBase):
    pass


class GroupRead(GroupBase):
    pass


class GroupUpdate(GroupBase):
    pass


class GroupDelete(GroupBase):
    pass


class GroupResponse(GroupBase):
    id: int

    class Config:
        orm_mode = True
