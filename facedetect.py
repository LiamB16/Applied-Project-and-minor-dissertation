import pathlib
import cv2

name = "Liam Bryant"
age = "22"
occupation = "student"

cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"

clf = cv2.CascadeClassifier(str(cascade_path))

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW) #captureDevice = camera # VideoCapture(number of cameras). 0 is the defualt number

while (True): #fixes issue of program crashing due to
    ret, frame =  camera.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    for(x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x+width, y+height), (255, 255, 0), 2)
        cv2.putText(frame, name, (x, y-50), cv2.FONT_HERSHEY_SIMPLEX, #adds text around rectangle
             0.75, (0, 255, 0), 2)
        cv2.putText(frame, age, (x, y-22), cv2.FONT_HERSHEY_SIMPLEX, #adds text around rectangle
             0.75, (0, 255, 0), 2)
        cv2.putText(frame, occupation, (x, y), cv2.FONT_HERSHEY_SIMPLEX, #adds text around rectangle
             0.75, (0, 255, 0), 2)
        print("G0037746")
        
    cv2.imshow("FACES", frame)
    if cv2.waitKey(1) == ord("q"):
        break
    
camera.release()
cv2.destroyAllWindows