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

bkg = "white"

# create a function to close the window
def close_window():
    root.destroy()

frame = tk.Frame(root)

label_Bank = tk.Label(frame, text="Bank ID: ", font=('verdana',12), bg=bkg)
entry_Bank = tk.Entry(frame, font=('verdana',12))

label_Value = tk.Label(frame, text="Current Balance: ", font=('verdana',12), bg=bkg)
entry_Value = tk.Entry(frame, font=('verdana',12))






def insertData():
    ID = "G0037748"
    bank = entry_Bank.get()
    value = entry_Value.get()
    
    try:
        insert_query = "INSERT INTO `Bank` VALUES (%s,%s,%s);"
        vals = (ID, bank, value)
        c.execute(insert_query, vals)
        db.commit()
        
        select_query = 'insert into daily_activity values ("G00377746", "Added new Bank", curdate(), curtime());'
        c.execute(select_query)
        db.commit(); #commits changes to database
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
label_Bank.grid(row=0, column=0)
entry_Bank.grid(row=0, column=1, pady=10, padx=10)

label_Value.grid(row=1, column=0)
entry_Value.grid(row=1, column=1, pady=10, padx=10)

button_insert.grid(row=2, column=0, columnspan=2)
btnCancel.grid(row=2, column=1, columnspan=2)

frame.grid(row=0, column=0)

root.mainloop()