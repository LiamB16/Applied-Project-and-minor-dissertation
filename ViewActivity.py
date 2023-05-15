import mysql.connector  # pip install mysql.connector
import tkinter  as tk 
from tkinter import * 
from tkinter import messagebox as msg
from sqlalchemy.exc import SQLAlchemyError


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
        
def display():
    c.execute("select * from daily_activity;")

    i=0 
    for student in c: 
        for j in range(len(student)):
            e = Entry(my_w, width=20, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1
display()


my_w.mainloop()
    
    

  