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
#root.iconbitmap("C:/Users/Liam/Desktop/Main project/images/favicon.ico")
# root.iconbitmap("c:/gui/codemy.ico")
root.geometry("400x400")

db = mysql.connector.connect(
    host="localhost",
    user="liam",
    passwd="root",
    database="knownIndividuals"
)

c = db.cursor()

my_menu = Menu(root)
root.config(menu=my_menu)

bkg= "#636e72"

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



# create edit item menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Add info", menu=edit_menu)
edit_menu.add_command(label="Assets", command=addAssets)
edit_menu.add_command(label="Bank", command=addBank)
edit_menu.add_command(label="criminal record", command=addCR)
edit_menu.add_command(label="education", command=addEducation)
edit_menu.add_command(label="Health Record", command=addHealth)

b = Button(root, text="Assets", command=Assets)
b.pack()

b2 = Button(root, text="Bank", command=Bank)
b2.pack()

b3 = Button(root, text="Education", command=Education)
b3.pack()

b4 = Button(root, text="Medical Condition", command=Health)
b4.pack()

b5 = Button(root, text="Crime", command=CR)
b5.pack()

root.mainloop()
