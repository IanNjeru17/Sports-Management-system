from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from base import Base

class Match(Base):
    __tablename__ = 'matches'
    
    id = Column(Integer, primary_key=True)
    home_team_id = Column(Integer, ForeignKey('teams.id'))
    away_team_id = Column(Integer, ForeignKey('teams.id'))
    field_id = Column(Integer, ForeignKey('fields.id'))
    referee_id = Column(Integer, ForeignKey('referees.id'))
    time_of_play = Column(DateTime, nullable=False)

    # Relationships
    home_team = relationship("Team", foreign_keys=[home_team_id], back_populates="home_matches")
    away_team = relationship("Team", foreign_keys=[away_team_id], back_populates="away_matches")
    field = relationship("Field") 
    referee = relationship("Referee")