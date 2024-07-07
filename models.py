from sqlalchemy import Column,Integer,String
from database import Base

class Users(Base):
    __tablename__ = "users"
    
    id  = Column(Integer,primary_key=True,index=True)
    full_name  = Column(String)
    username = Column(String,unique=True)
    hashed_password = Column(String)
    email = Column(String)     
