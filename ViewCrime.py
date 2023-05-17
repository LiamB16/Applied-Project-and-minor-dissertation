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
f = open("currentID.txt", "r")
id = f.read()

f2 = open("currentLogin.txt", "r")
id2 = f2.read()
print(id)
bkg = "white"
windowTitle = tk.Label(my_w, text='Criminal Offenses', bg='white',
                        fg='black', font=('Tahoma',20), pady=15)

windowTitle.grid(row = 0, column = 20)

  

c.execute("select crime from criminal_record where ID = %s;", [id])
trv=ttk.Treeview(my_w,selectmode='browse')
trv.grid(row = 2, column = 0, padx = 20, pady=20)
trv["columns"] = ("1")
trv['show']='headings'
trv.column("1",width=80,anchor='c') 

trv.heading("1",text="crime")

for dt in c: 
        trv.insert("", 'end',iid=dt[0],values=(dt[0]))
         # show the delete button     
          
e = tk.Button(my_w,width=5,text='Del',fg='red',relief='ridge',
anchor="c",command=lambda: del_data())  
e.grid(row=0, column=0) 


def del_data(): # delete record 
    selected_item = trv.selection()[0]
    try:
        my_var=msg.askyesnocancel("Delete Record",
           "Are you sure ? ",icon='warning')
        print(my_var)
        if my_var:
            query="DELETE FROM criminal_record WHERE crime=%s"
            my_data=[selected_item]
            c.execute(query,my_data)
            db.commit(); #commits changes to database
            trv.delete(selected_item)
            
            select_query = 'insert into daily_activity values (%s, "Deleted crime", curdate(), curtime());'
            val2=[id2]
            c.execute(select_query, val2)
            db.commit(); #commits changes to database
            msg.showwarning("Success", "Data Deleted")
             
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)

my_w.mainloop()