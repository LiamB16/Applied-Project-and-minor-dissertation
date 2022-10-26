from cv2 import cv2 #pip install opencv-python
webcam=cv2.VideoCapture(0) 

while True:
    ret,frame=webcam.read()
    
    if ret==True:
        cv2.imshow("Profiler", frame)
        key=cv2.waitKey(1)
        if key==ord("q"):
            break
webcam.release()
cv2.destroyAllWindows()