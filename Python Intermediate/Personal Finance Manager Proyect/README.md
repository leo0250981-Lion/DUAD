# Personal Finance Manager

A desktop application built with **PySimpleGUI** that allows users to manage personal finances in a structured and user-friendly way.

This project was developed to practice:

- Modularization
- Object-Oriented Programming (OOP)
- Input validation
- JSON file persistence
- Separation of logic and presentation
- Unit testing

---

## Features

- Main window displaying all income and expenses in a table
- Add Category (with optional color selection)
- Add Income (title, amount, category, date)
- Add Expense (title, amount, category, date)
- Validation of:
  - Required fields
  - Numeric amounts
  - Date format (`dd/mm/yyyy`)
  - Future dates prevention
- Error message if adding income/expense without categories
- Automatic data persistence (JSON)
- Unit tests for business logic (GUI-independent)

---

## Project Structure

```text
.
├── main.py              # Application entry point
├── interfaces.py        # GUI layouts (PySimpleGUI)
├── logic.py             # Business logic (FinanceManager)
├── models.py            # Data models
├── validators.py        # Input validation utilities
├── persistence.py       # JSON load/save
└── tests/
    └── test_logic.py    # Unit tests (no GUI dependency)
Architecture

The project follows a layered architecture:

Presentation Layer → main.py, interfaces.py

Business Logic Layer → logic.py, models.py, validators.py

Persistence Layer → persistence.py

This separation ensures:

Maintainability

Testability

Clear responsibility boundaries

Requirements

Python 3.10+

PySimpleGUI

Install dependency:

pip install PySimpleGUI
Running the Application
python main.py
Data Persistence

Data is automatically saved in:

finance_data.json

Data is saved when:

A category is added

A movement is added

The application closes

Existing data is loaded automatically at startup.

Running Unit Tests

Run:

python -m unittest -v

Tests validate:

Category creation

Duplicate category handling

Income/expense creation

Invalid category validation

Future date validation

Invalid amount types

Business rule enforcement

Validation Rules

Date format must be dd/mm/yyyy

Date cannot be in the future

Income amount must be > 0

Expense amount must be > 0

Categories must exist before adding movements

Title cannot be empty

Design Decisions

Expenses are stored internally as negative values

Income is stored as positive values

GUI contains no business logic

All financial rules live in logic.py

Validators are isolated for clarity and reusability

Possible Improvements

Filter movements by date range

Export to CSV

Display totals and net balance

Category-based row colors

Edit/Delete movements

Monthly reports

Technologies

Python

PySimpleGUI

JSON

unittest

📄 License

This project is for educational purposes.
