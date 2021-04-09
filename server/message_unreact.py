'''Remove react from message'''
# pylint: disable=W0622, C0413, C0411
from json import dumps
import sys
from .AccessError import AccessError, ValueError
sys.path.append("..")
import db
import Token

def message_unreact(token, message_id, react_id):
    '''Remove react from message'''
    if not Token.isValid(token):
        raise AccessError("Not a valid token!")

    if not message_id:
        raise ValueError('Invalid message_id')

    if react_id != '1':
        raise ValueError('Invalid react id')

    message_id = int(message_id)
    react_id = int(react_id)

    data = db.load_DB()
    u_id = db.get_from_token('u_id', token, data)

    if message_id not in db.get_all_messages(data):
        raise ValueError('Invalid message_id')

    reactusers = db.get_react_users(data, u_id, message_id, react_id, False)
    if u_id not in reactusers:
        raise AccessError('Message with ID message_id does not contain\
 an active React with ID react_id')

    cur_message = [msg for msg in data['messages'] if msg['message_id'] == message_id][0]
    for react in cur_message['reacts']:
        if react['react_id'] == react_id:
            react['u_ids'].remove(u_id)
    db.save_DB(data)
    return dumps({})
