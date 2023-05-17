import csv
import os
from tkinter import filedialog
import face_recognition
import cv2
import tkinter as tk
from tkinter import messagebox as msg
from PIL import ImageTk, Image
from tkinter import *

#file name containing images to use as a comparison 
dataset="images"
#prints out names of jpeg images
images=os.listdir(dataset)
#print(images)

f = open("C:/Users/Liam/Desktop/Main project/currentID.txt",'w+',newline= '')

# width and height
w = 400
h = 260

root = tk.Tk()     
def close_window():
    root.destroy()
    
filename = filedialog.askopenfilename(initialdir="C:/Users/Liam/Desktop/Main project/images", title= "select a file", filetypes=(("jpeg files", "*.jpg"),("png", "*.png*")))
print(filename) 
try:
    print("analysing")
    img = face_recognition.load_image_file(filename)
    unknown_encode=face_recognition.face_encodings(img)[0]
    for image in images:
        path=os.path.join(dataset, image)
        known_image=face_recognition.load_image_file(path)
        known_encode=face_recognition.face_encodings(known_image)[0]
        result=face_recognition.compare_faces([known_encode],unknown_encode)
        if result[0]==True:
            print("Match found")
            name=image.split(".")[0]
            f.write(name)
            f.close()      
            my_var=msg.askyesnocancel("Match found", "Do you want to view more about "+ name,icon='warning')
            print(my_var)
            if my_var:
                #close_window()
                import ViewUser 
            else:
                close_window()
                import menu
            
        else:
            print("unknown person")
except Exception as e:
        print(e)
              
root.mainloop()