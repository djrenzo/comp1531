from .user_profile_setname import *
from .auth_register import *
import pytest

#first name too long
def test_user_profile_setname_nameFirstOverflow():
	db.reset_DB()
	auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
	realtoken = Token.generateToken('testmail@gmail.com')
	with pytest.raises(ValueError):
		user_profile_setname(realtoken, 'Steaslkjdalskjdlaksjdlkajsldkajslkdjalksdjalskdjlaksjdlaksjdlkasjldkjas', 'Dai')
    
#last name too long
def test_user_profile_setname_nameLastOverflow():
	db.reset_DB()
	auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
	realtoken = Token.generateToken('testmail@gmail.com')
	with pytest.raises(ValueError):
		user_profile_setname(realtoken,'Steven', 'Aasjdalsjdlakjsldjalksdlaskdjlaksdjalskdalksjdlkasjdlkajdaskdlaksjladl')

#valid first and last name 
def test_user_profile_setname_vaildFirstLast():
	db.reset_DB()
	auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
	realtoken = Token.generateToken('testmail@gmail.com')
	assert(user_profile_setname(realtoken,'Hosh', 'Mehta') == {})