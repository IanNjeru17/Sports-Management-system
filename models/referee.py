from sqlalchemy import Column, Integer, String
from base import Base

class Referee(Base):
    __tablename__ = 'referees'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
