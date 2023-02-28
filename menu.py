import mysql.connector  # pip install mysql.connector
import tkinter as TK
from tkinter import *
import cv2  # pip install opencv-python
from tkinter import messagebox
import pathlib
import face_recognition

root = Tk()
root.title("profiler")
root.iconbitmap("C:/Users/Liam/Desktop/Main project/images/favicon.ico")
# root.iconbitmap("c:/gui/codemy.ico")
root.geometry("400x400")

db = mysql.connector.connect(
    host="localhost",
    user="liam",
    passwd="root",
    database="knownIndividuals"
)

c = db.cursor()

my_menu = Menu(root)
root.config(menu=my_menu)

global entry1
global entry2

bkg= "#636e72"

frame = TK.Frame(root, bg=bkg)

# click command
def our_command():
    pass

def Add():
    label_name = TK.Label(frame, text="Name: ")
    entry_name = TK.Entry(frame)
    
    label_age = TK.Label(frame, text="Age: ")
    entry_age = TK.Entry(frame)
    
    label_occupation = TK.Label(frame, text="Occupation: ")
    entry_occupation = TK.Entry(frame)
    
    label_image = TK.Label(frame, text="Image Link: ")
    entry_image = TK.Entry(frame)
    
    Button(root,text="Add",command=AddPerson,height=3,width=13, bd=6).place(x=100, y=120)
    
    label_name.grid(row=0, column=0)
    entry_name.grid(row=0, column=1)
    
    label_age.grid(row=1, column=0)
    entry_age.grid(row=1, column=1)
    
    label_occupation.grid(row=2, column=0)
    entry_occupation.grid(row=2, column=1)
    
    label_image.grid(row=3, column=0)
    entry_image.grid(row=3, column=1)
    
    frame.pack()
    
def AddPerson():
    try:
        c.execute("Insert into persons values('Liam', 22, 'student', 'c:/users/Liam', 'Y');")
    except Exception as e:
        print(e)
        c.rollback()
        c.close()


def DeletePerson():
    try:
        c.execute("delete from persons where name = 'Liam';")
    except Exception as e:
        print(e)
        c.rollback()
        c.close()


def Camera():
    #finds image in file and converts it to binary code
    img = cv2.imread("C:/Users/Liam/Desktop/Main project/images/Liam.jpg")
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_encoding = face_recognition.face_encodings(rgb_img)[0]

    #finds image in file and converts it to binary code
    img2 = cv2.imread("C:/Users/Liam/Desktop/Main project/images/LiamTest.jpg")
    rgb_img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_encoding2 = face_recognition.face_encodings(rgb_img)[0]

    #compares binary code of two images and sees if they are both the same
    results = face_recognition.compare_faces([img_encoding], img_encoding2)
    if results == [True]:
       #SQL query of the 
       print("found a match")
    else:
       print("unknown")
    
    #cv2.imshow("img", img)
    
#Redirects user to login page  
def LoginPage():
    Label(root,text="Username").place(x=20,y=20)
    Label(root,text="Password").place(x=20,y=70)
    
    entry1=Entry(root,bd=5)
    entry1.place(x=140, y=20)
    
    entry2=Entry(root,bd=5)
    entry2.place(x=140, y=70)
    
    Button(root,text="Login",command=Login,height=3,width=13, bd=6).place(x=100, y=120)#button actives Login() function
    
    return entry1, entry2

#Contains login function for verifying username and password 
def Login(entry1, entry2):
    username=entry1
    password=entry2
    
    #checks for blank pages
    if(username=="" and password==""):
        messagebox.showinfo("", "Blank entry not allowed")
    #checks for correct user
    elif(username=="Liam" and password=="Password"):
        messagebox.showinfo("", "Access Granted")
    #shows message for wrong user    
    else:
        messagebox.showinfo("", "incorrect")
        
def Monitor():
    ID = "" #variable used to ID individual 

    #SQL query gets data using ID variable
    name = "Liam Bryant"
    age = "22"
    occupation = "student"

    cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"

    clf = cv2.CascadeClassifier(str(cascade_path))

    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW) #captureDevice = camera # VideoCapture(number of cameras). 0 is the defualt number

    while (True): #runs camera on laptop
        ret, frame =  camera.read()
        #scales faces and shows image in color
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
        )
        #for every face captured, draw rectangle around face
        for(x, y, width, height) in faces:
            #draws rectangle
            cv2.rectangle(frame, (x, y), (x+width, y+height), (255, 255, 0), 2) #draws rectangle around head
            #displays text above square
            cv2.putText(frame, "name: " +name, (x, y-50), cv2.FONT_HERSHEY_SIMPLEX, #adds text around rectangle
             0.75, (0, 255, 0), 2)
            cv2.putText(frame, "age: " + age, (x, y-22), cv2.FONT_HERSHEY_SIMPLEX, #adds text around rectangle
             0.75, (0, 255, 0), 2)
            cv2.putText(frame, "occupation: " + occupation, (x, y), cv2.FONT_HERSHEY_SIMPLEX, #adds text around rectangle
             0.75, (0, 255, 0), 2)
            ID = "G00377746" 
            print(ID)
        #shows camera feed on laptop 
        cv2.imshow("FACES", frame)
        #kills camera if 'q' is pressed
        if cv2.waitKey(1) == ord("q"):
           break
    camera.release()
    cv2.destroyAllWindows
        
    
# create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="options", menu=file_menu)
file_menu.add_command(label="Customise Menu", command=our_command)
file_menu.add_command(label="Switch admins", command=our_command)

# create edit item menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Users", menu=edit_menu)
edit_menu.add_command(label="add known individual", command=Add)
edit_menu.add_command(label="remove individual", command=DeletePerson)
edit_menu.add_command(label="view database", command=DeletePerson)
edit_menu.add_command(label="set/remove admin", command=DeletePerson)

photo = TK.PhotoImage(file = "C:/Users/Liam/Pictures/Security.png")
label2 = TK.Label(root,  image = photo,  width = 300, height = 250,
                 bg = "white", fg = "black")
label2.pack()





b = Button(root, text="Monitor Mode", command=Monitor)
b.pack()

b2 = Button(root, text="Profile Mode", command=Camera)
b2.pack()

b3 = Button(root, text="Take attendance", command=Camera)
b3.pack()

b4 = Button(root, text="Logout", command=root.quit)
b4.pack()

root.mainloop()
