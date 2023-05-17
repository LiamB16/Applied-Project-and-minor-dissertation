import mysql.connector  # pip install mysql.connector
import tkinter  as tk 
from tkinter import * 
from tkinter import messagebox as msg
from sqlalchemy.exc import SQLAlchemyError
from tkinter import ttk


my_w = tk.Tk()
my_w.geometry("400x250")

#Logs into database
db = mysql.connector.connect(
    host="localhost",
    user="liam",
    passwd="root",
    database="knownindividuals"
)

c = db.cursor()
        

c.execute("select * from daily_activity;")
trv=ttk.Treeview(my_w,selectmode='browse')
trv.grid(row = 2, column = 0, padx = 20, pady=20)
trv["columns"] = ("1","2","3","4")
trv['show']='headings'
trv.column("1",width=80,anchor='c') 
trv.column("2",width=80,anchor='c')  
trv.column("3",width=80,anchor='c')
trv.column("4",width=80,anchor='c')  
trv.heading("1",text="ID")
trv.heading("2",text="activity")
trv.heading("3",text="date")
trv.heading("4",text="time")
for dt in c: 
        trv.insert("", 'end',iid=dt[0],values=(dt[0],dt[1],dt[2], dt[3]))
              
my_w.mainloop()
    
    

  