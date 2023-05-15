import numpy as np
import face_recognition
from PIL import Image, ImageDraw, ImageFont

face1 = face_recognition.load_image_file("C:/Users/Liam\Desktop/Main project/images/G00377746Test.jpg")
face1_encoding = face_recognition.face_encodings(face1)[0]

face_encodings = [face1_encoding]
face_names = ['G00377746', 'G00377747', 'G00377748']

image_array = face_recognition.load_image_file("C:/Users/Liam/Desktop/Main project/images/G00377747.jpg")
face_locations = face_recognition.face_locations(image_array)
face_encodings = face_recognition.face_encodings(image_array, face_locations)

image = Image.fromarray(image_array)
draw = ImageDraw.Draw(image)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(face_encodings, face_encoding)
    name = "Unknown person"

    face_distances = face_recognition.face_distance(face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)

    if matches[best_match_index]:
        name = face_names[best_match_index]
        print(name)
    else:
        print("result not found")



