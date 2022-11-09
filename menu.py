import mysql.connector  # pip install mysql.connector
from tkinter import *
from cv2 import cv2  # pip install opencv-python

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

# click command


def our_command():
    pass


def AddPerson():
    try:
        c.execute("Insert into persons values('Liam', 22, 'student');")
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

# create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="options", menu=file_menu)
file_menu.add_command(label="view users", command=our_command)
file_menu.add_command(label="view camera", command=Camera)
file_menu.add_command(label="quit program", command=root.quit)

# create edit item menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Users", menu=edit_menu)
edit_menu.add_command(label="add known individual", command=AddPerson)
edit_menu.add_command(label="remove individual", command=DeletePerson)

root.mainloop()
