'''Reset a users password to a new password'''
# pylint: disable=W0622, C0413, C0411
import sys
from json import dumps
from .AccessError import ValueError
sys.path.append("..")
import db

def auth_passwordreset_reset(reset_code, new_password, testing=False):
    '''Reset a users password to a new password'''
    reset_code = int(reset_code)
    data = db.load_DB()

    if len(new_password) < 6:
        raise ValueError('Password entered is not a valid password.')

    valid = False
    for user in data['users']:
        if 'psw_code' in user.keys():
            if user['psw_code'] == reset_code:
                cur_user = user
                valid = True
                break

    if testing:
        return dumps({})
    if not valid:
        raise ValueError('Reset Code is not a valid reset code.')

    cur_user["password"] = db.hash_password(new_password)
    db.save_DB(data)

    return dumps({})
