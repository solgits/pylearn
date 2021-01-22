import cv2

spimg = cv2.imread('SophieMarceau.jpg')

cv2.imshow('sp', spimg)
cv2.waitKey(0)
cv2.destroyAllWindows()