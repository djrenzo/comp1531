'''Test message_edit function'''
# pylint: disable=W0622, W0401, W0614, C0103, W0621
from ._include import *

@pytest.fixture(params=['Edit Message Here', 'Hello There', ' ', 'Bye'*50])
def edit_message(request):
    '''edit message'''
    return request.param

def confirm_sent_message(msg_id, all_msg, edit_message):
    '''confirm if message is sent'''
    flag = 0
    for msg in all_msg:
        if msg['message_id'] == msg_id:
            flag = 1
            print(msg['message'])
            if msg['message'] == edit_message:
                flag = 2
                break
            break
    return flag

def test_channel_invalid_token():
    '''Invalid Token'''
    db.reset_DB()
    with pytest.raises(AccessError):
        message_edit(None, None, "Random Message")

@pytest.mark.parametrize("message", ["Random Message", "Hello Everyone,\
 We're DishDANG", " ", "Bye"])
def test_channel_notAuthorised_to_edit(d, message, edit_message):
    '''# Invalid Token'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    channel_id = json.loads(channels_create(dict['token'], 'Test_Channel', True))['channel_id']
    message_id = json.loads(message_send(dict['token'], channel_id, message))['message_id']
    other_person = json.loads(auth_register("john@gmail.com", "hfghfghfg", "John", "Dean"))

    data = db.load_DB()
    assert confirm_sent_message(message_id, data['messages'], edit_message)
    with pytest.raises(AccessError):
        message_edit(other_person['token'], message_id, edit_message)

@pytest.mark.parametrize("message", ["Random Message", "Hello Everyone, We're DishDANG", " "])
def test_message_remove_succestful(d, message, edit_message):
    '''Message edit succestful'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    channel_id = json.loads(channels_create(dict['token'], 'Test_Channel', True))['channel_id']
    message_id = json.loads(message_send(dict['token'], channel_id, message))['message_id']

    data = db.load_DB()
    assert confirm_sent_message(message_id, data['messages'], message)
    message_edit(dict['token'], message_id, edit_message)
    data = db.load_DB()
    assert confirm_sent_message(message_id, data['messages'], edit_message) == 2
