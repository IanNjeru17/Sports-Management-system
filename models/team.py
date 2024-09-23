from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Team(Base):
    __tablename__ = 'teams'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    # Relationships for matches
    home_matches = relationship("Match", foreign_keys='Match.home_team_id', back_populates="home_team")
    away_matches = relationship("Match", foreign_keys='Match.away_team_id', back_populates="away_team")
