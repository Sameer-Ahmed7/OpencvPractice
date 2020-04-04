import cv2
import datetime


cap = cv2.VideoCapture(0)



while (cap.isOpened()):
    ret ,  frame = cap.read()
    date = datetime.datetime.now()
    font = cv2.FONT_HERSHEY_SIMPLEX
    frame = cv2.putText(frame,"Date:"+str(date),(40,40),font,1,(0,255,255),2)
    text = "width: "+str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))+" Height: "+str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame = cv2.putText(frame, text, (0, 480), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow("Image",frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        print("Closed video")
        break

cap.release()
cv2.destroyAllWindows()