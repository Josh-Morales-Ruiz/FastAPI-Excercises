from fastapi import APIRouter, Depends
from models.user_model import User
from database import get_db
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

router = APIRouter(tags=['user'])

@router.get('/test')
def hi(db: Session = Depends(get_db)):
    return { "message" : "Hi from postgresql"}

@router.post('/register')
def signup(user: User):
    pass

@router.post('/login')
def login():
    pass
