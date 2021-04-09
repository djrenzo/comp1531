'''Test channel_leave function'''
# pylint: disable=W0622, W0401, W0614, C0103, W0621
from ._include import *

def test_channel_leave_notExists(d):
    '''Channel Id does not exist'''
    db.reset_DB()
    owner = json.loads(auth_register("john@gmail.com", "hfghfghfg", "John", "Dean"))
    channel_id = json.loads(channels_create(owner['token'], 'Test_Channel', True))['channel_id']
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    channel_invite(owner['token'], channel_id, dict['u_id'])
    with pytest.raises(ValueError):
        channel_leave(dict['token'], 4354)

def test_channel_leave_success(d):
    '''Channel ID does exist'''
    db.reset_DB()
    owner = json.loads(auth_register("john@gmail.com", "hfghfghfg", "John", "Dean"))
    channel_id = json.loads(channels_create(owner['token'], 'Test_Channel', True))['channel_id']
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    channel_invite(owner['token'], channel_id, dict['u_id'])
    assert channel_leave(dict['token'], channel_id) == {}
