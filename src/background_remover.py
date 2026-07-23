from PIL import Image
import numpy as np
def add_alpha_channel(image):
    return image.convert("RGBA")
def apply_alpha(image, alpha):
    image.putalpha(alpha)
    return image
 
def create_dummy_mask(image):
    width, height = image.size

    mask = Image.new("L", (width, height), 0)
    img=np.array(mask)
    img[:, :width//2] = 255
    return Image.fromarray(img)

def remove_background(image):
    rgba = add_alpha_channel(image)
    mask = create_dummy_mask(image)
    mask.save("images/output/mask.png")

    return apply_alpha(image,mask)
