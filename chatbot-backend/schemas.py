from pydantic import BaseModel
from typing import Optional, List, Dict

class UserCreate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    thred_id: Optional[str] = None
    prompt: Optional[str] = None
    thread_data: Optional[List[Dict]] = None
    id: Optional[int] = None

class UserResponse(UserCreate):
    id: int
 

    class Config:
        orm_mode = True  # Tells Pydantic to treat the SQLAlchemy models like dictionaries
