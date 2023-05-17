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
f = open("currentID.txt", "r")
id = f.read()

f = open("currentLogin.txt", "r")
id2 = f.read()
print(id)

bkg = "white"


# create a function to close the window
def close_window():
    root.destroy()

frame = tk.Frame(root)

label_Illness = tk.Label(frame, text="Medical condition: ", font=('verdana',12), bg=bkg)
entry_Illness = tk.Entry(frame, font=('verdana',12))



def insertData():
    
    illness = entry_Illness.get()
    
    try:
       insert_query = "INSERT INTO `medical_condition` VALUES (%s, %s);"
       vals = (id, illness)
       c.execute(insert_query, vals)
       db.commit()
       
       select_query = 'insert into daily_activity VALUES (%s, "Added new medical condition", curdate(), curtime());'
       vals2 = (id2)
       c.execute(select_query, vals2)
       db.commit() #commits changes to database
       messagebox.showwarning("Success", "New data assigned")
       close_window()
    except Exception as e:
        print(e)
        c.rollback()
        c.close()
        messagebox.showwarning("Invalid data  ")

button_insert = tk.Button(root, text="insert", font=('verdana',14), bg='orange', command=insertData)
btnCancel = tk.Button(root, text='Cancel', bg='red', font=('Verdana',12), fg='#fff', padx=25, pady=10, command=close_window)

#Sets positins of buttons and text

label_Illness.grid(row=2, column=0)
entry_Illness.grid(row=2, column=1, pady=10, padx=10)

button_insert.grid(row=3, column=0, columnspan=2)
btnCancel.grid(row=3, column=1, columnspan=2)

frame.grid(row=1, column=0)

root.mainloop()