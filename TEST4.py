import os
import face_recognition
import cv2

#file name containing images to use as a comparison 
dataset="images"
#prints out names of jpeg images
images=os.listdir(dataset)
#print(images)

img=face_recognition.load_image_file("G00377746.jpg")
unknown_encode=face_recognition.face_encodings(img)[0]
for image in images:
    path=os.path.join(dataset, image)
    known_image=face_recognition.load_image_file(path)
    known_encode=face_recognition.face_encodings(known_image)[0]
    result=face_recognition.compare_faces([known_encode],unknown_encode)
    if result[0]==True:
        print("Match found")
        name=image.split(".")[0]
        print(name)

    else:
        print("unknown person")
