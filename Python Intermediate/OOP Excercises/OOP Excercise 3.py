#Create the Class named "student"
class Student:
    def __init__(self, name, score_1, score_2):
        self.name = name
        self.score_1 = score_1
        self.score_2 = score_2

    def to_dict(self):
        return {
            "name": self.name,
            "score_1": self.score_1,
            "score_2": self.score_2
        } 
#Import Students from CSV
import csv

def import_students_from_csv(filename):
    students = []

    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            student = Student(
                row["name"],
                float(row["score_1"]),
                float(row["score_2"])
            )
            students.append(student)

    return students
#Use the imported students
students = import_students_from_csv("students.csv")

for student in students:
    print(student.name, student.score_1, student.score_2)

#Export Students to CSV
def export_students_to_csv(filename, students):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["name", "score_1", "score_2"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for student in students:
            writer.writerow(student.to_dict())
#Test that exporting the students worked, students_output.csv should have created once the script is ran           
students = [
    Student("Carlos", 90, 85),
    Student("Maria", 88, 92)
]

export_students_to_csv("students_output.csv", students)
