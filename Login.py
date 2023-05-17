#login form
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import *
import PIL.Image
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

f = open("C:/Users/Liam/Desktop/Main project/currentLogin.txt",'w+',newline= '')

# create a function to close the window
def close_window():
    root.destroy()

# width and height
w = 400
h = 260

class loginForm:
    def __init__(self,master):
        
        self.master = master
        self.master.geometry('1166x718')
        self.master.state('zoomed')
        self.master.resizable(0,0)
        self.master.configure(bg='black')
    
        
        
        # start create widgets
        self.frame = tk.Frame(self.master)
        self.frame.place(x=500, y=700)
        self.frame.configure(bg='grey')
           
        self.Icon2 = tk.PhotoImage(file = 'C:/Users/Liam/Desktop/Main project/UI_images/LoginIcon.png')
        self.label4 = tk.Label(self.frame,  image = self.Icon2, width = 200, height = 180)
        
        self.btnsFrame = tk.Frame(self.frame, bg='#fff', padx=15, pady=15)
        
        self.windowTitle = tk.Label(self.frame, text='Profiler', bg='grey',
                                    fg='black', font=('Tahoma',20), pady=15)
        
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
        self.btnCancel = tk.Button(self.btnsFrame, text='Cancel', bg='red',
                                   font=('Verdana',12), fg='#fff', padx=25,
                                   pady=10, command=close_window)
        # end create widgets

        # start place widgets
        
        self.frame.pack()
        self.label4.grid(row=1, column=18, columnspan=2)
        self.windowTitle.grid(row=0, column=18, columnspan=2)
        self.usernameLabel.grid(row=2, column=18)
        self.usernameTextbox.grid(row=2, column=19)
        self.passwordLabel.grid(row=3, column=18, pady=(10,0))
        self.passwordTextbox.grid(row=3, column=19, pady=(10,0))
        self.btnsFrame.grid(row=4, column=18, columnspan=2, pady=10)
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
           try:
               select_query = 'insert into daily_activity values (%s, "Logged in", curdate(), curtime());'
               vals = [username]
               c.execute(select_query, vals)
               db.commit(); #commits changes to database
               f.write(username)
               f.close()
               close_window()
               import menu
           except Exception as e:
               print(e)
               c.rollback()
               c.close()
        else:
            messagebox.showwarning('Error', 'Enter a Valid Username & Password')




def main():
    login_window = loginForm(root)
    root.mainloop()

if __name__ == '__main__':
    main()