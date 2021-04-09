import jwt
import datetime
import db

def get_secret():
    return 'dishDANG'

def generateToken(email):
    newtoken = jwt.encode({'email' : email, 'timestamp': datetime.datetime.now().timestamp()}, get_secret(), algorithm='HS256').decode('utf-8')
    data = db.load_DB()
    tokens = db.get_from_token('tokens', newtoken, data)
    tokens.append(newtoken)

    for user in data['users']:
        if user['email'] == email:
            user['tokens'] = tokens
    db.save_DB(data)
    return newtoken

def decodeToken(token):
    return jwt.decode(token, get_secret(), algorithms=['HS256'])

def isValid(token):
    try:
        decoded = decodeToken(token)
        if decoded:
            tokens = db.get_from_token('tokens', token, db.load_DB())
            # print("tokens in db:", tokens)
            # print("token given", token)
            if token in tokens:
                return True
    except:
         return False

def removeToken(token):
    data = db.load_DB()
    email = db.get_from_token('email', token, data)

    for user in data['users']:
        if user['email'] == email:
            user['tokens'].remove(token)
    db.save_DB(data)
