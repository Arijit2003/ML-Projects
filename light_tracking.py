import cv2

#instance of video capture
cap=cv2.VideoCapture(0)
opened=cap.isOpened()

height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
fps=cap.get(cv2.CAP_PROP_FPS)
print("Width: {}".format(width)+" Height: {}".format(height))
print("FPS: {}".format(fps))

if(opened):
    while(cap.isOpened):
        ret,frame=cap.read()
        if(ret==True):
            grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            maxValue=cv2.minMaxLoc(grayFrame)[1]
            x_coord=cv2.minMaxLoc(grayFrame)[3][0]
            y_coord=cv2.minMaxLoc(grayFrame)[3][1]
            if(maxValue>220):
                dist=50
                coord1=(x_coord+dist,y_coord+dist)
                coord2=(x_coord-dist,y_coord-dist)
                thick=6
                color=(0,255,0)
                cv2.rectangle(frame,coord2,coord1,color,thick)
            cv2.imshow("Light Source",frame)
            if(cv2.waitKey(2)==ord("q")):
                break


cap.release()
cv2.destroyAllWindows()
