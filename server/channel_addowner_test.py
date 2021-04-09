'''Test channel_addowner function'''
# pylint: disable=W0622, W0401, W0614, C0103, W0621
import pytest
from .AccessError import ValueError
from ._include import *

def test_channel_addowner_notExists(d):
    ''' Channel Id does not exist'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    with pytest.raises(ValueError):
        channel_addowner(dict['token'], 723478923672384, dict['u_id'])

def test_channel_addowner_alreadyOwner(d):
    '''User to be made owner is already owner'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    channel_id = json.loads(channels_create(dict['token'], 'Test_Channel', True))['channel_id']
    with pytest.raises(ValueError):
        channel_addowner(dict['token'], channel_id, dict['u_id'])

def test_channel_addowner_exists(d):
    '''Channel ID does exist'''
    db.reset_DB()
    owner = json.loads(auth_register("john@gmail.com", "hfghfghfg", "John", "Dean"))
    channel_id = json.loads(channels_create(owner['token'], 'Test_Channel', True))['channel_id']
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    channel_invite(owner['token'], channel_id, dict['u_id'])
    assert channel_addowner(owner['token'], channel_id, dict['u_id']) == {}
