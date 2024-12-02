import uvicorn
from fastapi import FastAPI
from app.api.v1.endpoints import (
    company,
    branch,
    admin,
    chapter,
    group
)

app = FastAPI()

app.include_router(branch.router, prefix="/branch", tags=["Branch"])
app.include_router(company.router, prefix="/company", tags=["Company"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(chapter.router, prefix="/chapter", tags=["Chapter"])
app.include_router(group.router, prefix="/group", tags=["Group"])


if __name__ == "__main__":
    uvicorn.run(app)
