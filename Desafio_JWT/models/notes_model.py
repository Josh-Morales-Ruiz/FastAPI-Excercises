from pydantic import BaseModel, Field, ConfigDict

class NotesCreate(BaseModel):
    title: str = Field(min_length=3)
    content: str = Field(min_length=10)
    
class NotesResponse(BaseModel):
    id: int
    title: str
    content: str
    user_id: int
    
    model_config = ConfigDict(from_attributes=True)
    