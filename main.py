from fastapi import FastAPI
from routers import categories, tasks

app = FastAPI(title="Task tracker API")

app.include_router(categories.router , prefix='/categories')
app.include_router(tasks.router , prefix='/tasks')
