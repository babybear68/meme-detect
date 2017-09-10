import requests
import json
import base64
import util
import sys

def upload(query, n = 1):
    n = int(n)
    for name in [query + '_' + str(i) for i in range(n)]:
        with open("downloads/" + name + ".gif", "rb") as image_file:
            data = image_file.read()

        headers = {"Content-type": "image/gif", "Authorization": "Bearer " + util.getAccessToken()}

        r = requests.post(url = "https://www.googleapis.com/upload/storage/v1/b/meme-images/o?uploadType=media&name=" + name + ".gif", data = data, headers = headers)
        print name + ' ' + r.reason
        util.makePublic(name + ".gif")
