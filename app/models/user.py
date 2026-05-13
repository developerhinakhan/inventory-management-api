from sqlalchemy import Column,String,Boolean,Integer,DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class User(Base):
    __tablename__= "users"
    id= Column(Integer,primary_key=True,index=True)
    name= Column(String,nullable=False)
    email= Column(String,nullable=False,unique=True)
    password= Column(String,nullable=False)
    role= Column(String)
    is_active= Column(Boolean,default=True)
    created_at= Column(DateTime, default=func.now())
    updated_at= Column(DateTime, default= func.now())