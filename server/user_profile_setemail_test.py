from .user_profile_setemail import *
from.auth_register import *
import pytest

#Email entered is not a valid email.
def test_user_profile_setname_emailInvalid():
	db.reset_DB()
	auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
	realtoken = Token.generateToken('testmail@gmail.com')
	with pytest.raises(ValueError):
		user_profile_setemail(realtoken,'bademail')
    
#Email address is already being used by another user
def test_user_profile_setemail_emailTaken():
	db.reset_DB()
	auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
	
	auth_register('bobmail@gmail.com', 'pas123456', 'Bob', 'Smith')
	newtoken = Token.generateToken('bobmail@gmail.com')
	
	with pytest.raises(ValueError):
		user_profile_setemail(newtoken,'testmail@gmail.com')

#Email entered is  a valid email.
def test_user_profile_setname_emailValid():
	db.reset_DB()
	auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
	realtoken = Token.generateToken('testmail@gmail.com')
	assert(user_profile_setemail(realtoken,'z4194925@student.unsw.edu.au') == {})