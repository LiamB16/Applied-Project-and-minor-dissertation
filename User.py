import mysql.connector  # pip install mysql.connector
 
#Logs into database
db = mysql.connector.connect(
    host="localhost",
    user="liam",
    passwd="root",
    database="knownindividuals"
)

c = db.cursor()
 
#executes SQL command
c.execute("Insert into persons values('Liam', 22, 'student', 'c:/users/Liam', 'Y');")
db.commit(); #commits changes to database
for x in c:
    print(x)

c.execute("delete from persons where name = 'Liam';")
db.commit(); #commits changes to database
for x in c:
    print(x)
       

c.execute("select * from persons;")

for x in c:
    print(x)

  