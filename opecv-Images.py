import numpy as np
import cv2
# http://www.codebind.com/python/opencv-python-tutorial-beginners-read-write-show-images-opencv/

gray_img = cv2.imread("lena.jpg",0) #Gray Image
img = cv2.imread("lena.jpg",1) #Color Image
cv2.imshow("Color Image",img)
key = cv2.waitKey(0)
if key == ord("s"):
    cv2.imwrite("New_image.png",img)
    print("Saved Image")
elif key == ord("g"):
    cv2.imshow("Gray Image", gray_img)
    print("Gray Image Show")
    cv2.waitKey(0)
elif ord("q"):
    print("Image Closed")
    cv2.destroyAllWindows()
