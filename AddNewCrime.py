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
bkimg = tk.PhotoImage(file = "C:/Users/Liam/Pictures/GardaSiochanaLogo.png")
label2 = tk.Label(root,  image = bkimg, 
                bg = "white", fg = "black")


# create a function to close the window
def close_window():
    root.destroy()

frame = tk.Frame(root)
frame.config(width = 2000, height = 2000)

label_Crime = tk.Label(frame, text="Crime: ", font=('verdana',12), bg=bkg)
entry_Crime = tk.Entry(frame, font=('verdana',12))



def insertData():
    id = "G0037748"
    select_query = 'SELECT * FROM persons WHERE ID = "G00377760" AND occupation = "garda"; '
    c.execute(select_query, id)            
    guard = c.fetchone()
    print(guard)
    if guard is None:
        messagebox.showwarning("can't assign ", "Admin must be a member of garda sicohana to assign criminal data")
    else:
        try:
            crime = entry_Crime.get()
            insert_query = "INSERT INTO `Criminal_Record` VALUES (%s,%s);"
            vals = (id, crime)
            c.execute(insert_query, vals)
            db.commit()
            select_query = 'insert into daily_activity values ("G00377746", "Added new Crime", curdate(), curtime());'
            c.execute(select_query)
            db.commit(); #commits changes to database
            messagebox.showwarning("Success", "New data assigned")
            close_window()
        except Exception as e:
            print(e)
            c.rollback()
            c.close()
            messagebox.showwarning("Invalid data, Try Agaim  ")

button_insert = tk.Button(root, text="insert", font=('verdana',14), bg='orange', command=insertData)
btnCancel = tk.Button(root, text='Cancel', bg='red', font=('Verdana',12), fg='#fff', padx=25, pady=10, command=close_window)

#Sets positins of buttons and text
label2.grid(row=0, column=0)
label_Crime.grid(row=2, column=0)
entry_Crime.grid(row=2, column=1, pady=10, padx=10)

button_insert.grid(row=3, column=0, columnspan=2)
btnCancel.grid(row=3, column=1, columnspan=2)

frame.grid(row=1, column=0)


root.mainloop()