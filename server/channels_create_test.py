'''Test channels_create function'''
# pylint: disable=W0622, W0401, W0614, C0103, W0621, C0413, C0411
import sys
import pytest
from .AccessError import AccessError, ValueError
from .channels_create import channels_create
from .auth_register import auth_register
from json import dumps
sys.path.append("..")
import Token
import db

def test_invalid_token():
    '''Invalid token is used'''
    token = 'faketoken1232434'
    name = 'new channel'
    with pytest.raises(AccessError):
        channels_create(token, name, True)
        channels_create(token, name, False)

def test_invalid_name():
    '''Invalid channel name'''
    db.reset_DB()
    auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
    token = Token.generateToken('testmail@gmail.com')
    name = 'new channel'
    with pytest.raises(ValueError):
        channels_create(token, name*20, True)
        channels_create(token, name*20, False)

def test_valid_name_valid_token():
    '''Valid name, valid token'''
    db.reset_DB()
    auth_register('testmail1@gmail.com', 'pas123456', 'Bob', 'Smith')
    auth_register('testmail2@gmail.com', 'pas123456', 'Bob', 'Smith')
    token1 = Token.generateToken('testmail1@gmail.com')
    name = 'new channel'
    assert channels_create(token1, name, True) == dumps({'channel_id' : 1})
    assert channels_create(token1, name, False) == dumps({'channel_id' : 2})
