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

c.execute("select ID from persons;")

results = c.fetchall()

print(results)


