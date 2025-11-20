from sqlalchemy.orm import Session
from app import models, schemas

def get_questions(db: Session):
    return db.query(models.Question).all()

def get_question(db: Session, question_id: int): # вопрос по id
    return db.query(models.Question).filter(models.Question.id == question_id).first()

def create_question(db: Session, question: schemas.QuestionCreate):
    new_question = models.Question(text=question.text)
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question

def delete_question(db: Session, question_id: int):
    question = db.query(models.Question).filter(models.Question.id == question_id).first()
    if question:
        db.delete(question)
        db.commit()
    return question


def get_answer(db: Session, answer_id: int):
    return db.query(models.Answer).filter(models.Answer.id == answer_id).first()

def create_answer(db: Session, question_id: int, answer: schemas.AnswerCreate):
    new_answer = models.Answer(
        question_id=question_id,
        text=answer.text,
        user_id=answer.user_id
    )
    db.add(new_answer)
    db.commit()
    db.refresh(new_answer)
    return new_answer

def delete_answer(db: Session, answer_id: int):
    answer = db.query(models.Answer).filter(models.Answer.id == answer_id).first()
    if answer:
        db.delete(answer)
        db.commit()
    return answer
