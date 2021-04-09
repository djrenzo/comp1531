'''Change a users permissions'''
# pylint: disable=W0622, C0413, C0411
import sys
from json import dumps
from .AccessError import AccessError, ValueError
sys.path.append("..")
import db
import Token

def admin_userpermission_change(token, u_id, permission_id):
    '''Change a users permissions'''
    u_id = int(u_id)
    permission_id = int(permission_id)

    if not Token.isValid(token):
        raise AccessError("Not a valid token!")

    data = db.load_DB()
    token_permission_id = db.get_from_token('permission_id', token, data)

    all_uids = [user['u_id'] for user in data['users']]
    if not u_id in all_uids:
        raise ValueError("u_id does not refer to a valid user")

    if permission_id not in [1, 2, 3]:
        raise ValueError("Permission_id does not refer to a valid permission")

    if token_permission_id not in [1, 2]:
        raise AccessError("The authorised user is not an admin or owner")


    for user in data['users']:
        if u_id == user['u_id']:
            user['permission_id'] = permission_id

    db.save_DB(data)
    return dumps({})
