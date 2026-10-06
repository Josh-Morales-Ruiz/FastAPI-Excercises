from Server.Tracker_API.routers.categories import db_categories
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(tags=["Tareas"])

class TaskSchema(BaseModel):
    id: int
    title: str = Field(min_length=3)
    description: str = ""
    completed: bool = False
    category_id: int
    
db_tasks = []
    
@router.post('/')
def create_task(task: TaskSchema):
    cat_exist = any(cat["id"] == task.category_id for cat in db_categories)
    if not cat_exist:
        raise HTTPException(status_code=404, detail="La categoria especificada no existe")
    
    for id in db_tasks:
        if id["id"] == task.id:
            raise HTTPException(status_code=400, detail="No se admiten repetidos")
    
    new_task = task.model_dump()
    db_tasks.append(new_task)
    
    return { "message" : "Se creo una nueva tarea", "task" : new_task }
    
    
@router.get('/')
def create_task(completed: bool | None = None):
    if completed is not None:
        tasks = [t for t in db_tasks if t["completed"] == completed]
        return { "tasks" : tasks }
    
    return { "tasks" : db_tasks }

@router.put('/{task_id}/toggle')
def update_task(task_id: int):
    for task in db_tasks:
        task["completed"] = not task["completed"]
        return { "message" : "Estado actualizado", "task" : task}
    
    raise HTTPException(status_code=404, detail="Tarea no encontrada")


