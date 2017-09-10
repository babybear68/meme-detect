import requests
import json

def getAPIKey():
    keyFile = open("key.txt", 'r')
    key = keyFile.read().splitlines()[0]
    keyFile.close()
    return key

def getGCloudAPIKey():
    keyFile = open("gcloud-key.txt", 'r')
    key = keyFile.read().splitlines()[0]
    keyFile.close()
    return key

def getAccessToken():
    tokenFile = open("token.txt", 'r')
    token = tokenFile.read().splitlines()[0]
    tokenFile.close()
    return token

def makePublic(fileName):
    payload = json.dumps({"entity": "allUsers", "role": "READER"})
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + getAccessToken()}
    r = requests.post(url = "https://www.googleapis.com/storage/v1/b/meme-images/o/" + fileName + "/acl", data = payload, headers = headers)
    print "made public " + r.reason
