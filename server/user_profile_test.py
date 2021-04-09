from .user_profile import *
from .auth_register import *
from .user_profile_sethandle import *
from json import dumps
import sys

sys.path.append("..")
import db
import Token
import pytest

#User with u_id is not a valid user
def test_user_profile_invalidUser():
	with pytest.raises(ValueError):
		user_profile(-1, 1)

#User with u_id is a valid user (Assume handle_str = User123)
def test_user_profile_validUser():
	db.reset_DB()
	data = db.load_DB()
	auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
	token = Token.generateToken('testmail@gmail.com')
	u_id = db.new_u_id(data)
	user_profile_sethandle(token, 'Baggins')
	assert(user_profile(token, u_id) != {})
