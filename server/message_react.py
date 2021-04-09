'''Join existing user to a new channel'''
# pylint: disable=W0622, C0413, C0411
import sys
from json import dumps
from .AccessError import AccessError, ValueError
sys.path.append("..")
import db
import Token

def message_react(token, message_id, react_id):
    '''Join existing user to a new channel'''
    if not Token.isValid(token):
        raise AccessError("Not a valid token!")

    if not message_id:
        raise ValueError('Invalid message_id')

    if react_id != "1":
        raise ValueError('Invalid react id')

    message_id = int(message_id)
    react_id = int(react_id)
    data = db.load_DB()
    u_id = db.get_from_token('u_id', token, data)

    if message_id not in db.get_all_messages(data):
        raise ValueError('Invalid message_id')

    if u_id in db.get_react_users(data, u_id, message_id, react_id, False):
        raise AccessError('Message with ID message_id already\
 contains an active React with ID react_id')

    cur_message = [msg for msg in data['messages'] if msg['message_id'] == message_id][0]
    channel = [channel for channel in data['channels'] if channel['channel_id'] ==\
     cur_message['in_channel']][0]

    valid = False
    for react in cur_message['reacts']:
        if 'react_id' in react.keys():
            if react['react_id'] == react_id:
                react['u_ids'].append(u_id)
                valid = True

    if not valid:
        cur_message['reacts'].append({'react_id': react_id, 'u_ids': \
        db.get_react_users(data, u_id, message_id, react_id)})
    db.save_DB(data)
    return dumps({})
