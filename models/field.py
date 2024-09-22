from sqlalchemy import Column, Integer, String
from base import Base

class Field(Base):
    __tablename__ = 'fields'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
