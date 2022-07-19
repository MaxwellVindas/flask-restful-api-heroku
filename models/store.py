from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    # Items is a list of Item Objects but this is heavy
    # We use lazy='dynamic' to do not create the list of Items Object yet
    items = db.relationship('ItemModel', lazy='dynamic') 

    def __init__(self, name):
        self.name = name
    
    def json(self):
        return {'name' : self.name, 'items' : [item.json() for item in self.items.all()]} # With all SQLAlchemy will create the list of Items

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name LIMIT=1

    def save_to_db(self):
        db.session.add(self) 
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()