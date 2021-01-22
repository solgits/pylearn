# opencv를 이용하여 이미지를 흑백 이미지로 바꾸기
import cv2

spimg = cv2.imread('SophieMarceau.jpg')
spgray = cv2.cvtColor(spimg, cv2.COLOR_BGR2GRAY)

cv2.imshow('sp', spgray)
cv2.waitKey(0)
cv2.destroyAllWindows()