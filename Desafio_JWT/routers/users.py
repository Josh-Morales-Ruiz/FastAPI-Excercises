from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.user_model import User
from services.auth_service import create_access_token
from database import get_db
from sql_models.sql_user_model import UserModel
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

router = APIRouter(tags=['user'])

password_hash = PasswordHash.recommended()

@router.post('/register', status_code=201)
def signup(user: User, db: Session = Depends(get_db)):
    user_name = db.query(UserModel).filter(UserModel.username == user.username).first()
    
    if user_name:
        raise HTTPException(status_code=400, detail='Username already exists')

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
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.username == form_data.username).first()
    
    if not user or not password_hash.verify(
        form_data.password,
        user.password
    ):
        raise HTTPException(status_code=401, detail="Incorrect data", headers={"WWW-Authenticate" : "Bearer" })
   
    #Crear un token si los datos son correctos
    access_token = create_access_token(data={ "sub": user.username })
    
    return {
        "access_token" : access_token,
        "token_type" : "bearer"
    }
