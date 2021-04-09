'''Test message_unpin function'''
# pylint: disable=W0622, W0401, W0614, C0103, W0621
from ._include import *

def message_is_pinned(message_id):
    '''confirm if message is unpinned'''
    data = db.load_DB()
    for message in data['messages']:
        if message['message_id'] == int(message_id):
            return message['is_pinned']
    return False

def test_channel_invalid_token():
    '''Invalid Token'''
    db.reset_DB()
    with pytest.raises(AccessError):
        message_unpin(None, -1)

def test_channel_invalid_message_id(d):
    '''Invalid messenger ID'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    with pytest.raises(ValueError):
        message_unpin(dict['token'], -1)
