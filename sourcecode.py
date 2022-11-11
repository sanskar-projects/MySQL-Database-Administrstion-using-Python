import mysql.connector

conn=mysql.connector.connect(host='localhost',password='',user='root', database='') #ENTER YOUR PASSWORD AND NAME OF THE DATABASE WHICH YOU WANT TO USE

mycursor=conn.cursor()

#DEFINING FUNCTIONS FOR DDL AND DML COMMANDS

#1:CHECKING ESTABLISHMENT OF CONNECTION TO THE DATABASE
def connect():
    if conn.is_connected():
        print("Connected")
    else:
        print("Not connected")

#2:CREATE A DATABASE
def create():
    print("Enter database name to be created")
    x=input()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(x))
    print("Created")

#3:DROP A DATABASE
def drop(): 
    print("Enter database name to be dropped")
    x=input()
    mycursor.execute("DROP DATABASE IF EXISTS {}".format(x))
    print("Dropped")

#4:SHOW DATABASES
def show():
    mycursor.execute("SHOW DATABASES")
    for i in mycursor:
        print(i)

#5:Create a table
def createtable():
    print("Enter table name to be created")
    x=input()
    print("Enter column name having primary key constraint")
    y=input()
    print("Enter column type")
    z=input()
    mycursor.execute("CREATE TABLE IF NOT EXISTS {} ({} {} PRIMARY KEY)".format(x,y,z))
    print("Created")

#6:Drop a table
def droptable():
    print("Enter table name to be dropped")
    x=input()
    mycursor.execute("DROP TABLE {}".format(x))
    print("Dropped")
    
#7:Show tables
def showtables():
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)

#8:Show structure of a table
def desc():
    print("Enter table name to view structure")
    x=input()
    try:
        mycursor.execute("DESC {}".format(x))
        for x in mycursor:
            print(x)
    except:
        print("Please enter an existing table")

#9:Add a column in a table
def addcolumn():
    print("Enter table name to be altered")
    x=input()
    print("Enter column name")
    y=input()
    print("Enter column type")
    z=input()
    print("Enter constraint")
    p=input()    
    try:
        mycursor.execute("ALTER TABLE {} ADD COLUMN {} {} {}".format(x,y,z,p))
        print("Added")
        conn.commit()
    except:
        print("Please enter a non existent column and an existing table")

#10:Drop a column in a table
def dropcolumn():
    print("Enter table name to be altered")
    x=input()
    print("Enter column name")
    y=input()
    try:
        mycursor.execute("ALTER TABLE {} DROP COLUMN {}".format(x,y))
        print("Dropped")
        conn.commit()
    except:
        print("Please enter an existing column and existing table")

#1:Rename a column in a table
def renamecolumn():
    print("Enter table name to be altered")
    x=input()
    print("Enter column name")
    y=input()
    print("Enter new column name")
    z=input()
    try:
        mycursor.execute("ALTER TABLE {} RENAME COLUMN {} TO {}".format(x,y,z))
        print("Renamed")
        conn.commit()
    except:
        print("Please enter an existing column and existing table")

#12:Change type of a column in a table
def retypecolumn():
    print("Enter table name to be altered")
    x=input()
    print("Enter column name")
    y=input()
    print("Enter new column type with size")
    z=input()
    try:
        mycursor.execute("ALTER TABLE {} MODIFY {} {}".format(x,y,z))
        print("Changed")
        conn.commit()
    except:
        print("Please enter an existing column and table and a compatible column type")

#13:Insert a record in a table
def insert():
    print("Enter table name to insert values")
    x=input()
    print("Enter column name")
    y=input()
    print("Enter value")
    z=input()
    mycursor.execute("INSERT INTO {} ({}) VALUES({})".format(x,y,z))
    print("Inserted")
    conn.commit()

#14:Delete a record in a table
def delete():
    print("Enter table name to delete values")
    x=input()
    i=0
    print("Enter condition number {} for WHERE clause".format(i))
    y=input()
    try:
        mycursor.execute("DELETE FROM {} WHERE {}".format(x,y))
        print("Deleted")       
        conn.commit()
    except:
        print("Please enter an existing column and existing table and a compatible condition for WHERE clause")

#15:Clear a table
def clear():
    print("Enter table name to be cleared")
    x=input()
    try:
        mycursor.execute("DELETE FROM {}".format(x))
        print("Cleared")
        conn.commit()
    except:
        print("Please enter an existing table")

#16:Show a record in a table
def select():
    print("Enter table name to view records")
    x=input()
    i=0
    print("Enter column name")
    y=input()      
    print("Enter condition number {} for WHERE clause".format(i))
    z=input()
    print("Enter column name for ORDER BY clause")
    p=input()
    print("Press d if you want the records to be ordered in descending order else press any other key")
    q=input()
    try:
        if q=='d':
            mycursor.execute("SELECT {} FROM {} WHERE {} ORDER BY {} DESC".format(y,x,z,p))
        else:
            mycursor.execute("SELECT {} FROM {} WHERE {} ORDER BY {}".format(y,x,z,p))
        for x in mycursor:
            print(x)
    except:
        print("Please enter an existing table and compatible conditions for WHERE and ORDER BY clauses")

#17:Show all records in a table
def selectstar():
    print("Enter table name to view all records")
    x=input()
    try:
        mycursor.execute("SELECT * FROM {}".format(x))
        for x in mycursor:
            print(x)
    except:
        print("Please enter an existing table")

#18:Update a record in a table
def update():
    print("Enter table name to be updated")
    x=input()
    print("Enter column name")
    y=input()
    print("Enter value")
    z=input()
    print("Enter condition for WHERE clause")
    p=input()
    try:
        mycursor.execute("UPDATE {} SET {}={} WHERE {}".format(x,y,z,p))
        print("Updated")
        conn.commit()
    except:
        print("Please enter an existing table and existing column and compatible condition for WHERE clause also check the value you entered")

#MAIN MENU
def sql():
    print("MAIN MENU \n Enter your choice (1-18) \n 1:Check establishment of connection to the database \n 2:Create a database \n 3:Drop a database \n 4:Show databases \n 5:Create a table \n 6:Drop a table \n 7:Show tables \n 8:Show structure of a table \n 9:Add a column in a table \n 10:Drop a column in a table \n 11:Rename a column in a table \n 12:Change type of a column in a table \n 13:Insert a record in a table \n 14:Delete a record in a table \n 15:Clear a table \n 16:Show a record in a table \n 17:Show all records in a table \n 18:Update a record in a table \n")
    choice=int(input())
    if choice==1:
        connect()
    elif choice==2:
        create()
    elif choice==3:
        drop()
    elif choice==4:
        show()
    elif choice==5:
        createtable()
    elif choice==6:
        droptable()
    elif choice==7:
        showtables()
    elif choice==8:
        desc()
    elif choice==9:
        addcolumn()
    elif choice==10:
        dropcolumn()
    elif choice==11:
        renamecolumn()
    elif choice==12:
        retypecolumn()
    elif choice==13:
        insert()
    elif choice==14:
        delete()
    elif choice==15:
        clear()
    elif choice==16:
        select()
    elif choice==17:
        selectstar()
    elif choice==18:
        update()
    else:
        print("Invalid choice")

#PROGRAM EXECUTION BEGINS HERE
choice='y'
while choice=='y':
    sql()
    print("Press y to return to the main menu else press any other key to terminate the program")
    choice=input()
print("PROGRAM TERMINATED!!!!!!!!!!")
