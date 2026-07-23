from PIL import Image
import numpy as np
#PIL is the pillow library
img = Image.open("images/dog image.webp")
arr=np.array(img)
arr[200:205, :] = [255, 255, 0]
arr[:, 300:305] = [0, 0, 255]
new_img = Image.fromarray(arr)
new_img.show()
'''THE OBJECT img knows all this:
image width
image height
color mode
file format
every pixel'''
