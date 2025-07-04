import cv2
import numpy as np

frameWidth= 640
frameHeight= 480
cap= cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)

def empty(a):
    pass
cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars',640,240)
cv2.createTrackbar('hue min','TrackBars',0,179,empty)
cv2.createTrackbar('hue max','TrackBars',179,179,empty)
cv2.createTrackbar('sat min','TrackBars',0,255,empty)
cv2.createTrackbar('sat max','TrackBars',255,255,empty)
cv2.createTrackbar('val min','TrackBars',0,255,empty)
cv2.createTrackbar('val max','TrackBars',255,255,empty)

while True:
    _, img= cap.read()
    imgHSV= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('hue min', 'TrackBars')
    h_max = cv2.getTrackbarPos('hue max', 'TrackBars')
    s_min = cv2.getTrackbarPos('sat min', 'TrackBars')
    s_max = cv2.getTrackbarPos('sat max', 'TrackBars')
    v_min = cv2.getTrackbarPos('val min', 'TrackBars')
    v_max = cv2.getTrackbarPos('val max', 'TrackBars')
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    mask= cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    hStack= np.hstack([img,mask,imgResult])
    cv2.imshow('stack',hStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()