import sys
import search
import urllib

if sys.argv[1] == "trending":
    images = search.trending(int(sys.argv[2]))
else:
    images = search.search(sys.argv[1], int(sys.argv[2]))
for i in range(int(sys.argv[2])):
    image_url = images[i][0]
    urllib.urlretrieve(image_url, "downloads/" + sys.argv[1] + "_" + str(i) + ".gif")
