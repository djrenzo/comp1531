'''Gets the details of the channel'''
# pylint: disable=W0622, C0413, C0411
from .AccessError import AccessError, ValueError
from json import dumps
import sys
sys.path.append("..")
import db
import Token

def channel_details(token, channel_id):
    '''Gets the details of the channel'''
    if not Token.isValid(token):
        raise AccessError("Not a valid token!")

    database = db.load_DB()
    channel_id = int(channel_id)

    if channel_id not in db.get_all_channels(database):
        raise ValueError('Channel ID is not a valid channel')

    channel = db.get_channel_by_id(database, channel_id)

    if db.get_from_token("u_id", token, database) not in channel['members']:
        raise AccessError('Not authorised to view this channel')

    return dumps({
        "name" : channel['name'],
        "all_members" : [user for user in database["users"] if user['u_id'] in channel['members']],
        "owner_members" : [user for user in database["users"] if \
        user['u_id'] in channel['owner_members']]
        })
