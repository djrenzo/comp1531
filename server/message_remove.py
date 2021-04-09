'''Remove message from channel'''
# pylint: disable=W0622, C0413, C0411
import sys
from json import dumps
from .AccessError import AccessError, ValueError
sys.path.append("..")
import db
import Token

def message_remove(token, message_id):
    '''Remove message from channel'''
    if not Token.isValid(token):
        raise AccessError("Not a valid token!")

    message_id = int(message_id)
    data = db.load_DB()
    u_id = db.get_from_token('u_id', token, data)

    if message_id not in db.get_all_messages(data):
        raise ValueError('Message (based on ID) no longer exists')

    message = [msg for msg in data['messages'] if msg['message_id'] == message_id][0]
    channel = [channel for channel in data['channels'] if channel['channel_id'] ==\
     message['in_channel']][0]

    if u_id != message['u_id'] and db.get_from_token('permission_id', token, data) == 3\
     and u_id not in channel['owner_members']:
        raise AccessError('The authorised user is an admin or owner of this channel or the slackr')

    data['messages'].remove(message)
    db.save_DB(data)
    return dumps({})
