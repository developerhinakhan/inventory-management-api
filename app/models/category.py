from sqlalchemy import Column,String,Boolean,Integer,DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Category(Base):
    __tablename__ = 'category'
    id= Column(Integer,primary_key=True,index=True)
    name= Column(String,index= True)
    is_active= Column(Boolean,default=True)
    created_at= Column(DateTime,default=func.now())
    updated_at= Column(DateTime,default=func.now())