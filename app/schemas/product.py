from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    sku: str
    category_id: int
    sale_price: float
    cost_price: float
    min_stock_level: int

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    sku: Optional[str] = None
    category_id: Optional[int] = None
    sale_price: Optional[float] = None
    cost_price: Optional[float] = None
    min_stock_level: Optional[int] = None

class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    sku: str
    category_id: Optional[int] = None
    sale_price: float
    cost_price: float
    min_stock_level: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True