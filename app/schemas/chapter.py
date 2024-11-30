from pydantic import BaseModel


class ChapterBase(BaseModel):
    title: str
    subject_id: int
    company_id: int


class ChapterCreate(ChapterBase):
    pass


class ChapterRead(ChapterBase):
    pass


class ChapterUpdate(ChapterBase):
    pass


class ChapterDelete(ChapterBase):
    pass

    class Config:
        orm_mode = True
