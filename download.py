import sys
import search
import urllib

def download(query, n = 1):
    n = int(n)
    if query == "trending":
        images = search.trending(n)
    else:
        images = search.search(query, n)
    for i in range(n):
        image_url = images[i][0]
        urllib.urlretrieve(image_url, "downloads/" + query + "_" + str(i) + ".gif")
        if i % 5 == 4:
            print str(i + 1) + " completed"
