import RPi.GPIO as GPIO
import mysql.connector
from mfrc522 import SimpleMFRC522
from RPLCD.i2c import CharLCD
from gpiozero import Button
from time import sleep
from datetime import datetime

lcd = CharLCD('PCF8574', 0x27)

button = Button(16)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database = "Attendance_System"
)

reader = SimpleMFRC522()
mycursor = mydb.cursor()

def getTime():
    #timeFormat = datetime.now().strftime("%H:%M:%S - %B %d, %Y ")
    timeFormat = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    return timeFormat
    
def createDatabase(mycursor, name):
    mycursor.execute("CREATE DATABASE " + name)
    print("Database created")
    
def removeDatabase(mycursor, name):
    mycursor.execute("DROP DATABASE " + name)
    print("Database deleted")
    
def showDatabases(mycursor):
    mycursor.execute("SHOW DATABASES")
    print("DATABASES: ")
    for row in mycursor:
        print("   " + str(row))
        
def createTable_Repeat_notAllow(mycursor, name):
    mycursor.execute("SHOW TABLES")
    tableExist = False
    for row in mycursor:
        if row[0] == name:
            tableExist = True           
    if tableExist == False:
        if name == "Class_Table":
            mycursor.execute("CREATE TABLE " + name + " (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(250), Teacher VARCHAR(250))")
        elif name == "Student_Table":
            mycursor.execute("CREATE TABLE " + name + " (ID VARCHAR(250), firstName VARCHAR(250), lastName VARCHAR(250), nickName VARCHAR(250))")
        elif name == "Attendance_Table":
            mycursor.execute("CREATE TABLE " + name + " (stuID VARCHAR(250), classID VARCHAR(250), dateTime VARCHAR(250))")
    else:
        print("The table already existed")

def insertClass_Repeat_notAllow(mycursor, inputName, inputTeacher):
    sql = "SELECT * FROM Class_Table WHERE Name = \"" + inputName + "\" AND " + "Teacher = \"" + inputTeacher + "\""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if len(myresult) > 0:
        print("The class already existed")
    else:
        print("Inserted")
        val = (inputName, inputTeacher)
        mycursor.execute("INSERT INTO Class_Table (Name, Teacher) VALUES (%s, %s)", val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        
def getClassID(inputName):
    sql = "SELECT * FROM Class_Table WHERE Name = \"" + str(inputName) + "\""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult[0][0]
        
def insertStudent_Repeat_notAllow(mycursor, inputID, inputFirstName, inputLastName, inputNickName):
    sql = "SELECT * FROM Student_Table WHERE ID = \"" + inputID + "\""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if len(myresult) > 0:
        print("The student already existed")
    else:
        print("Inserted")
        val = (inputID, inputFirstName, inputLastName, inputNickName)
        mycursor.execute("INSERT INTO Student_Table (ID, firstName, lastName, nickName) VALUES (%s, %s, %s, %s)", val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        
def checkAttendance(mycursor, inputStuID, inputClassID, inputDateTime):
    val = (inputStuID, inputClassID, inputDateTime)
    mycursor.execute("INSERT INTO Attendance_Table (stuID, classID, dateTime) VALUES (%s, %s, %s)", val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted. " + getTime())
        
def checkExistStudent(mycursor, inputID):
    sql = "SELECT * FROM Student_Table WHERE ID = \"" + inputID + "\""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if len(myresult) > 0:
        return True
    else:
        return False    
        
def showTables(mycursor):
    mycursor.execute("SHOW TABLES")
    print("\nTables: ")
    for row in mycursor:
        print("   " + str(row))
    print("-------------------------------------------------------------\n")

def removeTable(mycursor, name):
    mycursor.execute("DROP TABLE " + name)
    print("Table deleted")

def updateTable(mycursor, tableName, desireField, newValue, oldValue):
    sql = "UPDATE " + tableName + " SET " + desireField + "= \"" + newValue + "\" WHERE " + desireField + " = \"" + oldValue + "\""
    mycursor.execute(sql)
    print("Updated")
    mydb.commit()

def selectData(mycursor, tableName):
    mycursor.execute("SELECT * FROM " + tableName)
    myresult = mycursor.fetchall()
    print("\n" + tableName + ": ")
    for x in myresult:
        print("   " + str(x))
    print("-------------------------------------------------------------\n")
        
def deleteData(mycursor, tableName, desireField, inputVal):
    sql = "DELETE FROM " + tableName + " WHERE " + desireField + "= \"" + inputVal + "\""
    mycursor.execute(sql)
    print("Deleted")
    mydb.commit()
    
def checkAttendanceLoop():
    FinalState = False
    className = input("Enter the class name: ")
    print("Start Checking Attendance... ")
    while FinalState == False:
        if button.is_pressed:
            print("Pressed")
            changeSub = input("Check Attendance for another subject? [Y/N] ")
            if changeSub == "n" or changeSub == "N":
                FinalState = True
            else:
                className = input("Enter the class name: ")
                print("Start Checking Attendance... ")
        if reader.read_id_no_block():
            id, name = reader.read()
            if checkExistStudent(mycursor, str(id)) == False:
                for i in range(3):
                    askQ = input(questArray[i])
                    ansArray.append(askQ)
                insertStudent_Repeat_notAllow(mycursor, str(id), ansArray[0 + factor], ansArray[1 + factor], ansArray[2 + factor])
                factor = factor + 3
                selectData(mycursor, "Student_Table")
                sleep(.3)
            else:
                inputClassID = getClassID(className)
                inputDateTime = getTime()
                checkAttendance(mycursor, str(id), inputClassID, inputDateTime)
    selectData(mycursor, "Attendance_Table")
    
def classTable_Fields():
    print("\nClass_Table's Fields")
    print("   - ID")
    print("   - Name")
    print("   - Teacher")
    print("-------------------------------------------------------------\n")
    
def studentTable_Fields():
    print("\nStudent_Table's Fields")
    print("   - ID")
    print("   - firstName")
    print("   - lastName")
    print("   - nickName")
    print("-------------------------------------------------------------\n")
        
#createDatabase(mycursor, "Attendance_System")
        
createTable_Repeat_notAllow(mycursor, "Class_Table")
createTable_Repeat_notAllow(mycursor, "Student_Table")
createTable_Repeat_notAllow(mycursor, "Attendance_Table")

showTables(mycursor)

insertClass_Repeat_notAllow(mycursor, "AP Calculus AB", "Ms. Chanty")
insertClass_Repeat_notAllow(mycursor, "AP Computer Science A", "Mr. Task")
insertClass_Repeat_notAllow(mycursor, "Statistics", "Mr. Tazim")
insertClass_Repeat_notAllow(mycursor, "Robotics", "Mr. Tim")
insertClass_Repeat_notAllow(mycursor, "Game Development", "Mr. Dawit")
insertClass_Repeat_notAllow(mycursor, "English 12", "Mr. David")
insertClass_Repeat_notAllow(mycursor, "Physical Education", "Mr. Jame")

selectData(mycursor, "Class_Table")
selectData(mycursor, "Student_Table")

questArray = ["First Name: ", "Last Name: ", "Nick Name: "]
ansArray = []
factor = 0

deleteData(mycursor, "Attendance_Table", "classID", "1")
deleteData(mycursor, "Attendance_Table", "classID", "4")

print("[1] Check Attendance")
print("[2] Edit Tables")

askInput = input("\nEnter the number: ")

if askInput == "1":
    checkAttendanceLoop()
elif askInput == "2":
    print("[1] Add")
    print("[2] Remove")
    print("[3] Update")
    askInput = input("\nEnter the number: ")
    if askInput == "1":
        print("[1] Students")
        print("[2] Classes")
        askInput = input("\nEnter the number: ")
        if askInput == "1":
            for i in range(3):
                askQ = input(questArray[i])
                ansArray.append(askQ)
            askID = input("Would you like to enter the ID manually? [Y/N] ")
            if askID == "n" or askID == "N":
                print("Press your ID card")
                id, name = reader.read()
            else:
                id = input("Enter your ID: ")
            insertStudent_Repeat_notAllow(mycursor, str(id), ansArray[0 + factor], ansArray[1 + factor], ansArray[2 + factor])
        elif askInput == "2":
            inputName = input("Enter the class name: ")
            inputTeacher = input("Enter the teacher name: ")
            insertClass_Repeat_notAllow(mycursor, inputName, inputTeacher)
            
    elif askInput == "2":
        print("[1] Students")
        print("[2] Classes")
        askInput = input("\nEnter the number: ")
        if askInput == "1":
            tableName = "Student_Table"
            studentTable_Fields()
        elif askInput == "2":
            tableName = "Class_Table"
            classTable_Fields()
        print("The data will be removed according to the field and the value")
        desireField = input("\nEnter the field you want to use to remove data: ")
        inputVal = input("Enter the value: ")
        deleteData(mycursor, tableName, desireField, inputVal)
    elif askInput == "3":
        print("[1] Students")
        print("[2] Classes")
        askInput = input("\nEnter the number: ")
        if askInput == "1":
            tableName = "Student_Table"
            studentTable_Fields()
        elif askInput == "2":
            tableName = "Class_Table"
            classTable_Fields()
        print("The data will be updated according to the field and the value")
        desireField = input("\nEnter the field you want to use to update data: ")
        oldValue = input("Change the data in " + desireField + " from ")
        newValue = input("to ")
        updateTable(mycursor, tableName, desireField, newValue, oldValue)

print("Done!")

    







