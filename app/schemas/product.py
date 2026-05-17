from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductCreate(BaseModel):
    name: str
    description: Optional[str]
    sku: str
    category_id: int
    sale_price: float
    cost_price: float
    min_stock_level: int
    
class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    sku: str
    category_id: int
    sale_price: float
    cost_price: float
    min_stock_level: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes=True
