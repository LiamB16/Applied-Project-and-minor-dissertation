import cv2 #pip install opencv-python
import face_recognition #pip install cspan, install dlib, install face_recognition
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="liam",
    passwd="root",
    database="knownIndividuals"
)

c = db.cursor()

#finds image in file and converts it to binary code
img = cv2.imread("C:/Users/Liam/Desktop/Main project/images/G00377746.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

#finds image in file and converts it to binary code
img2 = cv2.imread("C:/Users/Liam/Desktop/Main project/images/G00377746Test.jpg")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

#compares binary code of two images and sees if they are both the same
results = face_recognition.compare_faces([img_encoding], img_encoding2)
print(results)
if results == [True]:
  
  print("found a match")
  #removes the previously found person
  c.execute("delete from currentid;")
  db.commit()
  #puts in the name of the person who is currently identified, this is used as a reference to pull the correct data
  c.execute("insert into currentid values ('G00377746');")
  db.commit()
 
else:
  print("unknown")
    

cv2.imshow("img", img)