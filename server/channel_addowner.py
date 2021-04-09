'''Add ownership rights to a user of a channel'''
# pylint: disable=W0622, C0413, C0411
import sys
from .AccessError import AccessError, ValueError
sys.path.append("..")
import db
import Token

def channel_addowner(token, channel_id, u_id):
    '''Add ownership rights to a user of a channel'''
    if not Token.isValid(token):
        raise AccessError("Not a valid token!")

    channel_id = int(channel_id)
    u_id = int(u_id)
    database = db.load_DB()

    if channel_id not in db.get_all_channels(database):
        raise ValueError('Channel (based on ID) does not exist')

    for channel in database['channels']:
        if channel['channel_id'] == channel_id:
            if u_id in channel['owner_members']:
                raise ValueError('User already owner of this channel')

            if db.get_from_token('u_id', token, database) not in\
             channel['owner_members'] and \
             db.get_from_token('permission_id', token, database) == 3:
                raise AccessError('authorised user is not an owner of \
the slackr, or an owner of this channel')

            channel['owner_members'].append(u_id)
    db.save_DB(database)
    return {}
