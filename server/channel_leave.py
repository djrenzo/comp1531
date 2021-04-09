'''Join existing user to a new channel'''
# pylint: disable=W0622, C0413, C0411
import sys
from .AccessError import AccessError, ValueError
sys.path.append("..")
import db
import Token

def channel_leave(token, channel_id):
    '''Remove existing user from a channel'''
    if not Token.isValid(token):
        raise AccessError("Not a valid token!")

    channel_id = int(channel_id)
    database = db.load_DB()

    if channel_id not in db.get_all_channels(database):
        raise ValueError('Channel (based on ID) does not exist')

    u_id = db.get_from_token('u_id', token, database)
    channel = db.get_channel_by_id(database, channel_id)

    for channel in database['channels']:
        if channel['channel_id'] == channel_id:
            if u_id in channel['members']:
                channel['members'].remove(u_id)
    db.save_DB(database)
    return {}
