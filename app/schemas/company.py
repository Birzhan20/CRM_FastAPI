from pydantic import BaseModel


class CompanyBase(BaseModel):
    name: str
    username: str
    logo: str | None = None
    password: str


class CompanyCreate(CompanyBase):
    pass


class CompanyRead(CompanyBase):
    pass


class CompanyUpdate(CompanyBase):
    pass


class CompanyDelete(CompanyBase):
    pass


class CompanyResponse(CompanyBase):
    id: int

    class Config:
        from_attributes = True
