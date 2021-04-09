'''List all channels of server'''
#pylint:disable=C0413,C0411
from .AccessError import AccessError
from json import dumps
import sys
sys.path.append("..")
import db
import Token

def channels_listall(token):
    '''List all channels of server'''
    database = db.load_DB()
    if not Token.isValid(token):
        raise AccessError('Invalid Token')

    return dumps({'channels': [channel for channel in database['channels']]})
