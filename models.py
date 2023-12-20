from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime,text,TIMESTAMP

# Create a base model
Base = declarative_base()

# Define the events model
class Event(Base):
    __tablename__ = "events"

    # Define columns
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50), index=True, nullable=False)
    lastname = Column(String(50), index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    phonenumber = Column(String(15), index=True, nullable=False)
    selectedEvent = Column(String(100), index=True, nullable=False)
    numberoftickets = Column(Integer, nullable=False)
    additionalInfo = Column(String(255))
    gender = Column(String(10))
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), nullable=False)
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), onupdate=text("CURRENT_TIMESTAMP"), nullable=False)
    
    
class User(Base):
    __tablename__ ="users"
    
    id=    Column(Integer, primary_key=True)
    firstname = Column(String(50), index=True, nullable=False)
    lastname = Column(String(50), index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    phonenumber = Column(String(15), index=True, nullable=False)
    