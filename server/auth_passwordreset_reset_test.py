'''Test auth_passwordreset_reset function'''
# pylint: disable=W0622, W0401, W0614, C0103, W0621
from ._include import *

@pytest.mark.parametrize("password", ['sdsdfsdf1', 'sdfsdfsdfsd', 'aeryaergaer'])
def test_valid_resetCode(password):
    ''' Reset_code is valid'''
    db.reset_DB()
    auth_passwordreset_request('test123@outlook.com')
    # Have to locate email and hardcode in resetCode as
    # unable to attain code directly from site
    reset_code = '9999'
    assert auth_passwordreset_reset(reset_code, password, testing=True) != {}

@pytest.mark.parametrize("invalid_new_password", ['hi', 'bye', '123', ' '])
def test_invalid_password(invalid_new_password):
    ''' Password is invalid'''
    db.reset_DB()
    with pytest.raises(ValueError):
        auth_passwordreset_reset('12345', invalid_new_password)
