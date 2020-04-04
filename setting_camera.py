import cv2

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

cap.set(cv2.CAP_PROP_FRAME_WIDTH,1000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1000)

print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))


while (cap.isOpened()):
    ret ,  frame = cap.read()
    cv2.imshow("Image",frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        print("Closed video")
        break

cap.release()
cv2.destroyAllWindows()