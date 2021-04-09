'''Change a user profile's name'''
# pylint: disable=W0622, C0413, C0411
from .AccessError import AccessError, ValueError
import sys
sys.path.append("..")
import db
import Token

def user_profile_setname(token, name_first, name_last):
    '''Change a user profile's name'''
    if not Token.isValid(token):
        raise AccessError("Not a valid token!")

    database = db.load_DB()
    if len(name_first) > 50 or len(name_first) < 0:
        raise ValueError('Your First Name cannot be more than 50 characters.')

    if len(name_last) > 50 or len(name_last) < 0:
        raise ValueError('Your Last Name cannot be more than 50 characters.')
    u_id = db.get_from_token('u_id', token, database)

    for user in database['users']:
        if u_id == user['u_id']:
            user['name_first'] = name_first
            user['name_last'] = name_last

    db.save_DB(database)
    return {}
