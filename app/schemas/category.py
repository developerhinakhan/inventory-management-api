from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime

class CategoryCreate(BaseModel):
    name:str
    
class CategoryResponse(BaseModel):
    id:int
    name:str
    is_active:bool
    created_at:datetime
    updated_at:datetime    
    class config:
        orm_mode=  True #tells Pydantic that the model can read data directly from SQLAlchemy ORM objects.
    
    
    
    
    