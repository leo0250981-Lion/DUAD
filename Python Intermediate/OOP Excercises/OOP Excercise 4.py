#Circle Class
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

#Person and Bus Classes
class Person:
    def __init__(self, name):
        self.name = name

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} boarded the bus")
        else:
            print("The bus is full")

    def remove_passenger(self):
        if self.passengers:
            passenger = self.passengers.pop()
            print(f"{passenger.name} left the bus")
        else:
            print("There are no passengers on the bus")

#Student Management Project Using Objects
#Student Class 
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
    
#Using Objects 
def create_student(students_list):
    name = input("Enter student name: ")
    score_1 = float(input("Enter first score: "))
    score_2 = float(input("Enter second score: "))

    students_list.append(Student(name, score_1, score_2))

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

#Export Student from CSV
def export_students_to_csv(filename, students):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["name", "score_1", "score_2"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for student in students:
            writer.writerow(student.to_dict())

#Body Part Classes 
class Head:
    pass

class Hand:
    pass

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Feet:
    pass

class Leg:
    def __init__(self, feet):
        self.feet = feet

class Torso:
    def __init__(self, head, right_arm, left_arm):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm

#Human Class after we connect everything
class Human:
    def __init__(self):
        self.head = Head()

        self.right_hand = Hand()
        self.left_hand = Hand()

        self.right_arm = Arm(self.right_hand)
        self.left_arm = Arm(self.left_hand)

        self.right_feet = Feet()
        self.left_feet = Feet()

        self.right_leg = Leg(self.right_feet)
        self.left_leg = Leg(self.left_feet)

        self.torso = Torso(
            self.head,
            self.right_arm,
            self.left_arm
        )

