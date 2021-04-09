import db
import Token
import server
from .user_profile_sethandle import *
from .auth_register import *
from .AccessError import *
import pytest

def test_user_profile_sethandle_handleOverflow():
	db.reset_DB()
	auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
	realtoken = Token.generateToken('testmail@gmail.com')
	fakename = 'Yo'
	with pytest.raises(ValueError):
		user_profile_sethandle(realtoken, fakename*30)
		user_profile_sethandle(realtoken, fakename)

def test_user_profile_sethandle_handleValid():
	db.reset_DB()
	auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
	realtoken = Token.generateToken('testmail@gmail.com')
	name = 'Steven Dai'
	assert(user_profile_sethandle(realtoken, name) == {})