from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class StockIn(BaseModel):
    product_id:int
    quantity:int
    
class StockOut(BaseModel):
    product_id:int
    quantity:int


class InventoryResponse(BaseModel):
    id:int
    product_id:int
    quantity:int
    transaction_type:str
    current_stock:int
    created_at:datetime
    updated_at:datetime
    class Config:
        from_attributes=True
