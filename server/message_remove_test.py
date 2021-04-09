'''Test message_remove function'''
# pylint: disable=W0622, W0401, W0614, C0103, W0621
from ._include import *

def confirm_sent_message(msg_id, all_msg):
    '''confirm if message is removed'''
    flag = 0
    for msg in all_msg:
        if msg['message_id'] == msg_id:
            flag = 1
            break
    return flag

def test_channel_invalid_token():
    '''Invalid Token'''
    db.reset_DB()
    with pytest.raises(AccessError):
        message_remove(None, "Random Message")

@pytest.mark.parametrize("message", ["Random Message", "Hello Everyone, We're DishDANG", " "])
def test_message_remove_succestful(d, message):
    '''Message remove succestful'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    channel_id = json.loads(channels_create(dict['token'], 'Test_Channel', True))['channel_id']
    message_id = json.loads(message_send(dict['token'], channel_id, message))['message_id']

    data = db.load_DB()
    assert confirm_sent_message(message_id, data['messages'])
    message_id = message_remove(dict['token'], message_id)
    data = db.load_DB()
    assert confirm_sent_message(message_id, data['messages']) == 0
