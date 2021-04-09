from .standup import *
from .auth_register import *
from .channels_create import *
import pytest

# If channel does not exist
def test_notExisting_channel():
	db.reset_DB()
	auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
	realtoken = Token.generateToken('testmail@gmail.com')
	fake_channel = 70
	with pytest.raises(ValueError):
		standup_start(realtoken, fake_channel, 5)

# If channel does exist
def test_existing_channel_1():
	db.reset_DB()
	auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
	realtoken = Token.generateToken('testmail@gmail.com')
	channel_id = channels_create(realtoken,'Channel', True)
	assert(standup_start(realtoken, 1, 5))

# if the user is not a member of the channel
def test_message_not_member():
	db.reset_DB()
	admintoken = Token.generateToken('admin@gmail.com')
	channel_id = channels_create(admintoken,'Channel', True)
	auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
	realtoken = Token.generateToken('testmail@gmail.com')
	with pytest.raises(AccessError):
		standup_start(realtoken, 1, 5)

# If channel does exist and user member of channel
def test_existing_channel_2():
	db.reset_DB()
	auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
	realtoken = Token.generateToken('testmail@gmail.com')
	channel_id = channels_create(realtoken,'Channel', True)
	assert(standup_start(realtoken, 1, 5))
