# opencv를 이용하여 얼굴과 눈 인식

import cv2

jdimg = cv2.imread('SophieMarceau3.jpg')
#jdimg = cv2.imread('JamesDean.jpg')
jdgray = cv2.cvtColor(jdimg, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_cascase = cv2.CascadeClassifier('haarcascade_eye.xml')
faces = face_cascade.detectMultiScale(jdgray, 1.15, 3)

for (x,y,w,h) in faces:
    img = cv2.rectangle(jdimg, (x,y),(x + w, y + h), (255,0,0), 2)
    roi_gray = jdgray[y:y+h, x:x+w]
    roi_color = jdimg[y:y+h, x:x+w]
    eyes = eyes_cascase.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh),(0,255,0),2)


cv2.imshow('jdimg', jdimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
