import mysql.connector  # pip install mysql.connector
import tkinter as TK
from tkinter import *
from cv2 import cv2  # pip install opencv-python
from tkinter import messagebox

root = Tk()
root.title("profiler")
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

global entry1
global entry2

bkg= "#636e72"

frame = TK.Frame(root, bg=bkg)

# click command
def our_command():
    pass

def Add():
    label_name = TK.Label(frame, text="Name: ")
    entry_name = TK.Entry(frame)
    
    label_age = TK.Label(frame, text="Age: ")
    entry_age = TK.Entry(frame)
    
    label_occupation = TK.Label(frame, text="Occupation: ")
    entry_occupation = TK.Entry(frame)
    
    label_image = TK.Label(frame, text="Image Link: ")
    entry_image = TK.Entry(frame)
    
    Button(root,text="Add",command=AddPerson,height=3,width=13, bd=6).place(x=100, y=120)
    
    label_name.grid(row=0, column=0)
    entry_name.grid(row=0, column=1)
    
    label_age.grid(row=1, column=0)
    entry_age.grid(row=1, column=1)
    
    label_occupation.grid(row=2, column=0)
    entry_occupation.grid(row=2, column=1)
    
    label_image.grid(row=3, column=0)
    entry_image.grid(row=3, column=1)
    
    frame.pack()
    
def AddPerson():
    try:
        c.execute("Insert into persons values('Liam', 22, 'student', 'c:/users/Liam', 'Y');")
    except Exception as e:
        print(e)
        c.rollback()
        c.close()


def DeletePerson():
    try:
        c.execute("delete from persons where name = 'Liam';")
    except Exception as e:
        print(e)
        c.rollback()
        c.close()


def Camera():
    webcam = cv2.VideoCapture(0)
    while True:
        ret,frame = webcam.read()

        if ret == True:
           cv2.imshow("Profiler", frame)
           key = cv2.waitKey(1)
           if key == ord("q"):
              break
    webcam.release()
    cv2.destroyAllWindows()
    
#Redirects user to login page  
def LoginPage():
    Label(root,text="Username").place(x=20,y=20)
    Label(root,text="Password").place(x=20,y=70)
    
    entry1=Entry(root,bd=5)
    entry1.place(x=140, y=20)
    
    entry2=Entry(root,bd=5)
    entry2.place(x=140, y=70)
    
    Button(root,text="Login",command=Login,height=3,width=13, bd=6).place(x=100, y=120)#button actives Login() function
    
    return entry1, entry2

#Contains login function for verifying username and password 
def Login(entry1, entry2):
    username=entry1
    password=entry2
    
    #checks for blank pages
    if(username=="" and password==""):
        messagebox.showinfo("", "Blank entry not allowed")
    #checks for correct user
    elif(username=="Liam" and password=="Password"):
        messagebox.showinfo("", "Access Granted")
    #shows message for wrong user    
    else:
        messagebox.showinfo("", "incorrect")
        
    
# create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="options", menu=file_menu)
file_menu.add_command(label="view users", command=our_command)
file_menu.add_command(label="view camera", command=Camera)
file_menu.add_command(label="quit program", command=root.quit)

# create edit item menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Users", menu=edit_menu)
edit_menu.add_command(label="add known individual", command=Add)
edit_menu.add_command(label="remove individual", command=DeletePerson)
edit_menu.add_command(label="Login", command=LoginPage)

root.mainloop()
