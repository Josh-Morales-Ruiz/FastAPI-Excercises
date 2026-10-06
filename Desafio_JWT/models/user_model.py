from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    username: str = Field(min_length=3)
    password: str = Field(min_length=8)