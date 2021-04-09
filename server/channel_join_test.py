'''Test channel_join function'''
# pylint: disable=W0622, W0401, W0614, C0103, W0621
from ._include import *

def test_channel_join_notExists(d):
    '''Channel Id does not exist'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    with pytest.raises(ValueError):
        channel_join(dict['token'], 9897976868)

def test_channel_addowner_alreadyOwner(d):
    '''Channel (based on ID) does exist'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    channel_id = json.loads(channels_create(dict['token'], 'Test_Channel', True))['channel_id']
    assert channel_join(dict['token'], channel_id) == {}

def test_channel_addowner_exists(d):
    '''channel_id refers to a channel that is private'''
    db.reset_DB()
    dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
    channel_id = json.loads(channels_create(dict['token'], 'Test_Channel', False))['channel_id']
    with pytest.raises(AccessError):
        channel_join(dict['token'], channel_id)

# # channel_id refers to a channel that is private but authorised user is admin
# def test_channel_addowner_notAuthorised(d):
#     db.reset_DB()
#     dict = json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))
#     channel_id = json.loads(channels_create(dict['token'], 'Test_Channel', False))['channel_id']
#     with pytest.raises(AccessError):
#         channel_join(TOKEN OF ADMIN, channel_id)
