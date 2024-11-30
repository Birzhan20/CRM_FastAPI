from pydantic import BaseModel


class AdminBase(BaseModel):
    name: str
    branch_id: int


class AdminCreate(AdminBase):
    pass


class AdminRead(AdminBase):
    pass


class AdminUpdate(AdminBase):
    pass


class AdminDelete(AdminBase):
    pass


class AdminResponse(AdminBase):
    id: int

    class Config:
        orm_mode = True
