'''Logout a user'''
# pylint: disable=W0622, C0413, C0411
from json import dumps
import sys
sys.path.append("..")
import Token

def auth_logout(token):
    '''Logout a user'''
    if Token.isValid(token):
        try:
            decoded = Token.decodeToken(token)
            if decoded:
                Token.removeToken(token)
                return dumps({'is_success' : True})

        except NameError:
            return dumps({'is_success' : False})
    return dumps({'is_success' : False})
