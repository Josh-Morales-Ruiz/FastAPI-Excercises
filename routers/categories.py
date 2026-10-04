from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(tags=["Categorias"])

class CategoryScheme(BaseModel):
    id: int
    name: str = Field(min_length=3)


db_categories = []

@router.post('/')
def create_category(category: CategoryScheme):
    for cat in db_categories:
        if cat["id"] == category.id:
            raise HTTPException(status_code=400, detail="La categoria ya existe")
    
    new_cat = category.model_dump()
    db_categories.append(new_cat)
    
    return { "message" : "Se creo una nueva categoria", "category" : new_cat }

@router.get('/')
async def get_categories():
    return { "categories" : db_categories }