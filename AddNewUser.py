#login form
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image


import mysql.connector

#Logs into database
db = mysql.connector.connect(
    host="localhost",
    user="liam",
    passwd="root",
    database="knownindividuals"
)

c = db.cursor()
root = tk.Tk()
root.title("insert Data")

bkg = "#636e72"

# create a function to close the window
def close_window():
    root.destroy()

frame = tk.Frame(root)

label_ID = tk.Label(frame, text="ID: ", font=('verdana',12), bg=bkg)
entry_ID = tk.Entry(frame, font=('verdana',12))

label_firstname = tk.Label(frame, text="First Name: ", font=('verdana',12), bg=bkg)
entry_firstname = tk.Entry(frame, font=('verdana',12))

label_Lastname = tk.Label(frame, text="Last Name: ", font=('verdana',12), bg=bkg)
entry_Lastname = tk.Entry(frame, font=('verdana',12))

label_age = tk.Label(frame, text="age: ", font=('verdana',12), bg=bkg)
entry_age = tk.Entry(frame, font=('verdana',12))

label_occupation = tk.Label(frame, text="occupation: ", font=('verdana',12), bg=bkg)
entry_occupation = tk.Entry(frame, font=('verdana',12))

def insertData():
    ID = entry_ID.get()
    firstname = entry_firstname.get()
    Lastname = entry_Lastname.get()
    age = entry_age.get()
    occupation = entry_occupation.get()
    admin = 'N'
    password = ''
    insert_query = "INSERT INTO persons(`ID`, `name`,`sur-name`, `age`, `occupation`, `isadmin`, admin_password) values (%s,%s,%s,%s,%s,%s,%s)"
    vals = (ID, firstname, Lastname, age, occupation, admin, password)
    c.execute(insert_query, vals)
    db.commit()
    messagebox.showwarning('New User Added')
    close_window()

button_insert = tk.Button(root, text="insert", font=('verdana',14), bg='orange', command=insertData)
btnCancel = tk.Button(root, text='Cancel', bg='orange', font=('Verdana',12), fg='#fff', padx=25, pady=10, command=close_window)

#Sets positins of buttons and text
label_ID.grid(row=0, column=0)
entry_ID.grid(row=0, column=1, pady=10, padx=10)

label_firstname.grid(row=1, column=0)
entry_firstname.grid(row=1, column=1, pady=10, padx=10)

label_Lastname.grid(row=2, column=0)
entry_Lastname.grid(row=2, column=1, pady=10, padx=10)

label_age.grid(row=3, column=0)
entry_age.grid(row=3, column=1, pady=10, padx=10)

label_occupation.grid(row=4, column=0)
entry_occupation.grid(row=4, column=1, pady=10, padx=10)

button_insert.grid(row=4, column=0, columnspan=2)
btnCancel.grid(row=4, column=1, columnspan=2)

frame.grid(row=0, column=0)

root.mainloop()