'''Load and return all messages from a channel'''
# pylint: disable=W0622, C0413, C0411, C0103
from .AccessError import AccessError, ValueError
from json import dumps
import sys
from operator import itemgetter
sys.path.append("..")
import db
import Token

def channel_messages(token, channel_id, start):
    '''Load and return all messages from a channel'''
    if not Token.isValid(token):
        raise AccessError("Not a valid token!")

    database = db.load_DB()
    channel_id = int(channel_id)
    start = int(start)

    if channel_id not in db.get_all_channels(database):
        raise ValueError('Channel ID is not a valid channel')

    if database['messages']:
        if int(start) > len([message for message in database['messages'] \
        if message['in_channel'] == channel_id]):
            raise ValueError('start is greater than or equal to the total\
     number of messages in the channel')
    u_id = db.get_from_token("u_id", token, database)

    if database['messages']:
        messages = [msg for msg in database['messages'] if msg['in_channel'] == channel_id]
        messages = sorted(messages, key=itemgetter('time_created'), reverse=True)
        end = start + 50

        fmessages = []
        for message in messages:
            d = {}
            d['message_id'] = message['message_id']
            d['u_id'] = message['u_id']
            d['message'] = message['message']
            d['time_created'] = message['time_created']
            d['is_pinned'] = message['is_pinned']

            reacts = []
            for react in message['reacts']:
                d2 = {}
                d2['react_id'] = react['react_id']
                d2['u_ids'] = react['u_ids']
                d2['is_this_user_reacted'] = db.get_user_reacted(database, \
                u_id, message['message_id'], react['react_id'])
                reacts.append(d2)

            d['reacts'] = reacts
            fmessages.append(d)

        if len(messages) < 50:
            end = -1
    else:
        fmessages = []
        end = -1

    return dumps({'messages' : fmessages, 'start' : start, 'end' : end})
