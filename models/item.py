from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    # ForeignKey between Item with Store
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id')) # store is the table id is column
    store = db.relationship('StoreModel') # Name that will have the store inside item

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        # SQLAlchemy can translate the db raw to ItemModel class automatically
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name LIMIT=1

    def save_to_db(self):
        # SQLAlchemy can translate ItemModel instance to raw automatically
        db.session.add(self) # Session is a list of objects that will be store in DB
        db.session.commit() # Store the objects of Session to DB

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_all():
        # list(map(ItemModel.json, ItemModel.query.all()))
        # list(map(lambda item : item.json(), ItemModel.query.all()))
        return [item.json() for item in ItemModel.query.all()]
        