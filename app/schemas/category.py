from pydantic import BaseModel
from datetime import datetime

class CategoryCreate(BaseModel):
    name:str
    
class CategoryResponse(BaseModel):
    id:int
    name:str
    is_active:bool
    created_at:datetime
    updated_at:datetime    
    class Config:
        from_attributes =  True 
        
    
    
    
    
    