from pydantic import BaseModel


class EventSchema(BaseModel):
    firstname:str
    lastname:str
    email:str
    phonenumber:str
    selectedEvent:str
    numberoftickets:str
    additionalInfo:str
    gender:str
