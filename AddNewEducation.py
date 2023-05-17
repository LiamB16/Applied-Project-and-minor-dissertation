#login form
from tkinter import messagebox, ttk
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
f = open("currentID.txt", "r")
id = f.read()
print(id)

bkg = "white"

# create a function to close the window
def close_window():
    root.destroy()

frame = tk.Frame(root)

label_School = tk.Label(frame, text="School Name: ", font=('verdana',12), bg=bkg)
entry_School = tk.Entry(frame, font=('verdana',12))

label_Level = tk.Label(frame, text="Level: ", font=('verdana',12), bg=bkg)
entry_Level = tk.Entry(frame, font=('verdana',12))


label_Award = tk.Label(frame, text="Award: ", font=('verdana',12), bg=bkg)
entry_Award = tk.Entry(frame, font=('verdana',12))

label_Grad = tk.Label(frame, text="Graduation Year: ", font=('verdana',12), bg=bkg)
entry_Grad = tk.Entry(frame, font=('verdana',12))



def insertData():
    school = entry_School.get()
    level = entry_Level.get()
    award = entry_Award.get()
    grad = entry_Grad.get()
    
    
    insert_query = "INSERT INTO `Education` VALUES  (%s,%s,%s,%s,%s)"
    vals = [id, school, level, award, grad]
    c.execute(insert_query, vals)
    db.commit()
    
    select_query = 'insert into daily_activity values ("G00377746", "Added new Education", curdate(), curtime());'
    c.execute(select_query)
    db.commit(); #commits changes to database
    messagebox.showwarning("Success", "New data assigned")
    close_window()

button_insert = tk.Button(root, text="insert", font=('verdana',14), bg='orange', command=insertData)
btnCancel = tk.Button(root, text='Cancel', bg='red', font=('Verdana',12), fg='#fff', padx=25, pady=10, command=close_window)

#Sets positins of buttons and text
label_School.grid(row=2, column=0)
entry_School.grid(row=2, column=1, pady=10, padx=10)

label_Level.grid(row=3, column=0)
entry_Level.grid(row=3, column=1)

label_Award.grid(row=4, column=0)
entry_Award.grid(row=4, column=1, pady=10, padx=10)

label_Grad.grid(row=5, column=0)
entry_Grad.grid(row=5, column=1, pady=10, padx=10)

button_insert.grid(row=6, column=0, columnspan=2)
btnCancel.grid(row=6, column=1, columnspan=2)

frame.grid(row=1, column=0)

root.mainloop()