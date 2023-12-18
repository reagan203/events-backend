from fastapi import FastAPI

# INITIATE IT
app = FastAPI()

# define route
@app.get('/')
def index():
    return {"message": "Welcome to my first API"}
