from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Feedback(Base):
    __tablename__ = 'feedback'
    
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    rating = Column(Integer)
    comment = Column(String)
    
    user = relationship("User", back_populates="feedback")
    event = relationship("Event", back_populates="feedback")