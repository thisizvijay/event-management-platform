from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from data.base import Base

class Ticket(Base):
    __tablename__ = 'tickets'
    
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    ticket_price = Column(Integer)
    ticket_quantity = Column(Integer)
    
    user = relationship("User", back_populates="tickets")
    event = relationship("Event", back_populates="tickets")