from Server.Tracker_API.routers import categories
from fastapi import FastAPI
from Server.Tracker_API.routers import tasks

app = FastAPI(title="Task tracker API")

app.include_router(categories.router , prefix='/categories')
app.include_router(tasks.router , prefix='/tasks')
