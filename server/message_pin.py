'''Pin existing message in a channel'''
# pylint: disable=W0622, C0413, C0411
from .AccessError import AccessError, ValueError
from json import dumps
import sys
sys.path.append("..")
import db
import Token

def message_pin(token, message_id):
    '''Pin existing message in a channel'''
    if not Token.isValid(token):
        raise AccessError("Not a valid token!")

    message_id = int(message_id)

    database = db.load_DB()
    permission_id = db.get_from_token('permission_id', token, database) #true or false
    #loop through database for message ID
    if message_id not in db.get_all_messages(database):
        raise ValueError('message_id is not a valid message')
    #check admin of user
    if permission_id not in [1, 2]:
        raise ValueError('The authorised user is not an admin')

    #check if message_id is pinned
    for message in database['messages']:
        if message['message_id'] == message_id:
            if message['is_pinned']:
                raise ValueError('Message is already pinned')
            message['is_pinned'] = True

    db.save_DB(database)
    return dumps({})
