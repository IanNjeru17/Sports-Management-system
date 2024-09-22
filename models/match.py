from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from base import Base
from datetime import datetime

class Match(Base):
    __tablename__ = 'matches'
    
    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    field_id = Column(Integer, ForeignKey('fields.id'), nullable=False)
    referee_id = Column(Integer, ForeignKey('referees.id'), nullable=False)
    time_of_play = Column(DateTime, nullable=False)  # New field for match time

    team = relationship('Team', back_populates='matches')
    field = relationship('Field')
    referee = relationship('Referee')

    def __repr__(self):
        return f"<Match {self.team.name} at {self.time_of_play} on {self.field.name} with {self.referee.name}>"
