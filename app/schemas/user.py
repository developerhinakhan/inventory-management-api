from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    name:str
    email: EmailStr
    password:str
    role:Optional[str]="staff"
    
class UserResponse(BaseModel):
    id:int
    name:str
    email:EmailStr
    role:str
    created_at:datetime
    updated_at:datetime
    class Config:
        from_attributes= True
