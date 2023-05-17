import mysql.connector  # pip install mysql.connector
import tkinter as TK
from tkinter import *
import cv2  # pip install opencv-python
from tkinter import messagebox
import pathlib
import face_recognition
from PIL import ImageTk, Image

root = Tk()
root.title("profiler")
root.geometry("400x400")

db = mysql.connector.connect(
    host="localhost",
    user="liam",
    passwd="root",
    database="knownIndividuals"
)

c = db.cursor()

my_menu = Menu(root)
root.config(menu=my_menu, bg="grey")

f = open("currentID.txt", "r")
id = f.read()
print(id)

bkg= "black"

frame = TK.Frame(root, bg=bkg)

def Assets():
    import ViewAsset
def Bank():
    import ViewBank
def CR():
    import ViewCrime
def Education():
    import ViewEducation
def Health():
    import ViewConditions


def addHealth():
    import AddNewCondition
def addBank():
    import AddNewBank
def addCR():
    import AddNewCrime
def addEducation():
    import AddNewEducation
def addAssets():
    import AddNewAsset
def close_window():
    root.destroy()



# create edit item menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Add info", menu=edit_menu)
edit_menu.add_command(label="Assets", command=addAssets)
edit_menu.add_command(label="Bank", command=addBank)
edit_menu.add_command(label="criminal record", command=addCR)
edit_menu.add_command(label="education", command=addEducation)
edit_menu.add_command(label="Health Record", command=addHealth)
Title = Label(root, text='Profiler: ' + id, bg='grey',
                                    fg='black', font=('Tahoma',20), pady=15)
Title.pack()

photo = Image.open("C:/Users/Liam/Desktop/Main project/images/"+ id+".jpg")

resized = photo.resize((300, 300), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
i = Label(root, image=new_pic)
i.pack()

b = Button(root, text="Assets", bg='yellow', command=Assets)
b.pack()

b2 = Button(root, text="Bank", bg='yellow', command=Bank)
b2.pack()

b3 = Button(root, text="Education", bg='yellow', command=Education)
b3.pack()

b4 = Button(root, text="Medical Condition", bg='yellow', command=Health)
b4.pack()

b5 = Button(root, text="Crime", bg='yellow', command=CR)
b5.pack()


root.mainloop()
