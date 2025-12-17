🎓 Student Management System
📌 Overview

The Student Management System is a command-line interface (CLI) application built in Python that allows users to manage student academic information, including grades, sections, averages, and performance tracking.

The project is structured using modular design, follows good scope practices, and separates concerns across multiple files for maintainability and scalability.

✨ Features

Add new students

Validate student name, section, and grades

Display all registered students

Show the Top 3 students by average

Calculate global average score

Show failing students (below passing grade)

Export student data to CSV

Import student data from CSV

Delete students safely with confirmation

🗂️ Project Structure
student_system/
│
├── main.py          # Application entry point and menu control
├── menu.py          # Menu display and user option selection
├── actions.py       # Core business logic and validations
├── data.py          # CSV import/export handling
├── students.csv     # Generated CSV file (after export)
├── README.md        # Project documentation

⚙️ How It Works

The program starts from main.py

The menu is displayed using menu.py

Based on user selection, actions are executed from actions.py

Student data can be persisted using CSV functions in data.py

All data is managed in memory using Python lists and dictionaries

🧪 Data Validation Rules

Names must contain only letters and spaces

Sections must follow the format: 10A, 11B, etc.

Grades must be numeric values between 0 and 100

Passing grade is defined as 60

💾 CSV Support

Export student data to students.csv

Import existing student data from students.csv

Automatically converts grades back to numeric values on import

▶️ How to Run the Project

Make sure you have Python 3.10+ installed.

python main.py

🧠 Key Concepts Applied

Functions and scope (no global data misuse)

Input validation and error handling

Modular programming

Sorting and aggregation

File handling with CSV

Clean CLI interaction

✅ Author

Leonardo Escalona
Python Intermediate – Student Project


Pull Request Created on: 12/12/2025 

