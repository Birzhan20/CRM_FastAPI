import uvicorn
from fastapi import FastAPI
from app.api.v1.endpoints import (
    company,
    branch,
    admin,
    chapter,
    group,
    homework,
    lesson,
    material,
    payment,
    progress,
    student,
    subject,
    teacher,
)

app = FastAPI()

app.include_router(branch.router, prefix="/branch", tags=["Branch"])
app.include_router(company.router, prefix="/company", tags=["Company"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(chapter.router, prefix="/chapter", tags=["Chapter"])
app.include_router(group.router, prefix="/group", tags=["Group"])
app.include_router(homework.router, prefix="/homework", tags=["Homework"])
app.include_router(lesson.router, prefix="/lesson", tags=["Lesson"])
app.include_router(material.router, prefix="/material", tags=["Material"])
app.include_router(payment.router, prefix="/payment", tags=["Payment"])
app.include_router(progress.router, prefix="/progress", tags=["Progress"])
app.include_router(student.router, prefix="/student", tags=["Student"])
app.include_router(subject.router, prefix="/subject", tags=["Subject"])
app.include_router(teacher.router, prefix="/teacher", tags=["Teacher"])


if __name__ == "__main__":
    uvicorn.run(app)
