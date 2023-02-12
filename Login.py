import cv2 #pip install opencv-python
import face_recognition #pip install cspan, install dlib, install face_recognition
import cgi
from base64 import b64decode

formData = cgi.FieldStorage()
face_match = 0
image=formData.getvalue()