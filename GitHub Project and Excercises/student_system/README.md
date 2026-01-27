# Student Management System

## Overview
The Student Management System is a command-line interface (CLI) application developed in Python.  
It allows users to manage student academic records, including grades, sections, averages, and performance evaluation.

The project follows modular programming principles and proper separation of concerns to ensure clean, readable, and maintainable code.

---

## Features
- Add new students
- Validate student name, section, and grades
- Display all registered students
- Show the Top 3 students by average score
- Calculate the global average score
- Display failing students (below passing grade)
- Export student data to a CSV file
- Import student data from a CSV file
- Delete students safely with confirmation

---

## Project Structure
student_system/
│
├── main.py # Program entry point and application flow
├── menu.py # Menu display and user interaction
├── actions.py # Core business logic and validations
├── data.py # CSV import/export handling
├── students.csv # Generated CSV file (after export)
└── README.md # Project documentation


---

## System Workflow
1. The program starts execution in main.py
2. The menu is displayed using menu.py
3. User actions are handled by functions in actions.py
4. Student data can be saved and loaded using CSV files through data.py
5. All data is stored in memory using Python lists and dictionaries

---

## Data Validation Rules
- Student names must contain only letters and spaces
- Sections must follow the format: 10A, 11B, etc.
- Grades must be numeric values between 0 and 100
- The passing grade is defined as 60

---

## CSV Support
- Export student data to students.csv
- Import existing student data from students.csv
- Grades and averages are automatically converted back to numeric values upon import

---

## How to Run the Program
Ensure that Python 3.10 or higher is installed.

Run the application using the following command:
```bash
python main.py
