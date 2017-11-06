import numpy as np
import cv2
import sys

# Mat src, gray, dst;

# Load an image
src = cv2.imread(sys.argv[1], 1)

# Convert the image to Gray
gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)

cv2.namedWindow("Input Image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Input Image", src)
cv2.imwrite("Input Image.png", src)

# 0: Binary,
# 1: Binary Inverted,
# 2: Threshold Truncated,
# 3: Threshold to Zero,
# 4: Threshold to Zero Inverted
threshold_type = 2    # slider 1 [0, 4]
threshold_value = 128  # slider 2 [0 255]

ret, dst = cv2.threshold(gray, threshold_value, 255, threshold_type)
cv2.imshow("Thresholded Image", dst)
cv2.imwrite("Thresholded Image.png", dst)

current_threshold = 128
max_threshold = 255

# Binary Threshold
ret, thresholded = cv2.threshold(gray, current_threshold, max_threshold, cv2.THRESH_BINARY)
cv2.imshow("Binary threshold",thresholded)
cv2.imwrite("Binary threshold.png",thresholded)

# Band thresholding
threshold1 = 27
threshold2 = 125
ret, binary_image1 = cv2.threshold(gray, threshold1, max_threshold, cv2.THRESH_BINARY)
ret, binary_image2 = cv2.threshold(gray, threshold2, max_threshold, cv2.THRESH_BINARY_INV)
band_thresholded_image = cv2.bitwise_and(binary_image1, binary_image2)
cv2.imshow("Band Thresholding", band_thresholded_image)
cv2.imwrite("Band Thresholding.png", band_thresholded_image)

# Semi thresholding
ret, semi_thresholded_image = cv2.threshold(gray, current_threshold, max_threshold, cv2.THRESH_BINARY_INV or cv2.THRESH_OTSU)
semi_thresholded_image = cv2.bitwise_and(gray, semi_thresholded_image)
cv2.imshow("Semi Thresholding", semi_thresholded_image)
cv2.imwrite("Semi Thresholding.png", semi_thresholded_image)

# Adaptive thresholding
adaptive_thresh = cv2.adaptiveThreshold(gray, 255.0, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 10)
cv2.imshow("Adaptive Thresholding", adaptive_thresh)
cv2.imwrite("Adaptive Thresholding.png", adaptive_thresh)

cv2.waitKey(0)                                      

#free and close
cv2.destroyAllWindows()
