from typing import Union
from fastapi import FastAPI, Depends,HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
from models import Event
from schemas import EventSchema

# INITIATE IT
app = FastAPI()

# define route
@app.get('/')
def index():
    return {"message": "Welcome to my first API"}

# Return a list of events (you can add sample data)
@app.get('/events')
def events(db: Session = Depends(get_db)):
    events =db.query(Event).all()
    return events

# Include the event_id parameter in the function
@app.get('/events/{event_id}')
def event(event_id: int, db: Session = Depends(get_db)):
    event = db .query(Event).filter(Event.id ==event_id).first()
    return event

@app.post('/events')
def create_event(event:EventSchema,db: Session = Depends(get_db) ):
    #unpacks a dict and passes it as key value pairs
    new_event =Event(**event.model_dumpI())
    #adds the events to the transaction
    db.add(new_event)
    #commit the transaction
    db.commit()
    #get event from the db again
    db.refresh(new_event)
    return {"message": "Event created successfully","event": new_event}

@app.patch('/events/{event_id}')
def update_event(event_id: int):
    return {"message": f"Event {event_id} updated successfully"}

@app.delete('/events/{event_id}')
def delete_event(event_id: int, db:Session=Depends(get_db)):
    delete_event=db.query(Event).filter(Event.id ==event_id).first()
    if delete_event==None:
     raise HttpException(status_code=status.HTTP_404_NOT_FOUND,
                         detail=f"Event{event_id}does not exist")
    else:
     delete_event.delete()
     #running transactions with db
     db.commit()

     return response(status_code=status.HTTP_204_NO_CONTENT)
