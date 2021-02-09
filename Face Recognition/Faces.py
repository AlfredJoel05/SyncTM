import cv2 as cv

vid=cv.VideoCapture(0)
cascade = cv.CascadeClassifier('haarcascade_frontalcatface_default.xml')

def detect(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray= cv.equalizeHist(frame_gray)
    detections = cascade.detectMultiScale(frame_gray,1.2,5)
    if len(detections) > 0:
        (x,y,w,h) = detections[0]
        cv.rectangle(frame,(x,y),(x+h,y+w),(0,255,0),3)
    cv.imshow('Camera',frame)

while True:
    ret, frame = vid.read()
    detect(frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv.destroyAllWindows()