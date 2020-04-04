import cv2
#link : https://docs.opencv.org/master/d0/d86/tutorial_py_image_arithmetics.html


"""

# Get Points of images

def mouse_event(event,x,y,flags,parms):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("Right click")
        points.append((x,y))
        print(points)
        cv2.circle(img,(x,y),3,(0,255,255),-1)
        cv2.imshow("Image",img)


img = cv2.imread("messi.jpg",1)
cv2.imshow("Image",img)
points = []
cv2.setMouseCallback("Image",mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

"""

img = cv2.imread("messi.jpg")
print(img.size)
print(img.shape)
print(img.dtype)

b,g,r = cv2.split(img)     # Split into blue , green , red
img = cv2.merge((b,g,r))   # Merge blue green value into an image
"""

#358, 167), (430, 213)   for ball
#[(18, 170)] (90,216)  for grass
# Copy ball to grass and grass to ball
"""

ball = img[167:213, 358:430]
print(ball.shape)
grass = img[170:216, 18:90].copy()
print(grass.shape)
img[170:216, 18:90] = ball
img[167:213, 358:430] = grass
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

# Resize Image
img = cv2.imread("messi.jpg")
img2 = cv2.imread("logo.jpg")
print(img.shape)
print(img2.shape)

img = cv2.resize(img,(270,236))
img2 = cv2.resize(img2,(270,236))


# Add to images
"""
img3 = cv2.add(img,img2)
cv2.imshow("Image",img3)
"""
# add by waits
img3 = cv2.addWeighted(img,0.7,img2,0.3,0)
cv2.imshow("Image",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()









