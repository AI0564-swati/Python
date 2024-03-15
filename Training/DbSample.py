'''
1. Database - CRUD -
2. Select Database sw (Oracle, Mysql, SQL Server, dbeaver, MongoDb, SQLite (in built db),Postgrey)
3. Define Database based on your project
4. Create a table within DB
5. insert records
6. Select / read, update , delete
'''
import sqlite3 # step 2: Selecting Database sw 
conn=sqlite3.connect('Day15.db') # step 3: Defining Database - create or use
cursor=conn.cursor()

cursor. execute('create table if not exists emp(empno integer primary key, empname text)') # step 4: Creating a table
print('Done')


def create_emp(eno,ename): # parameter
    try:
        cursor.execute("insert into emp(empno,empname) values (?,?)", (eno,ename)) # insert records
        conn.commit() # save permenatly
        print("Employee Added")
    except sqlite3.IntegrityError:
        print("Employee already Exists")
        

def read_emp(eno):
    try:
        cursor.execute("Select * from emp where empno=?", (eno,))
        employees = cursor.fetchone()
        if employees:
            print("Emp No: ", employees[0], "Emp Name: ", employees[1])
        else:
            print("No Records Found")
    except Exception as e:
        print("Error: ",e)

def readall_emp():
    try:
        cursor.execute("Select * from emp")
        employees = cursor.fetchall()
        if employees:
            for emp in employees:
                print("Emp No: ", emp[0], "Emp Name: ", emp[1])
        else:
            print("No Records Found")
    except Exception as e:
        print("Error: ",e)

def update_emp():
    print("")

def delete_emp(eno):
    try:
        cursor.execute("Delete * from emp where empno=?", (eno,))
        employees = cursor.fetchone()
        if employees:
            print("Emp No: ", employees[0], "Emp Name: ", employees[1])
        else:
            print("No Records Found")
    except Exception as e:
        print("Error: ",e)

def display_menu():
    print("\n1.Create Employee")
    print("2. Read Employee")
    print("3. Read All Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")
    
def user_choice():
    while True:
        choice=int(input("Enter Choice : "))
        if choice in [1,2,3,4,5,6]:
            return choice
        else:
            print("Invalid choice")

while True:
    display_menu()
    ch=user_choice()
    if ch == 1:
        empno=int(input("Enter Emp Number : "))
        empname=input("Enter Name : ")
        create_emp(empno,empname) # arguments
    elif ch == 2:
        empno = int(input("Enter Employee No: "))
        read_emp(empno)
    elif ch == 3:
        readall_emp()
    elif ch == 4:
        # readall_emp()
        print("")
    elif ch == 5:
        empno = int(input("Enter Employee No: "))
        readall_emp(empno)
    elif ch == 5:
        # readall_emp()
        break














