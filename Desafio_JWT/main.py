from fastapi import FastAPI
from routers import users, notes

app = FastAPI(title='Desafio_JWT')

app.include_router(users.router, prefix='/user')
app.include_router(notes.router, prefix='/notes')

