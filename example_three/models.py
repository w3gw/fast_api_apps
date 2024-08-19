from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from .db_conn import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    hashed_password = Column(String, index=True)
    
 