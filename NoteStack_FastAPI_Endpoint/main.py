from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models, schemas, auth
from database import engine, SessionLocal

app = FastAPI()
# Reads all classes inheriting from Base and Converts them into SQL tables
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed = auth.hash_password(user.password)
    db_user = models.User(email=user.email, password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not auth.verify_password(user.password, db_user.password):
        raise HTTPException(401, "Invalid credentials")
    token = auth.create_token({"user_id": db_user.id})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/notes", response_model=schemas.NoteResponse)
def create_note(
    note: schemas.NoteCreate,
    user_id: int = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    db_note = models.Note(**note.dict(), owner_id=user_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@app.get("/notes", response_model=list[schemas.NoteResponse])
def get_notes(
    user_id: int = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(models.Note).filter(models.Note.owner_id == user_id).all()
