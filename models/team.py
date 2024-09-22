from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Team(Base):
    __tablename__ = 'teams'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    matches = relationship('Match', back_populates='team')
