from fastapi import FastAPI
from routers import users, notes
from database import Base, engine
from sql_models.sql_user_model import UserModel

Base.metadata.create_all(bind=engine)

app = FastAPI(title='Desafio_JWT')

app.include_router(users.router, prefix='/user')
app.include_router(notes.router, prefix='/notes')

