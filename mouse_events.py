import cv2
import numpy as np


#events = [i for i in dir(cv2)  if "EVENT" in i]    LIst of events
#print(events)

def mouse_event(event,x,y,flags,parms):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("Left button click")
        print(x,y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        #text = str(x)+" , "+str(y)
        #cv2.putText(img,text,(x,y),font,0.5,(0,255,255),2)
        cv2.circle(img,(x,y),10,(255,255,0),-1)
        cv2.imshow("Image",img)

    elif event == cv2.EVENT_RBUTTONDBLCLK:
        # Image is shown in Blue,Green,Red formate

        print("Right Button Click")
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "("+str(blue)+","+str(green)+","+str(red)+")"
        cv2.putText(img, text, (x, y), font, 0.5, (0, 255, 255), 2)
        cv2.imshow("Image", img)





#img = np.zeros((400,400,3),np.uint8)
img = cv2.imread("lena.jpg",1)
cv2.imshow("Image",img)
cv2.setMouseCallback("Image",mouse_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
