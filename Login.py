#login form
import tkinter as tk
from tkinter import messagebox

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

# create a function to close the window
def close_window():
    root.destroy()

# width and height
w = 400
h = 260

class loginForm:
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
        
        self.usernameLabel = tk.Label(self.frame, text='ID:', bg='#fff',
                                      font=('Verdana',16))
        self.usernameTextbox = tk.Entry(self.frame, font=('Verdana',12), width=25,
                                        borderwidth='2', relief='ridge')
        
        self.passwordLabel = tk.Label(self.frame, text='Password:', bg='#fff',
                                      font=('Verdana',16))
        self.passwordTextbox = tk.Entry(self.frame,show='*', font=('Verdana',12),
                                        width=25, borderwidth='2', relief='ridge')
        
        self.btnLogin = tk.Button(self.btnsFrame, text='Login', bg='green',
                                  font=('Verdana',12), fg='#fff', padx=25,
                                  pady=10, command=self.login_func)
        self.btnCancel = tk.Button(self.btnsFrame, text='Cancel', bg='orange',
                                   font=('Verdana',12), fg='#fff', padx=25,
                                   pady=10, command=close_window)
        # end create widgets

        # start place widgets
        self.frame.pack(fill='both')
        self.windowTitle.grid(row=0, column=0, columnspan=2)
        self.usernameLabel.grid(row=1, column=0)
        self.usernameTextbox.grid(row=1, column=1)
        self.passwordLabel.grid(row=2, column=0, pady=(10,0))
        self.passwordTextbox.grid(row=2, column=1, pady=(10,0))
        self.btnsFrame.grid(row=3, column=0, columnspan=2, pady=10)
        self.btnLogin.grid(row=0, column=0, padx=(0,35))
        self.btnCancel.grid(row=0, column=1)
        # end place widgets

    # create a function to login
    def login_func(self):
        username = self.usernameTextbox.get()
        password = self.passwordTextbox.get()
        print(username)
        print(password)
        select_query = 'SELECT * FROM Persons WHERE ID = %s and Admin_password = AES_ENCRYPT(%s, "KEY") and IsAdmin = "Y";'
        vals = (username, password,)
        c.execute(select_query, vals)
        
        user = c.fetchone()
        print(user)
        if user is not None:
           
           messagebox.showwarning('correct', 'Valid Username & Password')
        else:
            messagebox.showwarning('Error', 'Enter a Valid Username & Password')



def main():
    login_window = loginForm(root)
    root.mainloop()

if __name__ == '__main__':
    main()