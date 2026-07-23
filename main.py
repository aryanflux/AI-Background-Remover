from src.image_io import load_image, save_image
from src.background_remover import remove_background

img = load_image("images/input/dog image.webp")
result = remove_background(img)
save_image(result, "images/output/output.png")
print("Background removed successfully!")
print(result.mode)