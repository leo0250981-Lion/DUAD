from actions import (
    add_student,
    display_students,
    display_top_students,
    show_global_average,
    delete_student,
    show_failing_students
)
from data import export_data, import_data

students = []  # Shared list inside menu module

def show_menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add students")
        print("2. Show all students")
        print("3. Show top 3 students")
        print("4. Show global average score")
        print("5. Export data to CSV")
        print("6. Import data from CSV")
        print("7. Exit")
        print("8. Delete student")
        print("9. Show failing students")

        choice = input("Select an option (1-9): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            display_top_students(students)
        elif choice == "4":
            show_global_average(students)
        elif choice == "5":
            export_data(students)
        elif choice == "6":
            imported = import_data()
            if imported:
                students.clear()
                students.extend(imported)
        elif choice == "7":
            print("Exiting program...")
            break
        elif choice == "8":
            delete_student(students)
        elif choice == "9":
            show_failing_students(students)
        else:
            print("Invalid option. Please choose 1 to 9.")