#!/usr/bin/env python3
"""Flask server"""
import sys
from json import dumps
from flask_cors import CORS
from flask import Flask, request, send_file
from flask_mail import Mail, Message

from server.auth_login import auth_login
from server.auth_logout import auth_logout
from server.auth_register import auth_register
from server.auth_passwordreset_request import auth_passwordreset_request
from server.auth_passwordreset_reset import auth_passwordreset_reset

from server.channel_invite import channel_invite
from server.channel_details import channel_details
from server.channel_messages import channel_messages
from server.channel_leave import channel_leave
from server.channel_join import channel_join
from server.channel_addowner import channel_addowner
from server.channel_removeowner import channel_removeowner
from server.channels_list import channels_list
from server.channels_listall import channels_listall
from server.channels_create import channels_create

from server.message_sendlater import message_sendlater
from server.message_send import message_send
from server.message_remove import message_remove
from server.message_edit import message_edit
from server.message_react import message_react
from server.message_unreact import message_unreact
from server.message_pin import message_pin
from server.message_unpin import message_unpin

from server.user_profile import user_profile
from server.user_profile_setname import user_profile_setname
from server.user_profile_setemail import user_profile_setemail
from server.user_profile_sethandle import user_profile_sethandle
from server.user_profiles_uploadphoto import user_profiles_uploadphoto
from server.users_all import users_all
from server.standup import standup_start, standup_send, standup_active
from server.search import search
from server.admin_userpermission_change import admin_userpermission_change

def defaultHandler(err):
    # pylint: disable=C0103
    ''' Handle HTTP errors'''
    response = err.get_response()
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.description,
    })
    response.content_type = 'application/json'
    return response

APP = Flask(__name__)
APP.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='1531.dishdang@gmail.com',
    MAIL_PASSWORD='1531dishDANG'
)

APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)
CORS(APP)

@APP.route('/auth/passwordreset/request', methods=['POST'])
def auth_psw_reset_rqst():
    ''' Route to reset the password of an existing user'''
    # pylint: disable=C0103, W0703
    email = request.form.get('email')
    valid, code = auth_passwordreset_request(email)
    if valid:
        mail = Mail(APP)
        try:
            msg = Message("PASSWORD RESET", sender="1531.dishDANG@gmail.com", recipients=[email])
            msg.body = f"Your password reset code is: {code}"
            mail.send(msg)
        except Exception as e:
            return str(e)

    return dumps({})

@APP.route('/auth/passwordreset/reset', methods=['POST'])
def auth_psw_reset_reset():
    ''' Route to password reset'''
    return dumps(auth_passwordreset_reset(request.form.get('reset_code'), \
    request.form.get('new_password')))

@APP.route('/admin/userpermission/change', methods=['POST'])
def admin():
    ''' Route to userpermission change'''
    return admin_userpermission_change(request.form.get('token'), \
    request.form.get('u_id'), request.form.get('permission_id'))

@APP.route('/auth/register', methods=['POST'])
def auth_reg():
    ''' Route to register new user'''
    return auth_register(request.form.get('email'), request.form.get('password'), \
    request.form.get('name_first'), request.form.get('name_last'))

@APP.route('/auth/login', methods=['POST'])
def auth_log():
    ''' Route to login existing user'''
    return auth_login(request.form.get('email'), request.form.get('password'))

@APP.route('/auth/logout', methods=['POST'])
def auth_logex():
    ''' Route to logout current user'''
    return auth_logout(request.form.get('token'))

@APP.route('/channels/create', methods=['POST'])
def channels_crea():
    ''' Route to create new channel'''
    return channels_create(request.form.get('token'), request.form.get('name'), \
    request.form.get('is_public'))

@APP.route('/channels/list', methods=['GET'])
def channels_l():
    ''' Route to list all channels for a specific user'''
    return channels_list(request.args.get('token'))

@APP.route('/channels/listall', methods=['GET'])
def channels_la():
    ''' Route to list all channels'''
    return channels_listall(request.args.get('token'))

@APP.route('/channel/invite', methods=['POST'])
def channel_inv():
    ''' Route to list add existing user to a new channel'''
    return channel_invite(request.form.get('token'), request.form.get('channel_id'),\
    request.form.get('u_id'))

@APP.route('/channel/addowner', methods=['POST'])
def channel_addown():
    ''' Route to add new owner to channel'''
    return channel_addowner(request.form.get('token'), request.form.get('channel_id'),\
     request.form.get('u_id'))

@APP.route('/channel/removeowner', methods=['POST'])
def channel_remown():
    ''' Route to remowe owner from channel'''
    return channel_removeowner(request.form.get('token'), request.form.get('channel_id'),\
     request.form.get('u_id'))

@APP.route('/channel/details', methods=['GET'])
def channels_det():
    ''' Route to list all channel details'''
    return channel_details(request.args.get('token'), request.args.get('channel_id'))

@APP.route('/channel/messages', methods=['GET'])
def channels_msg():
    ''' Route to list all channel messages'''
    return channel_messages(request.args.get('token'), request.args.get('channel_id'),\
     request.args.get('start'))

@APP.route('/user/profile', methods=['GET'])
def us_prof():
    ''' Route to list a user profile'''
    return user_profile(request.args.get('token'), request.args.get('u_id'))

@APP.route('/user/profile/setemail', methods=['PUT'])
def us_prof_setemail():
    ''' Route to change a users email'''
    return user_profile_setemail(request.form.get('token'), request.form.get('email'))

@APP.route('/user/profile/setname', methods=['PUT'])
def us_prof_setname():
    ''' Route to change a users name'''
    return user_profile_setname(request.form.get('token'), request.form.get('name_first'),\
     request.form.get('name_last'))

@APP.route('/user/profile/sethandle', methods=['PUT'])
def us_prof_sethandle():
    ''' Route to change a users handle'''
    return user_profile_sethandle(request.form.get('token'), request.form.get('handle_str'))

@APP.route('/user/profiles/uploadphoto', methods=['POST'])
def us_prof_uplpic():
    ''' Route to upload a new profile picture'''
    return user_profiles_uploadphoto(request.form.get('token'), request.form.get('img_url'),\
     request.form.get('x_start'), request.form.get('y_start'), request.form.get('x_end'), \
     request.form.get('y_end'), port=(sys.argv[1] if len(sys.argv) > 1 else 5000))

@APP.route('/imgurl', methods=['GET'])
def imgurl():
    ''' Route to get a profile picture from the folder'''
    u_id = request.args.get('id')
    filename = f'imgurl/{u_id}.jpg'
    print(filename)
    return send_file(filename, mimetype='/image/jpg')

@APP.route('/users/all', methods=['GET'])
def usrs_all():
    ''' Route to list all users'''
    return users_all(request.args.get('token'))

@APP.route('/message/send', methods=['POST'])
def msg_send():
    ''' Route to send a new message'''
    return message_send(request.form.get('token'), request.form.get('channel_id'),\
     request.form.get('message'))

@APP.route('/message/sendlater', methods=['POST'])
def msg_sendlater():
    ''' Route to send a message at a later point in time'''
    return message_sendlater(request.form.get('token'), request.form.get('channel_id'),\
     request.form.get('message'), request.form.get('time_sent'))

@APP.route('/message/pin', methods=['POST'])
def msg_pin():
    ''' Route to pin an existing message'''
    return message_pin(request.form.get('token'), request.form.get('message_id'))

@APP.route('/message/unpin', methods=['POST'])
def msg_unpin():
    ''' Route to unpin an existing message'''
    return message_unpin(request.form.get('token'), request.form.get('message_id'))

@APP.route('/message/remove', methods=['DELETE'])
def msg_rem():
    ''' Route to remove an existing message'''
    return message_remove(request.form.get('token'), request.form.get('message_id'))

@APP.route('/message/edit', methods=['PUT'])
def msg_edit():
    ''' Route to edit an existing message'''
    return message_edit(request.form.get('token'), request.form.get('message_id'),\
     request.form.get('message'))

@APP.route('/message/react', methods=['POST'])
def msg_react():
    ''' Route to react to an existing message'''
    return message_react(request.form.get('token'), request.form.get('message_id'),\
     request.form.get('react_id'))

@APP.route('/message/unreact', methods=['POST'])
def msg_unreact():
    ''' Route to unreact to an existing message'''
    return message_unreact(request.form.get('token'), request.form.get('message_id'),\
     request.form.get('react_id'))

@APP.route('/channel/join', methods=['POST'])
def channel_j():
    ''' Route to join an existing channel'''
    return channel_join(request.form.get('token'), request.form.get('channel_id'))

@APP.route('/channel/leave', methods=['POST'])
def channel_lve():
    ''' Route to leave an existing channel'''
    return channel_leave(request.form.get('token'), request.form.get('channel_id'))

@APP.route('/search', methods=['GET'])
def serch():
    ''' Route to search all existing channels for messages based on keyword'''
    return search(request.args.get('token'), request.args.get('query_str'))

@APP.route('/standup/start', methods=['POST'])
def stndup_strt():
    ''' Route to start a standup in an existing channel'''
    return standup_start(request.form.get('token'), request.form.get('channel_id'),\
     request.form.get('length'))

@APP.route('/standup/send', methods=['POST'])
def stndup_snd():
    ''' Route to send a message in an existing standup in an existing channel'''
    return standup_send(request.form.get('token'), request.form.get('channel_id'),\
     request.form.get('message'))

@APP.route('/standup/active', methods=['GET'])
def stndup_act():
    ''' Route to check if a standup is activvin an existing channel'''
    return standup_active(request.args.get('token'), request.args.get('channel_id'))

if __name__ == '__main__':
    APP.run(port=(sys.argv[1] if len(sys.argv) > 1 else 5000))
