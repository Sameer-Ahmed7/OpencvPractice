'''
We used very basic thresholding technqiues in python
In this thresholding technqiue we set global vof our threshold like 127,50 etc. in this the problem is this
it become same for every pixels value so it's create a noisy image because some time lightning
So the issue will be resolve by adaptive thresholding by it's take thresh value for the smaller region '
different thresh value for different region
'''
# problem for previous thresholding

import cv2

"""
img = cv2.imread("suduko.jpg",0)


ret1,thr1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY) # 127 is global value we talk above

cv2.imshow("Image",img)
cv2.imshow("thr1",thr1)

# it's show noisy image after thresholding

cv2.waitKey(0)
cv2.destroyAllWindows()
"""

"""
So the problem is resolve by adaptive_threshold
link : https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#adaptive-thresholding
we have 2 type of adaptive thresholding
1) Adaptive threshold Mean C
2) Adaptive threshold Gaussian C

"""


img = cv2.imread("suduko.jpg",0)
#Simple thresholding
ret1,thr1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY) # 127 is global value we talk above

# Adaptive threshold Mean C
thr2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2) # Block size is for neighbourhood pixels , and c is constant

# Adaptive threshold Gauusian C
thr3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2) # Block size is for neighbourhood pixels , and c is constant

#Note if we apply thresholding in Color of bgr image it's shows an error so we will put in gray scale image
# link https://stackoverflow.com/questions/27014207/failure-to-use-adaptivethreshold-cv-8uc1-in-function-adaptivethreshold


cv2.imshow("Image",img)
cv2.imshow("thr1",thr1)
cv2.imshow("thr2",thr2)
cv2.imshow("thr3",thr3)



cv2.waitKey(0)
cv2.destroyAllWindows()


