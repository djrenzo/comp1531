'''Join existing user to a new channel'''
# pylint: disable=W0622, C0413, C0411
import sys
from .AccessError import AccessError, ValueError
sys.path.append("..")
import db
import Token

def channel_join(token, channel_id):
    '''Join existing user to a new channel'''
    if not Token.isValid(token):
        raise AccessError("Not a valid token!")

    channel_id = int(channel_id)
    database = db.load_DB()
    u_id = db.get_from_token('u_id', token, database)

    if channel_id not in db.get_all_channels(database):
        raise ValueError('Channel (based on ID) does not exist')

    channel = db.get_channel_by_id(database, channel_id)
    if not channel['is_public']:
        if db.get_from_token('permission_id', token, database) not in [1, 2]:
            raise AccessError('channel_id refers to a channel that is private \
    (when the authorised user is not an admin)')

    for channel in database['channels']:
        if channel['channel_id'] == channel_id:
            if not u_id in channel['members']:
                channel['members'].append(u_id)
    db.save_DB(database)

    return {}
