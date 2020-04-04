import cv2
import numpy as np

img = np.zeros((700,700,3),np.uint8) # Black image

#img = cv2.imread("lena.jpg",1)
img = cv2.line(img, (0, 0), (400, 400), (0, 255, 0), 10) # Draw Line color is bgr formate
img = cv2.arrowedLine(img, (0, 400), (255, 40), (255, 0, 24), 10) # Draw Arrow Line
img = cv2.rectangle(img,(255,255),(400,400),(0,0,255),-1) #if thicknees = -1 means fill
img = cv2.circle(img,(327,327),50,(0,255,255),-1) #if thicknees = -1 means fill
font = cv2.FONT_HERSHEY_COMPLEX

img = cv2.putText(img,"Hello Sameer",(100,100),font,2,(0,255,255),10)


cv2.imshow("Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()