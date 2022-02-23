import cv2

cap = cv2.VideoCapture('video.mp4')

k=0
while cap.isOpened():
    ret, frame = cap.read()
    crop = frame[200:450, 100:300]
    if not ret:
        break
    cv2.imshow('video_origin', frame)
    cv2.imshow('video_crop', crop)
    if cv2.waitKey(20) == ord('q'):
        break
    if cv2.waitKey(20) == ord('s'):  # 자른 동영상 캡쳐
        k +=1
        cv2.imwrite('capture'+str(k)+'.jpg',crop)
cap.release()
cv2.destroyAllWindows()
