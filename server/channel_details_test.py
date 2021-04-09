'''Test channel_addowner function'''
# pylint: disable=W0622, C0413, C0411

import sys
import pytest
from .auth_register import auth_register
from .AccessError import AccessError, ValueError
from .channel_details import channel_details
from .channels_create import channels_create
sys.path.append("..")
import db
import Token

def test_channel_details_not_exists():
    '''Channel does not exist'''
    db.reset_DB()
    auth_register('hosh_mail@gmail.com', 'pas123456', 'Hosh', 'Mehta')
    token = Token.generateToken('hosh_mail@gmail.com')
    with pytest.raises(ValueError):
        channel_details(token, -4)

def test_channel_details_exists():
    '''Channel exists'''
    db.reset_DB()
    auth_register('hosh_mail@gmail.com', 'pas123456', 'Hosh', 'Mehta')
    token = Token.generateToken('hosh_mail@gmail.com')
    channels_create(token, 'Test', True)#['channel_id']
    assert channel_details(token, 1)

def test_channel_details_user_notmember():
    '''User is not a member'''
    db.reset_DB()
    auth_register('hosh_mail@gmail.com', 'pas123456', 'Hosh', 'Mehta')
    token = Token.generateToken('hosh_mail@gmail.com')

    auth_register('josh_mail@gmail.com', 'pas123456', 'Josh', 'Greta')
    token_main = Token.generateToken('josh_mail@gmail.com')

    channels_create(token_main, 'Test', True)
    with pytest.raises(AccessError):
        channel_details(token, 1)

def test_channel_details_user_member():
    '''User is a member'''
    db.reset_DB()
    auth_register('hosh_mail@gmail.com', 'pas123456', 'Hosh', 'Mehta')
    token = Token.generateToken('hosh_mail@gmail.com')
    channels_create(token, 'Test', True)
    print(channel_details(token, 1))
    assert channel_details(token, 1)
