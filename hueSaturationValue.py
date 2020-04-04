# Hue is basically used for hight feature image extractions
import cv2
import numpy as np

# First we used image to take hsv in this image
# Manually we put values
'''
while True:
    img = cv2.imread("mnm.jpg")
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) # Convert BGR to HSV

    # We Find out blue color mnm so we need to put upper blue range and lower blue range
    l_b = np.array([102,63,148])
    u_b = np.array([148,255,255])

    # Then we find Thereshold

    mask = cv2.inRange(hsv,l_b,u_b)

    # Then we create bit wise multiplication we already known multiply show strangth value if we multiply

    res = cv2.bitwise_and(img,img,mask=mask)
    print(res)

    cv2.imshow("Image",img)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",res)

    key = cv2.waitKey(1)

    if key == 27:
        break
cv2.destroyAllWindows()
'''

# 2nd we create a trackbar to measure colours in images
'''
def color(x):
    pass

# Trackbars Create
cv2.namedWindow("Trackbar")
cv2.createTrackbar("LH","Trackbar",0,255,color) # Low hue value
cv2.createTrackbar("LS","Trackbar",0,255,color) # Low Saturation value
cv2.createTrackbar("LV","Trackbar",0,255,color) # Low value

# Because value is upper we down 255 to 0 that's why we put 255,255
cv2.createTrackbar("UH","Trackbar",255,255,color) # upper hue value
cv2.createTrackbar("US","Trackbar",255,255,color) # upper saturation value
cv2.createTrackbar("UV","Trackbar",255,255,color) # upper values


while True:
    #img = cv2.imread("mnm.jpg")
    img = cv2.imread("mnm.jpg")
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) # Convert BGR to HSV

    # Get lower Limits
    LH = cv2.getTrackbarPos("LH","Trackbar")
    LS = cv2.getTrackbarPos("LS", "Trackbar")
    LV = cv2.getTrackbarPos("LV", "Trackbar")


    # Get upper Limits
    UH = cv2.getTrackbarPos("UH","Trackbar")
    US = cv2.getTrackbarPos("US", "Trackbar")
    UV = cv2.getTrackbarPos("UV", "Trackbar")

    # We Find out blue color mnm so we need to put upper blue range and lower blue range
    low = np.array([LH,LS,LV])
    upper = np.array([UH,US,UV])

    # Then we find Thereshold

    mask = cv2.inRange(hsv,low,upper)

    # Then we create bit wise multiplication we already known multiply show strangth value if we multiply

    res = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("Image",img)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",res)

    key = cv2.waitKey(1)

    if key == 27:
        break
cv2.destroyAllWindows()
'''


# For Live streaming or video

def color(x):
    pass


cap = cv2.VideoCapture(0);  # Captured video

# Trackbars Create
cv2.namedWindow('Trackbar')
cv2.createTrackbar("LH","Trackbar",0,255,color) # Low hue value
cv2.createTrackbar("LS","Trackbar",0,255,color) # Low Saturation value
cv2.createTrackbar("LV","Trackbar",0,255,color) # Low value

# Because value is upper we down 255 to 0 that's why we put 255,255
cv2.createTrackbar("UH","Trackbar",255,255,color) # upper hue value
cv2.createTrackbar("US","Trackbar",255,255,color) # upper saturation value
cv2.createTrackbar("UV","Trackbar",255,255,color) # upper values
cv2.resizeWindow("Trackbar",500,10)

while True:
    ret,img = cap.read()
    #img = cv2.imread("mnm.jpg")
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) # Convert BGR to HSV

    # Get lower Limits
    LH = cv2.getTrackbarPos("LH","Trackbar")
    LS = cv2.getTrackbarPos("LS", "Trackbar")
    LV = cv2.getTrackbarPos("LV", "Trackbar")


    # Get upper Limits
    UH = cv2.getTrackbarPos("UH","Trackbar")
    US = cv2.getTrackbarPos("US", "Trackbar")
    UV = cv2.getTrackbarPos("UV", "Trackbar")

    # We Find out blue color mnm so we need to put upper blue range and lower blue range
    low = np.array([LH,LS,LV])
    upper = np.array([UH,US,UV])

    # Then we find Thereshold

    mask = cv2.inRange(hsv,low,upper)

    # Then we create bit wise multiplication we already known multiply show strangth value if we multiply

    res = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("Image",img)
    cv2.resizeWindow("Image", 500, 500)
    cv2.imshow("Mask",mask)
    cv2.resizeWindow("Mask", 500, 300)
    cv2.imshow("Result",res)
    cv2.resizeWindow("Result", 500, 500)

    key = cv2.waitKey(1)

    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()

