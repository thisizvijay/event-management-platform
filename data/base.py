from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from data.models.feedback import Feedback
from data.models.tickets import Ticket

engine = create_engine('your_database_url')
Base = declarative_base()
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_ticket = Ticket(event_id=1, user_id=1, ticket_price=50, ticket_quantity=2)
session.add(new_ticket)
session.commit()

new_feedback = Feedback(event_id=1, user_id=1, rating=5, comment="Great event!")
session.add(new_feedback)
session.commit()

tickets = session.query(Ticket).all()
feedbacks = session.query(Feedback).all()