import cv2
import numpy as np


#events = [i for i in dir(cv2)  if "EVENT" in i]    LIst of events
#print(events)

# Condition # 1 : for if condition when we click left double click we create a circle and draw a line

# Condition # 2 : for elif condition when we move mouse we create image on same what we click

# Condition # 3 : for elif 2 condition when we click right double click we create a circle on new window same color

def mouse_event(event,x,y,flags,parms):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("Left button Click")
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        cv2.imshow("Image",img)
        points.append((x,y))
        if len(points)>=2:     # we create line when circle is 2 because line take 2 point
            cv2.line(img,points[-1],points[-2],(0,255,255),3)
            cv2.imshow("Image",img)



    elif event == cv2.EVENT_MOUSEMOVE:

        #Image in bgr formate

        print("Mouse Move")
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]

        event_img = np.zeros((512,512,3),np.uint8)
        event_img[:] = [blue,green,red]
        cv2.imshow("Event Image",event_img)

    """
        elif event == cv2.EVENT_RBUTTONDBLCLK:




            # Image in bgr formate

            print("Right Button")
            blue = img[x,y,0]
            print(blue)
            green = img[x,y,1]
            print(green)
            red = img[x,y,2]
            print(red)
            color = np.array([blue,green,red])

            event_img = np.zeros((512,512,3),np.uint8)
            cv2.circle(event_img,(x,y),4,color,-1)
            cv2.imshow("Event Image",event_img)
        """


#img = np.zeros((512,512,3),np.uint8)
img = cv2.imread("lena.jpg",1)
cv2.imshow("Image",img)
points = []
cv2.setMouseCallback("Image",mouse_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
