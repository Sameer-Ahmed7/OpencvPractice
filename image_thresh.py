# For thresholding
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html

'''


Thresholding is segmentation technqiue in which we seprate from it's background
the process is to compare each of the pixels of image with a predefine threshold value
and this type oc comparision of each type of pixels is divides import image into tow groups
1) Intensity value is less the the threshold value
2) Intensity value is greater the the threshold value
using different thresh technqiue WE can give different thresh value which
are higher then the thresh value and intensity less then the thresh value

'''

import cv2
import numpy as np

img = cv2.imread("grad.jpg")
img = cv2.resize(img,(200,200))

'''
# some technqiues of threshold
# Thresh binary is compare thresh value is less then intinsity the value is 0 or vise versa
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)  # 127 is comparision if value is less then 127 or greater then 127
# Thresh binary inv is compare thresh value is greater then intinsity the value is 0 or vise versa
ret2,th2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)  # 127 is comparision if value is less then 127 or greater then 127
'''

# thresh value change
# Thresh binary is compare thresh value is less then intinsity the value is 0 or vise versa
ret1,th1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)  # 50 is comparision if value is less then 50 or greater then 50
# Thresh binary inv is compare thresh value is greater then intinsity the value is 0 or vise versa
ret2,th2 = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)  # 200 is comparision if value is less then 200 or greater then 200
# In thresh trunc the value is less then thresh is remain same or if greater then it will become thresh value
ret3,th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)  # 127 is comparision if value is less then 127 or greater then 127
# In thresh tozero the value is less then thresh it's will be zero or if greater then it remain same
ret4,th4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)  # 127 is comparision if value is less then 127 or greater then 127
# In thresh tozero inv the value is greater then thresh it's will be zero or if less then thresh it remain same
ret5,th5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)  # 127 is comparision if value is less then 127 or greater then 127



cv2.imshow("Image",img)
cv2.imshow("th1",th1)
cv2.imshow("th2",th2)
cv2.imshow("th3",th3)
cv2.imshow("th4",th4)
cv2.imshow("th5",th5)

cv2.waitKey(0)
cv2.destroyAllWindows()