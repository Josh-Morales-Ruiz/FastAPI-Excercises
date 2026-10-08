from pydantic import BaseModel, Field

class NotesCreate(BaseModel):
    title: str = Field(min_length=3)
    content: str = Field(min_length=10)
    user_id: int
    