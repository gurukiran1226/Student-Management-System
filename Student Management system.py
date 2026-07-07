students = {}

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

def add_student():
    roll = input("Enter roll number: ")
    if roll in students:
        print("Student already exists!")
        return
    
    name = input("Enter student name: ")
    marks = []
    for i in range(3):
        mark = float(input(f"Enter marks of subject {i+1}: "))
        marks.append(mark)
    
    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)
    
    students[roll] = {
        "Name": name,
        "Marks": marks,
        "Total": total,
        "Average": average,
        "Grade": grade,
    }
    print("Student record added successfully!")

def search_students():
    roll = input("Enter roll number to search: ")
    if roll in students:
        s = students[roll]
        print("\nStudent Details")
        print("---------------------")
        print("Roll Number  :", roll)
        print("Name         :", s["Name"])
        print("Marks        :", s["Marks"])
        print("Total        :", s["Total"])
        print("Average      :", round(s["Average"], 2))
        print("Grade        :", s["Grade"])
    else:
        print("Student not found!")
    

def display_students():
    if not students:
        print("No student record found :")
        return()
    print("\n All students Records")
    print("-" * 60)
    for roll, s in students.items():
        print("Roll Number :",roll)
        print("Name         :", s["Name"])
        print("Marks        :", s["Marks"])
        print("Total        :", s["Total"])
        print("Average      :", round(s["Average"], 2))
        print("Grade        :", s["Grade"])
#main menu
while True:
    print("\n===== STUDENT RECORD MANAGEMENT SYSTEM=====")
    print("1.Add student Record")
    print("2.Search student Details")
    print("3.Display All Students Records")
    print("4.Exit")
    choice = input("Enter your choice :")
    if choice == "1":
        add_student()
    elif choice =="2":
        search_students()
    elif choice == "3":
        display_students()
    elif choice =="4":
        print("Thank you !")
    else:
        print("Invalid choice ! please try again")
