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

windowTitle = tk.Label(my_w, text='Asset information', bg='white',
                        fg='black', font=('Tahoma',20), pady=15)
bkimg = tk.PhotoImage(file = "C:/Users/Liam/Pictures/BankOfIrelandLogo.png")
label2 = tk.Label(my_w,  image = bkimg, width = 200, height = 200,
        bg = "white", fg = "black")

windowTitle.grid(row = 0, column = 20)
label2.grid(row = 1, column = 20) 
        
def display():
    c.execute("select Asset, valuedAt, AssetID from assets where ID = 'G00377746';")

    i=3
    for student in c: 
        for j in range(len(student)):
            e = Entry(my_w, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
         # show the delete button     
            e = tk.Button(my_w,width=5,text='Del',fg='red',relief='ridge',
            anchor="w",command=lambda k=student[0]:del_data(k))  
            e.grid(row=i, column=8) 
        i=i+1
display()

def del_data(s_id): # delete record 
    try:
        my_var=msg.askyesnocancel("Delete Record",
           "Are you sure ? ",icon='warning')
        print(my_var)
        if my_var:
            query="DELETE FROM Assets WHERE Asset=%s"
            my_data=[s_id]
            c.execute(query,my_data)
            db.commit(); #commits changes to database
            
            select_query = 'insert into daily_activity values ("G00377746", "Deleted asset", curdate(), curtime());'
            c.execute(select_query)
            db.commit(); #commits changes to database
            msg.showwarning("Success", "Data Deleted")
            print("Row Deleted  ")
            
            for row in my_w.grid_slaves():# remove widgets
                row.grid_forget()
            display() # refresh the list 
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)

my_w.mainloop()