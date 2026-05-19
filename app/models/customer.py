from sqlalchemy import Column,Integer,String,Boolean,DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Customer(Base):
    __tablename__='customers'
    id= Column(Integer,primary_key=True,index=True)
    name= Column(String,nullable=False)
    phone_num= Column(String,nullable=False)
    address= Column(String,nullable=False)
    is_active= Column(Boolean,default=True)
    created_at= Column(DateTime,default=func.now())
    updated_at= Column(DateTime,default=func.now())
    