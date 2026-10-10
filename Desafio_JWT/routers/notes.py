from fastapi import APIRouter, Depends, status, HTTPException
from services.auth_service import get_current_user
from models.notes_model import NotesCreate, NotesResponse
from sql_models.sql_user_model import UserModel
from sql_models.sql_notes_model import NotesModel
from sqlalchemy.orm import Session
from typing import Annotated
from database import get_db

router = APIRouter(tags=['notes'])

def get_note(db: Annotated[Session, Depends(get_db)], current_user: Annotated[UserModel, Depends(get_current_user)]) -> list[NotesModel]:
    notes = db.query(NotesModel).filter(NotesModel.user_id == current_user.id).all()
    return notes

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
        db.rollback()
        raise
    
    return new_note

@router.get('/', response_model=list[NotesResponse])
def read_note(
    list_notes: Annotated[list[NotesModel], Depends(get_note)]
):
    return list_notes

@router.delete('/{note_id}')
def delete_note(
    note_id: int,
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[UserModel, Depends(get_current_user)],
):
    note = db.query(NotesModel).filter(NotesModel.id == note_id, NotesModel.user_id == current_user.id).first()
    
    if note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='The Note does not exist')
    
    try:
        db.delete(note)
        db.commit()
    except Exception:
        db.rollback()
        raise
    
    return { "message" : "The note was deleted" }
    