from sqlalchemy import  Column, Integer, String
from app.config import Base

class User(Base):
    __tablename__ ="Users"
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)