'''Get user profile details'''
# pylint: disable=W0622, C0413, C0411
import sys
from .AccessError import ValueError
from json import dumps
sys.path.append("..")
import db
import Token

def user_profile(token, u_id):
    '''Get user profile details'''
    if not Token.isValid(token):
        raise ValueError("Not a valid token!")

    data = db.load_DB()
    user = [user for user in data['users'] if user['u_id'] == int(u_id)][0]
    return dumps(user)
