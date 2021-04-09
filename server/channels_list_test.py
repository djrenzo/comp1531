'''Test channels_list function'''
# pylint: disable=C0413,C0411
import sys
from json import dumps
from .channels_list import channels_list
from .channels_create import channels_create
from .auth_register import auth_register
sys.path.append("..")
import Token
import db

def test_channels_list():
    '''Test channels_list function'''
    db.reset_DB()
    auth_register('al@gmail.com', 'pas123456', 'Bob', 'Smith')
    token = Token.generateToken('al@gmail.com')
    channels_create(token, "Hi", True)
    assert channels_list(token) == dumps({'channels' : [{"channel_id": 1, "is_public": True, \
    "owner_members": [1], "members": [1], "name": "Hi"}]})
