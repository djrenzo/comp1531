'''Allow a user to upload a photo'''
# pylint: disable=W0622, C0413, C0411, E1101, R0913
from .AccessError import AccessError
from json import dumps
import sys
import cv2
import numpy as np
import urllib
sys.path.append("..")
import db
import Token

def user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end, port):
    '''Allow a user to upload a photo'''
    if not Token.isValid(token):
        raise AccessError("Not a valid token!")
    data = db.load_DB()
    u_id = db.get_from_token("u_id", token, data)
    print("URL ==", img_url)
    resp = urllib.request.urlopen(img_url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, -1)
    crop = image[int(y_start):int(y_end), int(x_start):int(x_end)]
    cv2.imwrite(f'imgurl/{u_id}.jpg', crop)

    for user in data['users']:
        if user['u_id'] == u_id:
            user['profile_img_url'] = f'http://127.0.0.1:{port}/imgurl?id={u_id}'

    db.save_DB(data)

    return dumps({})
