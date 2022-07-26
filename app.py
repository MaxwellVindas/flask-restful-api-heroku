from datetime import timedelta
import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemsList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['DEBUG'] = True
api = Api(app) # In charge to registry the endpoints

app.secret_key = 'SUPER-SECRET'
jwt = JWT(app, authenticate, identity) # Create the /auth endpoint used to authorization
# config JWT to expire within half an hour
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Disable the tracking extension, SQLAlchemy already has one
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL_CUSTOM', 'sqlite:///sqlite_data.db') # Set type and path of DB

#Adding the endpoints to the Api object
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemsList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')


if __name__ == '__main__':
    from db import db
    db.init_app(app) # Initialize SQLAlchemy to ensure that we can use it

    if app.config['DEBUG']:
        @app.before_first_request # Call this function automatically before the first request
        def create_tables():
            db.create_all() # SQLAlchemy create the DB for us automatically
            
    
    app.run(port=5000)