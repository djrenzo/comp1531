'''Test message_unreact function'''
# pylint: disable=W0622, W0401, W0614, C0103, W0621
from ._include import *

def message_flags(msg_id, all_msg):
    '''check if message is reacted'''
    flag = 0
    for msg in all_msg:
        if msg['message_id'] == msg_id:
            flag = 1
            if msg['reacts'] != 1:
                flag = 2
                break
            break
    return flag

def test_channel_invalid_token():
    '''Invalid Token'''
    db.reset_DB()
    with pytest.raises(AccessError):
        message_unreact(None, None, 1)

def test_channel_invalid_message_id(d):
    '''Invalid messenger ID'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    with pytest.raises(ValueError):
        message_unreact(dict['token'], None, 1)

@pytest.mark.parametrize("react_id", [4, 2, -1, 'Apple', ' ', None])
def test_channel_invalid_react_id(d, react_id):
    '''Invalid react ID'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    channel_id = json.loads(channels_create(dict['token'], 'Test_Channel', True))['channel_id']
    message_id = json.loads(message_send(dict['token'], channel_id, "Random Message"))['message_id']
    with pytest.raises(ValueError):
        message_unreact(dict['token'], message_id, react_id)

def test_message_react_successfull(d):
    '''Message react succesfull'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    channel_id = json.loads(channels_create(dict['token'], 'Test_Channel', True))['channel_id']
    message_id = json.loads(message_send(dict['token'], channel_id, "Hi Green"))['message_id']

    data = db.load_DB()
    message_react(dict['token'], message_id, '1')
    data = db.load_DB()
    message_unreact(dict['token'], message_id, '1')
    data = db.load_DB()
    assert message_flags(message_id, data['messages']) == 2
