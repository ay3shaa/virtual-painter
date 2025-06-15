import cv2
import numpy as np

frameWidth= 640
frameHeight= 480
cap= cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)

colors= [[111,116,62,179,255,255],
         [0,116,114,10,255,255]]

color_values=[[255,0,0],        #BGR values
              [0,0,255]]

points= []


def find_color(img, colors,color_values):
    img_hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count=0
    new_points=[]
    for col in colors:
        lower = np.array(col[0:3])
        upper = np.array(col[3:6])
        mask = cv2.inRange(img_hsv, lower, upper)
        x,y=getContours(mask)
        cv2.circle(imgResult,(x,y),5,color_values[count],cv2.FILLED)
        if x!=0 and y!=0:
            new_points.append([x,y,count])
        count+=1
    return new_points   #cv2.imshow(str(col[0]),mask)

def getContours(img):
    contours,hierarchy= cv2.findContours(img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h= 0,0,0,0
    for cnt in contours:
        area= cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgResult,cnt,-1,(255,0,0),2)
            peri= cv2.arcLength(cnt,True)
            approx= cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h= cv2.boundingRect(approx)
    return x+w//2,y

def drawOnScreen(points,color_values):
    for point in points:
        cv2.circle(imgResult, (point[0], point[1]), 15, color_values[point[2]], cv2.FILLED)


while True:
    success, img= cap.read()
    imgResult= img.copy()
    new_points= find_color(img, colors,color_values)
    if len(new_points)!=0:
        for new in new_points:
            points.append(new)
    if len(points)!=0:
        drawOnScreen(points,color_values)
    cv2.imshow('webcam',imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break