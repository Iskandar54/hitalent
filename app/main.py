from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.base import Base, engine
from app.routers import questions, answers

# $$$ Временное решение
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title="Q&A Service", lifespan=lifespan)

app.include_router(questions.router)
app.include_router(answers.router)

@app.get("/")
def root():
    return {"message": "Q&A API is running"}