from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class Inventory(Base):
    __tablename__= 'inventory'
    id= Column(Integer,primary_key=True,index=True)
    product_id= Column(Integer,ForeignKey("product.id"))
    quantity= Column(Integer)
    transaction_type= Column(String)
    current_stock= Column(Integer)
    created_at= Column(DateTime,default=func.now())
    updated_at= Column(DateTime,default=func.now())
    