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
    
    c.execute("select * from Education where ID = 'G00377746';")

    i=0 
    for student in c: 
        for j in range(len(student)):
            e = Entry(my_w, width=20, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
         # show the delete button     
            e = tk.Button(my_w,width=5,text='Del',fg='red',relief='ridge',
            anchor="w",command=lambda k=student[0]:del_data(k))  
            e.grid(row=i, column=8) 
         # show the info button     
            e = tk.Button(my_w,width=5,text='info',fg='blue',relief='ridge',
            anchor="w",command=lambda k=student[0]:del_data(k))  
            e.grid(row=i, column=7) 
        i=i+1
display()

def del_data(s_id): # delete record 
    try:
        my_var=msg.askyesnocancel("Delete Record",
           "Are you sure ? ",icon='warning')
        print(my_var)
        if my_var:
            query="DELETE FROM persons WHERE id=%s"
            my_data=[s_id]
            c.execute(query,my_data)
            db.commit(); #commits changes to database
            print("Row Deleted  ")
            
            for row in my_w.grid_slaves():# remove widgets
                row.grid_forget()
            display() # refresh the list 
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
my_w.mainloop()