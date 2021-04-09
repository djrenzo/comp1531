'''Test auth_login function'''
# pylint: disable=W0622, W0401, W0614, C0103, W0621

# Include Libraries 
from .AccessError import *
from flask import Flask, request
import pytest
import json
import sys
import jwt

# Include Backend Functions
# Authorised Functions
from .auth_login import auth_login
from .auth_logout import auth_logout
from .auth_passwordreset_reset import auth_passwordreset_reset
from .auth_passwordreset_request import auth_passwordreset_request
from .auth_register import auth_register

# Channel Functions
from .channel_addowner import channel_addowner
from .channel_details import channel_details
from .channel_invite import channel_invite
from .channel_join import channel_join
from .channel_leave import channel_leave
from .channel_messages import channel_messages
from .channel_removeowner import channel_removeowner
from .channels_create import channels_create
from .channels_list import channels_list
from .channels_listall import channels_listall

# Message Functions
from .message_edit import message_edit
from .message_pin import message_pin
from .message_react import message_react
from .message_remove import message_remove
from .message_send import message_send
from .message_sendlater import message_sendlater
from .message_unpin import message_unpin
from .message_unreact import message_unreact
from .search import search

# User Functions
from .user_profile_setemail import user_profile_setemail
from .user_profile_sethandle import user_profile_sethandle
from .user_profile_setname import user_profile_setname
from .user_profiles_uploadphoto import user_profiles_uploadphoto

# Include global functions
sys.path.append("..")
import db
import Token

@pytest.fixture(params = [{ 'email' : 'stevendai301@hotmail.com',
                            'psw' : 'asdjfhasdj',
                            'f_name' : "Steven",
                            'l_name' : "Dai"
                          } , 
                          { 'email' : 'marcrocca5@hotmail.com',
                            'psw' : 'hruuegruegre',
                            'f_name' : "Marc",
                            'l_name' : "Rocca"
                          } ,
                          { 'email' : 'matthew@hotmail.com',
                            'psw' : 'sdfsdfsdfsdf',
                            'f_name' : "Matt",
                            'l_name' : "Corby"
                          } ,
                          ])
def d(request):
    return request.param 

def test_auth_register_bad_email():
    '''email is not valid'''
    db.reset_DB()
    password = 'TestPass'
    with pytest.raises(ValueError):
        auth_login('test123', password)
        auth_login('@gmail.com', password)
        auth_login('test123@', password)
        auth_login('test123@hotmail', password)

def test_auth_login_not_registered(d):
    '''email is valid but not registered'''
    db.reset_DB()
    auth_register(d['email'], d['psw'], d['f_name'], d['l_name'])

    with pytest.raises(ValueError):
        auth_login('randomemail@gmail.com', 'asdjfhasdj')

def test_auth_login_incorrectPassword_1(d):
    '''valid and registered email but incorect password (call auth_register)'''
    db.reset_DB()
    wrong_psw = 'wrongpassword1'
    auth_register(d['email'], d['psw'], d['f_name'], d['l_name'])

    with pytest.raises(ValueError):
        auth_login(d['email'], wrong_psw)

def test_auth_login_Registered(d):
    '''valid and registered email and correct password, returns u_id and token'''
    db.reset_DB()
    auth_register(d['email'], d['psw'], d['f_name'], d['l_name'])

    dict = json.loads(auth_login(d['email'], d['psw']))
    token = dict['token']
    u_id = dict['u_id']

    email_decod = Token.decodeToken(token)['email']
    assert u_id == 1
    assert email_decod == d['email']
    db.reset_DB()
