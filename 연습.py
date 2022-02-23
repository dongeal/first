import cv2
import random

'''
img=cv2.imread('img.jpg')
cv2.imshow('test',img)
cv2.waitKey(0)

radius=30
color=(255,255,0)
thick=2
cv2.circle(img,(300,300),radius,color,thick,cv2.LINE_AA)
cv2.imshow('test',img)

cv2.waitKey(0)

'''

cap=cv2.VideoCapture('video.mp4')


thick=2
while cap.isOpened() :
    ret, frame=cap.read()
    if not ret :
        print('no more frame')
        break

    cv2.imshow('video', frame)
    color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    center =(random.randrange(1, 300), random.randrange(1, 600))
    radius = random.randrange(5,100)
    if random.random()>0.5:
        cv2.circle(frame, center, radius, color, thick, cv2.LINE_AA)
        cv2.imshow('video', frame)
    else :
        cv2.circle(frame, center, radius, color, cv2.FILLED, cv2.LINE_AA)
        cv2.imshow('video', frame)

    if cv2.waitKey(20) == ord('q') :
        print('quit by user input')
        break
cap.release()


cv2.destroyAllWindows()
