from PIL import Image
import numpy as np

img = Image.open("images/dog image.webp").convert("L")
arr = np.array(img)
print(arr.shape)
binary = np.zeros_like(arr)