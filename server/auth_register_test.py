'''Test auth_register function'''
# pylint: disable=W0622, W0401, W0614, C0103, W0621
from ._include import *

@pytest.mark.parametrize("email", ['@gmail.com', 'test123@', 'test123@hotmail', ' '])
def test_auth_register_bad_email(email):
    '''incorrect email is provided'''
    db.reset_DB()
    with pytest.raises(ValueError):
        auth_register(email, 'TestPass', 'Test', 'Name')

@pytest.mark.parametrize("email", ['test123@outlook.com', 'test123@hotmail.com',\
 'tree@hotmail.com'])
def test_auth_register_already_used(email):
    '''email is already in use by existing user on server'''
    db.reset_DB()
    auth_register(email, 'TestPass', 'Test', 'Name')
    with pytest.raises(ValueError):
        auth_register(email, 'TestPass', 'Test', 'Name')

@pytest.mark.parametrize("password", ['1', 'ab', '2cd'])
def test_auth_register_bad_password(password):
    '''bad password is provided'''
    db.reset_DB()
    with pytest.raises(ValueError):
        auth_register('didier.renzo@gmail.com', password, 'Test', 'Name')

@pytest.mark.parametrize("name", ['a'*51, 'adb'*52, 'rcd'*90])
def test_auth_register_bad_firstname(name):
    '''first name is too long'''
    db.reset_DB()
    with pytest.raises(ValueError):
        auth_register('didier.renzo@gmail.com', 'asdasdasd', name, 'Last_Name')

@pytest.mark.parametrize("name", ['a'*51, 'adb'*52, 'rcd'*90])
def test_auth_register_bad_lastname(name):
    '''last name is too long'''
    db.reset_DB()
    with pytest.raises(ValueError):
        auth_register('didier.renzo@gmail.com', 'asdasdasd', 'First_N', name)

def test_auth_register_success(d):
    '''successfully register a new user'''
    db.reset_DB()
    assert json.loads(auth_register(d['email'], d['psw'], d['f_name'], d['l_name']))['u_id'] == 1
