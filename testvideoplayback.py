import cv2 as cv
import matplotlib.pyplot as plt
cap = cv.VideoCapture('wiffleBalls.mov')
fps = cap.get(cv.CAP_PROP_FPS)
print('Frames per second: ', fps)
ret, BGR = cap.read()
while ret:
    RGB = cv.cvtColor(BGR, cv.COLOR_BGR2RGB)
    plt.figure(1)
    plt.clf()
    plt.imshow(RGB)
    plt.pause(0.001)
    ret,BGR = cap.read()
cap.release()
