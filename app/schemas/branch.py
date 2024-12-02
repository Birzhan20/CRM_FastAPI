from pydantic import BaseModel


class BranchBase(BaseModel):
    name: str
    company_id: int


class BranchCreate(BranchBase):
    pass


class BranchRead(BranchBase):
    pass


class BranchUpdate(BranchBase):
    pass


class BranchDelete(BranchBase):
    pass


class BranchResponse(BranchBase):
    id: int

    class Config:
        from_attributes = True
