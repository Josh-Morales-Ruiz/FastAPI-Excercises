from fastapi import FastAPI
from routers import categories, tasks

app = FastAPI()

app.include_router(categories.router , prefix='/categories')
app.include_router(tasks.router , prefix='/tasks')
