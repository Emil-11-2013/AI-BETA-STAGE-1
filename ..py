import cv2

image = cv2.imread('boy.png')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resized_image = cv2.resize(gray_image, (224, 224))

cv2.imshow("Prosseced image", resized_image)

cv2.imshow("Loaded Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Image Dimensions: {image.shape}")