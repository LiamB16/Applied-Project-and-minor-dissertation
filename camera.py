import cv2 #pip install opencv
import numpy as npy
import face_recognition as face_rec #pip install cspan, install dlib, install face_recognition

# function
def resize(img, size) :
    width = int(img.shape[1]*size)
    height = int(img.shape[0] * size)
    dimension = (width, height)
    return cv2.resize(img, dimension, interpolation= cv2.INTER_AREA)


# img declaration
Liam = face_rec.load_image_file('images\Liam.jpg') #loads image from file
Liam = cv2.cvtColor(Liam, cv2.COLOR_BGR2RGB) #shows image in color
Liam = resize(Liam, 0.50) #adjusts size of image

# test image declaration
Liam_Test = face_rec.load_image_file('images\LiamTest.jpg')
Liam_Test = resize(Liam_Test, 0.50)
Liam_Test = cv2.cvtColor(Liam_Test, cv2.COLOR_BGR2RGB)

# finding face location
faceLoc_Liam = face_rec.face_locations(Liam)[0]
encode_Liam = face_rec.face_encodings(Liam)[0]
cv2.rectangle(Liam, (faceLoc_Liam[3], faceLoc_Liam[0]), (faceLoc_Liam[1], faceLoc_Liam[2]), (255, 0, 255), 3)

# finding test face location
faceLoc_LiamTest = face_rec.face_locations(Liam_Test)[0]
encode_LiamTest= face_rec.face_encodings(Liam_Test)[0]
cv2.rectangle(Liam, (faceLoc_Liam[3], faceLoc_Liam[0]), (faceLoc_Liam[1], faceLoc_Liam[2]), (255, 0, 255), 3)

# Compares two faces to identify match
results = face_rec.compare_faces([encode_Liam], encode_LiamTest)
print(results)
cv2.putText(Liam_Test, f'{results}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255), 2 )

cv2.imshow('main_img', Liam)
cv2.imshow('test_img', Liam_Test)
cv2.waitKey(0)
cv2.destroyAllWindows()