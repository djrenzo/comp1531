'''Test message_sendlater function'''
# pylint: disable=W0622, W0401, W0614, C0103, W0621
from datetime import datetime
from ._include import *

def test_channel_removeowner_notExists(d):
    '''Channel Id does not exist'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    with pytest.raises(ValueError):
        message_sendlater(dict['token'], 745634634, "Random Message", \
        datetime(2020, 10, 6).timestamp())

def test_channel_invalid_token():
    '''Invalid Token'''
    db.reset_DB()
    with pytest.raises(AccessError):
        message_sendlater(None, None, "Random Message", datetime(2020, 10, 6).timestamp())

def test_message_sendlater_messageGreaterThousand(d):
    '''Message too long'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    channel_id = json.loads(channels_create(dict['token'], 'Test_Channel', True))['channel_id']
    with pytest.raises(ValueError):
        message_sendlater(dict['token'], channel_id, "Random Message"*500, \
        datetime(2020, 10, 6).timestamp())

def test_message_sendlater_timeinPast(d):
    '''time is in the past'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    channel_id = json.loads(channels_create(dict['token'], 'Test_Channel', True))['channel_id']
    with pytest.raises(ValueError):
        message_sendlater(dict['token'], channel_id, "Random Message"*500, \
        datetime(2012, 8, 4).timestamp())

def test_message_sendlater_success(d):
    '''send message at a later time successfully'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    token = dict['token']
    channel_id = json.loads(channels_create(dict['token'], 'Test_Channel', True))['channel_id']
    assert message_sendlater(token, channel_id, "Random Message", \
    datetime.now().timestamp() + 0.01, testing=True)
