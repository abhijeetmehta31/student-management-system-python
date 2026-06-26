students = []

try :
 with open("students.txt", "r") as file:
    for line in file:
        line = line.strip()
        parts = line.split(",")

        student = {
            "name": parts[0],
            "roll_no": int(parts[1]),
            "course": parts[2]
        }

        students.append(student)
except FileNotFoundError:
 pass

def add_student():
    name = input("Enter name :")
    roll_no = int(input("Enter roll_no : "))
    course = input("Enter course : ")

    for student in students:
        if student["roll_no"] == roll_no:
           print("Roll Number Already Exists")
           return

    student = {
        "name": name,
        "roll_no": roll_no,
        "course": course
    }
    students.append(student)

    save_students()
    print("Student Added Successfully")

def view_student():
    if len(students) == 0:
        print("No Students Found")
        return
    
    for i in students:
        print(f"Name: {i['name']}")
        print(f"Roll No: {i['roll_no']}")
        print(f"Course: {i['course']}")



def search_student():
    roll = int(input("Enter roll_no : "))

    found = False

    for student in students:
        if student["roll_no"] == roll:
            print(f"Name: {student['name']}")
            print(f"Roll No: {student['roll_no']}")
            print(f"Course: {student['course']}")

            found = True
            break

    if found == False:
        print("Student Not Found")

def delete_student():
     roll = int(input("Enter roll_no : "))

     found = False

     for student in students:
        if student["roll_no"] == roll:
            students.remove(student)
            save_students()
            print("Student Deleted Successfully")

            found = True
            break

     if found == False:
         print("Student Not Found")

def update_student():
    roll = int(input("Enter roll_no : "))

    found = False

    for student in students:
        if student["roll_no"] == roll:
            student["name"] = input("Enter new name : ")
            student["course"] = input("Enter new course : ")
            save_students()

            found = True
            break

    if found == False:
         print("invalid roll_no")
        
def save_students():
    with open("students.txt", "w") as file:
        for student in students:
            file.write(
    f"{student['name']},{student['roll_no']},{student['course']}\n")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = int(input("Enter your choice : "))
    if choice == 1:
        add_student()

    elif choice == 2:
        view_student()

    elif choice == 3:
        search_student()

    elif choice == 4:
        delete_student()

    elif choice == 5:
        update_student()

    elif choice == 6:
        print("Good bye")
        break
    
    else:
        print("Invalid input")
