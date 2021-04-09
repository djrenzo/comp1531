'''Search all messages on server by keyword'''
# pylint: disable=W0622, C0413, C0411
from .AccessError import AccessError
from json import dumps
import sys
sys.path.append("..")
import db
import Token

def search(token, query_str):
    '''Search all messages on server by keyword'''
    if not Token.isValid(token):
        raise AccessError('Invalid Token.')

    data = db.load_DB()
    u_id = db.get_from_token('u_id', token, data)

    channels = [ch['channel_id'] for ch in data['channels'] if u_id in ch['members']]

    messages = []
    for channel in channels:
        messages.extend([msg for msg in data['messages'] if msg['in_channel'] == \
        channel if query_str in msg['message']])

    return dumps({'messages' : messages})
