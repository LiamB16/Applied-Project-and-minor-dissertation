import mysql.connector  # pip install mysql.connector
import tkinter as TK
from tkinter import *
import cv2  # pip install opencv-python
from tkinter import messagebox
import pathlib
import face_recognition


root = Tk()
root.title("profiler")
root.iconbitmap("C:/Users/Liam/Desktop/Main project/images/favicon.ico")
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
    print("ok")
def Bank():
    print("ok")
def CR():
    print("ok")
def Education():
    print("ok")
def Health():
    print("ok")
    
def main(): 
# create a menu item
    file_menu = Menu(my_menu)
    my_menu.add_cascade(label="options", menu=file_menu)
    file_menu.add_command(label="Customise Menu", command=Assets)
    file_menu.add_command(label="Switch admins", command=Assets)

# create edit item menu
    edit_menu = Menu(my_menu)
    my_menu.add_cascade(label="Users", menu=edit_menu)
    edit_menu.add_command(label="Assets", command=Assets)
    edit_menu.add_command(label="Bank", command=Bank)
    edit_menu.add_command(label="criminal record", command=CR)
    edit_menu.add_command(label="education", command=Education)
    edit_menu.add_command(label="Health Record", command=Health)

    #photo = TK.PhotoImage(file = "C:/Users/Liam/Desktop/Main project/images/G00377746.jpg")
    select_query = 'select ID from currentlylogin;'
    c.execute(select_query)
    ID = c.fetchone()
    #ShowID = TK.Label(root, tuple='ID: ' + ID, bg='#fff',
                                     # font=('Verdana',16))
    
    #ShowID.pack()


    b = Button(root, text="Monitor Mode", command=Assets)
    b.pack()

    b2 = Button(root, text="Profile Mode", command=Bank)
    b2.pack()

    b3 = Button(root, text="Take attendance", command=CR)
    b3.pack()

    b4 = Button(root, text="Logout", command=CR)
    b4.pack()

if __name__ == '__main__':
    main()
