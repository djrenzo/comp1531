'''Test channel_messages function'''
# pylint: disable=W0622, W0401, W0614, C0103, W0621, C0413, C0411
import pytest
import sys
from .channel_messages import channel_messages
from .channels_create import channels_create
from .AccessError import *
from .auth_register import auth_register
from json import dumps, loads
sys.path.append("..")
import db

db.reset_DB()
def create_token(First, Last):
    '''Function to auth register a user and get its token'''
    email = 'test@gmail.com'
    password = 'Password123'
    token = loads(auth_register(email, password, First, Last))['token']
    return {'token' : token}

John = create_token('John', 'Appleseed')
channels_create(John['token'], 'TestChannel', True)
channel_id = 1
print(channel_id)

def test_channel_messages_notExists():
    '''Channel does not exist'''
    with pytest.raises(ValueError):
        channel_messages(John['token'], 43544536, 0)

def test_channel_messages_exists():
    '''Channel exists'''
    assert channel_messages(John['token'], channel_id, 0) ==\
     dumps({"messages": [], "start": 0, "end": -1})

def test_channel_messages_startGreaterMessages():
    '''start > messages'''
    with pytest.raises(ValueError):
        channel_messages(John['token'], 1234567890, -1)

def test_channel_messages_startLessMessages():
    '''start < messages'''
    assert channel_messages(John['token'], channel_id, 0) ==\
     dumps({"messages": [], "start": 0, "end": -1})

def test_channel_messages_usernotMember():
    '''user is not a member'''
    with pytest.raises(ValueError):
        Alfredo = create_token('Alfredo', 'Johnson')
        channel_messages(Alfredo['token'], channel_id, 0)

def test_channel_messages_userMember():
    '''user is a member'''
    assert channel_messages(John['token'], channel_id, 0) ==\
     dumps({"messages": [], "start": 0, "end": -1})
