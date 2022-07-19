import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help='This field cannot be left blank'
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help='This field cannot be left blank'
    )

    def post(self):
        body = UserRegister.parser.parse_args()
        username = body.get('username')

        if UserModel.find_by_username(username):
            return {'Message':f'The user {username} already exists'}, 400
        
        user = UserModel(**body)
        user.save_to_db()
        return {'Message':'User created successfully'}, 201

