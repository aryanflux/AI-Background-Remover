from PIL import Image
def convert_to_grayscale(image):
    return image.convert("L")

def resize_image(image, width, height):
    return image.resize((width, height))