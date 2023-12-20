# models.py
from sqlalchemy import Column, Integer, String, DateTime, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    firstname = Column(String(50), index=True, nullable=False)
    lastname = Column(String(50), index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    phonenumber = Column(String(15), index=True, nullable=False)
    selectedEvent = Column(String(100), index=True, nullable=False)
    numberoftickets = Column(Integer, nullable=False)  # Change the data type to Integer
    additionalInfo = Column(String(255))
    gender = Column(String(10))
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), nullable=False)
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), onupdate=text("CURRENT_TIMESTAMP"), nullable=False)

    bookings = relationship("Booking", backref="event")

# schemas.py
from pydantic import BaseModel

class EventCreate(BaseModel):
    firstname: str
    lastname: str
    email: str
    phonenumber: str
    selectedEvent: str
    numberoftickets: int
    additionalInfo: str
    gender: str
