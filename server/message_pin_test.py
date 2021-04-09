'''Test message_pin function'''
# pylint: disable=W0622, W0401, W0614, C0103, W0621
from ._include import *

def message_is_pinned(message_id):
    ''' helper to check if message is pinned'''
    data = db.load_DB()
    for message in data['messages']:
        if message['message_id'] == int(message_id):
            return message['is_pinned']
    return False

def test_channel_invalid_token():
    '''Invalid Token'''
    db.reset_DB()
    with pytest.raises(AccessError):
        message_pin(None, -1)

def test_channel_invalid_message_id(d):
    '''Invalid messenger ID'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    with pytest.raises(ValueError):
        message_pin(dict['token'], -1)

def test_message_remove_succestful():
    '''Message pin succestful'''
    db.reset_DB()
    admintoken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9\
.eyJlbWFpbCI6ImFkbWluQGdtYWlsLmNvbSIsInRpbWVzdGFtcCI6MTU3Mzg3NzgzNC40MTE1OTR9.\
5CkB0u_oaGvmpsxbeOSmMqlLGkSc4DJwRferSCePx8U'
    channel_id = json.loads(channels_create(admintoken, 'Test_Channel', True))['channel_id']
    message_id = json.loads(message_send(admintoken, channel_id, "Random Message"))['message_id']
    message_pin(admintoken, message_id)
    assert message_is_pinned(message_id)
