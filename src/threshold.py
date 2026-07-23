from PIL import Image
import numpy as np

img = Image.open("images/dog image.webp").convert("L")
arr = np.array(img)

print(arr.shape)
threshold = int(input("Enter threshold: "))

binary = np.where(arr >= threshold, 255, 0).astype(arr.dtype)
output = Image.fromarray(binary)
output.show()
output.save("outputs/threshold.png")