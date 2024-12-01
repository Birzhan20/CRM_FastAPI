from pydantic import BaseModel


class AdminBase(BaseModel):
    name: str
    branch_id: int



class AdminCreate(AdminBase):
    password: str


class AdminRead(AdminBase):
    pass


class AdminUpdate(AdminBase):
    password: str


class AdminDelete(AdminBase):
    pass


class AdminResponse(AdminBase):
    id: int

    class Config:
        from_attributes = True
