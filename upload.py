import requests
import json
import base64
import util
import sys

def upload(name):
    with open("downloads/" + name + ".gif", "rb") as image_file:
        data = image_file.read()

    headers = {"Content-type": "image/gif", "Authorization": "Bearer " + util.getAccessToken()}

    r = requests.post(url = "https://www.googleapis.com/upload/storage/v1/b/meme-images/o?uploadType=media&name=" + name + ".gif", data = data, headers = headers)
    print name + ' ' + r.reason

def main():
    for name in [sys.argv[1] + '_' + str(i) for i in range(int(sys.argv[2]))]:
        upload(name)
        util.makePublic(name + ".gif")

main()
