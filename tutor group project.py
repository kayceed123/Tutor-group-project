#Importing csv so that i can import newandimprovednamebook.csv
import csv

runacoupletimes= True
#add student details
def add_students():
    students=open("newandimprovednamebook.csv","a")
    #Adding a student Id which is added to row 1
    Identity=(input("Enter a student ID"))
    #Adding a students forename which is added to row 2
    forename=input("Enter the students forename")
    #Adding a students surname which is added to row 3
    surname=input("Enter the students surname")
    #Closing newandimprovednamebook.csv
    students.close()
    with open("newandimprovednamebook.csv","a") as file:
        #Writes a new column using the ID, forename and surname
        file.write("\n"+str(Identity) + "," + forename + "," + surname)


#view student details
def view_student():
    students=open("newandimprovednamebook.csv","r")
    searchstudent=input("What students would you like to search for?")
    for x in students:
        if students[1]==searchstudent:
            print(x)
        else:
            print("Student not found")
    students.close

#Create report
def create_report():
    students=open("newandimprovednamebook.csv","r")
    print(students)


access=False
while access==False:
    username=input("Please enter your username")
    password=input("Please enter your password")
    if username=="teacher123" and password=="pass123":
        print("\n Access granted")
        access=True
    else:
        print("\nAccess denied")

    while runacoupletimes==True:
        menu=int(input("\nWelcome to the menu \n\n Press 1 to add student details \n 2 to view student details \n 3 to create a report \n 4 to log out"))
        if menu==1:
            add_students()
            runacoupletimes==False
        elif menu==2:
            view_student()
            runacoupletimes==False
        elif menu==3:
            create_report()
            runacoupletimes==False
        elif menu==4:
            runacoupletimes=False
        else:
            print("Invalid input")