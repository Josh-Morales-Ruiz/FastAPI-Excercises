from fastapi import APIRouter
from pydantic import BaseModel

class Categories(BaseModel):
    id: str
    name: str

router = APIRouter()

category = []

@router.post('/category/create')
def create_category(create_category: Categories):
    user = create_category
    
    if len(user.name) < 8:
        return { f"Name must have 8 characters at least" }
    
    category.append({ "id": user.id, "name": user.name })
    
    return { "message" : "A new category has been created", "category" : category }

@router.get('/category/info')
async def get_categories():
    return { "message" : "Categories listed successfully", "categories" : category }