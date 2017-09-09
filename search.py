import urllib,json
import util
import random

def search(query, n = 1):
    data = json.loads(urllib.urlopen("https://api.giphy.com/v1/gifs/search?api_key=" + util.getAPIKey() + "&q=" + query + "&limit=25").read())
    return [(data["data"][i]["images"]["downsized_medium"]["url"],
        (data["data"][i]["images"]["downsized_medium"]["height"],
        data["data"][i]["images"]["downsized_medium"]["width"])) for i in range(n)]

def trending(n = 1):
    data = json.loads(urllib.urlopen("https://api.giphy.com/v1/gifs/trending?api_key=" + util.getAPIKey() + "&limit=25").read())
    return [(data["data"][i]["images"]["downsized_medium"]["url"],
        (data["data"][i]["images"]["downsized_medium"]["height"],
        data["data"][i]["images"]["downsized_medium"]["width"])) for i in range(n)]
