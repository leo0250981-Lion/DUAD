employees = [
    {"name": "Leonardo", "email": "leonardo@company.com", "department": "IT"},
    {"name": "Emma", "email": "emma@company.com", "department": "Marketing"},
    {"name": "James", "email": "james@company.com", "department": "Finance"},
    {"name": "Olivia", "email": "olivia@company.com", "department": "IT"},
    {"name": "Michael", "email": "michael@company.com", "department": "Finance"},
]

# Dictionary where we will group employees by department
grouped_by_department = {}

# Loop through each employee
for employee in employees:
    department = employee["department"]
    name = employee["name"]

    # If the department doesn't exist yet, create it with a new list
    if department not in grouped_by_department:
        grouped_by_department[department] = [name]
    else:
        # If it exists, append the employee name
        grouped_by_department[department].append(name)

print(grouped_by_department)
