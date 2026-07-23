from src.image_io import load_image, save_image
from src.preprocessing import resize_image, convert_to_grayscale

img = load_image("images/inputs/dog image.webp")
resized = resize_image(img, 512, 512)
new_img=convert_to_grayscale(resized)
save_image(new_img, "images/outputs/resized.png")

print("Image resized successfully!")