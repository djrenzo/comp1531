'''Register a user'''
# pylint: disable=W0622, C0413, C0411
from .AccessError import ValueError
from json import dumps
import sys
sys.path.append("..")
import db
import Token

def auth_register(email, password, name_first, name_last):
    '''Register a user'''
    data = db.load_DB()
    users = data["users"]

    if users:
        all_emails = [user['email'] for user in users]
    else:
        all_emails = []

    if not db.check_mail(email):
        raise ValueError('Email is not a valid email adress')

    if email in all_emails:
        raise ValueError('Email address is already being used by another user')

    if len(password) < 6:
        raise ValueError('Password entered is not a valid password.')

    if len(name_first) > 50 or not name_first:
        raise ValueError('Your First Name cannot be more than 50 characters.')

    if len(name_last) > 50 or not name_last:
        raise ValueError('Your Last Name cannot be more than 50 characters.')

    u_id = db.new_u_id(data)
    data['users'].append({
        'tokens': [],
        'profile_img_url' : 'https://www.thehumanenterprise.com.au/wp-content/uploads/2017/06/\
Empty-Profile-Testimonials.jpg',
        'handle_str': name_first+name_last,
        'u_id' : u_id,
        'email' : email.lower(),
        'password' : db.hash_password(password),
        'name_first' : name_first,
        'name_last' : name_last,
        'permission_id' : 3})
    db.save_DB(data)
    return dumps({'u_id': u_id, 'token' : Token.generateToken(email)})
