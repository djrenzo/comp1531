'''Test standup_send function'''
# pylint: disable=W0622, W0401, W0614, C0103, W0621
import pytest
from .standup import *
from .auth_register import *
from .channel_invite import *
from .channels_create import *

def test_notExisting_channel():
    '''If channel does not exist'''
    db.reset_DB()
    auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
    realtoken = Token.generateToken('testmail@gmail.com')
    fake_channel = 70
    with pytest.raises(ValueError):
        standup_send(realtoken, fake_channel, 'Hi')

def test_message_too_long():
    '''If the message is too long'''
    db.reset_DB()
    auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
    realtoken = Token.generateToken('testmail@gmail.com')
    channels_create(realtoken, 'Bye', True)
    message = 'Hi'
    with pytest.raises(ValueError):
        standup_send(realtoken, 1, message*1001)

def test_message_not_member():
    '''if the user is not a member of the channel'''
    db.reset_DB()
    admintoken = Token.generateToken('admin@gmail.com')
    channels_create(admintoken, 'Channel', True)
    auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
    realtoken = Token.generateToken('testmail@gmail.com')
    with pytest.raises(ValueError):
        standup_send(realtoken, 1, 'Hi')

def test_existing_channel():
    '''If channel does exist, message correct length, user member of channel'''
    db.reset_DB()
    auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
    realtoken = Token.generateToken('testmail@gmail.com')
    channels_create(realtoken, 'Bye', True)
    message = 'Hi'
    with pytest.raises(ValueError):
        standup_send(realtoken, 1, message)
