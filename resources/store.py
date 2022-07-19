from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message' : 'Store do not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message' : f'A store with the name {name} already exists'}, 400
        store = StoreModel(name)
        store.save_to_db()

        return store.json(), 201


    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if not store:
            return {'message' : f'A store with the name {name} does not exists'}, 400
        
        store.delete_from_db()
        return {'message' : f'The store {name} was deleted successfully'}


class StoreList(Resource):
    def get(self):
        return {'stores' : [store.json() for store in StoreModel.query.all()]}
