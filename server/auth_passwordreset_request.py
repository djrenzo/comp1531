'''Let a user request a password reset'''
# pylint: disable=W0622, C0413, C0411
import sys
from random import randint
sys.path.append("..")
import db

def auth_passwordreset_request(email):
    '''Let a user request a password reset'''
    data = db.load_DB()
    allmails = [user['email'] for user in data['users']]

    if email in allmails:
        code = randint(999, 9999)
        for user in data['users']:
            if user['email'] == email:
                user['psw_code'] = code

        db.save_DB(data)
        return (True, code)

    return (False, 0000)
