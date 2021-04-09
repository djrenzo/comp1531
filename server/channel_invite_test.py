'''Test channel_invite function'''
# pylint: disable=W0622, W0401, W0614, C0103, W0621
from ._include import *

def test_channel_addowner_notExists(d):
    '''Channel Id does not exist'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    with pytest.raises(ValueError):
        channel_invite(dict['token'], 723478923672384, dict['u_id'])

def test_channel_addowner_alreadyOwner(d):
    '''User to be made member is already member'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    channel_id = json.loads(channels_create(dict['token'], 'Test_Channel', True))['channel_id']
    with pytest.raises(AccessError):
        channel_invite(dict['token'], channel_id, dict['u_id'])

def test_channel_addowner_exists(d):
    '''Channel ID does exist'''
    db.reset_DB()
    owner = json.loads(auth_register("john@gmail.com", "hfghfghfg", "John", "Dean"))
    channel_id = json.loads(channels_create(owner['token'], 'Test_Channel', True))['channel_id']
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    assert channel_invite(owner['token'], channel_id, dict['u_id']) == json.dumps({})

def test_channel_addowner_notAuthorised(d):
    '''User added as owner is a member of channel'''
    db.reset_DB()
    owner = json.loads(auth_register("john@gmail.com", "hfghfghfg", "John", "Dean"))
    channel_id = json.loads(channels_create(owner['token'], 'Test_Channel', True))['channel_id']
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    with pytest.raises(AccessError):
        channel_invite(dict['token'], channel_id, 0)
