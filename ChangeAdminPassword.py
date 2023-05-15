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
            
            self.windowTitle = tk.Label(self.frame, text='Assign New Admin', bg='#fff',
                                        fg='blue', font=('Tahoma',20), pady=30)
            
            self.oldLabel = tk.Label(self.frame, text='Old password: ', bg='#fff',
                                        font=('Verdana',16))
            self.oldTextbox = tk.Entry(self.frame, font=('Verdana',12), width=25,
                                            borderwidth='2', relief='ridge')
            self.newLabel = tk.Label(self.frame, text='New password: ', bg='#fff',
                                        font=('Verdana',16))
            self.newTextbox = tk.Entry(self.frame, font=('Verdana',12), width=25,
                                            borderwidth='2', relief='ridge')
            
            self.btnLogin = tk.Button(self.btnsFrame, text='Assign', bg='green',
                                    font=('Verdana',12), fg='#fff', padx=25,
                                    pady=10, command=self.Assign)
            self.btnCancel = tk.Button(self.btnsFrame, text='Cancel', bg='red',
                                    font=('Verdana',12), fg='#fff', padx=25,
                                    pady=10, command=close_window)
            # end create widgets

            # start place widgets
            self.frame.pack(fill='both')
            self.windowTitle.grid(row=0, column=0, columnspan=2)
            self.oldLabel.grid(row=1, column=0)
            self.oldTextbox.grid(row=1, column=1)
            self.newLabel.grid(row=2, column=0)
            self.newTextbox.grid(row=2, column=1)
            self.btnsFrame.grid(row=4, column=0, columnspan=2, pady=10)
            self.btnLogin.grid(row=0, column=0, padx=(0,35))
            self.btnCancel.grid(row=0, column=1)
            # end place widgets


    def Assign(self):
        id = self.oldTextbox.get()
        select_query = 'SELECT * FROM persons WHERE ID = "G00377746" and Admin_password = AES_ENCRYPT(%s, "KEY"); '
        val = [id]
        c.execute(select_query, val)
                
        oldpass = c.fetchone()
        
        if oldpass is None:
            messagebox.showwarning("can't change password", "Old password is incorrect")
       
        else:
            id2 = self.newTextbox.get()
            query= "update persons SET Admin_password = AES_ENCRYPT('%s', 'KEY') where ID = 'G00377746';"
            my_data=(id2)
            c.execute(query,my_data)
            print(my_data)
            db.commit(); #commits changes to database
            messagebox.showwarning("Success", "New password assigned")
            close_window()
def main():
    AssignAdmin_window = AssignAdmin_Form(root)
    root.mainloop()

if __name__ == '__main__':
    main()