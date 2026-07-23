from PIL import Image
import numpy as np

img = Image.open("images/dog image.webp")
arr = np.array(img)

red = arr[:, :, 0]
green = arr[:, :, 1]
blue = arr[:, :, 2]

Image.fromarray(red).save("outputs/red_channel.png")
Image.fromarray(green).save("outputs/green_channel.png")
Image.fromarray(blue).save("outputs/blue_channel.png")