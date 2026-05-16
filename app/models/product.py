from sqlalchemy import Column,String,Boolean,Float,Integer,DateTime,ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__='product'
    id= Column(Integer,primary_key=True,index=True)
    name= Column(String(255),index=True,nullable=False)
    description= Column(String,nullable=True)
    sku= Column(String(100),index=True,nullable=True)
    category_id= Column(Integer,ForeignKey("category.id"))
    category=relationship("Category", backref="products")
    sale_price= Column(Float,nullable=False)
    cost_price= Column(Float,nullable=False)
    min_stock_level= Column(Integer,nullable=True)
    is_active= Column(Boolean,default=True)
    created_at= Column(DateTime, default=func.now())
    updated_at= Column(DateTime, default=func.now(),onupdate=func.now())
    


