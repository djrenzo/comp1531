'''List all the channels of a certain user'''
# pylint: disable=C0413
from json import dumps
import sys
sys.path.append("..")
import db

def channels_list(token):
    '''List all the channels of a certain user'''
    database = db.load_DB()
    u_id = db.get_from_token('u_id', token, database)

    return dumps({'channels': [channel for channel in database['channels'] \
    if u_id in channel['members']]})
