from app.db.base import SessionLocal
from sqlalchemy.orm import Session

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()