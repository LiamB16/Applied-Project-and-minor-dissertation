import pathlib
import cv2

name = "Liam"
age = "22"
occupation = "student"

cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
clf = cv2.CascadeClassifier(str(cascade_path))

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
while (True):
    img = cv2.imread('C:/Users/Liam/Desktop/Main project/images/Liam.jpg')
# Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
    faces = clf.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=4
    )
# Draw rectangle around the faces
    for (x, y, w, h) in faces:
       cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
       
# Display the output
    cv2.imshow('img', img)
    if cv2.waitKey(1) == ord("q"):
        break