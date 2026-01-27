from menu import show_menu
from actions import (
    add_student,
    display_students,
    top_3_students,
    global_average,
    show_failing_students,
    delete_student
)
from data import export_data, import_data


def main():
    students = []  # estado principal del programa

    while True:
        option = show_menu().strip()

        if option == "1":
            add_student(students)

        elif option == "2":
            display_students(students)

        elif option == "3":
            top_3_students(students)

        elif option == "4":
            global_average(students)

        elif option == "5":
            show_failing_students(students)

        elif option == "6":
            export_data(students)

        elif option == "7":
            students = import_data()  # IMPORTANTE: reasignar

        elif option == "8":
            delete_student(students)

        elif option == "9":
            print("Exiting the program...")
            break



if __name__ == "__main__":
    main()
