'''All functions related to standups'''
# pylint: disable=W0622, C0413, C0411, R0903
from .AccessError import AccessError, ValueError
from json import dumps
import sys
import datetime
from datetime import timezone
from threading import Timer
sys.path.append("..")
import db
import Token

class Standup():
    '''Standup Class'''
    def __init__(self, channel_id, length):
        self.channel_id = channel_id
        self.length = length
        self.time_finish = (datetime.datetime.now() + datetime.timedelta(seconds=length))\
        .timestamp()

def standup_finish(token, channel_id, standup_id):
    '''finish standup and print summary to channel'''
    data = db.load_DB()
    u_id = db.get_from_token('u_id', token, data)

    summary = []
    for standup in data['standups']:
        if standup['standup_id'] == standup_id:
            for message in standup['messages']:
                summary.append(f"{message['name_first']}: {message['message']}")

    summary = '\n'.join(summary)
    print(summary)

    time = datetime.datetime.now()
    timestamp = time.replace(tzinfo=timezone.utc).timestamp()

    msg_id = db.new_message_id(data)
    data['messages'].append({'message_id' : msg_id, 'u_id' : u_id, 'message' :\
     summary, 'time_created' : timestamp, 'reacts' : [], 'is_pinned' : False, \
     'in_channel' : channel_id, 'is_unread' : True})
    db.save_DB(data)

def standup_start(token, channel_id, length):
    '''start a standup timer'''
    if not Token.isValid(token):
        raise AccessError("Not a valid token!")

    data = db.load_DB()
    channel_id = int(channel_id)
    length = int(length)

    if channel_id not in db.get_all_channels(data):
        raise ValueError("Invalid channel_id")

    u_id = db.get_from_token('u_id', token, data)

    valid = False
    for channel in data['channels']:
        if channel['channel_id'] == channel_id:
            if u_id in channel['members']:
                valid = True

    if not valid:
        raise AccessError("Not a member of this channel")

    snew = Standup(channel_id, length)
    standup_id = db.new_standup_id(data)
    data['standups'].append({'standup_id' : standup_id, 'in_channel' : channel_id, \
    'time_finish' : snew.time_finish, 'messages' : []})
    db.save_DB(data)

    timer = Timer(length, standup_finish, args=(token, channel_id, standup_id))
    timer.start()
    return dumps({'time_finish' : snew.time_finish})


def standup_active(token, channel_id):
    '''check if a standup is currently active'''
    if not Token.isValid(token):
        raise AccessError("Not a valid token!")

    data = db.load_DB()
    channel_id = int(channel_id)

    if channel_id not in db.get_all_channels(data):
        raise ValueError("Invalid channel_id")

    for standup in data['standups']:
        if datetime.datetime.now().timestamp() < standup['time_finish'] and \
        standup['in_channel'] == channel_id:
            return dumps({'is_active' : True, 'time_finish' : standup['time_finish']})

    return dumps({'is_active' : False, 'time_finish' : None})


def standup_send(token, channel_id, message):
    '''send messages while standup is in progress'''
    if not Token.isValid(token):
        raise AccessError("Not a valid token!")

    channel_id = int(channel_id)
    data = db.load_DB()
    u_id = db.get_from_token('u_id', token, data)
    name_first = db.get_from_token('name_first', token, data)

    if len(message) > 1000:
        raise ValueError('Message cannot contain more than 1000 characters')

    active_standup = False
    for standup in data['standups']:
        if datetime.datetime.now().timestamp() < standup['time_finish'] and \
        standup['in_channel'] == channel_id:
            cur_standup = standup
            active_standup = True

    if not active_standup:
        raise ValueError('An active standup is not currently running in this channel')

    channel = [ch for ch in data['channels'] if ch['channel_id'] == channel_id][0]
    if u_id not in channel['members']:
        raise AccessError('Authorised user is not a member of channel with channel_id')

    cur_standup['messages'].append({'u_id' : u_id, 'message' : message, 'name_first': name_first})
    db.save_DB(data)

    return dumps({})
