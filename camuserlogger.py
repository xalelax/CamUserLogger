import cv2

cv2.namedWindow("Webcam feed")
vc = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:

    rval, frame = vc.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    

    faces = face_cascade.detectMultiScale(gray, 1.2, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow("Webcam feed", frame)

    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break


vc.release()
cv2.destroyWindow("Webcam feed")





