'''Change a user profile's handle'''
# pylint: disable=W0622, C0413, C0411
import sys
from .AccessError import AccessError, ValueError
sys.path.append("..")
import db
import Token

def user_profile_sethandle(token, handle_str):
    '''Change a user profile's handle'''
    if not Token.isValid(token):
        raise AccessError("Not a valid token!")

    database = db.load_DB()
    u_id = db.get_from_token('u_id', token, database)
    users = database['users']

    if len(handle_str) > 20 or len(handle_str) < 3:
        raise ValueError('handle_str must be between 3 and 20 characters')

    #check if handle_str is already used
    if users:
        all_handle = [user['handle_str'] for user in users]
    else:
        all_handle = []

    if handle_str in all_handle:
        raise ValueError('handle is already used by another user')

    for user in database['users']:
        if u_id == user['u_id']:
            user['handle_str'] = handle_str

    db.save_DB(database)
    return {}
