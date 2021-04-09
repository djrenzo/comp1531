'''Edit a message'''
# pylint: disable=W0622, C0413, C0411
from .AccessError import AccessError, ValueError
from json import dumps
import sys
sys.path.append("..")
import db
import Token

def message_edit(token, message_id, message):
    '''Edit a message'''
    if not Token.isValid(token):
        raise AccessError("Not a valid token!")

    data = db.load_DB()
    message_id = int(message_id)
    if message_id not in db.get_all_messages(data):
        raise ValueError('Message doesnt exist')

    u_id = db.get_from_token('u_id', token, data)
    cur_message = [msg for msg in data['messages'] if msg['message_id'] == message_id][0]
    channel = [channel for channel in data['channels'] if channel['channel_id'] ==\
     cur_message['in_channel']][0]

    if u_id != cur_message['u_id'] and db.get_from_token('permission_id', token, data) == 3 and\
     u_id not in channel['owner_members']:
        raise AccessError('The authorised user is an admin or owner of this channel or the slackr')

    if message == "":
        data['messages'].remove(cur_message)

    else:
        cur_message['message'] = message
        data['messages'].remove(cur_message)
        data['messages'].append(cur_message)

    db.save_DB(data)
    return dumps({})
