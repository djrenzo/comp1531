'''Test search function'''
# pylint: disable=W0622, C0413, C0411
import sys
from .search import search
from .auth_register import auth_register
from .channels_create import channels_create
from .message_send import message_send
sys.path.append("..")
import db
import Token


def test_search():
    '''Test that all strings in messages are the same as the query_str'''
    db.reset_DB()
    auth_register('hosh_mail@gmail.com', 'pas123456', 'Hosh', 'Mehta')
    token = Token.generateToken('hosh_mail@gmail.com')
    channels_create(token, 'Yes', True)
    message_send(token, 1, 'Hi')
    query_str = 'Hi'
    messages = search(token, query_str)
    for _ in messages:
        assert query_str == 'Hi'
