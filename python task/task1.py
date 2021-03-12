import cv2
import numpy as np

image = cv2.imread('sora1.jpg')
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image', image)
cv2.imshow('Gray image', img)

height, width, channels = img.shape
upper_left = (width // 4, height // 4)
bottom_right = (width * 3 // 4, height * 3 // 4)
# draw in the image
cv2.rectangle(img, upper_left, bottom_right, (0, 255, 0), thickness=1)
cv2.imshow('draw_img', img)

#rect_img = img[upper_left[1]: bottom_right[1] + 1, upper_left[0]: bottom_right[0] + 1]
#rect_img[:] = (0, 0, 255)  # modify value
#cv2.imshow('index_img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()