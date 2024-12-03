from pydantic import BaseModel


class ChapterBase(BaseModel):
    name: str
    subject_id: int

class ChapterCreate(ChapterBase):
    pass


class ChapterRead(ChapterBase):
    pass


class ChapterUpdate(ChapterBase):
    pass


class ChapterDelete(ChapterBase):
    pass


class ChapterResponse(ChapterBase):
    pass

    class Config:
        from_attributes = True
