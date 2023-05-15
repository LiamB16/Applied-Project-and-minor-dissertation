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

bkg = "white"

# create a function to close the window
def close_window():
    root.destroy()

frame = tk.Frame(root)

label_School = tk.Label(frame, text="School Name: ", font=('verdana',12), bg=bkg)
entry_School = tk.Entry(frame, font=('verdana',12))

label_Level = tk.Label(frame, text="Level: ", font=('verdana',12), bg=bkg)
combo = ttk.Combobox(values=["secondary school", "university", "community college", "Medical School"])

label_Award = tk.Label(frame, text="Award: ", font=('verdana',12), bg=bkg)
combo2 = ttk.Combobox(values=["N/A","diploma", "Level 7", "Level 8", "Doctorite"])

label_Grad = tk.Label(frame, text="Graduation Year: ", font=('verdana',12), bg=bkg)
combo3 = ttk.Combobox(values=[ "N/A", "2023","2022","2021",
"2020","2019","2018","2017","2016","2015","2014","2013","2012","2011", 
"2010","2009","2008","2007","2006","2005","2004","2003","2002","2001",
"2000","1999","1998","1997","1996","1995","1994","1993","1992","1991",
"1990","1989","1988","1987","1986","1985","1984","1983","1982","1981",
"1980","1979","1978","1977","1976","1975","1974","1973","1972","1971",
"1970"])



def insertData():
    ID = "G00377746"
    level = combo.get()
    award = combo2.get()
    grad = combo3.get()
    
    
    insert_query = "INSERT INTO `Education` VALUES values (%s,%s,%s,%s,%s)"
    vals = (ID, level, award, grad)
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
combo.grid(row=3, column=1)

label_Award.grid(row=4, column=0)
combo2.grid(row=1, column=1, pady=10, padx=10)

label_Grad.grid(row=5, column=0)
combo3.grid(row=5, column=1, pady=10, padx=10)

button_insert.grid(row=6, column=0, columnspan=2)
btnCancel.grid(row=6, column=1, columnspan=2)

frame.grid(row=1, column=0)

root.mainloop()