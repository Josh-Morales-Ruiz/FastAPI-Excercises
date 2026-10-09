from fastapi import APIRouter, Depends, status
from services.auth_service import get_current_user
from models.notes_model import NotesCreate, NotesResponse
from sql_models.sql_user_model import UserModel
from sql_models.sql_notes_model import NotesModel
from sqlalchemy.orm import Session
from typing import Annotated
from database import get_db

router = APIRouter(tags=['notes'])

@router.post('/', status_code=status.HTTP_201_CREATED)
def add_note(
    note_data: NotesCreate, 
    current_user: Annotated[UserModel, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)]
):
    new_note = NotesModel(
        title=note_data.title,
        content=note_data.content,
        user_id=current_user.id
    )
    
    try:
        db.add(new_note)
        db.commit()
        db.refresh(new_note)
    except Exception:
        db.rollback
        raise
    
    return new_note

@router.get('/')
def read_note():
    pass

@router.delete('/{note_id}')
def delete_note(note_id: int):
    pass