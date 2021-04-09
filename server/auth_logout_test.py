'''Test auth_logout function'''
# pylint: disable=W0622, W0401, W0614, C0103, W0621
from ._include import *

def test_auth_logout_valid(d):
    '''token is valid'''
    db.reset_DB()
    auth_register(d['email'], d['psw'], d['f_name'], d['l_name'])
    token = json.loads(auth_login(d['email'], d['psw']))['token']
    assert auth_logout(token) == json.dumps({'is_success' : True})

def test_auth_logout_invalid():
    '''token is invalid'''
    db.reset_DB()
    email = 'test123@gmail.com'
    psw = 'asdjfhasdj'
    auth_register(email, psw, 'Steven', 'Dai')
    invalid_token = 'kasjdlakj'
    assert auth_logout(invalid_token) == json.dumps({'is_success' : False})
