from PIL import Image

def load_image(path):
    img=Image.open(path)
    return img

def save_image(image,path):
    image.save(path)
