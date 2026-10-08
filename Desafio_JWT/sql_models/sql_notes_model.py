from sqlalchemy import Column, Integer, String
from database import Base

class NotesModel(Base):
    __tablename__ = "notes"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey=('users.id'), nullable=False)