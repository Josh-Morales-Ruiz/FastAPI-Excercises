from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.get('/task')
async def get_categories():
    return { "message" : "Hello from categories "}