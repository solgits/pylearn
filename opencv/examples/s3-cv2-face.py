# opencv를 이용하여 얼굴인식

import cv2

# spimg = cv2.imread('SophieMarceau.jpg')
spimg = cv2.imread('SophieMarceau4.jpg')
spgray = cv2.cvtColor(spimg, cv2.COLOR_BGR2GRAY)

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face.detectMultiScale(spgray, 1.10, 1)

for (x,y,w,h) in faces:
    spimg = cv2.rectangle(spimg, (x,y),(x + w, y + h), (255,0,0), 2)

cv2.imshow('spimg', spimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
