import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
BGR = cv.imread('im30.png')
RGB = cv.cvtColor(BGR, cv.COLOR_BGR2RGB)
binary = np.logical_and(RGB[:,:,2]>100,RGB[:,:,2]<150)
blue = 255*np.uint8(binary)
blur = cv.medianBlur(blue,15)
plt.figure(1)
plt.clf()
plt.imshow(blue, cmap='gray')
plt.pause(0.001)
plt.figure(2)
plt.clf()
plt.imshow(blur, cmap='gray')
plt.pause(0.001)
plt.show()
