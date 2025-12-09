def is_valid_name(name):
    return name.replace(" ", "").isalpha() and len(name) > 0


def is_valid_section(section):
    return len(section) == 3 and section[:-1].isdigit() and section[-1].isalpha()


def student_exists(students, name, section):
    return any(s["name"] == name and s["section"] == section for s in students)


def get_valid_grade(subject):
    while True:
        try:
            grade = float(input(f"Enter grade for {subject} (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a numeric value.")


def add_student(students):
    print("\n--- Add Student ---")

    while True:
        name = input("Enter full name: ").strip()
        if not is_valid_name(name):
            print("Invalid name. Cannot be empty and must contain only letters.")
            continue
        break

    while True:
        section = input("Enter section (e.g., 11B): ").strip().upper()
        if not is_valid_section(section):
            print("Invalid section format. Example: 10A, 11B")
            continue
        if student_exists(students, name, section):
            print("This student already exists!")
            continue
        break

    spanish = get_valid_grade("Spanish")
    english = get_valid_grade("English")
    socials = get_valid_grade("Socials")
    science = get_valid_grade("Science")

    average = (spanish + english + socials + science) / 4

    student = {
        "name": name,
        "section": section,
        "spanish": spanish,
        "english": english,
        "socials": socials,
        "science": science,
        "average": average,
    }

    students.append(student)
    print("Student added successfully!")


def display_students(students):
    if not students:
        print("No students registered.")
        return

    print("\n--- All Students ---")
    for s in students:
        print(f"{s['name']} | Section: {s['section']} | Avg: {s['average']:.2f}")


def display_top_students(students):
    if len(students) < 3:
        print("Not enough students to calculate Top 3.")
        return

    top = sorted(students, key=lambda x: x["average"], reverse=True)[:3]

    print("\n--- Top 3 Students ---")
    for s in top:
        print(f"{s['name']} | Avg: {s['average']:.2f}")


def show_global_average(students):
    if not students:
        print("No students to calculate average.")
        return

    global_avg = sum(s["average"] for s in students) / len(students)
    print(f"\nGlobal average score: {global_avg:.2f}")


def delete_student(students):
    print("\n--- Delete Student ---")
    name = input("Enter the name of the student: ").strip()
    section = input("Enter the section (e.g., 11B): ").strip().upper()

    for s in students:
        if s["name"] == name and s["section"] == section:
            confirm = input("Are you sure you want to delete this student? (yes/no): ").lower()
            if confirm == "yes":
                students.remove(s)
                print("Student removed successfully!")
            else:
                print("Operation canceled.")
            return
    
    print("Student not found.")


def show_failing_students(students):
    print("\n--- Failing Students (below 60 in any subject) ---")

    failing_list = [
        s for s in students if s["spanish"] < 60 or s["english"] < 60 or s["socials"] < 60 or s["science"] < 60
    ]

    if not failing_list:
        print("No failing students.")
        return

    for s in failing_list:
        failed_subjects = []
        if s["spanish"] < 60:
            failed_subjects.append(f"Spanish ({s['spanish']})")
        if s["english"] < 60:
            failed_subjects.append(f"English ({s['english']})")
        if s["socials"] < 60:
            failed_subjects.append(f"Socials ({s['socials']})")
        if s["science"] < 60:
            failed_subjects.append(f"Science ({s['science']})")

        print(f"{s['name']} | Section: {s['section']} | Failed: {', '.join(failed_subjects)}")