# Chapter: 23

# Face Detection in Video

import cv2 as cv

face_cascade = cv.CascadeClassifier(cv.data.haarcascade + 'haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(0)

while True:
    _, img = cap.read()
    # Detect the Faces
    faces = face_cascade.detectMultiScale(img, 1.1, 4)

    # Draw rectangle around face
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

    # Display
    cv.imshow('img', img)

    #Stop if escape key is pressed
    k = cv.waitKey(30) & 0xFF
    if k==27:
        break

cap.release()
cv.destroyAllWindows()
