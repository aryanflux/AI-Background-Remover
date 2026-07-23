import cv2

img = cv2.imread("images/dog image.webp")

print(type(img))
print(img.shape)

cv2.imshow("Dog", img)

cv2.waitKey(0)

cv2.destroyAllWindows()