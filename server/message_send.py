'''Send message to a channel'''
# pylint: disable=W0622, C0413, C0411
from json import dumps
import sys
from .AccessError import AccessError, ValueError
import datetime
from datetime import timezone
sys.path.append("..")
import db
import Token

def message_send(token, channel_id, message, testing=False):
    '''Send message to a channel'''
    if testing:
        return dumps({'message_id' : 1})

    if not Token.isValid(token):
        raise AccessError("Not a valid token!")

    channel_id = int(channel_id)
    data = db.load_DB()
    u_id = db.get_from_token('u_id', token, data)

    if len(message) > 1000:
        raise ValueError('Message cannot contain more than 1000 characters')

    channel = [ch for ch in data['channels'] if ch['channel_id'] == channel_id][0]

    if u_id not in channel['members']:
        raise AccessError('Authorised user is not a member of channel with channel_id')

    time = datetime.datetime.now()
    timestamp = time.replace(tzinfo=timezone.utc).timestamp()

    msg_id = db.new_message_id(data)
    data['messages'].append({'message_id' : msg_id, 'u_id' : u_id, 'message' : message, \
    'time_created' : timestamp, 'reacts' : [], 'is_pinned' : False, 'in_channel' : channel_id, \
    'is_unread' : True})
    db.save_DB(data)
    return dumps({'message_id' : msg_id})
