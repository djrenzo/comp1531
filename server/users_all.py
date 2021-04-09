'''Get a list of all users on the server'''
# pylint: disable=W0622, C0413, C0411
from .AccessError import AccessError
from json import dumps
import sys
sys.path.append("..")
import db
import Token

def users_all(token):
    '''Get a list of all users on the server'''
    data = db.load_DB()
    users = data['users']

    if not Token.isValid(token):
        raise AccessError("Not a valid token!")

    return dumps({'users': users})
