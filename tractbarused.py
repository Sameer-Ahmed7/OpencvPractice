import cv2
import numpy as np

# Tackbar for b,g,r value change
'''
def color(x):
    print(x)

img = np.zeros((500,500,3),np.uint8)
cv2.namedWindow("Image")

cv2.createTrackbar("B", "Image", 0, 255, color)
cv2.createTrackbar("G", "Image", 0, 255, color)
cv2.createTrackbar("R", "Image", 0, 255, color)
cv2.createTrackbar("Switch","Image",0,1,color)

while True:

    cv2.imshow("Image", img)

    b = cv2.getTrackbarPos("B","Image")
    g = cv2.getTrackbarPos("G","Image")
    r = cv2.getTrackbarPos("R","Image")
    s = cv2.getTrackbarPos("Switch","Image")

    if s == 0:
        print("Switch is closed")

    else:
        img[:] = [b,g,r]
    key = cv2.waitKey(1)
    if key == 27:   # Escape key
        break


cv2.destroyAllWindows()

'''

# For Color to black and white image
def color(x):
    print(x)
cv2.namedWindow("Image")

cv2.createTrackbar("Color:0 and Gray:1 ","Image",0,1,color)
while(1):

    img = cv2.imread("messi.jpg")
    c = cv2.getTrackbarPos("Color:0 and Gray:1 ","Image")
    if c == 0:
        pass
    else:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Image",img)


    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()















