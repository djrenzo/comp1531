'''Test channels_listall function'''
#pylint:disable=C0413,C0411
import sys
from json import dumps
from .auth_register import auth_register
from .channels_listall import channels_listall
from. channels_create import channels_create
sys.path.append("..")
import db
import Token

def test_channels_listall():
    '''Test channels_listall function'''
    db.reset_DB()
    auth_register('al@gmail.com', 'pas123456', 'Bob', 'Smith')
    token = Token.generateToken('al@gmail.com')
    channels_create(token, 'Hi', True)
    channels_create(token, 'Bye', True)
    assert channels_listall(token) == dumps({'channels' : [{"channel_id": 1, "is_public": True,\
     "owner_members": [1], "members": [1], "name": "Hi"}, {"channel_id": 2, "is_public": True, \
     "owner_members": [1], "members": [1], "name": "Bye"}]})
