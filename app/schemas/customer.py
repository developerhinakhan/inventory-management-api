from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CustomerCreate(BaseModel):
    name:str
    phone_num:str
    address:str
    
class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    phone_num: Optional[str] = None
    address: Optional[str] = None
    
class CustomerResponse(BaseModel):
    id:int
    name:str
    phone_num:str
    address:str
    is_active:bool
    created_at:datetime
    updated_at:datetime
    class Config:
        from_attributes=True