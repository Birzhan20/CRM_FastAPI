from fastapi import FastAPI
from app.api.v1.endpoints import user, company, branch

app = FastAPI()

app.include_router(user.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(branch.router, prefix="/api/v1/branches", tags=["Branches"])
app.include_router(company.router, prefix="/api/v1/companies", tags=["Companies"])
