#login form
import tkinter as tk
from tkinter import messagebox

import mysql.connector



db = mysql.connector.connect(
    host="localhost",
    user="liam",
    passwd="root",
    database="knownIndividuals"
)

c = db.cursor()
root = tk.Tk()
# create a function to close the window
def close_window():
    root.destroy()

# width and height
w = 400
h = 260
class AssignAdmin_Form:
    def __init__(self,master):  
            self.master = master
            # start center window
            ws = self.master.winfo_screenwidth()
            hs = self.master.winfo_screenheight()
            x = (ws-w)/2
            y = (hs-h)/2
            self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
            # end center window

            # start create widgets
            self.frame = tk.Frame(self.master, bg='#fff')
            
            self.btnsFrame = tk.Frame(self.frame, bg='#fff', padx=40, pady=15)
            
            self.windowTitle = tk.Label(self.frame, text='Login Window', bg='#fff',
                                        fg='blue', font=('Tahoma',20), pady=30)
            
            self.usernameLabel = tk.Label(self.frame, text='ID: ', bg='#fff',
                                        font=('Verdana',16))
            self.usernameTextbox = tk.Entry(self.frame, font=('Verdana',12), width=25,
                                            borderwidth='2', relief='ridge')
            
            
            self.btnLogin = tk.Button(self.btnsFrame, text='Assign', bg='green',
                                    font=('Verdana',12), fg='#fff', padx=25,
                                    pady=10, command=self.Assign)
            self.btnCancel = tk.Button(self.btnsFrame, text='Cancel', bg='orange',
                                    font=('Verdana',12), fg='#fff', padx=25,
                                    pady=10, command=close_window)
            # end create widgets

            # start place widgets
            self.frame.pack(fill='both')
            self.windowTitle.grid(row=0, column=0, columnspan=2)
            self.usernameLabel.grid(row=1, column=0)
            self.usernameTextbox.grid(row=1, column=1)
            self.btnsFrame.grid(row=3, column=0, columnspan=2, pady=10)
            self.btnLogin.grid(row=0, column=0, padx=(0,35))
            self.btnCancel.grid(row=0, column=1)
            # end place widgets


    def Assign(self):
        id = self.usernameTextbox.get()
        select_query = 'SELECT * FROM criminal_record WHERE ID = %s; '
        val = [id]
        c.execute(select_query, val)
                
        NewAdmin = c.fetchone()
        print(NewAdmin)
        if NewAdmin is not None:
            messagebox.showwarning("can't assign admin, they have a criminal record")
       
        else:
            query= 'update persons SET isadmin = "Y" where ID = %s;'
            my_data=[id]
            c.execute(query,my_data)
            db.commit(); #commits changes to database
            messagebox.showwarning("New Admin assigned  ")
            close_window()
def main():
    AssignAdmin_window = AssignAdmin_Form(root)
    root.mainloop()

if __name__ == '__main__':
    main()