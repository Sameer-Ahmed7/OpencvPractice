import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID') # or ("X","V","I","D")

out = cv2.VideoWriter("new_video.mp4",fourcc,20.0,(640,480))   # http://www.fourcc.org/codecs.php
                                                                # (add,fourcc,frame per second,(wid,heig)

while (cap.isOpened()):

    #Properties
    # https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d

    ret, frame = cap.read()

    if ret == True:
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print("Height : "+str(height)+" Width :"+str(width))
        cv2.imshow("Color Video", frame)
        gray_scale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray Video", gray_scale)

        out.write(frame)

        key = cv2.waitKey(1)
        if key == ord("q"):
            print("Closed Video")
            break

    else:
        break



cap.release()
out.release()
cv2.destroyAllWindows()
