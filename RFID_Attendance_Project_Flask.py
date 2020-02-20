from flask import Flask 
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database = "Attendance_System"
)

mycursor = mydb.cursor()

def showTables(mycursor):
    mycursor.execute("SHOW TABLES")
    print("\nTables: ")
    for row in mycursor:
        print("   " + str(row))

def selectData(mycursor, tableName):
    mycursor.execute("SELECT * FROM " + tableName)
    myresult = mycursor.fetchall()
    print("\n" + tableName + ": ")
    for x in myresult:
        print("   " + str(x))
        
def getClassName(inputID):
    sql = "SELECT * FROM Class_Table WHERE ID = \"" + str(inputID) + "\""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult[0][1]

def getElement(tableName, inputField, inputValue, desirePosition):
    sql = "SELECT * FROM " + tableName + " WHERE " + inputField + " = \"" + str(inputValue) + "\""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult[0][desirePosition]
        
def addHTML(tableName):
    HTML = ""
    mycursor.execute("SELECT * FROM " + tableName)
    myresult = mycursor.fetchall()
    for i in range(len(myresult)):
        HTML += "<tr>\n"
        for j in range(len(myresult[i])):
            HTML += "   <td>" + str(myresult[i][j]) + "</td>\n"
        HTML += "   <td>" + getElement("Class_Table", "ID", myresult[i][1], 1) + "</td>\n"
        HTML += "   <td>" + getElement("Student_Table", "ID", myresult[i][0], 1) + "</td>\n"
        HTML += "</tr>\n"
    return HTML

def addHTMLEdited(tableName):
    HTML = ""
    mycursor.execute("SELECT * FROM " + tableName)
    myresult = mycursor.fetchall()
    for i in range(len(myresult)):
        HTML += "<tr>\n"
        HTML += "   <td>" + str(myresult[i][0]) + "</td>\n"
        HTML += "   <td>" + getElement("Student_Table", "ID", myresult[i][0], 1) + "</td>\n"
        HTML += "   <td>" + str(myresult[i][1]) + "</td>\n"
        HTML += "   <td>" + getElement("Class_Table", "ID", myresult[i][1], 1) + "</td>\n"
        HTML += "   <td>" + str(myresult[i][2]) + "</td>\n"
        HTML += "</tr>\n"
    return HTML
    
showTables(mycursor)
selectData(mycursor, "Attendance_Table")
selectData(mycursor, "Class_Table")
selectData(mycursor, "Student_Table")
addHTML("Attendance_Table")

app = Flask(__name__, static_url_path = "", static_folder = "static") 

@app.route("/")
def home():
    myhtml = '''
    <style>
    
    body {
        background-color: #151515;
    }
    
    h1 {
        color: white;
        text-align: center;
        font-family: Arial, Helvetica, sans-serif;
    }
    
    hr {
        width: 90%;
    }
    
    table {
        width: 80%;
        color: white;
        text-align: center;
        border: 2px solid white;
        border-right: transparent;
        border-bottom: transparent;
    }
    
    th, td {
        border-right: 2px solid white;
        border-bottom: 2px solid white;
        height: 35px;
    }
    
    th {height: 50px;}
    
    </style>
    
    <br>
    <h1>Attendance Table</h1>
    <hr><br><br>
    <table align = "center">
        <tr>
            <th>stuID</th>
            <th>stuName</th>
            <th>classID</th> 
            <th>className</th>
            <th>dateTime</th>
        </tr>
    '''
    return myhtml + addHTMLEdited("Attendance_Table") + "</table><br><br><hr><br><br>"

# Run the code and go to http://localhost:5000/
if __name__ == "__main__":
    app.run()