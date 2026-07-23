'''goal
If ANY pixel in this neighborhood is white, make the output pixel white.'''
import numpy as np

img = np.array([
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,255,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
], dtype=np.uint8)
print(img)

dilated = np.zeros_like(img)
for i in range(1, img.shape[0]-1):
    for j in range(1, img.shape[1]-1):
        neighborhood = img[i-1:i+2, j-1:j+2]

        if np.any(neighborhood == 255):
            dilated[i, j] = 255
        else:
            dilated[i, j] = 0
            