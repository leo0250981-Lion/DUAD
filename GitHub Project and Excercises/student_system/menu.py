def show_menu():
    print("\n=== STUDENT MANAGEMENT SYSTEM ===")
    print("1. Add new student")
    print("2. Display all students")
    print("3. Top 3 students by average")
    print("4. Global average score")
    print("5. Show failing students")
    print("6. Export students to CSV")
    print("7. Import students from CSV")
    print("8. Delete a student")
    print("9. Exit")

    while True:
        option = input("Select an option (1-9): ").strip()
        if option in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            return option
        print("Invalid option. Please try again.")
