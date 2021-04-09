'''Adds existing user to a new channel'''
# pylint: disable=W0622, C0413, C0411
from .AccessError import AccessError, ValueError
from json import dumps
import sys
sys.path.append("..")
import Token
import db

def channel_invite(token, channel_id, u_id):
    '''Adds existing user to a new channel'''
    channel_id = int(channel_id)
    u_id = int(u_id)

    # Raise error if invalid token
    if not Token.isValid(token):
        raise AccessError('Invalid Token.')

    database = db.load_DB()
    # Check if valid channel_id
    if channel_id not in db.get_all_channels(database):
        raise ValueError('Invalid Channel ID.')

    # Check if authorised user is a member of the channel
    channel = db.get_channel_by_id(database, channel_id)
    if not db.get_from_token('u_id', token, database) in channel['members']:
        raise AccessError('You are not a member of this channel so \
you cannot invite others to join.')

	# Check if valid user ID for user to be adde
    if u_id not in db.get_all_users(database):
        raise AccessError('Invalid user id.')

    if u_id in channel['members']:
        raise AccessError('User already part of the channel')

    database['channels'].remove(channel)
    channel['members'].append(u_id)
    database['channels'].append(channel)
    db.save_DB(database)

    return dumps({})
