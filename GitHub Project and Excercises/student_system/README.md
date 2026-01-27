# 🎓 Student Management System

## 📌 General Description
The **Student Management System** is a command-line interface (CLI) application developed in **Python**. Its purpose is to manage student academic information, including student registration, grade management, average calculations, and performance evaluation.

This project was designed following **modular programming principles**, **proper scope management**, and **separation of concerns**, ensuring clean, readable, and maintainable code.

---

## ✨ Features
- ➕ Register new students
- ✅ Validate student names, sections, and grades
- 📋 Display all registered students
- 🏆 Display the Top 3 students based on average score
- 📊 Calculate the global average score
- ❌ Identify failing students (below the passing grade)
- 💾 Export student data to a CSV file
- 📂 Import student data from a CSV file
- 🗑 Safely delete students with confirmation

---

## 🗂️ Project Structure
student_system/
│
├── main.py # Program entry point and application flow
├── menu.py # Menu display and user interaction
├── actions.py # Core business logic and validations
├── data.py # CSV import/export handling
├── students.csv # Generated CSV file (after export)
└── README.md # Project documentation


---

## ⚙️ System Workflow
1. The program execution starts in `main.py`
2. The main menu is displayed using `menu.py`
3. Based on user input, corresponding actions are executed from `actions.py`
4. Student data persistence is handled through CSV functions in `data.py`
5. All data is managed in memory using Python lists and dictionaries

---

## 🧪 Data Validation Rules
- Student names must contain only letters and spaces
- Sections must follow the format: `10A`, `11B`, etc.
- Grades must be numeric values between **0 and 100**
- The passing grade is defined as **60**

---

## 💾 CSV Support
- Export student data to `students.csv`
- Import existing student data from `students.csv`
- Grades and averages are automatically converted back to numeric values upon import

---

## ▶️ How to Run the Program
Ensure that **Python 3.10 or higher** is installed.

Run the application using the following command:
```bash
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
