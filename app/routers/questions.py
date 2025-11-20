from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.db.deps import get_db

router = APIRouter(prefix="/questions", tags=["questions"])

@router.get("/", response_model=list[schemas.QuestionRead])
def read_questions(db: Session = Depends(get_db)):
    return crud.get_questions(db)

@router.post("/", response_model=schemas.QuestionRead)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    return crud.create_question(db, question)

@router.get("/{question_id}", response_model=schemas.QuestionRead)
def read_question(question_id: int, db: Session = Depends(get_db)):
    question = crud.get_question(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@router.delete("/{question_id}", response_model=schemas.QuestionRead)
def delete_question(question_id: int, db: Session = Depends(get_db)):
    question = crud.delete_question(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question
