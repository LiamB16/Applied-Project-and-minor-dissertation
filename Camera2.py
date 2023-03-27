import cv2 #pip install opencv-python
import face_recognition #pip install cspan, install dlib, install face_recognition

#finds image in file and converts it to binary code
img = cv2.imread("C:/Users/Liam/Desktop/Main project/images/G00377746.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

#finds image in file and converts it to binary code
img2 = cv2.imread("C:/Users/Liam/Desktop/Main project/images/G00377746Test.jpg")
rgb_img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img)[0]

#compares binary code of two images and sees if they are both the same
results = face_recognition.compare_faces([img_encoding], img_encoding2)
if results == [True]:
  #SQL query of the 
  print("found a match")
 
else:
  print("unknown")
    

cv2.imshow("img", img)