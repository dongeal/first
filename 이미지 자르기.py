import cv2
img = cv2.imread('img.jpg')
# print(img.shape) (390,640, 3)

crop= img[5:300, 100:600] # 세로 5-300, 가로 100-600

cv2.imshow('img',img)
cv2.imshow('crop',crop)

cv2.waitKey(0)
cv2.destroyAllWindows()