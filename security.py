from werkzeug.security import safe_str_cmp
from models.user import UserModel

# It's called when the user call /auth
# receive the username and password as parameters
# Try to Authenticate the user with the previous values
# Return JWT Token
def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user
# Every request that has decorator @jwt_required call this endpoint first
# Check the payload to verify the JWT Token
def identity(payload):
    user_id = payload.get('identity')
    return UserModel.find_by_id(user_id)