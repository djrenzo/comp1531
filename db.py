import re
from json import *
import Token
import os
import hashlib

standardDB = {"channels": [],
"users": [
{
    "tokens": [
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFkbWluQGdtYWlsLmNvbSIsInRpbWVzdGFtcCI6MTU3Mzg3NzgzNC40MTE1OTR9.5CkB0u_oaGvmpsxbeOSmMqlLGkSc4DJwRferSCePx8U"
    ],
    "profile_img_url": "https://crmbusiness.files.wordpress.com/2014/11/administrator.jpg",
    "handle_str": "JackCrisp",
    "u_id": 0,
    "email": "admin@gmail.com",
    "password": "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9",
    "name_first": "Jack",
    "name_last": "Crisp",
    "permission_id": 1
}
],
"messages": [],
"standups": []}

def load_DB():
    if os.path.isfile("./database.json"):

        f = open("database.json","r")
        datastring= f.read()
        if not datastring is "":
            data = loads(datastring)
            return data

    database = standardDB

    js = dumps(database)
    f = open("database.json","w")
    f.write(js)
    f.close()

    return database

def save_DB(db):
    js = dumps(db, indent=4)
    f = open("database.json","w")
    f.write(js)
    f.close()

def reset_DB():
    database = standardDB

    js = dumps(database)
    f = open("database.json","w")
    f.write(js)
    f.close()

def new_u_id(db):
    if db['users'] == []:
        return 1
    return max([int(user['u_id']) for user in db["users"]]) + 1

def new_channel_id(db):
    if db['channels'] == []:
        return 1
    return max([int(channel['channel_id']) for channel in db["channels"]]) + 1

def new_message_id(db):
    if db['messages'] == []:
        return 1
    return max([int(msg['message_id']) for msg in db['messages']]) + 1

def new_standup_id(db):
    if db['standups'] == []:
        return 1
    return max([int(stndup['standup_id']) for stndup in db['standups']]) + 1

def get_react_users(db, u_id, message_id, react_id, b=True):
    msg = [message for message in db['messages'] if message['message_id'] == message_id][0]
    if msg['reacts'] == []:
        if b:
            return [u_id]
        else:
            return []

    cur_react = [r for r in msg['reacts'] if r['react_id'] == react_id][0]
    if b:
        cur_react['u_ids'].append(u_id)
    return cur_react['u_ids']

def get_user_reacted(db, u_id, message_id, react_id):
    msg = [message for message in db['messages'] if message['message_id'] == message_id][0]
    if msg['reacts'] == []:
        return False

    cur_react = [r for r in msg['reacts'] if r['react_id'] == react_id][0]
    if u_id in cur_react['u_ids']:
        return True
    return False

def get_from_token(val, token, db):
    email = Token.decodeToken(token)['email']
    output = [user[val] for user in db['users'] if user['email'] == email]
    if output:
        return output[0]
    return []

def check_mail(email):
    if(re.search(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',email)):
        return True
    return False

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def from_db(func):
    def wrapper(*args, **kwargs):
        f = func(*args, **kwargs)
        return [value[f[0]] for value in f[2][f[1]]]
    return wrapper

@from_db
def get_all_channels(data):
    return ('channel_id', 'channels', data)

@from_db
def get_all_messages(data):
    return ('message_id', 'messages', data)

@from_db
def get_all_users(data):
    return ('u_id', 'users', data)

def get_channel_by_id(data, channel_id):
    return [channel for channel in data['channels'] if channel['channel_id'] == channel_id][0]
