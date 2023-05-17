import mysql.connector  # pip install mysql.connector
import tkinter as tk
from tkinter import *
import cv2  # pip install opencv-python
from tkinter import messagebox
import pathlib
import face_recognition

root = tk.Tk()
root.title("profiler")
root.iconbitmap("C:/Users/Liam/Desktop/Main project/UI_images/favicon.ico")

root.configure(bg='grey')

db = mysql.connector.connect(
    host="localhost",
    user="liam",
    passwd="root",
    database="knownIndividuals"
)

c = db.cursor()

f = open("currentLogin.txt", "r")
id = f.read()

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
def Activity():
    import ViewActivity
def chgpass():
    import ChangeAdminPassword as CAP
    CAP.main()
   

def profile():
    import Profile_Person               
def Monitor():
    import monitor
def attendance():
    import attendance
def close_window():
    root.destroy()

        
 

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Users", menu=edit_menu)
edit_menu.add_command(label="add new person", command=Add)
edit_menu.add_command(label="view database", command=Users)
edit_menu.add_command(label="view profiler activity", command=Activity)
edit_menu.add_command(label="change admin password", command=chgpass)

Title = tk.Label(root, text='Profiler', bg='grey',
                                    fg='black', font=('Tahoma',20), pady=15)
Title.pack()

IDTitle = tk.Label(root, text='Admin ID:'+ id, bg='grey',
                                    fg='black', font=('Tahoma',20), pady=15)
IDTitle.pack()

photo = tk.PhotoImage(file = "C:/Users/Liam/Desktop/Main project/UI_images/Security.png")
label2 = tk.Label(root,  image = photo,  width = 200, height = 150,
                bg = "white", fg = "black")
label2.place(x=5, y=70)


b = Button(root, text="Monitor Mode", command=Monitor)
b.place(x=5, y=230)

photo2 = tk.PhotoImage(file = "C:/Users/Liam/Desktop/Main project/UI_images/profile.png")
label3 = tk.Label(root,  image = photo2,  width = 200, height = 150,
                bg = "white", fg = "black")
label3.place(x=215, y=70)

b2 = Button(root, text="Profile Mode", command=profile)
b2.place(x=215, y=230)

photo3 = tk.PhotoImage(file = "C:/Users/Liam/Desktop/Main project/UI_images/attendance.png")
label4 = tk.Label(root,  image = photo3,  width = 200, height = 150,
                bg = "white", fg = "black")
label4.place(x=825, y=70)

b3 = Button(root, text="Take attendance", command=attendance)
b3.place(x=825, y=230)

photo4 = tk.PhotoImage(file = "C:/Users/Liam/Desktop/Main project/UI_images/logoff.png")
label5 = tk.Label(root,  image = photo4,  width = 200, height = 150,
                bg = "white", fg = "black")
label5.place(x=1055, y=70)


b4 = Button(root, text="Logout", command=close_window)
b4.place(x=1055, y=230)

root.mainloop()
