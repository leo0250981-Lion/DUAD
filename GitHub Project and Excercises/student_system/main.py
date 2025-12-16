from menu import show_menu

def main():
    while True:
        option = show_menu()

        if option == "1":
            print("Add new student")
        elif option == "2":
            print("Display all students")
        elif option == "3":
            print("Top 3 students by average")
        elif option == "4":
            print("Global average score")
        elif option == "5":
            print("Show failing students")
        elif option == "6":
            print("Export students to CSV")
        elif option == "7":
            print("Import students from CSV")
        elif option == "8":
            print("Delete a student")
        elif option == "9":
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
