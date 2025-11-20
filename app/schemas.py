from datetime import datetime
from pydantic import BaseModel, Field

class QuestionBase(BaseModel):
    text: str = Field(..., min_length=1, max_length=1000)

class QuestionCreate(QuestionBase):
    pass

class QuestionRead(QuestionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True  # переводим в схемы


class AnswerBase(BaseModel):
    text: str = Field(..., min_length=1, max_length=1000)
    user_id: str = Field(..., min_length=1)

class AnswerCreate(AnswerBase):
    pass

class AnswerRead(AnswerBase):
    id: int
    question_id: int
    created_at: datetime

    class Config:
        orm_mode = True
