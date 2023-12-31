from pydantic import BaseModel


class EventSchema(BaseModel):
    firstname:str
    lastname:str
    email:str
    phonenumber:str
    selectedEvent:str
    numberoftickets:int
    additionalInfo:str
    gender:str


class UserSchema(BaseModel):
    firstname:str
    lastname:str
    email:str
    phonenumber:str
        
        