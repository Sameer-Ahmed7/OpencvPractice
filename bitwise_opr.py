import cv2
import numpy as np

# https://docs.opencv.org/master/d0/d86/tutorial_py_image_arithmetics.html
"""
def mouse_event(event,x,y,flags,params):
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(img,(x,y),3,(0,255,255),-1)
        points.append((x,y))
        print(points)
        cv2.imshow("Image",img)




img = cv2.imread("blackandwhite.png")
cv2.imshow("Image",img)
points = []
cv2.setMouseCallback("Image",mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

# Create Images
# Dimesnions of image [(75, 1), (154, 54)] create rectangular

img = cv2.imread("blackandwhite.png")
#print(img.shape)  # (212, 238, 3) we create second pic according to this image

img2 = np.zeros((212, 238, 3), np.uint8)
cv2.rectangle(img2,(75,1),(154,54),(255,255,255),-1)
cv2.imshow("image 1",img)
cv2.imshow("image 2",img2)

# Bitwise operations
# And operations
"""
bitAnd = cv2.bitwise_and(img2,img)
cv2.imshow("Bitwise And",bitAnd)"""

# Or operations
'''
bitOr = cv2.bitwise_or(img2,img)
cv2.imshow("Bitwise or",bitOr)
'''

# XOR operations
'''
bitXor = cv2.bitwise_xor(img2,img)
cv2.imshow("Bitwise XOR",bitXor)'''

# Not operation
bitNot1 = cv2.bitwise_not(img)
cv2.imshow("Bitwise Not 1",bitNot1)
bitNot2 = cv2.bitwise_not(img2)
cv2.imshow("Bitwise Not 2",bitNot2)



cv2.waitKey(0)
cv2.destroyAllWindows()























