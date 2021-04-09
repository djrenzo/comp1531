'''Send a message at a later point in time'''
# pylint: disable=W0622, C0413, C0411
import sys
from datetime import datetime
from threading import Timer
from json import dumps
from .AccessError import AccessError, ValueError
from .message_send import message_send
sys.path.append("..")
import db
import Token

def message_sendlater(token, channel_id, message, time_sent, testing=False):
    '''Send a message at a later point in time'''
    if not Token.isValid(token):
        raise AccessError("Not a valid token!")

    database = db.load_DB()
    channel_id = int(channel_id)
    time_sent = float(time_sent)
    all_channel_ids = [channel['channel_id'] for channel in database['channels'] if \
    channel_id == channel['channel_id']]

    if channel_id not in all_channel_ids:
        raise ValueError('Channel ID is not a valid channel')

    if len(message) > 1000:
        raise ValueError('Message is greater than 1000')

    if time_sent < datetime.now().timestamp():
        raise ValueError('Time sent is a time in the past')

    length = time_sent - datetime.now().timestamp()

    timer = Timer(length, message_send, args=(token, channel_id, message, testing))
    timer.start()
    return dumps({})
