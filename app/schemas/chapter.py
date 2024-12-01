from pydantic import BaseModel


class ChapterBase(BaseModel):
    title: str


class ChapterCreate(ChapterBase):
    subject_id: int


class ChapterRead(ChapterBase):
    subject_id: int


class ChapterUpdate(ChapterBase):
    pass


class ChapterDelete(ChapterBase):
    pass


class ChapterResponse(ChapterBase):
    pass

    class Config:
        from_attributes = True
