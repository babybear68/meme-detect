import sys
import io
import base64
import search
try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen


root = tk.Tk()
root.title("display " + sys.argv[0])
image = search.search(sys.argv[1])
# a little more than width and height of image
w = int(image[1][1])
h = int(image[1][0])
x = 80
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

image_url = image[0]

image_byt = urlopen(image_url).read()
image_b64 = base64.encodestring(image_byt)
photo = tk.PhotoImage(data=image_b64)

# create a white canvas
cv = tk.Canvas(bg='white')
cv.pack(side='top', fill='both', expand='yes')

# put the image on the canvas with
# create_image(xpos, ypos, image, anchor)
cv.create_image(10, 10, image=photo, anchor='nw')

root.mainloop()
