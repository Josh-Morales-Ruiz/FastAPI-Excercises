from fastapi import APIRouter, Depends, HTTPException
from models.user_model import User
from database import get_db
from sql_models.sql_user_model import UserModel
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

router = APIRouter(tags=['user'])

@router.post('/register', status_code=201)
def signup(user: User, db: Session = Depends(get_db)):
    user_name = db.query(UserModel).filter(UserModel.username == user.username).first()
    
    if user_name:
        raise HTTPException(status_code=400, detail='Username already exists')
    
    password_hash = PasswordHash.recommended()
    hashed_password = password_hash.hash(user.password)
    
    #Enviamos esos datos a nuestra tabla de postgresql
    new_user = UserModel(
        username = user.username,
        password = hashed_password
    )
    
    #Como buena practica validamos que en realidad se haga el commit
    try:
        db.add(new_user)
        db.commit()
        #Actualizamos los datos generados con los datos de la db
        db.refresh(new_user)
    except Exception:
        db.rollback()
        raise
    
    #Retornamos como diccionario los nuevos datos generados
    return { "id" : new_user.id, "username" : new_user.username }

@router.post('/login')
def login(user: User, db: Session = Depends(get_db)):
    #Crear un token si los datos son correctos
    pass
