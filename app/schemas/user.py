from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str
    role_id: int  # Se envía el ID del rol al crear

class UserOut(UserBase):
    id: int
    role_name: str  
   

    class Config:
        orm_mode = True