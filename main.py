from typing import Union

from fastapi import FastAPI

from schemas import EventSchema






# INITIATE IT
app = FastAPI()

# define route
@app.get('/')
def index():
    return {"message": "Welcome to my first API"}

# Return a list of events (you can add sample data)
@app.get('/events')
def events():
    return []

# Include the event_id parameter in the function
@app.get('/events/{event_id}')
def event():
    return {}

@app.post('/events')
def create_event(event:EventSchema):
    print(event)
    return {"message": "Event created successfully"}

@app.patch('/events/{event_id}')
def update_event(event_id: int):
    return {"message": f"Event {event_id} updated successfully"}

@app.delete('/events/{event_id}')
def delete_event(event_id: int):
    return {"message": f"Event {event_id} deleted successfully"}
