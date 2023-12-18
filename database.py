from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#connect to our pg db
engine = create_engine("postgres://admin:pozrfHxuB1VB5JVxkyEuvM72T3itLBq5@dpg-cm019ned3nmc738hqo90-a.frankfurt-postgres.render.com/events_gd4t")

#create connection with sessionmaker
SessionLocal =sessionmaker(bind=engine)

# def method to get db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    
