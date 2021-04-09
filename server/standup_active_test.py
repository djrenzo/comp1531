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
		standup_active(realtoken, fake_channel)

# If channel does exist
def test_existing_channel():
	db.reset_DB()
	auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
	realtoken = Token.generateToken('testmail@gmail.com')
	channel_id = channels_create(realtoken,'Channel', True)
	assert(standup_active(realtoken, 1) != {})
