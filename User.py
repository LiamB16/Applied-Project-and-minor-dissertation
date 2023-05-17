import mysql.connector  # pip install mysql.connector
import tkinter  as tk 
from tkinter import * 
from tkinter import messagebox as msg
from sqlalchemy.exc import SQLAlchemyError
from tkinter import messagebox

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
f2 = open("currentLogin.txt", "r")
id2 = f2.read()
 
def display():
    c.execute("select ID, name, age, occupation, IsAdmin from persons;")

    i=0 
    for student in c: 
        for j in range(len(student)):
            e = Entry(my_w, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
         # show the delete button     
            e = tk.Button(my_w,width=5,text='Del',fg='red',relief='ridge',
            anchor="w",command=lambda k=student[0]:del_data(k))  
            e.grid(row=i, column=8) 
         # show the info button     
            e = tk.Button(my_w,width=5,text='info',fg='blue',relief='ridge',
            anchor="w",command=lambda k=student[0]:view_data(k))  
            e.grid(row=i, column=7) 
        # show the remove button     
            e = tk.Button(my_w,width=15,text='remove as admin',fg='Black',relief='ridge',
            anchor="w",command=lambda k=student[0]:Remove_admin(k))  
            e.grid(row=i, column=9) 
        # show the remove button     
        e = tk.Button(my_w,width=15,text='assign as admin',fg='Black',relief='ridge',
        anchor="w",command=lambda k=student[0]:add_admin(k))  
        e.grid(row=i, column=10) 
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
        
def view_data(s_id): # delete record 
    try:
        my_var=msg.askyesnocancel("view Record",
           "are you sure you want to view data relating to " + s_id,icon='warning')
        print(my_var)
        if my_var:
            f = open("C:/Users/Liam/Desktop/Main project/currentID.txt",'w+',newline= '')
            f.write(s_id)
            f.close()
            import ViewUser 
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        
def Remove_admin(s_id): # delete record 
    try:
        my_var=msg.askyesnocancel("view Record",
           "are you sure you want to remove " + s_id + " as admin",icon='warning')
        print(my_var)
        if my_var: 
            query="update persons SET isadmin = 'N', Admin_password = AES_ENCRYPT('', 'KEY') where ID = %s; "
            my_data=[s_id]
            c.execute(query,my_data)
            db.commit(); #commits changes to database
            print("Admin removed")
            
            for row in my_w.grid_slaves():# remove widgets
                row.grid_forget()
            display() # refresh the list 
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)

def add_admin(s_id):
    try:
        my_var=msg.askyesnocancel("view Record",
        "are you sure you want to remove " + s_id + " as admin",icon='warning')
        print(my_var)
        if my_var: 
             
            select_query = 'SELECT * FROM criminal_record WHERE ID = %s; '
            val = [s_id]
            c.execute(select_query, val)
                
            NewAdmin = c.fetchone()
            print(NewAdmin)
            if NewAdmin is not None:
                messagebox.showwarning("can't assign admin", "they have a criminal record")
       
            else:
                query= "select * from persons where ID = %s and IsAdmin = 'Y';"
                my_data=[s_id]
                c.execute(query,my_data)
                IsAlreadyAdmin = c.fetchone()
                if IsAlreadyAdmin is not None:
                    messagebox.showwarning("can't assign admin", "Already Admin")
                else:
                    query= "update persons SET isadmin = 'Y', Admin_password = AES_ENCRYPT('password', 'KEY') where ID = %s;"
                    my_data=[s_id]
                    c.execute(query,my_data)
                    db.commit(); #commits changes to database
                    
                    select_query = 'insert into daily_activity values (%s, "Assigned new admin", curdate(), curtime());'
                    val2= (id2)
                    c.execute(select_query, val2)
                    db.commit(); #commits changes to database
                    messagebox.showwarning("Success", "New data assigned")
                    for row in my_w.grid_slaves():# remove widgets
                        row.grid_forget()
                    display() # refresh the list 
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
my_w.mainloop()
    
    

  