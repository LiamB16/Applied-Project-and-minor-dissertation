import mysql.connector  # pip install mysql.connector
import tkinter as tk
from tkinter import *
import cv2  # pip install opencv-python
from tkinter import messagebox
import pathlib
import face_recognition
#import Login as Log # login class created for admin login
#import User as U # User class created for pulling relevant data from 

root = tk.Tk()
root.title("profiler")
root.iconbitmap("C:/Users/Liam/Desktop/Main project/UI_images/favicon.ico")
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

frame = tk.Frame(root, bg=bkg)

# click command
def our_command():
    
    
    pass
def Set_admin():
    import AssignAdmin as AA
    AA.main()
def Add():
    import AddNewUser
def Users():
    import User 
    
    
    

def DeletePerson():
    try:
        c.execute("delete from persons where name = 'Liam';")
    except Exception as e:
        print(e)
        c.rollback()
        c.close()


def Camera():
    print("Profile")
    
            
def Monitor():
    print("monitor")
        
 

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Users", menu=edit_menu)
edit_menu.add_command(label="add new person", command=Add)
edit_menu.add_command(label="view database", command=Users)
edit_menu.add_command(label="set/remove admin", command=DeletePerson)

photo = tk.PhotoImage(file = "C:/Users/Liam/Pictures/Security.png")
label2 = tk.Label(root,  image = photo,  width = 300, height = 250,
                bg = "white", fg = "black")
label2.pack()


b = Button(root, text="Monitor Mode", command=Monitor)
b.place(x=25, y=100)
b.pack()

b2 = Button(root, text="Profile Mode", command=Camera)
b2.pack()

b3 = Button(root, text="Take attendance", command=Camera)
b3.pack()

b4 = Button(root, text="Logout", command=root.quit)
b4.pack()

root.mainloop()
