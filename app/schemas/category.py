from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CategoryCreate(BaseModel):
    name:str
    
class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    
class CategoryResponse(BaseModel):
    id:int
    name:str
    is_active:bool
    created_at:datetime
    updated_at:datetime    
    class Config:
        from_attributes =  True 
        
    
    
    
    
    