import imp
from app import app
from db import db

db.init_app(app) # Initialize SQLAlchemy to ensure that we can use it
@app.before_first_request # Call this function automatically before the first request
def create_tables():
    db.create_all() # SQLAlchemy create the DB for us automatically