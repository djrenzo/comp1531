'''Log a user in'''
# pylint: disable=W0622, C0413, C0411
from json import dumps
from .AccessError import ValueError
import sys
sys.path.append("..")
import Token
import db

def auth_login(email, password):
    '''Change a users permissions'''
    database = db.load_DB()
    users = database["users"]
    hashed_password = db.hash_password(password)

    if not db.check_mail(email):
        raise ValueError(description="Email entered is not a valid email")

    allemails = [user['email'] for user in users]
    if email not in allemails:
        raise ValueError("Email entered does not belong to a user")

    u_id = [user['u_id'] for user in users if user['email'] == email][0]
    token = Token.generateToken(email)
    psw = db.get_from_token('password', token, database)

    if psw != hashed_password:
        raise ValueError("Password is not correct")

    return dumps({'u_id': u_id, 'token' : token})
