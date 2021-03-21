# Joey Sheridan
# 3/21/2021
# CPSC 408 - Databases
# Assignment 3


import sqlite3
import pandas as pd
from pandas import DataFrame

# Establishes connection to database . . .
conn = sqlite3.connect('./Student.sqlite')
my_cursor = conn.cursor()


# Creates the temp student table in the Student database when application starts
def create_students_table():
    my_cursor.execute('''
    CREATE TABLE students(
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT ,
    FirstName TEXT,
    LastName TEXT,
    GPA REAL,
    Major TEXT,
    FacultyAdvisor TEXT,
    Address TEXT,
    City TEXT,
    State TEXT,
    ZipCode Text,
    MobilePhoneNumber TEXT,
    isDeleted INTEGER DEFAULT 0
);
''')


# Deletes the temporary student table from the Student database when app closes
def delete_table():
    my_cursor.execute("drop table students")


# Uses Pandas to convert ./students.csv to a sqlite table in our Students.sqlite database . . .
def data_ingestion():
    student_data = pd.read_csv('./students.csv')
    student_data.to_sql('students', conn, if_exists='append', index=False)


# Displays student table
def display():
    my_cursor.execute('SELECT * FROM students')
    my_records = my_cursor.fetchall()
    df = DataFrame(my_records, columns={'StudentID', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor',
                                        'Address', 'City', 'State', 'ZipCode', 'MobilePhoneNumber', 'isDeleted'})
    print(df)
    # del df


# Adds a new students to table
def add_student():
    records = []
    print("\nCreating new student . . .  \n")
    first_name = input("Enter First Name : ")
    last_name = input("Enter Last Name : ")
    gpa = input("Enter GPA : ")
    major = input("Enter Major : ")
    faculty_advisor = input("Enter Faculty Advisor : ")
    address = input("Enter address : ")
    city = input("Enter City : ")
    state = input("Enter State : ")
    zip_code = input("Enter Zip Code : ")
    mobile_phone_number = input("Enter Mobile Phone Number : ")

    records.append(
        (first_name, last_name, gpa, major, faculty_advisor, address, city, state, zip_code, mobile_phone_number))
    conn.executemany("INSERT INTO students(FirstName, LastName, GPA, Major, FacultyAdvisor, Address, City, "
                     "State, ZipCode, MobilePhoneNumber) VALUES(?,?,?,?,?,?,?,?,?,?)", records)

    print("\n New Student Created . . .\n")
    conn.commit()


# Updates the Major , Advisor, or Phone number of an existing student by ID
def update_student():
    print("\nUpdating New Student . . .")
    print("Please chose one of the following to update")
    print("[Major]      [Advisor]       [MobilePhoneNumber]")
    choice = input(":")
    while choice.upper() != "MAJOR" and choice.upper() != "ADVISOR" and choice.upper() != "MOBILEPHONENUMBER":
        print("Input Invalid")
        print("Please chose one of the following to update")
        print("[Major]      [Advisor]       [MobilePhoneNumber]")
        choice = input()

    if choice.upper() == "MAJOR":
        student_id = input("\nEnter the Student ID of the Student you wish to update: ")
        major = input("Enter the new Major : ")
        my_cursor.execute("UPDATE students SET Major = ? WHERE StudentID = ?", (major, student_id,))
        print("\nUpdate Complete\n")
    if choice.upper() == "ADVISOR":
        student_id = input("\nEnter the Student ID of the Student you wish to update: ")
        advisor = input("Enter the new Advisor : ")
        my_cursor.execute("UPDATE students SET Advisor = ? WHERE StudentID = ?", (advisor, student_id,))
        print("\nUpdate Complete\n")
    if choice.upper() == "MOBILEPHONENUMBER":
        student_id = input("\nEnter the Student ID of the Student you wish to update: ")
        mobil = input("Enter the new Mobile Phone Number : ")
        my_cursor.execute("UPDATE students SET MobilePhoneNumber = ? WHERE StudentID = ?", (mobil, student_id,))
        print("\nUpdate Complete\n")
    conn.commit()


# Displays student tuples with common criteria
def display_by():
    val = []
    print("\nSearching Student by Attribute . . .")
    print("Please chose one of the following attributes to search by")
    print("[Major]  [GPA]  [City]  [State]  [Advisor]")
    choice = input(":")
    while choice.upper() != "MAJOR" and choice.upper() != "GPA" and choice.upper() != "CITY" and choice.upper() != "STATE" and choice.upper() != "ADVISOR":
        print("Input Invalid")
        print("Please chose one of the following attributes to search by")
        print("[Major]  [GPA]  [City]  [State]  [Advisor]")
        choice = input()
    if choice.upper() == "MAJOR":
        major = input("Enter the Major you are looking for : ")
        val.append(major)
        print("Returning all Students that Major in " + major + "\n")
        my_cursor.execute('SELECT * FROM students WHERE Major = ?', val)
        my_records = my_cursor.fetchall()
        df = DataFrame(my_records, columns={'StudentID', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor',
                                            'Address', 'City', 'State', 'ZipCode', 'MobilePhoneNumber', 'isDeleted'})
        print(df)
        del df
    if choice.upper() == "GPA":
        gpa = input("Enter the GPA you are looking for : ")
        val.append(gpa)
        print("Returning all Students that have a GPA of " + gpa + "\n")
        my_cursor.execute('SELECT * FROM students WHERE GPA = ?', val)
        my_records = my_cursor.fetchall()
        df = DataFrame(my_records, columns={'StudentID', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor',
                                            'Address', 'City', 'State', 'ZipCode', 'MobilePhoneNumber', 'isDeleted'})
        print(df)
        del df
    if choice.upper() == "CITY":
        city = input("Enter the City you are looking for : ")
        val.append(city)
        print("Returning all Students that live in the City of " + city + "\n")
        my_cursor.execute('SELECT * FROM students WHERE City = ?', val)
        my_records = my_cursor.fetchall()
        df = DataFrame(my_records, columns={'StudentID', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor',
                                            'Address', 'City', 'State', 'ZipCode', 'MobilePhoneNumber', 'isDeleted'})
        print(df)
        del df
    if choice.upper() == "STATE":
        state = input("Enter the State you are looking for : ")
        val.append(state)
        print("Returning all Students that live in the State of " + state + "\n")
        my_cursor.execute('SELECT * FROM students WHERE State = ?', val)
        my_records = my_cursor.fetchall()
        df = DataFrame(my_records, columns={'StudentID', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor',
                                            'Address', 'City', 'State', 'ZipCode', 'MobilePhoneNumber', 'isDeleted'})
        print(df)
        del df
    if choice.upper() == "ADVISOR":
        advisor = input("Enter the Advisor you are looking for : ")
        val.append(advisor)
        print("Returning all Students that have " + advisor + " as their advisor\n")
        my_cursor.execute('SELECT * FROM students WHERE Advisor = ?', val)
        my_records = my_cursor.fetchall()
        df = DataFrame(my_records, columns={'StudentID', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor',
                                            'Address', 'City', 'State', 'ZipCode', 'MobilePhoneNumber', 'isDeleted'})
        print(df)
        del df


# Soft Deletes a student entry by updating isDeleted to 1
def delete():
    id = input("Enter the ID of the Student you wish to Delete : ")
    my_cursor.execute("UPDATE students SET isDeleted = 1 WHERE StudentID = ?", [id])
    conn.commit()
    print("Student has been (soft)Deleted")


# Application body
def main():
    is_done = False;
    create_students_table()
    print("\n#Creating a temporary students table in Students database#\n")
    print("Assignment 3 : Joey Sheridan")
    print("[1] Import students.csv to Table")
    print("[2] Add new Student to Table")
    print("[3] Update Student in Table")
    print("[4] Soft Delete Student in Table")
    print("[5] Search Table by Attribute")
    print("[6] Exit\n")
    x = int(input(":"))
    while x != 1 and x != 2 and x != 3 and x != 4 and x != 5 and x != 6:
        print("INPUT INVALID. SELECT A NUMBER")
        print("[1] Import students.csv to Table")
        print("[2] Add new Student to Table")
        print("[3] Update Student in Table")
        print("[4] Soft Delete Student in Table")
        print("[5] Search Table by Attribute")
        print("[6] Exit\n")
        x = int(input(":"))
    while not is_done:
        if x == 1:
            data_ingestion()
            print("\n[1] Import students.csv to Table")
            print("[2] Add new Student to Table")
            print("[3] Update Student in Table")
            print("[4] Soft Delete Student in Table")
            print("[5] Search Table by Attribute")
            print("[6] Exit\n")
            x = int(input(":"))
            while x != 1 and x != 2 and x != 3 and x != 4 and x != 5 and x != 6:
                print("INPUT INVALID. SELECT A NUMBER")
                print("[1] Import students.csv to Table")
                print("[2] Add new Student to Table")
                print("[3] Update Student in Table")
                print("[4] Soft Delete Student in Table")
                print("[5] Search Table by Attribute")
                print("[6] Exit\n")
                x = int(input(":"))
        elif x == 2:
            add_student()
            print("\n[1] Import students.csv to Table")
            print("[2] Add new Student to Table")
            print("[3] Update Student in Table")
            print("[4] Soft Delete Student in Table")
            print("[5] Search Table by Attribute")
            print("[6] Exit\n")
            x = int(input(":"))
            while x != 1 and x != 2 and x != 3 and x != 4 and x != 5 and x != 6:
                print("INPUT INVALID. SELECT A NUMBER")
                print("[1] Import students.csv to Table")
                print("[2] Add new Student to Table")
                print("[3] Update Student in Table")
                print("[4] Soft Delete Student in Table")
                print("[5] Search Table by Attribute")
                print("[6] Exit\n")
                x = int(input(":"))
        elif x == 3:
            update_student()
            print("\n[1] Import students.csv to Table")
            print("[2] Add new Student to Table")
            print("[3] Update Student in Table")
            print("[4] Soft Delete Student in Table")
            print("[5] Search Table by Attribute")
            print("[6] Exit\n")
            x = int(input(":"))
            while x != 1 and x != 2 and x != 3 and x != 4 and x != 5 and x != 6:
                print("INPUT INVALID. SELECT A NUMBER")
                print("[1] Import students.csv to Table")
                print("[2] Add new Student to Table")
                print("[3] Update Student in Table")
                print("[4] Soft Delete Student in Table")
                print("[5] Search Table by Attribute")
                print("[6] Exit\n")
                x = int(input(":"))
        elif x == 4:
            delete()
            print("\n[1] Import students.csv to Table")
            print("[2] Add new Student to Table")
            print("[3] Update Student in Table")
            print("[4] Soft Delete Student in Table")
            print("[5] Search Table by Attribute")
            print("[6] Exit\n")
            x = int(input(":"))
            while x != 1 and x != 2 and x != 3 and x != 4 and x != 5 and x != 6:
                print("INPUT INVALID. SELECT A NUMBER")
                print("[1] Import students.csv to Table")
                print("[2] Add new Student to Table")
                print("[3] Update Student in Table")
                print("[4] Soft Delete Student in Table")
                print("[5] Search Table by Attribute")
                print("[6] Exit\n")
                x = int(input(":"))
        elif x == 5:
            display_by()
            print("\n[1] Import students.csv to Table")
            print("[2] Add new Student to Table")
            print("[3] Update Student in Table")
            print("[4] Soft Delete Student in Table")
            print("[5] Search Table by Attribute")
            print("[6] Exit\n")
            x = int(input(":"))
            while x != 1 and x != 2 and x != 3 and x != 4 and x != 5 and x != 6:
                print("INPUT INVALID. SELECT A NUMBER")
                print("[1] Import students.csv to Table")
                print("[2] Add new Student to Table")
                print("[3] Update Student in Table")
                print("[4] Soft Delete Student in Table")
                print("[5] Search Table by Attribute")
                print("[6] Exit\n")
                x = int(input(":"))
        elif x == 6:
            delete_table()
            is_done = True;
        else:
            print("INPUT INVALID")
            print("ENTER THE NUMBER OF YOUR DESIRED OPERATION\n")
            print("[1] Import students.csv to Table")
            print("[2] Add new Student to Table")
            print("[3] Update Student in Table")
            print("[4] Soft Delete Student in Table")
            print("[5] Search Table by Attribute")
            print("[6] Exit\n")
            x = int(input(":"))
            while x != 1 and x != 2 and x != 3 and x != 4 and x != 5 and x != 6:
                print("INPUT INVALID. SELECT A NUMBER")
                print("[1] Import students.csv to Table")
                print("[2] Add new Student to Table")
                print("[3] Update Student in Table")
                print("[4] Soft Delete Student in Table")
                print("[5] Search Table by Attribute")
                print("[6] Exit\n")
                x = int(input(":"))
    print("Thank you for your time =) \nDeleting temporary students table \nExiting application")


main()
conn.close()
