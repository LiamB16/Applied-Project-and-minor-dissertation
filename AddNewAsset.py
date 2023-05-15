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

label_Asset = tk.Label(frame, text="Asset: ", font=('verdana',12), bg=bkg)
entry_Asset = tk.Entry(frame, font=('verdana',12))

label_Value = tk.Label(frame, text="Market Value: ", font=('verdana',12), bg=bkg)
entry_Value = tk.Entry(frame, font=('verdana',12))

label_Asset_ID = tk.Label(frame, text="regiseration: ", font=('verdana',12), bg=bkg)
entry_Asset_ID = tk.Entry(frame, font=('verdana',12))




def insertData():
    ID = "G0037748"
    asset = entry_Asset.get()
    value = entry_Value.get()
    asset_id = entry_Asset_ID.get()
    
    try:
        insert_query = "INSERT INTO `Assets` VALUES (%s,%s,%s,%s);"
        vals = (ID, asset, value, asset_id)
        c.execute(insert_query, vals)
        db.commit()
        
        select_query = 'insert into daily_activity values ("G00377746", "Added new asset", curdate(), curtime());'
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
label_Asset.grid(row=0, column=0)
entry_Asset.grid(row=0, column=1, pady=10, padx=10)

label_Value.grid(row=1, column=0)
entry_Value.grid(row=1, column=1, pady=10, padx=10)

label_Asset_ID.grid(row=2, column=0)
entry_Asset_ID.grid(row=2, column=1, pady=10, padx=10)

button_insert.grid(row=3, column=0, columnspan=2)
btnCancel.grid(row=3, column=1, columnspan=2)

frame.grid(row=0, column=0)

root.mainloop()