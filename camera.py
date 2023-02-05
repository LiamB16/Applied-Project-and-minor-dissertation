import cv2 #pip install opencv
import numpy as npy
import face_recognition #pip install cspan, install dlib, install face_recognition

img = cv2.imread("C:/Users/Liam/Desktop/Main project/images/Liam.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

img2 = cv2.imread("C:/Users/Liam/Desktop/Main project/images/LiamTest.jpg")
rgb_img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img)[0]

results = face_recognition.compare_faces([img_encoding], img_encoding2)
print("Results ", results)

cv2.imshow("img", img)