import cv2 as cv
import numpy as np
import sys

img = np.zeros((300, 300, 3), dtype='uint8')
# img[150, 150] = 244

# img[50:150:, 20:25] = 0xff, 100, 0xff
# img[50:150:, 160:165] = 0xff, 100, 0xff
# img[145:150:, 20:160] = 0xff, 100, 0xff
# img[50:55:, 20:160] = 0xff, 100, 0xff

cv.rectangle(img[50:], (0,0), (50, 50), (0xff, 100, 0xff), thickness=1)
cv.imshow('zxc', img)


while True:
    if (cv.waitKey(0) & 0xFF) == ord('q'):
        sys.exit()
