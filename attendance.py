import cv2 #pip install opencv-python
import face_recognition #pip install cspan, install dlib, install face_recognition
import numpy as np
import os
import glob
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)
#reads in image and converts it into bimary data
img = cv2.imread("C:/Users/Liam/Desktop/Main project/images/Liam.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

#sorts binary code into an array
known_faces_encoding = [
    img_encoding
]
#sorts names into an array
known_faces_names = [
    "Liam"
]

students = known_faces_names.copy()

face_location = []
face_encoding = []
face_names = []
s = True
# gets cuurent date
now = datetime.now()
current_date = now.strftime("%D-%M-%Y")

# opens and creates file
f = open(current_date +'.csv','w+',newline= '')
lnwriter = csv.writer(f)
#runs video camera 
while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = small_frame[:,:,::-1]
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_faces_encoding, face_encodings)
            name = ""
            face_distance = face_recognition.face_distance(known_faces_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]
             
            face_names.append(name)
            if name in known_faces_names:
                if name in students:
                    students.remove(name)
                    print(students)
                    #records hour minutes and seconds person was seen
                    current_time = now.strftime("%H-%M-%S")
                    #writes time to csv file
                    lnwriter.writerrow([name,current_time])
        cv2.imshow("attendance system", frame)
        #kills camera
        if cv2.waitKey(1) == ord("q"):
           break
       
    video_capture.release()
    cv2.destroyAllWindows()
    f.close()
    
