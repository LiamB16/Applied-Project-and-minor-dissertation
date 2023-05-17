# Applied-Project-and-minor-dissertation
The purpose of this README file is to explain the purpose of this project and instruct the user on how to set up the projects on computers

# Purpose
The profiler is a facial recognition security program that is designed to identify specific people and pull up information like name, occupation and age. The profiler is capable of 
* allowing users to use the webcam to id people
* allow the user to give an image that can be compared to see if they're a match
* allow users to take attendance of indivduals and record the date and time they were seen.
* add and delete information or people on the profiler.
* designate admins to allow specific people to access the program or unassign them to prevent them from accessing it.



The information on the profiler relates to
* criminal record
* bank record 
* assets
* medical record
* education background

This is all designed based on what a government would keep track off.
# How to setup on PC
Requirements:
* Python version 3.7
* Wampserver64 with MySQL 
* dlib file (provided in repo)

1. use the command "git clone (repo link)" to clone the repository to the 
2. download the required libraries. These can be obtain using "pip install (import name)"
3. adjust the file paths for image files in the code and username and password of SQL database. Since the repo was cloned, the file paths may be different on machines
4. copy the knownindividuls.sql to MySQL. This can be done by open the path "C:\wamp64\bin\mysql\mysql5.7.36\bin" in the command line. Once you are in the bin folder, type the following command " mysql -p -u (username) KnownIndividuals < "C:\Users\Liam\Desktop\Main project\knownIndividuals.sql". You will be prompted for a password, but if you are using root, just hit enter.
once it is all finish, 
5. run the "login.py" file in visual studio code.
# NOTE 
must use python 3.7 due to dlib compatability.

# NOTE FOR EXAMINERS
all information in this database is fake for demonstration purposes
