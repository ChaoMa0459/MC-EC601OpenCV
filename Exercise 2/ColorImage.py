import numpy as np
import cv2
import sys

src = cv2.imread(sys.argv[1], 1) # sys.argv[1], the example input is Lenna.png
cv2.namedWindow('Original image', cv2.WINDOW_AUTOSIZE)
cv2.imshow( 'Original image', src)

# RGB
input_planes = []
input_planes = cv2.split(src)
cv2.imshow('Red',   input_planes[2])
cv2.imshow('Green',   input_planes[1])
cv2.imshow('Blue',   input_planes[0])

cv2.imwrite('Red.png',   input_planes[2])
cv2.imwrite('Green.png',   input_planes[1])
cv2.imwrite('Blue.png',   input_planes[0])

RGB_part = src[20,25]
print("RGB part",RGB_part)

# YCC
ycrcb_image = cv2.cvtColor(src, cv2.COLOR_BGR2YCR_CB)
ycc_planes = []
ycc_planes = cv2.split(ycrcb_image)
cv2.imshow('Y',   ycc_planes[0])
cv2.imshow('Cb',   ycc_planes[1])
cv2.imshow('Cr',   ycc_planes[2])

cv2.imwrite('Y.png',   ycc_planes[0])
cv2.imwrite('Cb.png',   ycc_planes[1])
cv2.imwrite('Cr.png',   ycc_planes[2])

YCC_part = ycrcb_image[20,25]
print("YCC part:", YCC_part)

# HSV
hsv_image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
hsv_planes = []
hsv_planes = cv2.split(hsv_image)
cv2.imshow('Hue',   hsv_planes[0])
cv2.imshow('Saturation',   hsv_planes[1])
cv2.imshow('Value',   hsv_planes[2])

cv2.imwrite('Hue.png',   hsv_planes[0])
cv2.imwrite('Saturation.png',   hsv_planes[1])
cv2.imwrite('Value.png',   hsv_planes[2])

hsv_part = hsv_image[20,25]
print("HSV part",hsv_part)

cv2.waitKey(0)                                      

#free and close
cv2.destroyAllWindows()
