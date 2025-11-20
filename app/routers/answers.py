from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.db.deps import get_db

router = APIRouter(prefix="/answers", tags=["answers"])

@router.get("/{answer_id}", response_model=schemas.AnswerRead)
def read_answer(answer_id: int, db: Session = Depends(get_db)):
    answer = crud.get_answer(db, answer_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    return answer

@router.post("/questions/{question_id}/", response_model=schemas.AnswerRead)
def create_answer(question_id: int, answer: schemas.AnswerCreate, db: Session = Depends(get_db)):
    question = crud.get_question(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return crud.create_answer(db, question_id, answer)

@router.delete("/{answer_id}", response_model=schemas.AnswerRead)
def delete_answer(answer_id: int, db: Session = Depends(get_db)):
    answer = crud.delete_answer(db, answer_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    return answer