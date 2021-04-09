'''Create a new channel'''
# pylint: disable=W0622, C0413, C0411
from .AccessError import AccessError, ValueError
from json import dumps
import sys
sys.path.append("..")
import db
import Token

def channels_create(token, name, is_public):
    '''Create a new channel'''
    if not Token.isValid(token):
        raise AccessError('Invalid Token')

    database = db.load_DB()
    email = Token.decodeToken(token)['email']

    for user in database['users']:
        if email == user['email']:
            owner_id = user['u_id']
            break

	# # Confirm valid name
    if len(name) >= 20:
        raise ValueError('Use a name with less than 20 characters.')

 	# Create Channel
    channel_id = db.new_channel_id(database)
    database['channels'].append({'channel_id' : channel_id, 'is_public' : is_public, \
    'owner_members' : [owner_id], 'members' : [owner_id], 'name' : name})
    db.save_DB(database)
    return dumps({'channel_id': channel_id})
