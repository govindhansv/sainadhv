student_databse={} # Dictionary

def add_student():
        roll = input("Enter roll number : ")
        if roll in student_databse:
            print("Roll number already in db :")
        else:
            name = input("Enter name : ")
            print("Student ",name,"added successfully")
            student_databse[roll] = name
            print(student_databse[roll])

def update_student():
     roll = input("Enter roll number of student to update :")
     if roll in student_databse:
          name = input("enter new name ")
          student_databse[roll] =name 
     else:
          print("Enter valid roll no.")

def display_student():
     for roll in student_databse:
          print(student_databse[roll])

def remove_a_student():
    roll = input("Enter roll no to remove : ")
    if roll in student_databse:
         student_databse.pop(roll)
         print(" Removed ", student_databse)

while True:
    ch = input("Enter choice : 1.Create 2.Update 3.Display 4.exit")
    if ch == "1":
        add_student()
    elif ch == "2":
        update_student()
    elif ch == "3":
        display_student()
    elif ch == "4":
        remove_a_student()
    else:
         print("Invalid choice ")