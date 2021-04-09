'''Change a user profile's email'''
# pylint: disable=W0622, C0413, C0411
import sys
from .AccessError import AccessError, ValueError
sys.path.append("..")
import db
import Token

def user_profile_setemail(token, email):
    '''Change a user profile's email'''

    if not Token.isValid(token):
        raise AccessError("Not a valid token!")

    database = db.load_DB()
    u_id = db.get_from_token('u_id', token, database)

    if database['users']:
        all_emails = [user['email'] for user in database['users']]
    else:
        all_emails = []

    if not db.check_mail(email):
        raise ValueError('Email entered is not a valid email')

    if email in all_emails:
        raise ValueError('Email address is already being used by another user')

    for user in database['users']:
        if u_id == user['u_id']:
            user['email'] = email

    db.save_DB(database)
    return {}
