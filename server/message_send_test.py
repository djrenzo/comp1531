'''Test message_send function'''
# pylint: disable=W0622, W0401, W0614, C0103, W0621
from ._include import *

def test_channel_invalid_token():
    '''Invalid Token'''
    db.reset_DB()
    with pytest.raises(AccessError):
        message_send(None, None, "Random Message")

def test_message_send_valid_token(d):
    '''valid token'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    channel_id = json.loads(channels_create(dict['token'], 'Test_Channel', True))['channel_id']
    assert message_send(dict['token'], channel_id, "Random Message")

def test_message_sendlater_messageGreaterThousand(d):
    '''Message too long'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    channel_id = json.loads(channels_create(dict['token'], 'Test_Channel', True))['channel_id']
    with pytest.raises(ValueError):
        message_send(dict['token'], channel_id, "Random Message"*500)

def test_message_sendlater_success(d):
    '''send successfully'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    channel_id = json.loads(channels_create(dict['token'], 'Test_Channel', True))['channel_id']
    assert message_send(dict['token'], channel_id, "Random Message")
