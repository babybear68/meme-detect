import requests
import util
import json

def detect(query, n = 1):
    n = int(n)
    labels = {}
    failedCount = 0
    for i in range(n):
        payload = json.dumps({"requests": [{"image": {"source": {"imageUri": "gs://meme-images/" + query + "_" + str(i) + ".gif"}}, "features": [{"type": "LABEL_DETECTION"}]}]})
        r = requests.post(url = "https://vision.googleapis.com/v1/images:annotate?key=" + util.getGCloudAPIKey(), data = payload)
        #print r.json()["responses"][0]["labelAnnotations"][0]["description"]
        rJSON = r.json()
        if rJSON["responses"][0].has_key("error"):
            failedCount += 1
            continue
        for i in range(len(rJSON["responses"][0]["labelAnnotations"])):
            if rJSON["responses"][0]["labelAnnotations"][i]["description"] in labels:
                labels[rJSON["responses"][0]["labelAnnotations"][i]["description"]] += 1
            else:
                labels[rJSON["responses"][0]["labelAnnotations"][i]["description"]] = 1

    print "failed " + str(failedCount) + "\n"

    for key in sorted(labels, key = labels.get, reverse = True):
        print key + " " + str(labels[key])
