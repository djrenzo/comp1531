'''Test channel_join function'''
# pylint: disable=W0622, W0401, W0614, C0103, W0621
from ._include import *

def test_channel_removeowner_notexists(d):
    '''Channel Id does not exist'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    with pytest.raises(ValueError):
        channel_removeowner(dict['token'], 723478923672384, dict['u_id'])

def test_channel_removeowner_not_owner(d):
    '''User to be removed as owner is not an owner'''
    db.reset_DB()
    owner = json.loads(auth_register("john@gmail.com", "hfghfghfg", "John", "Dean"))
    channel_id = json.loads(channels_create(owner['token'], 'Test_Channel', True))['channel_id']
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    with pytest.raises(ValueError):
        channel_removeowner(owner['token'], channel_id, dict['u_id'])

def test_channel_removeowner_success(d):
    '''Test for success'''
    db.reset_DB()
    owner = json.loads(auth_register("john@gmail.com", "hfghfghfg", "John", "Dean"))
    channel_id = json.loads(channels_create(owner['token'], 'Test_Channel', True))['channel_id']
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    channel_invite(owner['token'], channel_id, dict['u_id'])
    channel_addowner(owner['token'], channel_id, dict['u_id'])
    assert channel_removeowner(owner['token'], channel_id, dict['u_id']) == {}

def test_channel_removeowner_notmember(d):
    '''User from token is not authorised to give users owner permissions'''
    db.reset_DB()
    owner = json.loads(auth_register("john@gmail.com", "hfghfghfg", "John", "Dean"))
    channel_id = json.loads(channels_create(owner['token'], 'Test_Channel', True))['channel_id']
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    channel_invite(owner['token'], channel_id, dict['u_id'])
    with pytest.raises(ValueError):
        channel_removeowner(dict['token'], channel_id, dict['u_id'])
