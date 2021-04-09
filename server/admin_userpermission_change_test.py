'''Tests to test admin_userpermission_change function'''
# pylint: disable=W0622, C0413, C0411
from json import dumps
import sys
import pytest
from .AccessError import AccessError, ValueError
from .admin_userpermission_change import admin_userpermission_change
from .auth_register import auth_register
sys.path.append('..')
import db
import Token

def test_invalid_user():
    '''If user ID does not exist'''
    db.reset_DB()
    auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
    realtoken = Token.generateToken('testmail@gmail.com')
    with pytest.raises(ValueError):
        admin_userpermission_change(realtoken, -5, 1)

def test_valid_user():
    '''If user ID does exist function will execute'''
    # Make user an owner so no errors triggered
    db.reset_DB()
    auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
    realtoken = Token.generateToken('admin@gmail.com')
    assert admin_userpermission_change(realtoken, 1, 1) == dumps({})

def test_invalid_u_id():
    '''If u_id does not refer to admin or owner'''
    db.reset_DB()
    auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
    realtoken = Token.generateToken('testmail@gmail.com')
    with pytest.raises(AccessError):
        admin_userpermission_change(realtoken, 1, 1)

def test_valid_u_id():
    '''If u_id is valid and does refer to admin or owner'''
    db.reset_DB()
    auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
    realtoken = Token.generateToken('admin@gmail.com')
    assert admin_userpermission_change(realtoken, 1, 1) == dumps({})

def test_invalid_permission_id():
    '''If permission ID does not exist'''
    db.reset_DB()
    auth_register('testmail@gmail.com', 'pas123456', 'Bob', 'Smith')
    realtoken = Token.generateToken('admin@gmail.com')
    with pytest.raises(ValueError):
        admin_userpermission_change(realtoken, 1, 5)
