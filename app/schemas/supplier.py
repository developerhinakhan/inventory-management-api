from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SupplierCreate(BaseModel):
    name:str
    phone_num:str
    shop_name:str
    address:str
    
class SupplierUpdate(BaseModel):
    name: Optional[str] = None
    phone_num: Optional[str] = None
    shop_name: Optional[str] = None
    address: Optional[str] = None
    
class SupplierResponse(BaseModel):
    id:int
    name:str
    phone_num:str
    shop_name:str
    address:str
    is_active:bool
    created_at:datetime
    updated_at:datetime
    class Config:
        from_attributes=True